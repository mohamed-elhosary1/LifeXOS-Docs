# Supabase Edge Functions

LifeXOS relies on several Supabase Edge Functions for operations that require secure execution, such as AI prompt generation, profile analysis, and administrative tasks.

## Directory: `supabase/functions/`

### 1. `ai-copilot`
**Purpose**: Primary endpoint for AI interactions in the app. It acts as the "Copilot" for managing tasks, habits, and studies.
- **Features**:
  - Handles two modes: Planner (`PLANNER_SYSTEM`) and Mastermind (`MASTERMIND_SYSTEM`).
  - Fetches the user's local state (tasks, habits, etc.) passed via payload to build the system context.
  - Supports streaming (`text/event-stream`).
  - Supports function calling (tools) so the AI can execute actions.
  - Tries Gemini API first, with fallback to OpenAI if Gemini fails or is rate-limited.
- **Inputs**: `{ messages: Array, stream: boolean, mode: string, tasks, habits, courses, subjects, etc. }`
- **Outputs**: Streaming text chunks or a single JSON response containing AI message/tool calls.

### 2. `lifexos-ai`
**Purpose**: Handles background or simpler AI generation requests, often tailored to specific summaries or generating the dashboard reports.
- **Features**: 
  - Retrieves the user's `user_ai_profiles` and appends communication/productivity preferences to the prompt.
  - Periodically invokes `aie-analyzer` if the message threshold is reached.
  - Tries Gemini models first (`gemini-3.6-flash`), falls back to `gemini-3.5-flash` or OpenAI.
- **Inputs**: `{ messages, tasks, habits, sessions, lang, userName }`
- **Outputs**: `{ content: string }`

### 3. `aie-analyzer`
**Purpose**: Asynchronously analyzes the user's chat history and interactions to build and update their AI Personalization Profile (`user_ai_profiles`).
- **Features**: 
  - Triggered by `lifexos-ai` or run as a standalone task.
  - Extracts parameters for Communication, Productivity, Knowledge, AI Preferences, and Behavior.
  - Saves versions to `ai_profile_versions` for auditing and rollback capabilities.
- **Inputs**: `{ messages: Array }`
- **Outputs**: Updates the database; returns `{ success: true, version: number }`.

### 4. `aie-memory-manager`
**Purpose**: Manages and processes long-term context retention. (Used in conjunction with the AIE system to prune or summarize older memory/chat history so context windows don't overflow).
- **Features**: Handles `chat_history` payload logic in the DB.

### 5. `submit-feedback`
**Purpose**: Simple endpoint for users to submit feedback directly from the app.
- **Features**: Inserts a row into the `public.user_feedbacks` table.
- **Inputs**: `{ feedback_type, title, description, user_email }`
- **Outputs**: `{ success: boolean }`

### 6. `delete-account`
**Purpose**: Securely deletes a user's account from Supabase Auth.
- **Features**: Triggers the `ON DELETE CASCADE` constraints in the database, automatically cleaning up `user_data`, `user_ai_profiles`, etc.
- **Inputs**: Bearer token of the user requesting deletion.
- **Outputs**: Success confirmation or unauthorized error.

### 7. `planner-chat`
**Purpose**: Dedicated endpoint for specific conversational flows inside the Planner view.
- **Features**: Streamlines prompts focused on scheduling and time-blocking.

### 8. `_shared`
**Purpose**: Contains shared Deno modules and utility functions used across all Edge Functions.
- **Contents**:
  - `cors.ts`: CORS headers.
  - `auth.ts`: Validates `Authorization` JWTs and retrieves user details.
  - `rate-limit.ts`: Throttles function invocations.
  - `prompt-injection.ts`: Basic heuristic checks for malicious prompt payloads.
