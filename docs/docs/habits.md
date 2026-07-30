# Habits

Habit tracking in LifeXOS (`src/pages/Habits.tsx`) is designed to build consistency through customizable frequencies and visual history.

## Habit Frequencies

A habit can be configured with one of four recurrence patterns:
1. **Daily**: Expected to be completed every single day.
2. **Weekly**: Expected to be completed a specific number of times per week (`timesPerPeriod`).
3. **Monthly**: Expected to be completed a specific number of times per month (`timesPerPeriod`).
4. **Custom Days**: Expected to be completed on specific days of the week (e.g., Monday, Wednesday, Friday).

## Features

- **Streaks**: The app calculates and displays the user's current streak (consecutive completions based on the defined frequency).
- **Interactive Check-ins**: Clicking a habit triggers an animated burst and plays a completion sound.
- **Visual History**: The `HabitsHorizontalCalendar` component renders a 30-day heatmap. Each day shows a color-coded square based on the percentage of active habits completed on that day (ranging from grey/empty to deep green for 100% completion).
- **Inline Editing**: Users can edit the habit title or change the frequency directly from the habit card.
