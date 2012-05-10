from google.appengine.ext import db

class String(db.Model):
    data = db.StringProperty(required=True)

class PlayerCount(db.Model):
    timestamp = db.IntegerProperty(required=True)
    
    A3 = db.IntegerProperty(required=True)
    WC = db.IntegerProperty(required=True)
    AD = db.IntegerProperty(required=True)
