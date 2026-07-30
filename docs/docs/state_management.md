# State Management

LifeXOS eschews traditional third-party state managers like Redux or Zustand in favor of a **Custom Pub/Sub In-Memory Store** located in `src/lib/store.ts`.

## Core Mechanics
- **In-Memory Cache**: The state is held in a mutable `cache` object.
- **Pub/Sub System**: Components subscribe to updates using `subscribeStore(fn)`. When the cache updates, `notifyListeners()` triggers a re-render.
- **Debounced Backend Sync**: When state mutates (e.g., `addTask`, `updateCourse`), `debouncedSave()` is invoked. This waits 500ms before upserting the entire JSON payload to the Supabase `user_data` table.

## Data Structure
The state holds arrays of:
- `tasks`: Global list of all tasks.
- `courses` & `subjects`: Educational structures.
- `goals` & `habits`: Long-term planning.
- `plans` & `dayRecords`: Historical and future data.

## Normalization & Deduplication
- **`normalizeTasks()`**: Evaluates task deadlines and statuses, ensuring that tasks correctly move in and out of the "My Day" view.
- **`deduplicateSections()`**: Cleans up duplicate categories to ensure relational integrity without a strict SQL schema.

## Why this architecture?
By syncing an entire structured JSON object to Supabase, the application achieves incredible client-side speed. The user interacts purely with the in-memory cache, ensuring 0ms latency for UI updates, while Supabase acts as a durable snapshot store.
