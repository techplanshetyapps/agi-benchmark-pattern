#README.md
# AI Travel Concierge & ARC-AGI Task Benchmark Suite

## Overview
An advanced AI-powered platform that plans, optimizes, and adapts travel itineraries in real-time while integrating an automated ARC-AGI-1 Task Generation Runner for frontier reasoning model evaluation. It provides users with a robust web interface to generate custom travel schedules and trigger complex AI evaluation tasks dynamically.

---

## Tech Stack
* **Cloud PaaS:** Render PaaS Server (Automated deployment via `render.yaml` and `build.sh`)
* **Process Manager:** Gunicorn WSGI Application Server
* **Backend Framework:** Django 5.x Python Web Framework
* **Database:** SQLite (ORM-driven structured job & itinerary storage)
* **AI & Integration:** Ollama & OpenAI-compatible endpoints with robust fallback generation routines
* **Frontend Experience:** Responsive HTML5/JavaScript dashboard featuring WebGL sky background textures, interactive mouse-tracking (`mousemove`), falling geometric/smog particle simulation, digital terminal styling, and ASCII shell animation
* **Version Control:** GitHub

---

## Setup
1. **Repository Configuration:** Ensure your project root contains `manage.py`, `requirements.txt`, `build.sh`, and `render.yaml`.
2. **Environment Variables:** Configure necessary environment variables including `OPENAI_BASE_URL`, `OLLAMA_MODEL`, and execution parameters.
3. **Render Deployment:** Link your GitHub repository to a new Web Service on Render with the start command:
   ```bash
   gunicorn mysite.wsgi:application
    ```
4. **Build & Execution:** Push your code changes to GitHub to initiate the automatic build and WhiteNoise static asset collection workflow.

   ## Features
* **AI Travel Concierge:** Dynamic destination, date range, and budget selection generating personalized day-by-day itineraries with built-in cost optimization.
* **ARC-AGI-1 Task Generator:** Creates fresh, distribution-matched tasks via backend python scripts (`generate_tasks.py` and `generate_tasks_stratified.py`) designed to evaluate reasoning models.
* **Interactive Dashboard UI:** Immersive frontend featuring WebGL shaders, particle simulations, and terminal-style feedback.

---

## Technical Workflow
1. **Request Reception:** Django views handle incoming HTTP POST requests from the HTML dashboard for task generation or itinerary planning (`trigger_task_generation`, `ai_concierge_plan`).
2. **Subprocess & API Execution:** The backend dynamically invokes internal generation scripts or communicates with OpenAI-compatible/Ollama endpoints via `requests`/`httpx`.
3. **Database Persistence:** Processed outputs, job states, standard logs, and travel itineraries are securely structured and saved using Django's SQLite ORM models (`GenerationJob`, `TravelItinerary`).
4. **JSON Response Delivery:** Results and execution statuses are returned asynchronously to update the front-end dashboard in real time.
