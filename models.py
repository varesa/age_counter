from google.appengine.ext import db

class String(db.Model):
    data = db.StringProperty(required=True)

class PlayerCount(db.Model):
    timestamp = db.IntegerProperty(required=true)
    
    A3 = db.IntegerProperty(required=true)
    WC = db.IntegerProperty(required=true)
    AD = db.IntegerProperty(required=true)
