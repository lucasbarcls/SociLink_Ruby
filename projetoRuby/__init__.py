from flask import Flask, render_template, url_for
from  flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt  import Bcrypt
 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clientes.db"
app.config["SECRET_KEY"] = "669078de481043d580b39fed44a0d175"


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_maneger = LoginManager(app)
login_maneger.login_view = "homepage"


#from projetoRuby import routes