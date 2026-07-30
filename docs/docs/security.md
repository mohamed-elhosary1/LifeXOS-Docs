# Security & RLS Policies

LifeXOS enforces strict data privacy at the database level using PostgreSQL Row Level Security (RLS) in Supabase. This guarantees that users cannot access or modify each other's data, regardless of any potential flaws in the frontend client.

## Row Level Security (RLS)

### `public.user_data`
- **Enable RLS**: `ALTER TABLE public.user_data ENABLE ROW LEVEL SECURITY;`
- **SELECT**: `"Users can view their own data"` — `USING (auth.uid() = user_id)`
- **INSERT**: `"Users can insert their own data"` — `WITH CHECK (auth.uid() = user_id)`
- **UPDATE**: `"Users can update their own data"` — `USING (auth.uid() = user_id)`
- **DELETE**: `"Users can delete their own data"` — `USING (auth.uid() = user_id)`

### `public.user_ai_profiles`
- **Enable RLS**: `ALTER TABLE public.user_ai_profiles ENABLE ROW LEVEL SECURITY;`
- **SELECT**: `"Users can view their own AI profile."` — `USING (auth.uid() = user_id)`
- **UPDATE**: `"Users can update their own AI profile."` — `USING (auth.uid() = user_id)`
- **INSERT**: `"Users can insert their own AI profile."` — `WITH CHECK (auth.uid() = user_id)`

### `public.ai_profile_versions`
- **Enable RLS**: `ALTER TABLE public.ai_profile_versions ENABLE ROW LEVEL SECURITY;`
- **SELECT**: `"Users can view their own AI profile versions."` — `USING (auth.uid() = user_id)`
- **INSERT**: `"Users can insert their own AI profile versions."` — `WITH CHECK (auth.uid() = user_id)`
- *(Updates and Deletes are not allowed by design to preserve audit integrity)*

### `public.user_audit_logs`
- **Enable RLS**: `ALTER TABLE public.user_audit_logs ENABLE ROW LEVEL SECURITY;`
- **SELECT**: `"Users can view their own audit logs"` — `USING (auth.uid() = user_id)`
- **SELECT (Admin)**: `"Admins can view all audit logs"` — `USING (true)` *(Mock policy currently)*
- **INSERT**: `"Users can insert their own audit logs"` — `WITH CHECK (auth.uid() = user_id)`

### `public.user_feedbacks`
- **Enable RLS**: `ALTER TABLE public.user_feedbacks ENABLE ROW LEVEL SECURITY;`
- **SELECT**: `"Users can view their own feedbacks"` — `USING (auth.uid() = user_id)`
- **INSERT**: `"Users can insert their own feedbacks"` — `WITH CHECK (auth.uid() = user_id)`

### Storage Bucket: `avatars`
- **SELECT**: `"avatars_select_own"` — `USING (bucket_id = 'avatars' AND auth.uid()::text = (storage.foldername(name))[1])`
- **INSERT**: `"avatars_insert_own"` — `WITH CHECK (...)`
- **UPDATE**: `"avatars_update_own"` — `USING (...)`
- **DELETE**: `"avatars_delete_own"` — `USING (...)`

## Database Triggers & Functions

To prevent users from manually tampering with internal timestamps or bypassing profile creation, the database handles these with `SECURITY DEFINER` functions.

1. **Auto-Create `user_data` Row**
   - **Trigger**: `on_auth_user_created` (Fires `AFTER INSERT ON auth.users`)
   - **Function**: `public.handle_new_user()`
   - **Security**: Runs as `SECURITY DEFINER` to bypass RLS during user signup.
   - **Action**: Inserts a blank JSON structure into `user_data` for the new `auth.users.id`.
   - **Permissions**: `REVOKE EXECUTE ON FUNCTION public.handle_new_user() FROM PUBLIC, anon, authenticated;`

2. **Auto-Create `user_ai_profiles` Row**
   - **Trigger**: `on_auth_user_created_ai_profile` (Fires `AFTER INSERT ON auth.users`)
   - **Function**: `public.handle_new_user_ai_profile()`
   - **Security**: Runs as `SECURITY DEFINER`.
   - **Action**: Inserts default profile row into `user_ai_profiles`.

3. **Auto-Update Timestamps**
   - **Trigger**: `update_user_data_updated_at`, `update_user_ai_profiles_updated_at` (Fires `BEFORE UPDATE`)
   - **Function**: `public.update_updated_at_column()`
   - **Action**: Forces the `updated_at` column to `now()` or `timezone('utc'::text, now())` ignoring user input.
   - **Permissions**: `REVOKE EXECUTE ON FUNCTION public.update_updated_at_column() FROM PUBLIC, anon, authenticated;`

## Edge Function Security
- **Rate Limiting**: Checks applied inside Edge Functions via the `_shared/rate-limit.ts` logic.
- **Prompt Injection Defense**: Evaluated heuristically before passing user input to the LLMs.
- **Secret Management**: API keys (`GEMINI_API_KEY`, etc.) are stripped of quotes and validated before requests.
