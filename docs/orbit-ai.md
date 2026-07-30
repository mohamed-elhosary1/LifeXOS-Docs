# Orbit AI

**Purpose:** Orbit AI is the intelligent, context-aware heart of LifeXOS. Unlike traditional chatbots that require explicit prompting, Orbit is designed to understand your life's context based on your workspaces, tasks, and habits.
**Last Updated:** 2026-07-31

## Table of Contents
- [Architecture & Integration](#architecture-integration)
- [Features](#features)
- [Future Development](#future-development)

## Architecture & Integration

Orbit AI is integrated directly into the frontend React application, leveraging custom hooks to manage its memory and proactive notification capabilities.

### Core Components

1. **`OrbitAI.tsx` & `OrbitAI.css`**
   - The primary UI component for the Orbit AI. It provides a chat interface, context displays, and actionable suggestions.
   - It is available globally across the application, typically accessed via a toggle in the application layout or sidebar.

2. **`useOrbitMemory.ts`**
   - **Purpose:** Manages the AI's contextual awareness.
   - **Functionality:** This hook listens to the user's current state (active workspace, current page, recently viewed notes) and feeds this metadata into the AI's context window. When a user asks a question like "What should I focus on today?", Orbit already knows what is in their `MyDay` view.

3. **`useOrbitNotifications.ts`**
   - **Purpose:** Handles proactive, non-intrusive nudges.
   - **Functionality:** Orbit AI can determine if a user is falling behind on a habit or has an impending deadline. This hook triggers toasts or subtle UI indicators to keep the user on track without being annoying.

## Features

- **Contextual Search & Summarization:** Ask Orbit to "Summarize my meeting notes from yesterday" or "Find the task related to the Q3 launch."
- **Task Generation:** Orbit can parse natural language (e.g., "Remind me to call John tomorrow at 5 PM") and automatically create structured tasks in your planner.
- **Productivity Insights:** By analyzing your habit completion rates and task velocity, Orbit can suggest schedule adjustments to prevent burnout.
- **Workflow Automation:** (Planned) Orbit will be able to trigger sequences of actions, such as setting up a new project folder structure with boilerplate tasks.

## Future Development

The roadmap for Orbit AI includes deeper integrations with the Supabase backend via Edge Functions to allow for heavy background processing (like embedding generation for semantic search across all notes and tasks) without impacting the frontend client performance.


**Related Documents:**
- [Index](index.md)