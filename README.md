# urlesson
This project implements a tutoring platform where users can interact through a web interface. It is based on Django and provides the core backend logic, database setup, and a modern frontend using Tailwind CSS.

# 1. Tech Stack

**Backend:** Python, Django

**Frontend:** HTML, CSS (Tailwind)

**Dev Tools:** django-tailwind, django-browser-reload

**Database:** SQLite

# 2. Demo
[Watch demo](demo/urlesson_demo2.mp4)

# 3. Future

The project is rewritting and extending into a more scalable architecture using Django (backend) + React (frontend) + PostgreSQL + Docker.

**Future development will include:**

- real-time chat between users,

- file sharing functionality,

- a review and rating system verified by AI to ensure authenticity and quality,

- and an integrated AI chatbot to support users and enhance the learning experience.

# 4. How to run

1. Clone the repository and navigate to the project folder:

```bash
git clone https://github.com/MiloszJasica/urlesson.git
cd urlesson
```
2. Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install required packages:

```bash
pip install django-tailwind
pip install django-browser-reload
```
4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the Django development server:

```bash
source venv/bin/activate
python manage.py runserver
```

6. Run Tailwind
```bash
source venv/bin/activate         
python manage.py tailwind start
```
