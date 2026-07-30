# API Reference & Data Syncing

Unlike a traditional REST API backend, LifeXOS relies on a local-first state architecture using React/Vite in the frontend, backed by a global singleton state (`store.ts`), and synced to Supabase `user_data` JSONB columns via debounced calls.

## Core State & Sync Architecture
1. **Local Mutations**: Data operations (add task, complete habit, change course) execute synchronously in memory in `src/lib/store.ts`.
2. **Debounced Sync**: Once modified, `debouncedSave()` schedules a Supabase `upsert` after 500ms.
3. **Database Target**: `public.user_data`. The entire JSON blob of tasks, courses, subjects, habits, goals, day_records, plans, and study_sessions is uploaded at once.
4. **Offline Resilience**: Since the source of truth for the session is the local memory/indexedDB, brief offline states just pause the sync until connectivity resumes.

## Direct API Endpoints (Supabase Edge Functions)
While core data is synced via the `@supabase/supabase-js` database API, AI and account administration logic uses Edge Functions.

### Invoke a Function
```javascript
import { supabase } from '@/integrations/supabase/client';

const { data, error } = await supabase.functions.invoke('function-name', {
  body: { /* payload */ }
});
```

### `ai-copilot`
- **Method**: POST
- **Payload**:
  ```json
  {
    "messages": [{ "role": "user", "content": "Help me plan my day." }],
    "mode": "plan",
    "tasks": [...],
    "habits": [...],
    "stream": true
  }
  ```
- **Returns**: `text/event-stream` when streaming, or a JSON payload otherwise.

### `lifexos-ai`
- **Method**: POST
- **Payload**:
  ```json
  {
    "messages": [{ "role": "user", "content": "Summary of today" }],
    "tasks": [...],
    "sessions": [...],
    "lang": "en",
    "userName": "Cassidy"
  }
  ```
- **Returns**: `{"content": "AI text response"}`

### `submit-feedback`
- **Method**: POST
- **Payload**:
  ```json
  {
    "title": "Bug in calendar",
    "description": "Can't add a date.",
    "feedback_type": "bug",
    "user_email": "user@example.com"
  }
  ```
- **Returns**: `{"success": true}`

### `delete-account`
- **Method**: POST
- **Payload**: Empty JSON `{}` (relies on Auth header).
- **Returns**: `{"success": true}`

## Interacting with the AI
The AI system acts on the user's data by outputting function/tool calls in its response (in the backend Edge Function). The backend automatically injects context from the user's local state, allowing the AI to know their pending tasks and completed habits without the user having to explain it.
