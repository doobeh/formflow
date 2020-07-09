from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


app = Flask(__name__)
app.secret_key = 'QUIET!'


class ExampleForm(FlaskForm):
    email = StringField('Email', validators=[
        validators.data_required(), validators.length(min=4, max=30)
    ])
    password = PasswordField('Password', validators=[validators.length(min=8)])


@app.route('/', methods=['post', 'get'])
def home():
    form = ExampleForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        return render_template('success.html', email=email, password=password)
    return render_template('home.html', form=form)

