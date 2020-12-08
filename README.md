# Django_Social_Network

Used Tech Stack

1. Django
2. Sqlite 
3. Semantic UI

### Screenshots of the project page

## Auto Search page
<img src="ss/search_box.png" height="600">

##  Search Result
<img src="ss/search_result.PNG" height="600">

## Home page
<img src="ss/home-page.PNG" height="600">

## All User Profile page
<img src="ss/all-profiles.PNG" height="600">

## Profile Details page
<img src="ss/profile-details.PNG" height="600">

## Recieved Invites page
<img src="ss/recieved_invites.PNG" height="600">

## Friend request send page
<img src="ss/to-invites.PNG" height="600">

## User Profile page
<img src="ss/user-profile.PNG" height="600">

## User Profile Update page
<img src="ss/user-profile-update.PNG" height="600">

<a name="local-venv"></a>
### Local environment

#### Install

1. Create a virtual environment

    `virtualenv venv`

    Or

    `python3.8 -m venv venv`

2. Activate it

    `source venv/bin/activate`

3. Clone the repository and install the packages in the virtual env:

    `pip install -r requirements.txt`

4. Add `.env` file.

    `cp .env.dev.sample .env`

5. Add Github client ID and client secret in the `.env` file

#### Run

1.With the venv activate it, execute:

    python manage.py collectstatic

*Note* : Collect static is not necessary when debug is True (in dev mode)

2. Create initial database:

    `python manage.py migrate`


3. Load demo data (optional):

    `python manage.py loaddata fixtures/app_name_initial_data.json --app app.model_name`

4. Run server:

    `python manage.py runserver`


#### Run test:
``python manage.py test``

#### To dump data:
``python manage.py dumpdata --format=json --indent 4 app_name > app_name/fixtures/app_name_initial_data.json``

Show your support by 🌟 the project!!
