# Supabase Configuration

The LifeXOS backend is primarily managed through the Supabase CLI, defining the infrastructure as code.

## Project Information
- **Project ID**: `fdtinjhomdpxzcvfmsev`
- **Configuration File**: `supabase/config.toml`
- **Migrations Directory**: `supabase/migrations/` (and `backup/` for older scripts)
- **Functions Directory**: `supabase/functions/`

## `config.toml` Edge Function Settings
The Edge Functions are explicitly registered in `config.toml`. Some functions have `verify_jwt = false` because the authentication check is handled manually inside the function code using the `_shared/auth.ts` module, allowing them to return custom unauthorized responses or support CORS preflight requests smoothly.

- **`[functions.profile-analyzer]`**
  - **Enabled**: `true`
  - **Verify JWT**: `false`
  - **Entrypoint**: `./functions/profile-analyzer/index.ts`
  *(Note: This function may be an alias or earlier version of `aie-analyzer`)*

- **`[functions.aie-memory-manager]`**
  - **Enabled**: `true`
  - **Verify JWT**: `false`
  - **Entrypoint**: `./functions/aie-memory-manager/index.ts`

- **`[functions.aie-analyzer]`**
  - **Enabled**: `true`
  - **Verify JWT**: `false`
  - **Entrypoint**: `./functions/aie-analyzer/index.ts`

## Deployment & Migrations
- **Migrations**: Database schema changes (tables, RLS policies, functions, triggers) are stored as standard `.sql` files with timestamps in `supabase/migrations/`.
- **Applying Changes**: The project can be linked to the remote Supabase project, and changes are pushed via `supabase db push` and `supabase functions deploy`.
- **Environment Variables**: Edge functions require secrets such as `GEMINI_API_KEY`, `OPENAI_API_KEY`, `GPT`, and `LIFEXOS_API_KEY` which must be set via `supabase secrets set`.

## Storage Buckets
- **`avatars` Bucket**: Configured for user profile images. Handled via standard RLS policies (users can select, insert, update, delete their own avatars).
