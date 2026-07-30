# Orbit AI

Orbit AI (`src/components/OrbitAI.tsx`) is the integrated conversational assistant designed to help users organize their day and extract insights from their workspace.

## Core Capabilities
- **Context Awareness**: When a user sends a prompt, the application bundles the prompt with the user's current `tasks`, `habits`, and `studySessions`, sending it to the `lifexos-ai` Supabase edge function. This allows Orbit to answer questions based directly on the user's actual productivity data.
- **Chat History**: Messages are persisted locally via `localStorage` and synchronized with the `user_ai_profiles` table in Supabase.
- **Markdown Rendering**: AI responses are rendered using `ReactMarkdown` with `remarkGfm` support for tables, lists, and formatting.
- **Typewriter Effect**: Newly received AI messages are animated character-by-character via the `TypewriterText` component to simulate real-time typing.
- **Background Memory Extraction**: When the chat sidebar is closed, the component silently invokes the `aie-analyzer` edge function to parse recent user messages and extract long-term memory or preferences.

## What Orbit AI Can Do
- Analyze daily progress and summarize remaining tasks.
- Provide motivation or advice based on current study sessions and habit streaks.
- Maintain context of previous messages within the active chat session.

## What Orbit AI Cannot Do (Not Implemented)
- It **cannot** directly mutate or create workspace items autonomously (e.g., it cannot create a new task, course, or habit on behalf of the user). It is strictly an advisory/read-only conversational agent.
- It does not support file attachments (the UI shows a paperclip icon, but file upload functionality is not implemented).
