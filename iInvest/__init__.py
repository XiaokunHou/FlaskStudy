import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask.ext.bcrypt import Bcrypt
<<<<<<< HEAD
#from flask_babelex import Babel
import flask_login as login
from flask.ext.babel import Babel
from flask import Flask, url_for, redirect, render_template, request, session
#import flask_admin as admin

app=Flask(__name__,template_folder='templates')
=======
#from flask.ext.babelex import Babel
from flask.ext.babel import Babel
#import flask_admin as admin

app=Flask(__name__,template_folder='templates')
app.config.from_pyfile('setting.cfg')
babel= Babel(app)
>>>>>>> 62cf15a7590404335e2a29bf4db2fb33744f5d8a

app.config.from_object('config')
csrf=CsrfProtect(app)
bcrypt=Bcrypt(app)
db=SQLAlchemy(app)
babel=Babel(app)

@babel.localeselector
def get_locale():
    #print request.accept_languages.best_match(LANGUAGES.keys())
    return 'zh_Hans_CN'


from iInvest import trustProductView, articleView, assetManagementView, views
from iInvest.manage import views
