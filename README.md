# comp446-project
This is a project made for Internet Computing in 8 weeks, from proposal to product. It is a basic media list maker that pulls movie runtime or number of TV show seasons and episodes from Wikipedia. For shows that can't be found, the user has the option to input media information on their own with the help of a Wikipedia embed.

It is made using Django as the backend and vanilla HTML/CSS/JS for frontend. Some help from Alpine.js and HTMX were used to supplement JS. 
## Setup Instructions
* Create a virtual environment and install the required dependencies with `pip install -r requirements.txt`
* In `list/views.py`, change the email in the `User Agent` to your email. 
* Activate the virtual environment
* Run `manage.py migrate` to generate a database
* Run `manage.py runserver` to start the development server 