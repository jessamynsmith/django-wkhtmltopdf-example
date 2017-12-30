# Django Wkhtmltodpf Example

Django sample app that uses wkhtmltodpf to generate PDFs.
https://django-wkhtmltodpf-example.herokuapp.com


Like my work? Tip me! https://www.paypal.me/jessamynsmith


### Development

Install system dependencies using a package manager. E.g. for OSX, using homebrew:

    brew install python3
    brew install postgresql  # optional, will use sqlite if not available

Install wkhtmltopdf 0.12.3 for your system from the following link:

    https://github.com/wkhtmltopdf/wkhtmltopdf/releases/tag/0.12.3

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/django-wkhtmltodpf-example.git

Create a virtualenv using Python 3 and install dependencies. I recommend using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv django_wkhtmltodpf_example --python=/path/to/python3
    pip install -r requirements.txt

Set environment variables as desired. Recommended dev settings:

    export DJANGO_DEBUG=1
    export DJANGO_ENABLE_SSL=0

Optional environment variables, generally only required in production:

    ADMIN_NAME
    ADMIN_EMAIL
    DJANGO_SECRET_KEY
    REPLY_TO_EMAIL
    SENDGRID_PASSWORD
    SENDGRID_USERNAME
    
You can add the exporting of environment variables to the virtualenv activate script so they are always available.

Set up a local symlink to the system wkhtmltopdf that mimics the location on heroku. In the project directory:

    mkdir bin
    cd bin
    which wkhtmltopdf
    ln -s /path/to/wkhtmltopdf wkhtmltopdf  # Must use the value retrieved in the previous step

If you don't configure postgresql, the app will use sqlite. If you use postgresql, you need an additional environment variable:

    export DATABASE_URL='postgres://<username>@127.0.0.1:5432/django_wkhtmltodpf_example'

Set up db:

    createdb django_wkhtmltodpf_example
    python manage.py migrate

Check code style:

    flake8

Run server:

    python manage.py runserver
    
Or run using gunicorn:

    gunicorn django_wkhtmltodpf_example.wsgi

### Continuous Integration and Deployment

This project is already set up for deployment to Heroku.

Make a new Heroku app, and add the following addons:

    Heroku Postgres
    SendGrid
    
Add Heroku buildpacks:

    heroku buildpacks:set heroku/python -i 1
    heroku buildpacks:set https://github.com/dscout/wkhtmltopdf-buildpack.git -i 2

Deploy:

    git push heroku master
    heroku run python manage.py migrate
