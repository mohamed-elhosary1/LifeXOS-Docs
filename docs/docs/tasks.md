# Tasks & My Day

Task management in LifeXOS is divided into two primary domains: the central **To-Do** inbox and the **My Day** daily planner.

## To-Do List (`src/pages/ToDo.tsx`)

The To-Do page acts as an inbox for tasks that are not explicitly assigned to a specific day or folder. 
- **Central Tasks Array**: All tasks are stored in a unified array in `store.ts`.
- **Unassigned Tasks**: Tasks without a `categoryId` or categorized as `"general"`.
- **Categorization**: Users can seamlessly move tasks to specific "Sections" (Courses, Subjects, or Goals).
- **On Hold**: Tasks can be marked as "On Hold", hiding them from the active list but keeping them pending.
- **Completion**: Completed tasks are moved to a collapsible "Completed" section.

## My Day Planner (`src/pages/MyDay.tsx`)

The My Day page provides a focused, daily view for executing tasks.
- **Time Groups**: Tasks can be drag-and-dropped into specific time blocks:
  - Morning
  - Afternoon
  - Night
  - Anytime
- **Interactive UI**: DndKit is used to enable drag-and-drop sorting and group assignment.
- **Progress Tracking**: A progress bar tracks the ratio of completed tasks to total tasks scheduled for the day.
- **Neglected Items**: The system detects items that have been ignored for a long time. Users can "Snooze" these warnings.
- **Upcoming Exams**: A widget dynamically pulls exams scheduled within the next 14 days and highlights them with urgency colors based on proximity.
- **Quick Habits**: Habits scheduled for the current day are rendered inline, allowing users to check them off directly from the My Day view, complete with a confetti celebration.
