# Authentication

**Purpose:** LifeXOS utilizes **Supabase Auth** for secure, robust, and scalable user authentication.
**Last Updated:** 2026-07-31



## Table of Contents
- [Overview](#overview)
- [Implementation Details](#implementation-details)
- [Security (Row Level Security)](#security-row-level-security)

## Overview

Supabase provides a complete identity suite out of the box, seamlessly integrating with the PostgreSQL database via Row Level Security (RLS).

### Supported Methods
- **Email / Password:** Standard credential login.
- **OAuth Providers:** (e.g., Google, GitHub) for quick access.
- **Magic Links:** Passwordless email login.

## Implementation Details

### Client-Side Setup

The authentication state is managed via the Supabase Javascript Client and exposed to the React application via a Context Provider.

```typescript
// Example: src/contexts/AuthContext.tsx
import { createContext, useContext, useEffect, useState } from 'react';
import { supabase } from '@/lib/supabase';
import { Session, User } from '@supabase/supabase-js';

// Setup provider to wrap the application and provide user state
```

### Route Protection

React Router is used to protect routes that require authentication.

```typescript
// Example Route Wrapper
const ProtectedRoute = ({ children }) => {
  const { user } = useAuth();
  if (!user) return <Navigate to="/login" replace />;
  return children;
};
```

## Security (Row Level Security)

All user data is protected at the database level using PostgreSQL Row Level Security. A user can only access rows where `user_id` matches their authenticated ID.

```sql
-- Example RLS Policy
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view their own tasks" ON tasks
  FOR SELECT USING (auth.uid() = user_id);
```


**Related Documents:**
- [Index](index.md)