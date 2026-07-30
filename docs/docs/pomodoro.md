# Pomodoro & Study Timer

The Pomodoro page (`src/pages/Pomodoro.tsx` & `src/lib/pomodoroStore.ts`) combines a focus timer with automatic study session logging.

## Timer Mechanics
- **Focus & Break Modes**: The timer cycles between work sessions and break sessions. Sound alerts notify the user upon completion of a segment.
- **Elapsed Time Tracking**: The timer calculates elapsed seconds based on real wall-clock time (`Date.now() - startedAt`). This ensures the timer remains accurate even if the browser tab is suspended or minimized.
- **Presets**: Users can select predefined work/break intervals (e.g., 25/5, 50/10, 90/20) or define custom preferences in their settings.

## Automatic Session Logging
When a work segment exceeds 1 minute (or completes successfully), the app automatically creates a `StudySession` record. This record logs the `durationMinutes`, the specific date, and associates the time with the active Course, Subject, or Task.

## Task Queuing & Fast Map
- **Task Queue**: Users can select a specific Section (Course/Subject) and queue multiple tasks. The timer will display the "Up Next" list.
- **Auto-Advance**: When the current task is marked "Done", it is crossed off, and the timer automatically advances the focus to the next task in the queue.
- **Fast Map Panel**: An integrated sidebar component that allows users to view and update notes for the currently active task without leaving the timer interface.

## Manual Logging
A "Log Time" utility is provided for users to manually enter study minutes retroactively, associating them with a specific section or custom label.
