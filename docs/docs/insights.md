# Insights & Analytics

The Insights page (`src/pages/Insights.tsx`) provides a comprehensive dashboard for tracking productivity over time.

## Data Periods
Users can toggle between four analytical periods:
1. **Today**
2. **Week**
3. **Month**
4. **Lifetime**

## Core Metrics
- **Total Study**: Aggregated duration of all study sessions in the selected period.
- **Sessions**: The raw count of completed study blocks.
- **Tasks Done**: Number of tasks completed within the timeframe.
- **Day Streak**: The current consecutive number of days with at least one study session recorded.

## Highlights & Breakdowns
- **Best Performance**: Lifetime scan identifying the single best Day, Week, and Month by total study duration.
- **By Section**: A breakdown ranking which Courses, Subjects, or broad categories received the most study time.
- **Recent Sessions**: A chronologically ordered list of recently completed study blocks.

## LifeXOS AI Analyst
The insights page integrates a premium AI analyst feature (`lifexos-ai` edge function).
- **Contextual Generation**: It passes the user's current tasks, habits, and study sessions to the AI.
- **Output**: Generates a custom productivity report with actionable recommendations (cached in `localStorage`).
- **Bilingual**: Supports generating reports in English or Arabic based on user preferences.
