import datetime
import time

import webapp2

import models

class Hello(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('Hello, webapp World!')

hello = webapp2.WSGIApplication([('/', Hello)],
                                debug=True)

class Count(webapp2.RequestHandler):
    def get(self):
        time = str(datetime.datetime.now())
        
        #e = models.String(data=time)
        #e.put()
        
        pc = models.PlayerCount(timestamp=time.time(), A3=time.time()/3, WC=time.time()/5, AD=time.time()/7)
        pc.put()
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, counting World! The date and time is ' + time + ' (' + time.time() + ')')

count = webapp2.WSGIApplication([('/count/?', Count)],
                                debug=True)

class GetData(webapp2.RequestHandler):
    def get(self):

	data = models.String.all()
	for value in data:
	    self.response.write(value.data + '\n')

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, getting World!')

getdata = webapp2.WSGIApplication([('/getdata/?', GetData)],
                                debug=True)
