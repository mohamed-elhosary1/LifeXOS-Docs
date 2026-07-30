# Workspace & Folders Architecture

The LifeXOS workspace is structured hierarchically to organize learning, work, and personal projects. The core units of organization are **Courses** and **Subjects**, which act as folders.

## Folder Configuration & Limits

Validation and configuration are strictly enforced via `src/lib/workspaceConfig.ts` and `src/lib/workspaceValidation.ts`.

| Property | Limit |
|----------|-------|
| `MAX_NESTING_DEPTH` | 1 (Folders can only be nested one level deep) |
| `MAX_SUBFOLDERS_PER_FOLDER` | 100 |
| `MAX_TASKS_PER_FOLDER` | 500 |
| `MAX_ATTACHMENTS_PER_FOLDER` | 1000 |
| `MAX_ATTACHMENT_SIZE_MB` | 5 MB |
| `MAX_TOTAL_TASKS` | 10000 |

## Core Types

- **`Course`**: Represents a top-level organization unit (e.g., a university course, a broad life category).
- **`Subject`**: Represents a sub-category or specific topic, typically nested within a Course.
- **Tasks Integration**: Tasks are no longer stored directly inside the Course/Subject objects (this approach is deprecated). Instead, tasks are managed in a central array and linked to a folder via `categoryId`.

## Validation Rules

- **Nesting**: `canAddSubfolder` prevents exceeding `MAX_NESTING_DEPTH` and `MAX_SUBFOLDERS_PER_FOLDER`.
- **Circular References**: `isCircularReference` guarantees that a folder cannot be set as its own parent or an ancestor of itself.
- **Task Capacity**: `canAddTask` checks both the workspace-wide limit (`MAX_TOTAL_TASKS`) and the folder-specific limit (`MAX_TASKS_PER_FOLDER`).
