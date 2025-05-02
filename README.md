# Is It My Birthday? 🎂

A simple Django web application that checks if today is your birthday and displays a special birthday message with a celebratory background when it is!

## Features

- Birthday checker: Tells you if today is your birthday or not
- Celebratory display: Shows a festive cake background with birthday wishes on your special day
- Simple and beginner-friendly codebase

## Screenshots

- Regular day view:
  ![Not your birthday](screenshots/not_birthday.png)

- Birthday view:
  ![Happy Birthday](screenshots/birthday.png)

## Prerequisites

- Python 3.8 or higher
- Django 4.2 or higher
- Basic knowledge of HTML and CSS

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/is-it-my-birthday.git
   cd is-it-my-birthday
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running Locally

1. Make sure your virtual environment is activated

2. Run migrations (first time only):
   ```
   python manage.py migrate
   ```

3. Start the development server:
   ```
   python manage.py runserver
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## How to Use

1. When you first access the application, you'll be prompted to enter your birth date
2. After submitting your birth date, the app will check if today is your birthday:
   - If it's not your birthday, you'll see a message saying "It's not your birthday yet!"
   - If it is your birthday, you'll see a festive cake background with "Happy Birthday!" and your personalized birthday wishes

## Project Structure

```
is-it-my-birthday/
│
├── birthday_app/              # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py              # User and birthday data models
│   ├── views.py               # View functions for checking birthdays
│   ├── urls.py                # URL patterns
│   ├── forms.py               # Forms for date input
│   └── tests.py
│
├── templates/                 # HTML templates
│   ├── base.html              # Base template with common elements
│   ├── birthday.html          # Shown when it's your birthday
│   └── not_birthday.html      # Shown when it's not your birthday
│
├── static/                    # Static files (CSS, JS, images)
│   ├── css/
│   │   ├── main.css           # Main styling
│   │   ├── birthday.css       # Birthday page specific styling
│   │   └── not_birthday.css   # Regular day styling
│   └── img/
│       └── cake.png           # Birthday cake background
│
├── is_it_my_birthday/         # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py                  # Django management script
├── requirements.txt           # Project dependencies
└── README.md                  # This file
```

## Customizing the App

### Changing the Birthday Display

To modify the birthday celebration page:

1. Edit the `templates/birthday.html` file to change the layout and message
2. Update the `static/css/birthday.css` file to change the styling
3. Replace the cake image in `static/img/` with your own celebration background

### Adding More Features

Some ideas for extending the project:

- Add a countdown to your next birthday
- Include animations using CSS or JavaScript
- Add sound effects for the birthday celebration
- Create a system for storing multiple birthdays (friends/family)
- Send email notifications when someone's birthday is approaching

## Contributing

This is a beginner project, so contributions are welcome! If you have ideas for improvements:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- This project was created as a beginner Django learning exercise
- Thanks to the Django documentation for making web development accessible to beginners
