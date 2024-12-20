from flask import render_template, redirect, url_for, request, flash, session
from flask_login import current_user, login_user, logout_user

from app.modules.auth import auth_bp
from app.modules.auth.forms import SignupForm, LoginForm
from app.modules.auth.models import User
from app.modules.auth.services import AuthenticationService
from app.modules.profile.services import UserProfileService
from app import db


import json

authentication_service = AuthenticationService()
user_profile_service = UserProfileService()


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        name = form.name.data
        surname = form.surname.data
        if not authentication_service.is_email_available(email):
            return render_template("auth/signup_form.html", form=form, error=f'Email {email} in use')

        try:
            user_data = {
            'email': email,
            'password': password,
            'name': name,
            'surname': surname
            }

            print(user_data)
            print("------------------------")
            
            authentication_service.send_verification_email(user_data)
        except Exception as exc:
            return render_template("auth/signup_form.html", form=form, error=f'Error creating user: {exc}')

        # Log user
        #login_user(user, remember=True)
        return redirect(url_for('public.index'))

    return render_template("auth/signup_form.html", form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        if authentication_service.login(form.email.data, form.password.data):
            return redirect(url_for('public.index'))

        return render_template("auth/login_form.html", form=form, error='Invalid credentials')

    return render_template('auth/login_form.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))

@auth_bp.route('/confirm/<token>')
def confirm_email(token):
    try:
        # Desencriptar el token y recuperar los datos del usuario
        user_data = authentication_service.serializer.loads(token, salt='email-confirmation-salt', max_age=3600)
    #except SignatureExpired:
    #    flash('The confirmation link has expired.', 'error')
    #    return redirect(url_for('auth.login'))
    except Exception:
        flash('Invalid confirmation token.', 'error')
        return redirect(url_for('auth.login'))

    try:
        # Crear el usuario en la base de datos
        user = authentication_service.create_with_profile(**user_data)
        login_user(user)
        return redirect(url_for('public.index'))
    except Exception as e:
        flash(f"Error creating user: {str(e)}", "error")
        return redirect(url_for('auth.signup'))

"""@auth_bp.route('/confirm/<token>')
def confirm_email(token):
    email = authentication_service.confirm_token(token)
    if not email:
        return redirect(url_for('auth.login'))

    # Recupera los datos del usuario desde la sesión
    user_data = session.get('pending_user')
    print("---------------------")
    print(session)
    print("---------------------")
    print(user_data) 
    if isinstance(user_data, str):  
        user_data = json.loads(user_data)
    if not user_data or user_data['email'] != email:
        flash("Confirmation link expired or invalid.", "error")
        print("-----------")
        return redirect(url_for('public.index'))
    print(user_data) 
    try:
        user = authentication_service.create_with_profile(user_data)
        login_user(user)
        session.pop('pending_user', None)  
        return redirect(url_for('public.index'))
    except Exception as e:
        flash("Error creating user. Please try again.", "error")
        return redirect(url_for('auth.scripts')) """