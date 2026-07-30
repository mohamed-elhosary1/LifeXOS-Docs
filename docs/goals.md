# Goals

**Purpose:** The **Goals** module in LifeXOS helps users define long-term objectives and break them down into actionable milestones and tasks.
**Last Updated:** 2026-07-31



## Table of Contents
- [Overview](#overview)
- [Technical Implementation](#technical-implementation)

## Overview

Goals use an OKR (Objectives and Key Results) inspired structure, ensuring that high-level ambitions translate into daily actions.

### Key Features
- **Goal Hierarchy:** Create overarching goals with specific milestones underneath.
- **Progress Tracking:** Automatically calculate progress based on completed milestones or linked tasks.
- **Vision Board:** A visual representation of your goals.

## Technical Implementation

### Components

- `GoalDashboard.tsx`: High-level view of all active goals.
- `GoalDetail.tsx`: Detailed view showing milestones, linked notes, and tasks.
- `ProgressBar.tsx`: Reusable UI component (Shadcn) to visually indicate completion percentage.

### Data Model

```sql
CREATE TABLE goals (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users,
  title TEXT NOT NULL,
  description TEXT,
  target_date DATE,
  status TEXT DEFAULT 'ACTIVE',
  progress INTEGER DEFAULT 0, -- 0 to 100
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE milestones (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  goal_id UUID REFERENCES goals ON DELETE CASCADE,
  title TEXT NOT NULL,
  completed BOOLEAN DEFAULT FALSE,
  due_date DATE
);
```

### State Management

When a milestone is marked as complete, a Supabase Database Trigger (or application-level logic) recalculates the `progress` of the parent `goal`.


**Related Documents:**
- [Index](index.md)