# Component Library Reference

This document outlines the reusable UI widgets and components found in `src/components/` and their respective purposes.

## Core UI Components

| Component | Purpose | Props | Usage |
|-----------|---------|-------|-------|
| `AppLayout.tsx` | Main application shell containing sidebar, background, and rendering routes. | `children: ReactNode` | Used to wrap all main application pages. |
| `AppSidebar.tsx` | Application sidebar for primary navigation. | N/A | Used within `AppLayout`. |
| `AnimatedBackground.tsx` | Global animated background effect. | N/A | Displayed behind the app content. |
| `ErrorBoundary.tsx` | Catches React rendering errors and displays a fallback UI. | `children` | Wraps root component. |
| `ThemeProvider.tsx` | Provides dark/light mode theming context. | `children` | Wraps root component. |

## Feature Components

| Component | Purpose | Props | Usage |
|-----------|---------|-------|-------|
| `TaskItem.tsx` | Displays a single task with completion, deletion, edit, and drag-and-drop actions. | `task: Task`, `onToggle`, `onDelete`, `onUpdate`, `sortable`, `showMyDayBtn`, etc. | Used in `MyDay`, `ToDo`, `Planned`, `Planner` pages. |
| `SortableTaskList.tsx` | A list of `TaskItem`s with drag-and-drop support. | `tasks: Task[]`, action callbacks | Used wherever lists of tasks are rendered. |
| `GoalProgressCard.tsx` | Displays progress towards a specific goal. | `goal` | Used in Dashboard/Goals pages. |
| `HabitsHorizontalCalendar.tsx` | A scrollable horizontal calendar for habit tracking. | `habits`, `onToggleHabit` | Used in Habits view. |
| `OrbitAI.tsx` & `AICopilot.tsx` | AI assistant interface and integration. | various | Used for AI interactions. |

## UI & Utility Components

| Component | Purpose | Props | Usage |
|-----------|---------|-------|-------|
| `TiltCard.tsx` | A card that tilts based on mouse movement. | `children` | Used for interactive cards like tasks/goals. |
| `ProgressBar.tsx` | Visual progress indicator. | `progress: number` | Used to show completion of goals/habits. |
| `InteractiveEmptyState.tsx` | Engaging empty state when lists are empty. | `title`, `description`, `icon` | Used when task/habit lists have no items. |
| `QuickAdd.tsx` | Floating or inline quick add input for tasks/notes. | `onSubmit` | Used across pages to add new items. |
| `RushModeToggle.tsx` | Toggle button for 'Rush Mode' feature. | `onToggle` | Used in MyDay or Settings. |

## Shared UI (`src/components/ui/`)
Contains atomic generic components like `Button`, `Input`, `Select`, `Textarea`, `Skeleton`, built upon Radix UI / shadcn base.
