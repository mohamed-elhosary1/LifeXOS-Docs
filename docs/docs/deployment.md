# Deployment

LifeXOS is configured for deployment on Vercel.

## Vercel Configuration (`vercel.json`)
The configuration focuses heavily on security and caching.

### Security Headers
Every request `/(.*)` returns strict security headers:
- `Strict-Transport-Security`: Enforces HTTPS.
- `X-Frame-Options`: Set to `DENY` to prevent clickjacking.
- `X-Content-Type-Options`: Set to `nosniff`.
- `Referrer-Policy`: Strict origin settings.
- `Permissions-Policy`: Disables camera, microphone, and geolocation access globally.
- `Content-Security-Policy`: A robust CSP allowing scripts and styles from the same origin and Google Fonts, while explicitly permitting connections to Supabase (`*.supabase.co`), Google Generative Language APIs, OpenAI APIs, and Web3Forms.

### Caching
Static assets in the `/assets/(.*)` directory are served with an immutable `Cache-Control` header for maximum lifetime cache hits (`max-age=31536000`), leveraging Vite's asset hashing.

## Progressive Web App (PWA)
The `vite-plugin-pwa` builds a service worker that caches the `index.html` shell and static assets. Navigation fallbacks ensure that the React Router handles routing correctly even offline, ignoring specific backend and API routes (e.g., Supabase Auth callbacks).
