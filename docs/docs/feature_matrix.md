# Feature Matrix

| Feature | Status | Current Implementation | Known Limitations | Future Improvements |
|---------|--------|------------------------|-------------------|---------------------|
| Task Management | Implemented | Create, edit, delete, drag-and-drop reorder, assign to My Day. Uses `TaskItem`. | Nested subtasks not fully supported. | Recurring tasks, advanced filtering. |
| Habit Tracking | Implemented | Create habits, daily check-offs via `HabitsHorizontalCalendar`. | Missing advanced streak analytics. | Custom habit schedules (e.g., every Tue/Thu). |
| Goal Setting | Implemented | Define goals, track progress via `GoalProgressCard`. | Integration between tasks and goals is basic. | Auto-update goals based on linked tasks. |
| AI Copilot (Orbit AI) | Implemented | Integrated via `OrbitAI.tsx` and `AICopilot.tsx`. Provides suggestions and parsing. | Dependent on external API availability. | Better context awareness of user's past data. |
| Focus / Pomodoro | Implemented | Timer functionality in `Pomodoro.tsx` & `Study.tsx`. | Cannot run timer in background perfectly without service workers. | Sync timer across devices. |
| Notes | Implemented | Note creation and editing in `Notes.tsx`. | Basic text/markdown editing. | Image uploads, folder organization. |
| Rush Mode | Implemented | `RushModeToggle.tsx` provides quick entry/action state. | Unknown. | Not implemented. |
| Localization / Themes | Implemented | Dark/Light mode (`ThemeProvider.tsx`), multi-language support. | Custom color palettes not fully implemented. | Allow users to create custom themes. |
