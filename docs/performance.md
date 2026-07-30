# Performance Guidelines

**Purpose:** LifeXOS aims to be lightning-fast. A sluggish "Life OS" is frustrating and unusable. This document covers our performance budgets, rendering strategies, and optimization techniques.
**Last Updated:** 2026-07-31



## Table of Contents
- [Core Metrics](#core-metrics)
- [React Rendering Optimizations](#react-rendering-optimizations)
- [State Management](#state-management)
- [Animation Performance](#animation-performance)
- [Bundle Size Management](#bundle-size-management)
- [Analyzing Performance](#analyzing-performance)

## Core Metrics

We measure our performance against standard Web Vitals:
- **LCP (Largest Contentful Paint)**: < 2.5s
- **FID (First Input Delay)**: < 100ms
- **CLS (Cumulative Layout Shift)**: < 0.1

---

## React Rendering Optimizations

### 1. Memoization
Use `React.memo`, `useMemo`, and `useCallback` judiciously. 
*Do not* over-memoize simple components, as the comparison cost can outweigh the re-render cost. 
*Do* memoize complex lists (like the Task List or Calendar grid) and heavy computational functions.

### 2. Virtualization
For long lists (e.g., a year's worth of habits, or hundreds of tasks), always use virtualization. We recommend `@tanstack/react-virtual`.

```tsx
// Example Virtualized List
import { useVirtualizer } from '@tanstack/react-virtual'

function TaskList({ tasks }) {
  const parentRef = React.useRef(null)
  
  const rowVirtualizer = useVirtualizer({
    count: tasks.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
  })

  // Render...
}
```

### 3. Code Splitting
Use React `lazy` and `Suspense` to split the bundle based on routes. The Settings panel, for example, shouldn't be loaded until the user navigates there.

---

## State Management

We use React Context and Zustand.
-   **Zustand**: Use for global, frequently updating state (like UI toggles, current workspace).
-   **React Query**: Use for server state. It handles caching, deduplication, and background refetching automatically.

> [!TIP]
> When using Zustand, always select specifically what you need to avoid unnecessary re-renders:
> `const theme = useStore((state) => state.theme);` (Good)
> `const state = useStore(); const theme = state.theme;` (Bad)

---

## Animation Performance

We use **Framer Motion** for animations.
-   Always animate `transform` and `opacity` properties. These are GPU-accelerated.
-   **Avoid** animating `width`, `height`, `top`, `left`, `margin`, or `padding`, as these trigger expensive layout recalculations (reflows).
-   Use `layout` prop in Framer Motion sparingly, only for complex shared element transitions.

---

## Bundle Size Management

We monitor our bundle size via Vite rollup plugins.
-   **Imports**: Be careful with heavy libraries. Use modular imports (e.g., `import { format } from 'date-fns'` instead of `import * as dateFns from 'date-fns'`).
-   **Icons**: We use `lucide-react`. Ensure the bundler tree-shakes unused icons.

## Analyzing Performance

To profile LifeXOS:
1.  Run the production build: `npm run build && npm run preview`.
2.  Open Chrome DevTools -> **Performance** tab.
3.  Record a trace while interacting with the app.
4.  Look for long tasks (red bars) and identify the components causing them using the React DevTools Profiler.


**Related Documents:**
- [Index](index.md)