import webapp2
import jinja2
import os
from google.appengine.api import users
from models import User
from models import Interest

jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

# gets current logged-in user
# so it is easy to access their data on each new page
# request_handler is key for self, but since this method isn't in a class
# that makes it very hard to call self xD
def get_logged_in_user(request_handler):
    # gets current user via a method defined in google app engine
    user = users.get_current_user()

    # if this user doesn't exist (aka no one is signed into Google)
    if not user:
        # send them to Google log-in url
        dict = {
            'log_in_url' : users.create_login_url('/')
        }
        # put that Google log-in link on the page and get them in!
        log_in_template = jinja_current_directory('templates/login-page.html')
        request_handler.response.write(log_in_template.render(dict))
        print 'transaction halted because user is not logged in'
        return None

    # at this point, the user is logged into google
    # now let's make sure that user has been logged into our site
    # aka do we have their Google ID in OUR model (which is called User)?
    # user (appengine) vs User (our own Model). Definitely not confusing
    existing_user = User.get_by_id(user.user_id())

    # if this person is not a user in our database, throw an error
    if not existing_user:
        print 'transaction halted because user not in database'
        request_handler.error(500)
        return None

    # otherwise if they exist in both Google and our site, let's return them
    # now we can easily access their information
    return existing_user

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
        login_dict = {}
        name = ""
        user = users.get_current_user()

        # if the user is logged with Google
        if user:
            # magical users method from app engine xD
            email_address = user.nickname()
            # uses User (model obj) method to get the user's Google ID.
            # hopefully it returns something...
            our_site_user = User.get_by_id(user.user_id())
            #dictionary - this gives the sign-out link
            signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))

            # if the user is logged in to both Google and us
            if our_site_user:
                self.response.write('''
                Welcome %s (%s)! <br> %s <br>''' % (
                 our_site_user.name,
                 email_address,
                 signout_link_html))

              # If the user is logged into Google but never been to us before..
            else:
                self.response.write('''
                 Welcome to our site, %s!  Please sign up! <br>
                 <form method="post" action="/login">
                 <input type="text" name="first_name">
                 <input type="text" name="last_name">
                 <input type="submit">
                 </form><br> %s <br>
                 ''' % (email_address, signout_link_html))

            # Otherwise, the user isn't logged in to Google or us!
        else:
            self.response.write('''
                Please log in to use our site! <br>
                <a href="%s">Sign in</a>''' % (
                  users.create_login_url('/')))

    def post(self):
        user = users.get_current_user()
        if not user:
            # You shouldn't be able to get here without being logged in to Google
            self.error(500)
            return
        our_user = User(
            email=user.nickname(),     # current user's email
            id=user.user_id(),         # current user's ID number
            name=self.request.get("first_name") + " " + self.request.get("last_name")
            )
        our_user.put()
        self.response.write('Thanks for signing up, %s!' %
            our_user.name)

        home_template = jinja_current_directory.get_template('templates/home-page.html')
        self.response.write(home_template.render())

            # need to figure out how we're doing interests
            # do they already exist? How do I get those interest objects made
            # before I put them into the our_user object like this??
            # interests=self.request.get('interests'),
            # university=self.request.get('university'),

class FormPage(webapp2.RequestHandler):
    def get(self):
        form_template = \
            jinja_current_directory.get_template('templates/form-and-profile-page.html')
        self.response.write(form_template.render())
    def submit_form(request):
        if request.method == 'POST':
            form = Form(request.POST)
            if not form.has_changed():
                self.response.write("Please fill out all fields before submitting.")
                # Generate Error
    def post(self):
        form_template = jinja_current_directory.get_template('templates/home-page.html')

        # get the user info from their form
        uni_in_form = self.request.get("schools")
        age_in_form = self.request.get("ages")
        major_in_form = self.request.get("majors")
        social_media_in_form = self.request.get("social_media_title")
        interest_in_form = self.request.get("interest_title")
        # image_in_form = self.request.get("image")

        # our_user is the existing_user
        our_user = get_logged_in_user(self)

        # give our_user values in the data store
        our_user.university = uni_in_form
        our_user.age = age_in_form
        our_user.major = major_in_form
        our_user.interest = interest_in_form
        # our_user.image = image_in_form

        # save those changes to our_user values
        our_user.put()

        self.response.write(form_template.render())


class PeoplePage(webapp2.RequestHandler):
    def get(self):
        current_user = get_logged_in_user(self)
        people_temp_dict = {}
        people_template = jinja_current_directory.get_template('templates/people-page.html')
        if not current_user.university:
            people_temp_dict = {'Error' : "ERROR fill out form first!"}
            self.response.write(people_template.render(people_temp_dict))
            return None

        # get list of all university matches
        uni_matches = User.query(User.university == current_user.university, User.name != current_user.name).fetch()
        # render matches into the html (or it should anyway)
        self.response.write(people_template.render(test_dict))


app = webapp2.WSGIApplication([
    ('/', StartPage),
    ('/home', HomePage),
    ('/login', LoginPage),
    ('/form', FormPage),
    ('/people', PeoplePage)
], debug=True)
