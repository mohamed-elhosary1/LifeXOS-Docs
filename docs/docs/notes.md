# Notes System

The Notes feature (`src/pages/Notes.tsx`) provides a streamlined, grid-based Markdown note-taking interface.

## Note Attributes
Each Note object contains:
- `id`, `title`, `content` (Markdown).
- `createdAt`, `updatedAt`.
- `favorite` (boolean).
- `archived` (boolean).
- `tags` (string array).

## Organization & Filtering
- **Sidebar Filters**: Quickly view "All Notes", "Favorites", "Recent" (updated in the last 7 days), or "Archive".
- **Tags Integration**: Extracts all unique tags used across the workspace. Clicking a tag in the sidebar filters the grid to show only matching notes. Tag badges are dynamically color-coded based on a string-hashing function (`getTagColorClass`).
- **Search**: Real-time text search querying the title, content, and tags.
- **Sorting**: Toggle between "Newest" and "Oldest" (based on `updatedAt`).

## Editor UI
- Notes are viewed and edited within a focused, slide-over modal overlay.
- Content changes are autosaved with a 400ms debounce directly to Supabase (`user_data` table).
- The editor includes dedicated buttons to toggle favorite/archive status, manage inline tags, and delete the note.
