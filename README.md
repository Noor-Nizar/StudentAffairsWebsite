# Student Affairs Website 🎓

This is a full-stack web application built with Django. The project is currently in an early stage with 5 commits as of the last update.

## 🚀 Getting Started

To get a local copy up and running, follow these steps:

1. **Clone the repository**
    ```bash
    git clone https://github.com/Noor-Nizar/StudentAffairsWebsite.git
    ```
2. **Install Django and other dependencies**
    ```bash
    pip install django
    ```
3. **Run the server**
    ```bash
    python manage.py runserver
    ```

## 📁 Project Structure

The project contains the following main directories and files:

- `Lib`
- `Scripts`
- `myworld`
- `venvdj`

## ⚙️ Application Settings

The application uses Django 4.0.4 and SQLite as the database. The `DEBUG` mode is currently set to `True`.

The application includes the following Django apps:

- `django.contrib.admin`
- `django.contrib.auth`
- `django.contrib.contenttypes`
- `django.contrib.sessions`
- `django.contrib.messages`
- `django.contrib.staticfiles`
- `members.apps.MembersConfig`

## 🌐 URLs

The application includes the following URL patterns:

- `''` : Includes `members.urls`
- `admin/` : Django admin site

## 📚 Models

The `Student` model in the `members` app has the following fields:

- `first_name` : A char field with a maximum length of 30.
- `last_name` : A char field with a maximum length of 30.
- `mail` : An email field.
- `phone` : A char field with a maximum length of 30.
- `id` : A char field with a maximum length of 30 and is the primary key.
- `gender` : A char field with a maximum length of 10 and a default value of "".
- `date_of_birth` : A date field.
- `level` : An integer field.
- `gpa` : A float field.
- `status` : A char field with a maximum length of 20 and a default value of "".
- `department` : A char field with a maximum length of 30 and a default value of "General".

## 🤝 Contributions

Contributions are what make the open-source community an incredible place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

⚠️ **Important:** The project's settings file suggests that the `SECRET_KEY` is not suitable for production and the `DEBUG` mode is currently set to `True`. You may want to review the settings before deploying this application in a production environment.
