# API & Data Fetching

**Purpose:** LifeXOS primarily interacts with the database directly from the client using the **Supabase JavaScript Client**.
**Last Updated:** 2026-07-31



## Table of Contents
- [Overview](#overview)
- [Example: Fetching Tasks](#example-fetching-tasks)
- [Edge Functions (Serverless API)](#edge-functions-serverless-api)

## Overview

By leveraging Supabase, we bypass the need for a traditional middleware REST API for most CRUD operations. The client securely queries the PostgreSQL database, restricted by Row Level Security (RLS).

### Data Fetching Strategy

LifeXOS uses **React Query (TanStack Query)** to manage asynchronous state, caching, and background updates.

| Technology | Purpose |
| :--- | :--- |
| `@supabase/supabase-js` | The transport layer; executes queries against the DB. |
| `@tanstack/react-query` | State management; handles caching, loading states, and refetching. |

## Example: Fetching Tasks

```typescript
import { useQuery } from '@tanstack/react-query';
import { supabase } from '@/lib/supabase';

// 1. Define the fetcher function
const fetchTasks = async () => {
  const { data, error } = await supabase
    .from('tasks')
    .select('*')
    .order('due_date', { ascending: true });

  if (error) throw new Error(error.message);
  return data;
};

// 2. Create a custom hook
export const useTasks = () => {
  return useQuery({
    queryKey: ['tasks'],
    queryFn: fetchTasks,
  });
};
```

## Edge Functions (Serverless API)

For operations that cannot be performed securely on the client (e.g., interacting with third-party APIs like OpenAI for "Orbit AI", handling webhooks, or complex data processing), LifeXOS uses **Supabase Edge Functions**.

Edge Functions are written in TypeScript, run on Deno, and are deployed globally.


**Related Documents:**
- [Index](index.md)