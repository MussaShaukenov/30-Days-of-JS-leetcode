# Twitter Clone

## Project Overview
Twitter Clone is a project for **Web Development** course in Kazakh-Britsh Technical Universty, Almaty, Kazakhstan. This project is a clone of the popular social media platform Twitter. It aims to replicate key features of Twitter, providing a platform for users to share updates, interact with others, and explore content. The project is structured into a frontend and a backend, each leveraging modern technologies for robust and scalable application development.

## Technology Stack

### Frontend
- **React**: A JavaScript library for building user interfaces.
- **Typescript**: A typed superset of JavaScript that compiles to plain JavaScript.
- **React Hooks API**: Enables functional components to have access to state and other React features.
- **Axios**: A promise-based HTTP client for making HTTP requests from node.js or XMLHttpRequests from the browser.
- **Ant Design**: A React UI library that contains a set of high-quality components and demos for building rich, interactive user interfaces.

### React architecture
```bash
src/
|-- api/
|   |-- apiRequest1.tsx
|   |-- apiRequest2.tsx
|   |-- ...
|-- components/
|   |-- Component1/
|   |   |-- Component1.tsx
|   |   |-- Component1.scss
|   |-- Component2/
|   |   |-- Component2.tsx
|   |   |-- Component2.scss
|   |-- ...
|-- constants/
|   |-- profile.ts
|-- index.tsx
|-- App.tsx
|-- index.css
|-- App.scss
```

### Backend
- **Django**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Django-Rest-Framework**: A powerful and flexible toolkit for building Web APIs.
- **JWT Auth**: JSON Web Token for authentication.
- **Swagger**: An Interface Description Language for describing RESTful APIs expressed using JSON.
- **Docker**: An open platform for developing, shipping, and running applications.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.

### Django architecture
```bash
project/
|-- manage.py
|-- Dockerfile
|-- core/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- app1/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- urls.py
|   |-- views.py
|-- ...
```

### Database
- **Postgres**: An open-source relational database with a strong focus on extensibility and standards compliance.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the repo
   ```sh 
   git clone https://github.com/MussaShaukenov/KBTU-project.git
   ```
2. Navigate to the project directory
   ```sh
    cd tsis 
    ```
3. Running the Application
   ```sh
   sudo docker-compose up -d --build 
   ```
4. Stopping the Application
   ```sh 
   docker-compose down 
   ```

### Contribution
Contributions to this project are welcomed. Please feel free to reach out to any of the team members for collaboration.

### License
**This project is licensed under the MIT License - see the LICENSE file for details.**