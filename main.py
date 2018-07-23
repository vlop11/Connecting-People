import webapp2
import jinja2
import os
from models import User
from models import Interest
from models import University

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class StartPage(webapp2.RequestHandler):
    def get(self):
        start_template = \
                jinja_current_directory.get_template('templates/start-page.html')
        self.response.write(start_template.render())

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = \
                jinja_current_directory.get_template('templates/home-page.html')
        self.response.write(home_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = \
                jinja_current_directory.get_template('templates/login-page.html')
        self.response.write(login_template.render())

class FormPage(webapp2.RequestHandler):
        def get(self):
            form_template = \
                    jinja_current_directory.get_template('templates/form-and-profile-page.html')
            self.response.write(form_template.render())

class PeoplePage(webapp2.RequestHandler):
        def get(self):
            people_template = \
                    jinja_current_directory.get_template('templates/people-page.html')
            self.response.write(people_template.render())

app = webapp2.WSGIApplication([
    ('/', StartPage),
    ('/home', HomePage),
    ('/login', LoginPage),
    ('/form', FormPage),
    ('/people', PeoplePage)
], debug=True)
