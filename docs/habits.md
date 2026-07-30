# Habits

**Purpose:** The **Habits** tracker in LifeXOS enables users to build positive routines and break negative ones through consistent tracking and visualization.
**Last Updated:** 2026-07-31



## Table of Contents
- [Overview](#overview)
- [Technical Implementation](#technical-implementation)

## Overview

Habits are tracked daily. The system uses a streak-based visualization mechanism similar to GitHub's contribution graph to encourage consistency.

### Key Features
- **Daily Check-ins:** Mark habits as complete with a single click.
- **Progress Visualizations:** Heatmaps and streak counters.
- **Flexible Scheduling:** Support for habits that occur daily, specific days of the week, or a set number of times per week.

## Technical Implementation

### Components

- `HabitList.tsx`: Displays the list of habits for the current day.
- `HabitHeatmap.tsx`: A calendar-like visualization showing historical completion data.
- `HabitForm.tsx`: Interface for creating or editing habit definitions.

### Data Model

The Habit system involves two main tables:

1.  **`habits`**: Defines the habit itself.
2.  **`habit_logs`**: Records completions.

```sql
CREATE TABLE habits (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users,
  name TEXT NOT NULL,
  frequency JSONB NOT NULL, -- e.g., {"type": "daily"} or {"type": "weekly", "days": [1,3,5]}
  color TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE habit_logs (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  habit_id UUID REFERENCES habits ON DELETE CASCADE,
  completed_date DATE NOT NULL,
  status TEXT DEFAULT 'COMPLETED',
  UNIQUE(habit_id, completed_date)
);
```

### Framer Motion Animations

When a user completes a habit, `framer-motion` is used to provide satisfying visual feedback (e.g., a subtle pop or checkmark animation).


**Related Documents:**
- [Index](index.md)