# Contributing to LifeXOS

**Purpose:** First off, thank you for considering contributing to LifeXOS! It's people like you that make LifeXOS such a great tool. 
**Last Updated:** 2026-07-31



## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Architecture Overview for Contributors](#architecture-overview-for-contributors)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct. Please be respectful, constructive, and inclusive.

## How Can I Contribute?

### 1. Reporting Bugs
- Check the issues to ensure the bug hasn't already been reported.
- Use the **Bug Report** issue template.
- Include detailed steps to reproduce, expected behavior, and your environment details (OS, browser, app version).

### 2. Suggesting Enhancements
- Open an issue using the **Feature Request** template.
- Explain *why* this enhancement would be useful and how it fits into the LifeXOS ecosystem.

### 3. Submitting Pull Requests
- Fork the repository and create your branch from `main`.
- If you've added code that should be tested, add tests!
- Ensure the test suite passes (`npm test`).
- Format your code (`npm run lint` and `npm run format`).
- Write descriptive commit messages following the Conventional Commits specification.

---

## Development Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-org/lifexos.git
   cd lifexos
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Set up Environment Variables:**
   Copy `.env.example` to `.env.local` and fill in your Supabase credentials.

4. **Start the development server:**
   ```bash
   npm run dev
   ```

---

## Architecture Overview for Contributors

Before diving in, familiarize yourself with our stack:
-   **Framework**: React (Vite)
-   **Styling**: TailwindCSS + shadcn/ui
-   **State**: Zustand + React Query
-   **Backend**: Supabase
-   **Drag & Drop**: dnd-kit

Please refer to the `architecture.md` and `testing.md` files for deeper dives into specific areas.

## Pull Request Process

1.  Update the README.md with details of changes to the interface, if applicable.
2.  Update the documentation in the `/docs` folder if you are introducing a new feature or modifying architecture.
3.  Your PR will be reviewed by at least one core maintainer.
4.  Once approved, it will be merged using "Squash and Merge".


**Related Documents:**
- [Index](index.md)