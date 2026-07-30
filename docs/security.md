# Security Guidelines

**Purpose:** Security is paramount at LifeXOS. We strive to protect user data, ensure secure communication, and build resilience against common vulnerabilities. This document outlines our security architecture, policies, and best practices.
**Last Updated:** 2026-07-31



## Table of Contents
- [Overview](#overview)
- [Authentication & Authorization](#authentication-authorization)
- [Data Protection](#data-protection)
- [Orbit AI Security](#orbit-ai-security)
- [Common Vulnerability Mitigations](#common-vulnerability-mitigations)
- [Reporting a Vulnerability](#reporting-a-vulnerability)

## Overview

LifeXOS leverages Supabase for backend services, meaning many of our security practices revolve around configuring Row Level Security (RLS) correctly, securing API keys, and managing user sessions securely via JWTs.

### Key Principles

1.  **Defense in Depth**: Security measures are applied at multiple layers (UI, API, Database).
2.  **Least Privilege**: Users and services have only the permissions necessary to perform their functions.
3.  **Secure by Default**: Default configurations should be the most secure option.

---

## Authentication & Authorization

We use Supabase Auth for handling user identity. 

### JWT and Sessions
-   Access tokens (JWTs) have short lifespans.
-   Refresh tokens are securely stored (HttpOnly cookies where possible, or secure local storage).
-   Session validation occurs on every authenticated route and API request.

### Row Level Security (RLS)

All database tables in Supabase **must** have RLS enabled. This ensures that users can only access their own data.

```sql
-- Example RLS Policy for 'tasks' table
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can view their own tasks"
  ON tasks FOR SELECT
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert their own tasks"
  ON tasks FOR INSERT
  WITH CHECK (auth.uid() = user_id);
```

> [!WARNING]
> Never disable RLS in production or use the Supabase Service Role key in the frontend client.

---

## Data Protection

### In Transit
All communication between the LifeXOS client and Supabase/Orbit AI APIs is encrypted using TLS 1.2 or higher (HTTPS).

### At Rest
Data at rest is encrypted by Supabase (underlying PostgreSQL database running on AWS/GCP). Sensitive fields (like API keys provided by the user for Orbit AI) are encrypted at the application level before insertion into the database.

---

## Orbit AI Security

When integrating with "Orbit AI" (the LifeXOS Orbit AI), we adhere to the following:
-   **No PII in Prompts**: Personal Identifiable Information should be scrubbed before sending data to external LLM providers, unless explicitly opted-in by the user.
-   **Rate Limiting**: AI endpoints are strictly rate-limited to prevent abuse and denial-of-service.
-   **Sanitization**: All outputs from Orbit AI are sanitized before being rendered in the DOM to prevent Cross-Site Scripting (XSS).

---

## Common Vulnerability Mitigations

| Vulnerability | Mitigation Strategy |
| :--- | :--- |
| **XSS** | React's default escaping, strict Content Security Policy (CSP), sanitizing AI output. |
| **CSRF** | Use of SameSite cookie attributes; Supabase handles CSRF protection for auth endpoints. |
| **SQLi** | Use of Supabase SDKs which parameterize queries by default; RLS policies. |
| **Clickjacking** | `X-Frame-Options: DENY` header in the production server config. |

## Reporting a Vulnerability

If you discover a security vulnerability within LifeXOS, please send an e-mail to `security@lifexos.example.com`. All security vulnerabilities will be promptly addressed. Please do not disclose vulnerabilities publicly before we have had a chance to patch them.


**Related Documents:**
- [Index](index.md)