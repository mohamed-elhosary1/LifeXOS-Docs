# Deployment

**Purpose:** LifeXOS is structured as a modern Jamstack application. The frontend is a static React Single Page Application (SPA) built with Vite, and the backend is entirely managed by Supabase.
**Last Updated:** 2026-07-31



## Table of Contents
- [Frontend Deployment](#frontend-deployment)
- [Backend Deployment (Supabase)](#backend-deployment-supabase)
- [Continuous Integration / Continuous Deployment (CI/CD)](#continuous-integration-continuous-deployment-cicd)

## Frontend Deployment

The frontend can be deployed to any static hosting provider. We recommend **Vercel** or **Netlify** for optimal performance and CI/CD integration.

### Steps for Vercel:
1. Connect your GitHub repository to Vercel.
2. Ensure the Framework Preset is set to `Vite`.
3. Build Command: `npm run build`
4. Output Directory: `dist`
5. Configure Environment Variables (see `environment.md`).

## Backend Deployment (Supabase)

The database schema, RLS policies, and Edge Functions are managed via the Supabase CLI.

### Migrations

Database changes should be tracked in migration files.

```bash
# Create a new migration file
supabase migration new init_schema

# Apply migrations to the linked remote project
supabase db push
```

### Edge Functions

Deploy Edge Functions using the CLI:

```bash
supabase functions deploy orbit-ai-chat
```

## Continuous Integration / Continuous Deployment (CI/CD)

We recommend using GitHub Actions to automate the deployment process.

1. **Frontend:** Triggered on merge to `main`, builds the Vite app and deploys to the hosting provider.
2. **Backend:** Triggered on changes to the `supabase/` directory, pushes migrations and deploys edge functions automatically.


**Related Documents:**
- [Index](index.md)