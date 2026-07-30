# Notes

**Purpose:** The **Notes** application within LifeXOS serves as a personal knowledge base. It supports rich text formatting, markdown, and hierarchical organization.
**Last Updated:** 2026-07-31



## Table of Contents
- [Overview](#overview)
- [Technical Implementation](#technical-implementation)
- [Orbit AI Capabilities](#orbit-ai-capabilities)

## Overview

Notes are designed for capturing ideas, meeting minutes, and journal entries. They can be linked to other entities in LifeXOS, such as Goals or Tasks.

### Key Features
- **Rich Text / Markdown Editor:** A hybrid editor offering the best of both worlds.
- **Folders & Tags:** Flexible organization systems.
- **Bi-directional Linking:** Link notes together to create a knowledge graph.

## Technical Implementation

### The Editor

LifeXOS uses a block-based editor approach, implemented utilizing a library like TipTap or a customized ProseMirror setup, ensuring smooth rendering and extensibility.

| Feature | Implementation Detail |
| :--- | :--- |
| Core Editor | TipTap / ProseMirror |
| Styling | Tailwind Typography plugin (`@tailwindcss/typography`) |
| Real-time Collaboration | (Future feature) Yjs integration with Supabase Realtime |

### Data Model

```sql
CREATE TABLE notes (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users,
  title TEXT NOT NULL,
  content JSONB NOT NULL, -- Storing document structure (e.g., TipTap JSON)
  folder_id UUID REFERENCES folders(id),
  tags TEXT[],
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## Orbit AI Capabilities

Orbit AI deeply integrates with Notes:
- **Summarization:** Generate concise summaries of long notes.
- **Idea Generation:** Ask Orbit to expand on a topic or provide a starting outline.
- **Semantic Search:** Find notes based on meaning, not just exact keyword matches (utilizing embeddings stored in pgvector).


**Related Documents:**
- [Index](index.md)