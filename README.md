# Arbilex Take Home

## Set Up

### Front End
You just need to install and run the app:
    
    cd arbilex/arbilex-frontend
    npm i
    npm start

### Back End
There is a trick here. The easiest way to get things going to to point this to a remote version of the database I set up. I will communicate the ip address to you privately. Put that ip address in the `arbilex/arbilex-backend/arbilex/settings.py` file under `DATABASES.HOST` (line 90) It should look like this:
    
    DATABASES = {

        'default': {

            'ENGINE': 'django.db.backends.postgresql_psycopg2',

            'NAME': 'arbilex',

            'USER': 'frank',

            'HOST': '<magic ip I sent you here>',

            'PASSWORD': 'arbilex'

        }

    }

Next you will need Python3.x to run this. I have that under `python3` so my startup looks like this:

    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip3 install django-cors-headers
    pip3 install psycopg2
    python3 manage.py runserver
    
If you did everything right, you should have the backend running on localhost:8000.
## Data Definitions
### Term Duration
This is straight forward, the `startDate` and `finishDate` are defined in the justices JSON.
### Decision Duration
This is defined from the case data as the time between `dateargument` until `datedecision` 
### Most Disenting Justice
A disenting justice is defined as a justice with `majority` to be 1. Anecdotal evidence verifies this as the correct way to determine disent. Obviously this in not a binary as justices may concur in part without concuring completely. 
## The Philsophy Behind this Solution
From the description of the task (and by the fact that I was given wireframes) I have taken this excersie to be a functional one. So that the question to be answered was "Can Frank produce this app with the desired functionality?" I did not, therefore, make a full test suite, include security considerations or significantly future proof the code. I also left some obvious optimizations on the cutting room floor which I will discuss below. The overriding philosophy here was to get something *works*. 
## Things Left Undone
Consistent with the above mentioned philosophy I have left many things undone. Some highlights (lowlights?)
### Testing
There is no testing to speak of. I have done other takehome with more robust testing suites and would be happy to share them. In a production app I would include unit tests and emphasize end to end tests as much as possible, ideally integrationg them into the CI/CD pipeline. 
### CSS Framework
I did not integrate a css frameowrk (bootstrap, materialUI, etc.) I am agnostic on these tools and think the designer should have input on them. The layout of the css is vanilla css and all lives in `App.css`. 
### Wireframe
I have not been asked to do a wireframe in over a decade. It is usual for the designer to provide color codes, fonts, pixel measurements etc. Those were not provided and I have eyeballed everything as best I could but the results are *not quite right* for that reason. The wireframe generation usually goes back and forth between the dev and designer to make sure all important elements are addressed, I consider this a reasonable first effort, particularly given the specifics were not provided.
### Responsive Design
This design is for desktop only and not responsive, although I did try to make it not look horrible on smaller screens. 
## Database/ETL
I imported the justices and decisions data into postgresql. I did merge the legacy and modern SCOTUS decision data but did not go all the way back to 1793 because it was hard to navigate 250 years on the slider. I also began work on a summary table to speed it up but dropped it because it was likely overkill for this project. If we were sure that the ranges were always to have a fixed end date (notice that arbitrary ranges aren't supported according to the mockup) then a summary table with and end date and the three data points would be easy to use and make the app super fast. However it seems logical that an improvement needed would be to allow those arbitrary ranges i.e. have a slider with a handle for begin and on for end. In that case you would want to structure the summary table differently, likely with day by day summaries with appropriate weights so the query would be a weighted average. 
### Raw SQL
I used raw sql in the app because orms are the devil. 

