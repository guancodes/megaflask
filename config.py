WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

import os
basedir = os.path.abspath(os.path.dirname(__file__))
#os is module, path is submodule, and dirname is a function
#path must be a module because all the classes are CamelCase
#abspath and dirname are not methods because they are not part of a class
#the function dirname returns a relative path
#a relative path is usually no good. So we need to convert it to an abspath.
#connecting to a data base wouldn't work if we use a relative path.

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
