from flask import render_template, current_app
from flask_babel import _
from app.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(_('[chirp] Reset Your Password'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))


def send_welcome_email(user):
    token = user.get_reset_password_token()
    send_email(_('[chirp] Welcome to Chirp'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/welcome.txt',
                                         user=user),
               html_body=render_template('email/welcome.html',
                                         user=user))

