# comp446-project
This is a project made for Internet Computing in 8 weeks, from proposal to product. It is a basic media list maker that pulls movie runtime or number of TV show seasons and episodes from Wikipedia. For shows that can't be found, the user has the option to input media information on their own with the help of a Wikipedia embed.

It is made using Django as the backend and vanilla HTML/CSS/JS for frontend. Some help from Alpine.js and htmx were used to supplement JS. 

## Setup Instructions
1. Create a virtual environment activate it
    * We followed these guides for [Windows](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html) and for [Mac](https://realpython.com/lessons/creating-virtual-environment/) to set up our virtual environments.    
2. Install the required dependencies with `pip install -r requirements.txt`
3. Run `python manage.py createsuperuser` to create an admin account for the list app.
4. In `list/views.py`, change the email in the `User Agent` to your email. 
5. Run `python manage.py migrate` to generate a database
6. Run `python manage.py runserver` to start the development server 

## Known Bugs
* It takes two clicks to get to a different list in 'My Lists'.
* Clicking inline with a list will open/close it.
* A user can enter a current place in a TV show that can go out of bounds of the show's season and episode count.
    * Negative values are accepted as well.
* The page quickly flashes when loading in the entries partial view.
* Site searches for titles in English, regardless of what user settings are set to.
* No current method to delete lists.

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