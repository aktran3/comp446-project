# comp446-project
This is a project made for Internet Computing in 8 weeks, from proposal to product. It is a basic media list maker that pulls movie runtime or number of TV show seasons and episodes from Wikipedia. For shows that can't be found, the user has the option to input media information on their own with the help of a Wikipedia embed.

It is made using Django as the backend and vanilla HTML/CSS/JS for frontend. Some help from Alpine.js and htmx were used to supplement JS. 

## Setup Instructions
* Create a virtual environment activate it
* Install the required dependencies with `pip install -r requirements.txt`
* In `list/views.py`, change the email in the `User Agent` to your email. 
* Run `python manage.py migrate` to generate a database
* Run `python manage.py runserver` to start the development server 

## Acknowledgments
The following are resources used in the making of this project: 
* [Django](https://www.djangoproject.com/) documentation
* [LearnDjango](https://learndjango.com/) tutorials
* [Alpine.js](https://alpinejs.dev/) documentation
* [htmx](https://htmx.org/) documentation
* [MDN](https://developer.mozilla.org/en-US/) documentation
* [Wikimedia REST API](https://www.mediawiki.org/wiki/Wikimedia_REST_API) documentation
* [Python](https://www.python.org/) and [Python Requests](https://docs.python-requests.org/en/latest/index.html#) documentation
* [W3schools](https://www.w3schools.com/) tutorials
* Various htmx, Django, and Alpine.js tutorials on YouTube by [BugBytes](https://www.youtube.com/@bugbytes3923)
* Logo uses [Vintage Television Vector](https://www.canva.com/icons/MAFo8xurb6g/) by Hello Swedish from Canva