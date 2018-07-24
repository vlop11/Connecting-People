from google.appengine.ext import ndb
from google.appengine.api import users  # allows access to Google ID for log-in purposes

class Interest(ndb.Model):
    # the information for EachInterst object will go here
    email = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)    # interest name                             ex. League of Legends
    alias = ndb.StringProperty(repeated=True)   # other names for interest                  ex. LoL or LOL
    number_of_users = ndb.IntegerProperty()     # how many people are interested in this    ex. 40

class User(ndb.Model):
    # user's name will be entered here
    name = ndb.StringProperty(required = True)

    #the image location will be entered here
    image = ndb.StringProperty()

    # A list of Interest objects... need to find how they are compared. Will they be separate? Will that matter?
    majors = ndb.KeyProperty(Major, repeated = True)

    #the index of the user's university will be here
    university = ndb.IntegerProperty()

class University(ndb.Model):
    # the ordered list of university names (held as a string) will go here
    university_array = ndb.StringProperty(repeated = True)

# Stuff that is no longer useful, but make cool notes
    # will hold an ordered list of EachInterest objects
    # LocalStructuredProperty means EachInterest will be a "blob"
    # so EachInterest will look like {'name': "somestring", 'alias': ["somestring", "someotherstring"], etc}
    # aka its values go into dictionary format (which is what I want)
