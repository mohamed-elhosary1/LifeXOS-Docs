# Technology Stack

**Purpose:** LifeXOS leverages a modern, cutting-edge technology stack designed for rapid development, exceptional performance, and a beautiful user experience.
**Last Updated:** 2026-07-31



## Table of Contents
- [Frontend Core](#frontend-core)
- [UI & Styling](#ui-styling)
- [State Management & Data Handling](#state-management-data-handling)
- [Backend & Infrastructure](#backend-infrastructure)
- [Desktop Support](#desktop-support)
- [Testing & Quality Assurance](#testing-quality-assurance)

## Frontend Core

| Technology | Purpose |
|------------|---------|
| **React 18** | The core UI library. We utilize hooks, concurrent rendering, and strict mode. |
| **Vite** | Next-generation frontend tooling. It provides lightning-fast HMR (Hot Module Replacement) and optimized production builds. |
| **TypeScript** | Ensures type safety across the entire application, preventing runtime errors and improving developer experience. |
| **React Router DOM** | Handles client-side routing, enabling the Single Page Application (SPA) experience without page reloads. |

## UI & Styling

| Technology | Purpose |
|------------|---------|
| **Tailwind CSS** | Utility-first CSS framework for rapid UI styling directly within JSX. |
| **shadcn/ui** | A collection of beautifully designed, accessible, and customizable components (Radix UI primitives combined with Tailwind). |
| **Framer Motion** | Powers fluid animations and page transitions across the app (`AdMotion.tsx`, `AnimatedBackground.tsx`). |
| **Lucide React** | A clean, consistent icon library. |
| **canvas-confetti** | Used for rewarding user interactions (e.g., completing a major goal or all daily tasks). |

## State Management & Data Handling

| Technology | Purpose |
|------------|---------|
| **TanStack React Query** | (Planned/Integrated) For robust data fetching, caching, synchronization, and optimistic UI updates. |
| **@dnd-kit** | A lightweight, performant, accessible drag-and-drop toolkit for React. Crucial for our sortable task lists and folder grids. |
| **date-fns** | Modern JavaScript date utility library for parsing, formatting, and manipulating dates in the Planner and Habits modules. |
| **Recharts** | Composable charting library built on React components, used for rendering data visualizations in the Insights module. |

## Backend & Infrastructure

| Technology | Purpose |
|------------|---------|
| **Supabase** | The open-source Firebase alternative. Provides our PostgreSQL database, Authentication, and Real-time APIs via `@supabase/supabase-js`. |

## Desktop Support

| Technology | Purpose |
|------------|---------|
| **Electron** | Packages the web application into a native cross-platform desktop app (Windows, macOS, Linux). |
| **electron-builder** | Tooling to compile and build the Electron executables. |

## Testing & Quality Assurance

| Technology | Purpose |
|------------|---------|
| **ESLint & Prettier** | Code linting and formatting. |
| **Vitest** | A Vite-native unit testing framework for testing hooks and utility functions. |
| **Playwright** | End-to-End (E2E) testing framework to ensure critical user flows (auth, task creation) work flawlessly. |
| **Sentry** | Error tracking and performance monitoring in production (`@sentry/react`). |


**Related Documents:**
- [Index](index.md)