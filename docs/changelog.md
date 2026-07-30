# Changelog

**Purpose:** All notable changes to the LifeXOS project will be documented in this file.
**Last Updated:** 2026-07-31



## Table of Contents
- [[Unreleased]](#unreleased)
- [[1.2.0] - 2026-07-15](#120-2026-07-15)
- [[1.1.0] - 2026-05-20](#110-2026-05-20)
- [[1.0.0] - 2026-02-10](#100-2026-02-10)

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Early prototype for Calendar integration.

---

## [1.2.0] - 2026-07-15

### Added
- **Kanban View**: Tasks can now be viewed and dragged in a Kanban board layout (using `dnd-kit`).
- **Orbit AI Summaries**: Select any Note and click the magic wand to generate an instant executive summary.
- **Custom Habit Frequencies**: You can now set habits to occur "3 times a week" or "every other day".

### Changed
- Migrated global state management from Redux to Zustand for better performance and simplicity.
- Updated shadcn/ui components to the latest versions.

### Fixed
- Resolved an issue where offline mutations would duplicate if the network dropped during a sync cycle.
- Fixed layout shift (CLS) on the dashboard during initial load.

---

## [1.1.0] - 2026-05-20

### Added
- **Dark Mode Support**: Full system-aware dark mode implementation using Tailwind CSS.
- **Export Data**: Users can now export their workspaces as JSON.
- **Keyboard Shortcuts**: Added a global command palette accessible via `Cmd/Ctrl + K`.

### Changed
- Improved accessibility (a11y) across all modal dialogs and dropdown menus.
- Optimized image loading strategies.

### Fixed
- Fixed a bug where completed tasks would sometimes reappear after a page refresh.

---

## [1.0.0] - 2026-02-10

### Added
- Initial public release! 🎉
- Workspaces and Projects hierarchy.
- Rich-text Notes editor.
- Task tracking with subtasks.
- Daily Habit tracker.
- Basic integration with Orbit AI for task generation.
- Offline-first architecture using Service Workers and IndexedDB.
- Supabase backend integration for Auth and Database.


**Related Documents:**
- [Index](index.md)