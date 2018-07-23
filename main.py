import webapp2
import jinja2
import os

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = \
                jinja_current_directory.get_template('templates/home.html')
        self.response.write(home_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = \
                jinja_current_directory.get_template('templates/login.html')
        self.response.write(login_template.render())

class FormPage(webapp2.RequestHandler):
        def get(self):
            form_template = \
                    jinja_current_directory.get_template('templates/form.html')
            self.response.write(form_template.render())

class PeoplePage(webapp2.RequestHandler):
        def get(self):
            people_template = \
                    jinja_current_directory.get_template('templates/people.html')
            self.response.write(people_template.render())

class ProfilePage(webapp2.RequestHandler):
        def get(self):
            profile_template = \
                    jinja_current_directory.get_template('templates/profile.html')
            self.response.write(profile_template.render())

class UserProfilePage(webapp2.RequestHandler):
        def get(self):
            userprof_template = \
                    jinja_current_directory.get_template('templates/userprof.html')
            self.response.write(userprof_template.render())

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/login', LoginPage),
    ('form'/ FormPage),
    ('people', PeoplePage),
    ('profile', ProfilePage),
    ('userprofile', UserProfilePage)
], debug=True)
