
# TIT TechHub - Official Website

![TIT TechHub Logo](https://raw.githubusercontent.com/your-username/tit-techhub-website/main/static/images/logo.png) 
<!-- Badilisha 'your-username' na jina lako halisi la GitHub na hakikisha logo ipo kwenye static/images/ -->

## 📌 About the Project

TIT TechHub is a modern, fully dynamic technology services company website built with **Django**, **PostgreSQL**, **HTML**, **CSS**, and **JavaScript**. 

The website is designed to be **fully controlled via the Django Admin Dashboard** with **zero hard-coded content**. Every text, image, service, team member, and statistic is dynamically fetched from the database, allowing administrators to update the site without touching a single line of code.

**Tagline:** *Innovate • Develop • Grow*

## ✨ Key Features

- **100% Dynamic Content:** Fully manageable via Django Admin (No hard-coded text or images).
- **Modern UI/UX:** Premium design with Glassmorphism effects, smooth animations, and a responsive layout.
- **Custom Admin Dashboard:** Control Site Settings, Home Page, About Page, Services, Team Members, Stats, and Core Values.
- **Contact Form:** Integrated contact form that saves messages directly to the database.
- **Dynamic Footer & Navbar:** Editable contact info, social media links, and site logo.
- **Secure:** Environment variables (`.env`) are used to protect sensitive data like `SECRET_KEY` and database credentials.
- **Responsive:** Fully optimized for Mobile, Tablet, and Desktop screens.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla), FontAwesome (Icons), Google Fonts (Poppins)
- **Media Management:** Pillow (For image uploads)
- **Environment Management:** python-dotenv

## 🚀 Getting Started (Local Development)

Follow these steps to run this project on your local machine.

### Prerequisites
- Python 3.8+
- PostgreSQL installed and running
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/tit-techhub-website.git
cd tit_techhub_website

2. Set Up Virtual Environment
bash

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
bash

pip install -r requirements.txt

(If requirements.txt is not available, install manually: pip install django psycopg2-binary python-dotenv Pillow)
4. Configure Environment Variables

Create a .env file in the root directory (where manage.py is located) and add the following variables:
env

SECRET_KEY=your_django_secret_key_here
DEBUG=True
DB_NAME=tit_techhub_db
DB_USER=postgres
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

(A .env.example file is provided as a template).
5. Set Up Database

Create a PostgreSQL database named tit_techhub_db (or whatever you specified in .env).
bash

python manage.py makemigrations
python manage.py migrate

6. Create Superuser (Admin)
bash

python manage.py createsuperuser

Follow the prompts to create your admin account.
7. Run the Development Server
bash

python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/
To access the Admin Dashboard, go to http://127.0.0.1:8000/admin/
📂 Project Structure
text

tit_techhub_website/
│
├── config/                  # Main Django project settings
│   ├── settings.py          # Database & Environment config
│   └── urls.py              # Main URL routing
│
├── core/                    # Core app (Site Settings, Home, Contact, Stats)
│   ├── models.py            # SiteSettings, HomePage, ContactMessage, Stat
│   └── admin.py             # Admin registration for Core models
│
├── about/                   # About app (About Page, Core Values, Team)
│   ├── models.py            # AboutPage, CoreValue, TeamMember
│   └── admin.py             # Admin registration for About models
│
├── services/                # Services app (Services, Target Market, Approach)
│   ├── models.py            # Service, TargetMarket, ApproachStep
│   └── admin.py             # Admin registration for Services models
│
├── templates/               # HTML Templates
│   ├── base.html            # Main layout (Navbar, Footer, Messages)
│   ├── home.html            # Home page (Hero section, Stats)
│   ├── about.html           # About page
│   ├── services.html        # Services page
│   ├── contact.html         # Contact page
│   └── includes/
│       └── footer.html      # Dynamic Footer
│
├── static/                  # Static files
│   ├── css/
│   │   └── style.css        # Main stylesheet
│   ├── js/
│   │   └── main.js          # Custom JavaScript
│   └── images/              # Logos & static images
│
├── media/                   # User-uploaded files (Admin uploads)
│
├── .env                     # Secret environment variables (NOT pushed to Git)
├── .env.example             # Example environment variables
├── .gitignore               # Files ignored by Git
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

🔐 Security Note

    Never commit your .env file to GitHub.

    Ensure .env and venv/ are included in your .gitignore.

    In production, set DEBUG=False and configure ALLOWED_HOSTS properly.

🌐 Deployment

This project is ready to be deployed on platforms like Render, Railway, or DigitalOcean.
Ensure you set the environment variables in the hosting provider's dashboard (do not upload the .env file).
📞 Contact & Links

    Company: TIT TechHub

    Email: tittechhub.official@gmail.com

    Phone: 0613950508

    Location: Dar es Salaam, Tanzania

Built wby the TIT TechHub Team.
