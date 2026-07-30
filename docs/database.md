# Database Architecture

**Purpose:** LifeXOS is powered by **PostgreSQL**, hosted on **Supabase**. This provides a robust, relational data structure with the added benefits of real-time subscriptions and vector embeddings for AI.
**Last Updated:** 2026-07-31



## Table of Contents
- [Overview](#overview)
- [Core Schema Structure](#core-schema-structure)
- [Row Level Security (RLS)](#row-level-security-rls)
- [pgvector and AI](#pgvector-and-ai)

## Overview

The schema is designed to be highly relational, linking core features (Habits, Tasks, Notes, Goals) together while maintaining strict isolation between user accounts.

## Core Schema Structure

| Table | Description |
| :--- | :--- |
| `users` | Extended profile data (managed by Supabase Auth). |
| `tasks` | Items for the Planner and general to-dos. |
| `habits` & `habit_logs` | Habit definitions and daily completion records. |
| `notes` & `folders` | Knowledge base documents and their hierarchy. |
| `goals` & `milestones` | Long-term objectives and actionable steps. |

## Row Level Security (RLS)

Security is enforced at the database layer. Every table that stores user data MUST have RLS enabled.

```sql
-- Standard RLS Template
ALTER TABLE [table_name] ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Enable read for users based on user_id" ON [table_name] FOR SELECT USING (auth.uid() = user_id);
CREATE POLICY "Enable insert for authenticated users only" ON [table_name] FOR INSERT WITH CHECK (auth.uid() = user_id);
CREATE POLICY "Enable update for users based on user_id" ON [table_name] FOR UPDATE USING (auth.uid() = user_id);
CREATE POLICY "Enable delete for users based on user_id" ON [table_name] FOR DELETE USING (auth.uid() = user_id);
```

## pgvector and AI

For the "Orbit AI" features, we utilize the `pgvector` extension to store embeddings of notes and tasks, enabling semantic search capabilities.

```sql
-- Enabling the vector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Example: Adding an embedding column to notes
ALTER TABLE notes ADD COLUMN embedding vector(1536); -- Size depends on the embedding model (e.g., OpenAI text-embedding-ada-002)
```


**Related Documents:**
- [Index](index.md)