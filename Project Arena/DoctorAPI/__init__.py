from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doctorAPI.db'
app.config['SECRET_KEY'] ='0769824d275c1e8b5a7d9ab5'
db = SQLAlchemy(app)
#login_manager = LoginManager(app) 
# ovo mi je problem pravilo. Ubacio sam i metodu koja stoji u dokumentaciji i isto kao na vjezbama,
# ali nisam uspio shvatiti zašto izbacuje exception i dalje


from DoctorAPI import routes