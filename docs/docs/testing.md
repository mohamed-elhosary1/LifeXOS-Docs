# Testing

LifeXOS utilizes a dual testing strategy.

## Unit and Component Testing
- **Vitest**: Configured via `vitest.config.ts` for fast unit tests.
- Uses `@testing-library/react` and `@testing-library/jest-dom` for assertions.

## End-to-End (E2E) Testing
- **Playwright**: Configured in `playwright.config.ts`.
- **Base URL**: Runs against `http://localhost:8080`.
- **Target Environments**: Tests execute across:
  - Desktop Chromium
  - Mobile Chrome (Pixel 5 simulation)
  - Mobile Safari (iPhone 12 simulation)
- **CI Optimizations**: In CI environments, workers are reduced to 1 and retries are enabled to handle flake.
- The web server is automatically spun up before tests using `npm run dev`.
