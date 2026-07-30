# Goals

The Goals feature (`src/pages/Goals.tsx`) allows users to create actionable plans linked to specific deadlines.

## PlanGoals

Goals are internally referred to as `PlanGoal` objects. Unlike standalone tasks or broad folders, a PlanGoal tracks progress by aggregating the completion status of specific tracked items.

### Key Attributes
- **Title & Deadline**: A user-defined string and a strict deadline date.
- **Tracked Items**: A Goal can track:
  - Specific, individual Task IDs.
  - Entire Groups (Course IDs, Subject IDs, or other LifeGoal IDs). If a group is selected, all tasks belonging to that group contribute to the goal's progress.

### Visualization & Progress
- **Progress Bar**: Calculates the percentage of completed tasks versus total tracked tasks.
- **Status Indicators**: Shows the number of days left until the deadline, or flags the goal as "Overdue" if the deadline has passed.
- **Completion**: When 100% of the tracked tasks are completed, the goal is automatically marked as completed.
