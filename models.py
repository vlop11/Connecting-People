from google.appengine.ext import ndb
from google.appengine.api import users  # allows access to Google ID for log-in purposes

class Interest(ndb.Model):
    # the information for Interst object will go here
    name = ndb.StringProperty(required=True)    # interest name                             ex. League of Legends
    alias = ndb.StringProperty(repeated=True)   # other names for interest                  ex. LoL or LOL
    number_of_users = ndb.IntegerProperty()     # how many people are interested in this    ex. 40

class User(ndb.Model):
    # user's name will be entered here
    name = ndb.StringProperty()

    # user's email MUST be entered when it is created, and it goes here
    email = ndb.StringProperty(required=True)


    #the image location will be entered here
    image = ndb.StringProperty()

    # A list of Interest objects... need to find how they are compared. Will they be separate? Will that matter?
    interests = ndb.KeyProperty(Interest, repeated = True)

    #the index of the user's university will be here
    university = ndb.StringProperty()

    major = ndb.StringProperty()

# Stuff that is no longer useful, but make cool notes
    # will hold an ordered list of EachInterest objects
    # LocalStructuredProperty means EachInterest will be a "blob"
    # so EachInterest will look like {'name': "somestring", 'alias': ["somestring", "someotherstring"], etc}
    # aka its values go into dictionary format (which is what I want)
