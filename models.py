from google.appengine.ext import db

class String(db.Model):
    data = db.StringProperty(required=True)