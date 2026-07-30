# Offline Mode Architecture

**Purpose:** LifeXOS is designed as a "local-first" or "offline-capable" application. We believe your Life OS should be accessible even when you are on an airplane or facing spotty internet connections.
**Last Updated:** 2026-07-31



## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Handling Conflicts](#handling-conflicts)
- [Developer Guidelines for Offline Features](#developer-guidelines-for-offline-features)
- [Limitations](#limitations)

This document outlines how offline mode is implemented, the technologies used, and guidelines for developers adding new features.

---

## Architecture Overview

We use a combination of **Service Workers**, **IndexedDB**, and **Optimistic UI Updates** to provide a seamless offline experience.

### 1. Service Workers (Caching)

Service Workers intercept network requests and serve cached static assets (HTML, CSS, JS, Images) when offline. 
We use Vite PWA plugin to manage our service worker.

*   **Strategy**: Cache-First for static assets, Network-First for API responses (where applicable).

### 2. IndexedDB (Local Data Store)

All user data fetched from Supabase is mirrored locally in IndexedDB. 
We use `idb` or a wrapper library like `Dexie.js` or `RxDB` (depending on the module) for querying local data.

### 3. Synchronization Engine

When a user performs an action while offline (e.g., creating a task):
1.  The UI updates immediately (Optimistic UI).
2.  The change is saved to the local IndexedDB.
3.  A "mutation event" is added to an offline queue.
4.  When the network is restored, the queue is processed sequentially, sending the changes to Supabase.

---

## Handling Conflicts

Since LifeXOS can run on multiple devices (e.g., laptop and phone), offline edits can result in conflicts.

**Resolution Strategy: Last-Write-Wins (LWW)**
Currently, we use a simple Last-Write-Wins strategy based on the `updated_at` timestamp.

> [!NOTE]
> Future roadmap items include exploring CRDTs (Conflict-free Replicated Data Types) for more complex document editing (like Notes).

---

## Developer Guidelines for Offline Features

When building a new feature in LifeXOS, follow these steps to ensure offline compatibility:

### 1. Define Local Schema
Ensure your IndexedDB schema matches your Supabase schema.

### 2. Use Data Hooks correctly
Wrap your Supabase calls in our custom data hooks (`useOfflineQuery`, `useOfflineMutation`).

```typescript
// Example: Using an offline mutation
const { mutate } = useOfflineMutation({
  mutationFn: (newTask) => supabase.from('tasks').insert(newTask),
  onMutate: async (newTask) => {
    // 1. Cancel outgoing refetches
    // 2. Snapshot previous value
    // 3. Optimistically update local cache
  },
  onError: (err, newTask, context) => {
    // Rollback to snapshot
  }
});
```

### 3. Testing Offline State
You can simulate offline mode in Chrome DevTools:
1. Open DevTools (F12).
2. Go to the **Network** tab.
3. Change the throttling dropdown from "No throttling" to "Offline".
4. Verify your feature handles the offline state gracefully without crashing.

## Limitations

- **Orbit AI**: AI features require a network connection and are disabled gracefully in offline mode.
- **Large Attachments**: Files and large images are not cached by default to save storage space.


**Related Documents:**
- [Index](index.md)