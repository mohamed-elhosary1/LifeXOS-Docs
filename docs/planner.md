# Planner

**Purpose:** The **Planner** feature in LifeXOS is designed to manage tasks, schedule events, and organize your daily agenda efficiently.
**Last Updated:** 2026-07-31



## Table of Contents
- [Overview](#overview)
- [Technical Implementation](#technical-implementation)
- [Data Model](#data-model)
- [Orbit AI Capabilities](#orbit-ai-capabilities)

## Overview

The Planner integrates a calendar view with a powerful task list, allowing users to block time for specific tasks. It heavily leverages `dnd-kit` for intuitive task reordering and scheduling.

### Key Features
- **Daily/Weekly/Monthly Views:** Flexible calendar displays.
- **Time Blocking:** Drag tasks onto the calendar to allocate time.
- **Task Prioritization:** Sort and filter tasks based on priority, context, or deadline.

## Technical Implementation

| Feature | Library / Tool | Description |
| :--- | :--- | :--- |
| Calendar View | `react-big-calendar` / Custom | Renders the timetable and handles date calculations. |
| Drag and Drop | `@dnd-kit/core` | Enables dragging tasks from the backlog onto the calendar grid. |
| Data Fetching | Supabase Client | Syncs tasks and events in real-time. |

## Data Model

Tasks are stored in the `tasks` table with the following core structure:

```sql
CREATE TABLE tasks (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users,
  title TEXT NOT NULL,
  description TEXT,
  status TEXT DEFAULT 'TODO', -- TODO, IN_PROGRESS, DONE
  due_date TIMESTAMP WITH TIME ZONE,
  scheduled_start TIMESTAMP WITH TIME ZONE,
  scheduled_end TIMESTAMP WITH TIME ZONE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## Orbit AI Capabilities

Orbit AI can analyze your Planner to suggest optimal times for unassigned tasks based on your historical productivity patterns and current workload.


**Related Documents:**
- [Index](index.md)