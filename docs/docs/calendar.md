# Calendar & Planned View

The Planned page (`src/pages/Planned.tsx`) provides a dual-pane interface combining a high-level monthly calendar with a granular weekly timeline.

## Monthly Calendar Heatmap (Left Pane)

- **Productivity Scoring**: Each day is assigned a productivity score (0.0 to 1.0) based on:
  - Task completion ratio (60% weight if habits exist).
  - Habit completion ratio (40% weight if tasks exist).
- **Perfect Days**: A day is marked "Perfect" (rendered with a shimmering gold gradient) if all tasks and all habits are completed.
- **Heatmap Colors**: Non-perfect days are colored with varying shades of green depending on the score.
- **Details Modal**: Clicking on any specific day in the calendar opens a modal displaying the exact tasks and habits scheduled for that day, along with their completion status.

## Weekly Timeline (Right Pane)

- **Week Navigation**: Users can page forward and backward week-by-week.
- **Expired Tasks List**: Automatically highlights scheduled tasks that are past their deadline but remain uncompleted.
- **Daily Task Lists**: Renders a vertical list of days for the currently selected week. Each day displays the tasks explicitly scheduled or deadlined for that date.
