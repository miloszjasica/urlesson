# urlesson
This project implements a tutoring platform where users can interact through a web interface. It is based on Django and provides the core backend logic, database setup and a frontend using Tailwind CSS.

The platform is built around two main user roles: **Student** and **Teacher**.

- **Students** can browse and choose teachers for specific subjects based on their preferences, availability, and pricing. They are able to schedule lessons by selecting time slots when a teacher is available and manage their upcoming lessons.

- **Teachers** can define their availability, set lesson prices, and manage incoming lesson requests by accepting or rejecting them. This allows teachers to fully control their schedules and teaching conditions.

urlesson also includes a **notification** system that keeps both students and teachers informed about important events such as lesson requests, confirmations, rejections, and schedule updates.

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
