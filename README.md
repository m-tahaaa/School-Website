# Lakhipur Middle School Portal

Django website and lightweight school administration portal for Lakhipur Middle School, Uttar Dinajpur, West Bengal.

## Run locally

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## Deploy a demo

This project includes `render.yaml` for a low-cost Render web service. Connect the repository to Render and choose **Blueprint** deployment. The build command installs dependencies, collects static files, and runs migrations automatically.

The demo uses SQLite. It is suitable for a presentation, but production data should move to a managed PostgreSQL database with regular backups.
