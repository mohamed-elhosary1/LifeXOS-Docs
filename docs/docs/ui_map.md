# UI Map

This document outlines the screens and navigation hierarchy in the application.

## Main Screens (Pages)

- **Landing (`Landing.tsx`)**: The initial entry point for non-authenticated users. Shows app features.
- **Auth (`Auth.tsx`)**: Login/Signup flows.
- **My Day (`MyDay.tsx`)**: The dashboard for today's focus. Displays tasks added to "My Day", daily habits, and quick insights.
- **To Do (`ToDo.tsx`)**: A master list of all uncompleted tasks.
- **Planner (`Planner.tsx`)**: Calendar or time-blocking view to schedule tasks over days/weeks.
- **Planned (`Planned.tsx`)**: Shows upcoming tasks filtered by scheduled dates.
- **Habits (`Habits.tsx`)**: Interface for creating, tracking, and viewing habit streaks.
- **Goals (`Goals.tsx`)**: High-level goal tracking, broken down into milestones or tasks.
- **Study / Pomodoro (`Study.tsx`, `Pomodoro.tsx`)**: Focus timers and study sessions tracking.
- **Notes (`Notes.tsx`)**: Rich text or markdown note-taking.
- **Insights (`Insights.tsx`)**: Analytics and statistics on user productivity (tasks completed, habit streaks).
- **Settings (`Settings.tsx`)**: App configuration, theme toggle, and account management.
- **Admin (`Admin/`)**: Administrative dashboard (if applicable).

## User Flows

1. **Onboarding**: User arrives at Landing -> Auth -> Complete Onboarding (`OnboardingModal.tsx`) -> Redirect to `My Day`.
2. **Task Management**: User creates a task in `ToDo` -> Assigns a date (moves to `Planned`) -> Flags for today (moves to `MyDay`).
3. **Daily Routine**: User opens `MyDay` -> Starts a `Pomodoro` timer for a task -> Marks task complete -> Checks off daily `Habits`.
4. **Navigation**: Users traverse these screens primarily via the `AppSidebar.tsx` navigation menu.
