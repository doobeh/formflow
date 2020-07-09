# Form Flow

Quick example showing how Flask-WTF flows through the templates
and using macros to render out some Tailwind formatted HTML around
those form fields.

Basic length validation is in, which is picked up by the macro if
validation failed.

## To run

    git clone https://github.com/doobeh/formflow
    cd formflow
    pipenv install
    export FLASK_APP=core.py
    export FLASK_DEBUG=True
    flask run
    