# Environment Variables

**Purpose:** LifeXOS requires several environment variables to function correctly, connecting the frontend client to the Supabase backend and configuring external services.
**Last Updated:** 2026-07-31



## Table of Contents
- [Setup Instructions](#setup-instructions)
- [Required Variables](#required-variables)
- [Development vs Production](#development-vs-production)

## Setup Instructions

1. Copy the example environment file:
   ```bash
   cp .env.example .env.local
   ```
2. Fill in the values in `.env.local` according to your specific environment.

## Required Variables

### Supabase Configuration

These variables are required for the application to communicate with your Supabase project. They can be found in your Supabase Dashboard under Project Settings -> API.

| Variable | Description | Security |
| :--- | :--- | :--- |
| `VITE_SUPABASE_URL` | The URL of your Supabase project. | Public |
| `VITE_SUPABASE_ANON_KEY` | The anonymous key for the Supabase API. Used by the client. | Public |

*Note: The `VITE_` prefix exposes these variables to the Vite build process and the frontend client.*

### Orbit AI Configuration (Edge Functions)

If you are deploying Edge Functions that interact with AI providers, you need to configure secrets within the Supabase environment, **NOT** in the frontend `.env` file.

Use the Supabase CLI to set secrets for Edge Functions:

```bash
supabase secrets set OPENAI_API_KEY=your_api_key_here
```

| Variable | Location | Description |
| :--- | :--- | :--- |
| `OPENAI_API_KEY` | Supabase Secrets | Key for accessing OpenAI models for Orbit AI features. |

## Development vs Production

- **Development:** Use `.env.local` for local development variables.
- **Production:** Configure these variables in your hosting provider's dashboard (e.g., Vercel Environment Variables settings).


**Related Documents:**
- [Index](index.md)