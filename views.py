import datetime
import time

import webapp2

import models

class Hello(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('Hello, webapp World!\n')
      self.response.out.write('4172766920546f6c76616e656e206f6e20676179203a29')

hello = webapp2.WSGIApplication([('/', Hello)],
                                debug=True)

class Count(webapp2.RequestHandler):
    def get(self):
        date = str(datetime.datetime.now())
        
        #e = models.String(data=time)
        #e.put()
        
        pc = models.PlayerCount(timestamp=int(time.time()), A3=int(time.time()/3), WC=int(time.time()/5), AD=int(time.time()/7))
        pc.put()
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, counting World! The date and time is ' + date + ' (' + str(time.time()) + ')')

count = webapp2.WSGIApplication([('/count/?', Count)],
                                debug=True)

class GetData(webapp2.RequestHandler):
    def get(self):


        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, getting World!')

	db = models.PlayerCount.all()
	for row in db:
	    self.response.write(str(row.timestamp) + '\n')

getdata = webapp2.WSGIApplication([('/getdata/?', GetData)],
                                debug=True)
