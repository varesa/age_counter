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
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('Hello, webapp World!')

count = webapp2.WSGIApplication([('/count', Count)],
                                debug=True)

class GetData(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('Hello, webapp World!')

getdata = webapp2.WSGIApplication([('/', GetData)],
                                debug=True)
