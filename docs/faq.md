# Frequently Asked Questions (FAQ)

**Purpose:** Here are the most common questions about using and configuring LifeXOS.
**Last Updated:** 2026-07-31



## Table of Contents
- [General](#general)
- [Data & Security](#data-security)
- [Features](#features)
- [Troubleshooting](#troubleshooting)

---

## General

### What is LifeXOS?
LifeXOS is a comprehensive, local-first "OS for your life". It combines task management, habit tracking, note-taking, and goal setting into one unified interface, powered by an Orbit AI called Orbit.

### Is LifeXOS free?
LifeXOS is open-source and free to self-host. We also offer a managed cloud version with a free tier and a premium tier for advanced AI features.

### Do I need internet to use it?
No! LifeXOS is built with an offline-first architecture. You can view, create, and edit data without a connection. Changes will sync automatically when you are back online. (Note: Orbit AI features require an internet connection).

---

## Data & Security

### Where is my data stored?
If you use our managed service, data is stored securely in our Supabase instances. If you self-host, your data is stored in your own database. Regardless, a local copy is always cached in your browser's IndexedDB.

### Can I export my data?
Yes. Go to **Settings > Data > Export**. You can download all your Workspaces, Tasks, Notes, and Habits as a structured JSON file or as Markdown files.

### Are my notes encrypted?
Data is encrypted in transit and at rest on the server. However, End-to-End Encryption (where even the server cannot read the data) is currently on our [roadmap](roadmap.md) and not yet implemented.

---

## Features

### How does Orbit AI work?
Orbit AI is your personal assistant. It can summarize notes, break down complex tasks into subtasks, and suggest habits based on your goals. You can invoke it using the magic wand icon or by hitting `Cmd/Ctrl + K` and typing a prompt.

### Can I change the theme?
Yes! LifeXOS supports Light mode, Dark mode, and System default. We also offer several accent color presets in **Settings > Appearance**.

### Why isn't my habit streak updating?
Habit streaks calculate based on your local timezone. Ensure your system clock is correct. If a day is missed, the streak resets. We currently do not support "freeze" days, but it's heavily requested!

---

## Troubleshooting

### The app is stuck on a loading screen!
Try clearing your browser cache and application data for the site, or perform a "Hard Refresh" (`Cmd/Ctrl + Shift + R`). If the issue persists, check our [Troubleshooting Guide](troubleshooting.md).


**Related Documents:**
- [Index](index.md)