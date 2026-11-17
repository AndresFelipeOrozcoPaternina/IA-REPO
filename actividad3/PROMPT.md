# Software Requirements Specification (SRS) & Prompt for 3D Interactive Corporate Training Platform

Requisitos compartidos para la actividad del concurso. IA utilizada por el equipo: **v0**. Este documento registra el encargo; sus requisitos no equivalen a funciones verificadas.

## Role and Context

You are an expert Full-Stack 3D Web Developer and Game Designer. Your task is to build a fully functional, interactive 3D web-based educational and training platform for a corporate environment. The application must feature a top-down / satellite-style camera tracking the player character.

## Tech Stack Recommendations

- **3D Rendering & Physics:** Three.js (or Babylon.js)
- **UI / Layout:** HTML5, CSS3, Bootstrap (via CDN)
- **Logic / Interactivity:** Vanilla JavaScript

## Functional Requirements

### 1. Onboarding & Character Customization (Initial Screen)

- **Username Input:** A simple text input to set a basic username (no database/complex authentication required for now).
- **Gender Selection:** Options for Male and Female.
- **Character Presets:** 3 basic 3D character presets with different skin tones and basic clothing variations.

### 2. Central Hub (Main Area)

- **Perspective:** Satellite / Top-down 3D camera following the player.
- **Rest Area:** A central lounge with seating where the character can sit down.
- **Introduction Station:** An interactive onboarding point near the center explaining the platform's features and navigation.

### 3. Right Wing: Technical Academy (Tech Classes)

- **Environment:** A classroom area displaying a schedule and list of classes.
- **Subjects Covered:** HTML, CSS, CSS Frameworks (Bootstrap), and Programming Logic with Python.
- **Day 1 Trial (HTML):** Features 3 basic coding/practical challenges for HTML. Includes a dedicated ranking/leaderboard system for technical scores.

### 4. Left Wing: Languages & Soft Skills

- **Environment:** Language and Emotional Management rooms.
- **Structure:** 2 classes per day (English and Emotional Management).
- **English Trial:** Features 3 beginner-level (A1) English challenges. Includes its own dedicated ranking/leaderboard system.

### 5. Upper Floor: Entertainment Zone

- **Access:** Stairs leading up from near the central rest area.
- **Mini-Games:** 3 rest/entertainment games (including Ping Pong and Air Hockey).
- **Interactive Ping Pong vs. CPU:** Fully playable, basic 2D/3D physics-based Ping Pong match against a computer opponent.
- **Energy System:** The player has an Energy Bar with a maximum of 5 points. Each mini-game session costs 2.5 energy points. Energy cannot be bought; it exclusively recharges by winning classes in the Tech or Language academies.

## Acceptance Criteria

1. The 3D world loads smoothly with a responsive top-down/satellite camera following the avatar.
2. Character customization works seamlessly before entering the main corporate hub.
3. Movement mechanics allow smooth navigation between the Central Hub, Right Wing, Left Wing, and Upper Floor.
4. The HTML and English trials allow users to complete the 3 challenges and view corresponding leaderboards.
5. The energy system correctly deducts points upon playing mini-games and restores them upon winning classes.
6. The UI incorporates clean styling using Bootstrap components.
