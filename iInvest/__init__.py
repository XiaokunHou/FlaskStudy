import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask.ext.bcrypt import Bcrypt
from flask.ext.babelex import Babel
#import flask_admin as admin

app=Flask(__name__,template_folder='templates')
babel= Babel(app)

app.config.from_object('config')
csrf=CsrfProtect(app)
bcrypt=Bcrypt(app)
db=SQLAlchemy(app)

from iInvest import trustProductView, articleView, assetManagementView, views
from iInvest.manage import views
