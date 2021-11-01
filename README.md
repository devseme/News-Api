# News-Api
This is an application constructed using Python 'Flask' faramework.It will help news readers  list and preview news articles from various sources.Here,news sources are categorised into topics from which a news reader 
can choose from and read their respective articles

## Technologies Used

- HTML 
- CSS 
- Bootstrap
- Python
- Flask

## Requirements

Python 3.8  
Flask

## Setting up the Project

  * Download and install Python 3.8
  * Download and install Git.
  * Fork the Repository.
  * Clone the repository to your local machine `$ git clone https://`
  * Change directory to NewsApi `$ cd NewApi
  
## Deployment
Here's a list of steps to be followed for deploying an app to heroku:

  * Run pipenv lock to generate the appropriate Pipfile.lock `$ pipenv lock`
  * Then create a Procfile which tells Heroku how to run the remote server where our code will live. `$ touch Procfile`
  * For now we’re telling Heroku to use gunicorn as our production server and look in our <project-file-name>.wsgi file for further instructions. `Update Procfile with - web: gunicorn <project_name>.wsgi --log-file - `
  * Next install [gunicorn](https://gunicorn.org) which we’ll use in production while still using Django’s internal server for local development use. `$ pipenv install gunicorn==19.9.0`
  * Finally update ALLOWED_HOSTS with '*' in settings.py file.
  * push the updates to the GitHub repository.
  * Login to heroku. `$ heroku login`
  * Create a new heroku app. `$ heroku create <app_name>`
  * Set git to use the name of your new app when you push to Heroku. `$ heroku git:remote -a <app_name>`
  * If there are no static files run `$ heroku config:set DISABLE_COLLECTSTATIC=1`
  * Push the code to Heroku. `$ git push heroku master`
  * Add free scaling so the app is actually running online. `$ heroku ps:scale web=1`

## Contributing

Feel free to raise a issue or make a pull request to fix a bug or add a new feature.(@Devseme)

### License

*MIT*
**Copyright (c) 2021 Ian Seme**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
