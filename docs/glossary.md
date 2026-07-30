# Glossary

**Purpose:** This document defines common terms, acronyms, and concepts used throughout the LifeXOS application and codebase.
**Last Updated:** 2026-07-31


---

### A

-   **Auth**: Short for Authentication/Authorization. LifeXOS uses Supabase Auth to manage user identities and access tokens.

### D

-   **dnd-kit**: A lightweight, performant, accessible and extensible drag & drop toolkit for React, used heavily in the Task Kanban boards and list reordering.

### G

-   **Goal**: A high-level objective in LifeXOS. Goals can have multiple Projects and Habits tied to them.

### H

-   **Habit**: A recurring action the user wishes to track. Habits build "streaks" upon consecutive completions.

### I

-   **IndexedDB**: A low-level API for client-side storage of significant amounts of structured data. Used by LifeXOS to enable offline mode.

### K

-   **Kanban**: A visual workflow management method. In LifeXOS, tasks can be viewed in a Kanban board (e.g., To Do, In Progress, Done).

### O

-   **Offline-First**: A development paradigm where the application is built to function without an internet connection as its primary state, syncing with the cloud only when a connection is available.
-   **Orbit AI**: The proprietary name for the Orbit AI integrated into LifeXOS, capable of generating tasks, summarizing notes, and providing contextual help.

### P

-   **PWA (Progressive Web App)**: A web application that uses modern web capabilities to deliver an app-like experience (installable, offline capable).
-   **Project**: A collection of Tasks and Notes aimed at completing a specific piece of work. Projects belong to Workspaces.

### R

-   **RLS (Row Level Security)**: A PostgreSQL feature (used via Supabase) that allows database policies to restrict which rows a user can access based on their authentication context.

### S

-   **shadcn/ui**: A collection of re-usable components built using Radix UI and Tailwind CSS, forming the foundation of LifeXOS's design system.
-   **Supabase**: The Backend-as-a-Service (BaaS) provider used by LifeXOS for PostgreSQL database hosting, authentication, and edge functions.

### T

-   **Task**: An actionable item with a distinct state (e.g., pending, completed).

### W

-   **Workspace**: The highest level of organization in LifeXOS. A user can have multiple workspaces (e.g., "Personal", "Work") to separate different areas of their life.

### Z

-   **Zustand**: A small, fast, and scalable bearbones state-management solution used in the React frontend of LifeXOS.


**Related Documents:**
- [Index](index.md)