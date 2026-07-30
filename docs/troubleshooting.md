# Troubleshooting Guide

**Purpose:** Encountering issues with LifeXOS? Follow these steps to diagnose and resolve common problems.
**Last Updated:** 2026-07-31



## Table of Contents
- [Basic Diagnostics](#basic-diagnostics)
- [Common Issues](#common-issues)
- [Still Need Help?](#still-need-help)

---

## Basic Diagnostics

Before diving into specific issues, try the "IT Crowd" approach:
1. **Refresh the page**: A simple refresh (`F5` or `Cmd/Ctrl + R`) solves many temporary UI glitches.
2. **Hard Refresh**: Clears the cache for the page (`Ctrl + F5` or `Cmd/Ctrl + Shift + R`).
3. **Check Network Tab**: Open Developer Tools (F12) and check if API calls are failing in the Network tab.
4. **Update Browser**: Ensure you are on a modern, updated browser (Chrome, Firefox, Safari, Edge).

---

## Common Issues

### 1. "Sync Failed" / Data Not Saving
*   **Symptom**: A red cloud icon appears, or changes you make aren't showing up on other devices.
*   **Cause**: Network interruption, authentication token expiry, or a conflict in the offline queue.
*   **Solution**:
    1. Check your internet connection.
    2. Try logging out and logging back in (this refreshes your auth token).
    3. Go to **Settings > Advanced > Force Sync**.
    4. If all else fails, go to **Settings > Advanced > Clear Local Data**. (Warning: this will delete unsynced offline changes).

### 2. Orbit AI Returns an Error
*   **Symptom**: Asking the AI a question results in a generic error or a timeout.
*   **Cause**: API rate limits exceeded, backend provider down, or missing API keys (if self-hosting).
*   **Solution**:
    1. Wait a few minutes; you may have hit the rate limit.
    2. If self-hosting, ensure your `VITE_OPENAI_API_KEY` (or relevant provider key) is correctly set in your environment variables.

### 3. Drag and Drop is Janky / Not Working
*   **Symptom**: Tasks cannot be dragged between Kanban columns, or the UI freezes during a drag.
*   **Cause**: Conflicting browser extensions or performance bottlenecks on massive boards.
*   **Solution**:
    1. Disable extensions that interfere with mouse events or DOM manipulation (e.g., ad blockers, gesture extensions) to see if it fixes the issue.
    2. If your board has over 500 tasks, try archiving completed tasks.

### 4. Blank Screen on Load (White Screen of Death)
*   **Symptom**: The app loads, but the screen remains entirely blank.
*   **Cause**: A fatal JavaScript error caused React to crash, usually due to malformed local state.
*   **Solution**:
    1. Open DevTools (F12) and check the Console tab for red error messages.
    2. Clear local storage: Application Tab -> Storage -> Local Storage -> Clear All. Refresh the page.

---

## Still Need Help?

If you cannot resolve the issue:
1. Gather console logs and network errors.
2. Check the [GitHub Issues](#) to see if it's a known bug.
3. Open a new issue with a detailed description and steps to reproduce.


**Related Documents:**
- [Index](index.md)