# Settings

The Settings page (`src/pages/Settings.tsx`) acts as the command center for user preferences and app customization. 

## Features

### 1. Appearance & Theme
- **Dark/Light Mode Toggle**: Manual toggle.
- **Auto Theme Switch**: Automatically swaps themes based on the user's local time (Sunrise/Sunset logic).
- **Color Palette Selection**: Choose from predefined theme colors or use a custom HSL picker.
- **Auto Color Rotation**: Automatically changes the app's accent color every 15 minutes.

### 2. Backgrounds
- **Interactive Particles**: The default animated node-based background.
- **Photos & Live Videos**: Selectable preset wallpapers.
- **Custom Upload**: Upload personal images or videos (up to 30 MB) to use as the application background.
- **Background Blur**: A slider to adjust the intensity of the backdrop blur effect behind glass UI elements.

### 3. General Preferences
- **Localization**: Switch between English and Arabic.
- **Pomodoro Adjustments**: Set custom duration for work sessions and breaks.
- **Daily Goals**: Set targeted hours for daily productivity.
- **Data Export**: Export a full text file backup of all tasks, habits, and sessions.

### 4. Privacy & AI
- **Continuous Learning (AIE)**: Toggle whether the Orbit AI assistant is permitted to analyze interaction patterns to personalize responses.

### 5. Notifications
- **Orbit AI Push Notifications**: Opt-in to browser-level push notifications to receive motivational prompts outside the app.
- **Neglect Alerts**: Toggle alerts for courses or goals that haven't been opened in a specified threshold of days.
