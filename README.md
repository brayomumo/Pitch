# Pitch

##  A web application that allows the users to post pitches, comment and vote on pitches.

## By [Brian Mumo](https://github.com/brayomumo)


## Description
This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (Pick-up Lines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

## User Stories
* As a user I would like to view the different categories.
* As a user I would like to see the pitches other people have posted.
* As a user I would like to comment on the different pitches and leave feedback.
* As a user I would like to submit a pitch in any category.
* As a user I would like to vote on the pitch they liked and give it a downvote or upvote.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display Various Pitch Categories | N/A | Various pitches grouped by category are displayed |
|Display pitches | **Click** on a Category| A page with a list of pitches from the selected category |
|Add new pitch | **Click** New pitch | User Should register/sign in to add new pitch |
|View Pitches | **Click** on a pitch | View a pitch and comments |
|Comment on a pitch | **Click** Comment | Registered User displays a form where a user can comment on a certain pitch |


## Setup/Installation Requirements
* internet access
* $ `git clone https://github.com/brayomumo/Pitch.git`
* $ `cd Pitch`
* $ `python3.6 -m venv virtual` (install virtual environment)
* $ `source virtual/bin/activate`
* $ `python3.6 -m pip install -r requirements.txt` (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ `chmod +x start.sh` (make the program executable)
* $ `./start.sh`


## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through brayomumo5@gmail.com or leave a commit [here](https://github.com/brayomumo/Pitch) on github.


## Known Bugs

The upvote and downvote is not working

## Technologies Used
- Python3.6
- Flask framework
- Bootstrap
- PostgreSQL

### License

**[MIT](./LICENSE)** (c) 2017 **Brayo mumo **