



http://localhost:5050
    PGADMIN_DEFAULT_EMAIL: raj@nola.com
    PGADMIN_DEFAULT_PASSWORD: admin




Install Python:
    https://www.python.org/

run docker compose
    docker compose -f "docker-compose.yml" up -d --build

Create a virtual environment:
    python -m venv ./.venv
    source .venv/bin/activate
    pip install -r requirements.txt




MicroSercise 
    1-ApiHandler
        uvicorn RouterApp:app --host localhost --port 55545 
    2-Translation
        python _MS3Translation.py
    3-Analysis
        python MS4Analysis.py


http://localhost:55545/docs
http://localhost:5050/browser/



local_pgdb
POSTGRES_USER: user
POSTGRES_PASSWORD: admin

PGADMIN_DEFAULT_EMAIL: raj@nola.com
PGADMIN_DEFAULT_PASSWORD: admin