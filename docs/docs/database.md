# Database Documentation

## Tables

### `user_data`
This is the primary data store for a user, containing all their state encoded as JSON blobs. This allows flexible data structures on the frontend.
- `id` (uuid)
- `user_id` (uuid, references auth.users)
- `courses` (jsonb)
- `day_records` (jsonb)
- `goals` (jsonb)
- `habits` (jsonb)
- `notes` (jsonb)
- `plans` (jsonb)
- `study_sessions` (jsonb)
- `subjects` (jsonb)
- `tasks` (jsonb)
- `created_at` (timestamp)
- `updated_at` (timestamp)

### `user_ai_profiles`
Stores the user's AI profile parameters and settings, built over time by the `aie-memory-manager` analyzing interactions.
- `user_id` (uuid, primary key)
- `chat_history` (jsonb, default '[]'::jsonb)
- `learning_enabled` (boolean)
- `communication` (jsonb)
- `productivity` (jsonb)
- `knowledge` (jsonb)
- `ai_preferences` (jsonb)
- `behavior` (jsonb)
- `version` (integer)
- `last_analyzed_at` (timestamp)

### `ai_profile_versions`
An audit log / history table for the `user_ai_profiles`. Each time the profile updates, a version snapshot is saved.
- `id` / `created_at` (assumed based on standard patterns)
- `user_id` (uuid)
- `version` (integer)
- `confidence_average` (numeric)
- `communication` (jsonb)
- `productivity` (jsonb)
- `knowledge` (jsonb)
- `ai_preferences` (jsonb)
- `behavior` (jsonb)
- `source` (text)
- `messages_analyzed` (integer)

### Data Types (Frontend to `user_data` mapping)
The frontend (`src/lib/types.ts`) manages tasks, exams, courses, subjects, habits, life goals, day records, study sessions, and plan goals. These are synced as JSON arrays to the `user_data` table.

## Relationships
- `user_data.user_id` -> `auth.users.id`
- `user_ai_profiles.user_id` -> `auth.users.id`
- `ai_profile_versions.user_id` -> `auth.users.id`
