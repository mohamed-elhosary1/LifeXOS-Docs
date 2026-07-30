# Workspace

**Purpose:** The **Workspace** is the central dashboard of LifeXOS. It aggregates all essential information—your upcoming tasks, current habits, pinned notes, and overarching goals—into a unified, high-level view.
**Last Updated:** 2026-07-31



## Table of Contents
- [Overview](#overview)
- [Component Architecture](#component-architecture)
- [State Management](#state-management)
- [Styling and Theming](#styling-and-theming)

## Overview

Built with React, Vite, and TailwindCSS, the Workspace is highly modular and interactive. It utilizes `framer-motion` for smooth transitions and `dnd-kit` for drag-and-drop customization.

### Key Features
- **Dashboard Widgets:** Customizable widgets displaying data from Planner, Habits, Notes, and Goals.
- **Drag-and-Drop Layout:** Users can arrange widgets according to their preference using `dnd-kit`.
- **Orbit AI Integration:** Quick access to the Orbit AI for summarizing day's activities.

## Component Architecture

| Component | Description | Location |
| :--- | :--- | :--- |
| `WorkspaceView.tsx` | The main container for the workspace dashboard. | `src/features/workspace/` |
| `WidgetGrid.tsx` | Handles the layout and rendering of individual widgets. | `src/features/workspace/components/` |
| `DraggableWidget.tsx` | Wrapper component providing drag-and-drop functionality via `dnd-kit`. | `src/features/workspace/components/` |

## State Management

Workspace layout preferences are stored in the user's preferences table in Supabase.

```typescript
// Example Interface for Workspace Configuration
interface WorkspaceConfig {
  widgets: string[]; // List of widget IDs
  layout: {
    [widgetId: string]: { x: number; y: number; w: number; h: number };
  };
}
```

## Styling and Theming

The Workspace relies heavily on Shadcn/UI for consistent component design and TailwindCSS for responsive grid layouts. Dark and light modes are fully supported.


**Related Documents:**
- [Index](index.md)