# Theme and Styling

The aesthetic of LifeXOS is driven by **Tailwind CSS**, enhanced with extensive **CSS Variables** and custom logic.

## Base CSS (`src/index.css`)
The application defines a strict color system using HSL variables (`--background`, `--primary`, `--card`, etc.) in both `:root` and `.dark` scopes. 
It also defines utility classes for its signature "Glassmorphism" look:
- `.glass-card`
- `.glass-sidebar`
- `.glass-fab`

## ThemeProvider & Palettes
Instead of just Light/Dark mode, the app supports dynamic color palettes.
- The `ThemeProvider` manages the base dark/light toggle and stores preferences in `localStorage`.
- `src/lib/themePalettes.ts` controls injecting custom HSL values to override `--primary` and other accent variables.
- Users can enable "Auto color rotation" to shuffle the primary color palette every 15 minutes.

## Custom Backgrounds
Managed by `src/lib/backgrounds.ts`, the app allows users to replace the standard background with:
1. Pre-selected Images.
2. Pre-selected looping Videos.
3. User-uploaded files (saved locally/indexedDB).
The background blur is also dynamically controlled via inline styles mapped to a user preference.
