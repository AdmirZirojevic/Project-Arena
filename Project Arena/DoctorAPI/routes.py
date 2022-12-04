from DoctorAPI import app
from DoctorAPI.forms import LoginForm
from DoctorAPI.doctor import User
from flask import render_template, flash, redirect
from flask_login import login_user



@app.route('/')
@app.route('/home', methods=['GET','POST'])
#@login_required
def home_page():
    return render_template('home.html')





@app.route('/login', methods=['GET', 'POST']) #nikako nisam uspio login.html elemente da renderujem preko base.html pa ovo sve nisam stigao ni testirati
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        doctor_login = User.query.filter_by(username=form.email.data).first()
        if doctor_login and doctor_login.check_password_correction( #htio sam password hashirat sa bcryptom, ali nisam stigao taj dio odradit)
            attempted_password=form.password.data
        ):
                login_user(doctor_login)
                flash(f'Success!', category='success')
                return redirect('home.html')
        else:
                flash('Pogresan e-mail ili password', category='danger')

    return render_template('login.html', form=form)