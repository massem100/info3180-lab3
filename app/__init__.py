from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Peter rabit bakes'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'username_'
app.config['MAIL_PASSWORD'] = 'password_'
mail = Mail(app)

from app import views
