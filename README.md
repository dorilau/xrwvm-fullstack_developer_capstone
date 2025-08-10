#  IBM Full Stack Developer Capstone

A full-stack application for browsing car dealerships, viewing reviews, and submitting your own.  
Built with **Django**, **Node.js**, **React**, and an integrated **Sentiment Analysis** service.

---

## Features

- **Dealer Listings** — Browse available dealerships.
- **Dealer Reviews** — View customer feedback and sentiment analysis.
- **Add Review** — Authenticated users can submit their own reviews.
- **Sentiment Analysis** — Uses Watson NLP to determine review sentiment.
- **Kubernetes Deployment** — Hosted on IBM Cloud Kubernetes Service.
- **Dockerised Backend** — Reproducible and containerised server setup.

---

## Tech Stack

| Layer           | Technology |
|-----------------|------------|
| Frontend        | React      |
| Backend         | Django, Django REST Framework |
| API Services    | Node.js for sentiment analysis |
| Database        | SQLite (local), IBM Cloud DB  |
| Deployment      | Docker, Kubernetes, IBM Code Engine |
| Hosting         | IBM Cloud Container Registry & Kubernetes |

---

## Architecture
Inside `server`:
- `djangoapp` — Django models, views, URLs, and helper modules such as `restapis.py` and `populate.py`.
- `djangoproj` — Project settings and root URL routing.
- `frontend` — React app and its build artefacts when compiled.
- `database` — Node and Express service with Mongoose models and route handlers.
- `deployment.yaml` and any Service or Ingress manifests for Kubernetes deployment.
- `Dockerfile`, `entrypoint.sh`, `.dockerignore` for container builds.
  
**Front end**  
- React app served from the `server/frontend` build output during production.

**Django app**  
- Located in `server/djangoapp`.
- Provides views for authentication, dealership listing, and review retrieval.
- Includes a data initialiser.
- Uses SQLite by default for models such as `CarMake` and `CarModel`.

**Node and Express service**  
- Located in `server/database`.
- Exposes dealership and review endpoints backed by MongoDB.

**Sentiment analysis microservice**  
- Accepts review text and returns a sentiment label.
- Consumed by the Django app to enrich review responses.

**Container and deployment**  
- Container images are built from `server/Dockerfile`.
- Images are pushed to IBM Cloud Container Registry.
- Kubernetes manifests live in the `server` folder.
