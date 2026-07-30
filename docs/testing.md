# Testing Strategy

**Purpose:** At LifeXOS, testing is a critical part of our CI/CD pipeline. We believe in shipping fast, but not at the cost of stability. This document outlines our testing philosophy and tools.
**Last Updated:** 2026-07-31



## Table of Contents
- [The Testing Pyramid](#the-testing-pyramid)
- [Tools We Use](#tools-we-use)
- [Writing Unit and Component Tests](#writing-unit-and-component-tests)
- [Writing End-to-End Tests](#writing-end-to-end-tests)
- [CI/CD Integration](#cicd-integration)
- [Running Tests Locally](#running-tests-locally)

## The Testing Pyramid

We adhere to the classic testing pyramid:
1.  **Unit Tests**: (Many) Fast, isolated tests for utility functions and hooks.
2.  **Integration Tests**: (Some) Tests for component interactions and data fetching.
3.  **End-to-End (E2E) Tests**: (Few) High-level tests covering critical user flows.

---

## Tools We Use

| Test Type | Tool | Purpose |
| :--- | :--- | :--- |
| **Unit** | Vitest | Fast test runner, API compatible with Jest. |
| **Component** | React Testing Library | Testing components from the user's perspective. |
| **E2E** | Playwright | Cross-browser automation for full flows. |
| **Mocking** | MSW (Mock Service Worker) | Intercepting network requests for API mocking. |

---

## Writing Unit and Component Tests

We use Vitest and React Testing Library (RTL).

### Guidelines
-   Test **behavior**, not implementation details.
-   Query elements using accessible roles (`getByRole`, `getByLabelText`) rather than test IDs where possible.
-   Use MSW to mock Supabase calls.

### Example: Testing a Component

```tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { TaskItem } from './TaskItem';

test('toggles task completion status', async () => {
  const mockOnToggle = vi.fn();
  const task = { id: '1', title: 'Buy milk', completed: false };

  render(<TaskItem task={task} onToggle={mockOnToggle} />);

  const checkbox = screen.getByRole('checkbox', { name: /buy milk/i });
  fireEvent.click(checkbox);

  expect(mockOnToggle).toHaveBeenCalledWith('1', true);
});
```

---

## Writing End-to-End Tests

We use Playwright for E2E tests. These run against a deployed staging environment or a fully built local environment.

### Critical Flows Covered by E2E
1. User Registration and Login.
2. Creating a Workspace.
3. Creating, editing, and completing a Task.
4. Saving a Note and verifying offline sync (simulated).

### Example: Playwright Test

```typescript
import { test, expect } from '@playwright/test';

test('user can create a new goal', async ({ page }) => {
  await page.goto('/dashboard');
  
  // Navigate to Goals
  await page.click('text=Goals');
  
  // Create Goal
  await page.click('button:has-text("New Goal")');
  await page.fill('input[name="title"]', 'Run a Marathon');
  await page.click('button:has-text("Save")');

  // Verify
  await expect(page.locator('text=Run a Marathon')).toBeVisible();
});
```

---

## CI/CD Integration

All tests run automatically on GitHub Actions for every Pull Request.
-   **PRs cannot be merged** if tests fail.
-   Test coverage reports are generated automatically. We aim for **80% coverage** on core utilities and hooks.

## Running Tests Locally

- `npm run test`: Runs Vitest in watch mode.
- `npm run test:ui`: Runs Vitest with the UI dashboard.
- `npm run test:e2e`: Runs Playwright tests (ensure local server is running).


**Related Documents:**
- [Index](index.md)