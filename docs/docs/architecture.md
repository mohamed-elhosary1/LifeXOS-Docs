# Architecture

LifeXOS employs a modular, component-based frontend architecture built on React and Vite, supported by a Supabase backend.

## Directory Structure
- **`src/`**: The core application root.
  - **`components/`**: Reusable UI parts. Contains layout wrappers (`AppLayout.tsx`), UI primitive elements, and specialized components like `FeedbackDialog`.
  - **`contexts/`**: React contexts providing global data streams.
    - `AuthContext`: Manages Supabase authentication state.
    - `LanguageContext`: Provides translation and i18n logic.
  - **`lib/`**: Business logic, utilities, and state.
    - `store.ts`: The central state management engine.
    - `themePalettes.ts` & `backgrounds.ts`: Handle complex aesthetic user preferences.
  - **`pages/`**: Primary route views. These are strictly lazy-loaded in `App.tsx` using `React.lazy` to improve initial bundle load times.

## Core Paradigms
- **Lazy Loading & Code Splitting**: All major routes (e.g., `MyDay`, `Study`, `Pomodoro`) are dynamically imported.
- **Error Boundaries**: A `GlobalErrorBoundary` catches chunk-loading errors and prompts users to refresh, which is crucial for a continuously deployed SPA.
- **Glassmorphism**: Visual elements heavily rely on CSS backdrop-filters, structured across `glass-card`, `glass-sidebar`, etc., mapped in `index.css`.
- **Offline & Storage**: Uses a custom sync mechanism. The store caches data locally in memory and synchronizes aggressively with a `user_data` JSONB column in Supabase. PWA support ensures the app remains installable and fast.
