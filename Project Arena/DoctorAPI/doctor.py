from DoctorAPI import db
from flask_login import UserMixin 

#@login_manager.user_loader   ovo nije radilo nikako i nisam aplikaciju mogao pokrenuti pa sam iz komentarisao na kraju
#def load_user(user_id):
 #   return User.query.get(int(user_id))
 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address =db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(length=60), nullable=False)
   # patients = db.relationship('Patient', backref='') ovo nisam siguran bio treba li







class Patient(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    appointment = db.Column(db.String(length=12), nullable=False)
    #doctor = db.Column(db.Integer(), db.ForeignKey('user.id')) ovo isto nisam siguran bio treba li

    def __repr__(self):
        return f'Patient {self.name}'