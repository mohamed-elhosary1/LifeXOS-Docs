# LifeXOS

LifeXOS is a comprehensive, AI-enhanced life management and productivity platform. Built with modern web technologies, it features task tracking, habit building, Pomodoro timers, study planning, note-taking, and in-depth insights into your daily progress.

## Vision
To provide a unified, highly-customizable workspace that seamlessly integrates study schedules, daily routines, long-term goals, and AI-driven personalization to boost productivity.

## Key Features
- **My Day & Tasks:** Daily planning with intelligent task normalization and categorization.
- **Study Planner & Pomodoro:** Course and subject management, integrated with a Pomodoro timer for focused sessions.
- **Habits & Goals:** Track recurring habits and overarching life goals.
- **Insights & Analytics:** Weekly reports and data visualizations.
- **AI Integration:** "Orbit AI" push notifications and adaptive intelligence learning toggles.
- **Deep Customization:** HSL color palettes, light/dark modes, custom backgrounds (images/videos), and blur controls.
- **PWA Ready:** Installable as a Progressive Web App for desktop and mobile.

## Tech Stack
- **Frontend:** React 18, TypeScript, Vite
- **Styling:** Tailwind CSS, Radix UI components, Framer Motion for animations
- **State Management:** Custom Pub/Sub store (`lib/store.ts`)
- **Backend/BaaS:** Supabase (Auth & Database)
- **Routing:** React Router v6
- **Testing:** Playwright (E2E), Vitest (Unit)
- **Deployment:** Vercel

## Architecture
The application is structured logically:
- `src/components/`: Reusable UI elements, many from shadcn/ui.
- `src/contexts/`: React Contexts (`AuthContext`, `LanguageContext`).
- `src/lib/`: Core utilities including the custom state store, theme palette logic, and background handlers.
- `src/pages/`: Lazy-loaded feature modules.

Detailed architectural overviews are available in the `docs/` directory.

## Setup & Local Development
1. Clone the repository.
2. Install dependencies: `npm install` (or use Bun/Yarn).
3. Ensure you have Supabase configured and the appropriate `.env` variables (`VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`).
4. Run the development server: `npm run dev`
5. Visit `http://localhost:8080`.

## Deployment
LifeXOS is optimized for deployment on Vercel. See `docs/deployment.md` for Vercel configurations and security headers.

## Contributing
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Roadmap
- [ ] Deeper AI Insights dashboard.
- [ ] Native mobile wrapper enhancements (currently supports PWA and basic Electron).
- [ ] Expanded multilingual support beyond English and Arabic.
