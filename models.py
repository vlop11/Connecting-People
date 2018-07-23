from google.appengine.ext import ndb

class User(ndb.Model):
    # user's name will be entered here
    name = ndb.StringProperty(required = True)

    #the image location will be entered here
    image = ndb.StringProperty()

    # These refer to an index in the Interest and University arrays
    # We use integers because it is MUCH faster to compare integers than strings
    # Thank you Taylor

    # The indexes of the user's interests will be here
    interests = ndb.IntegerProperty(repeated = True)

    #the index of the user's university will be here
    university = ndb.IntegerProperty(required = True)

class Interest(ndb.Model):
    # will hold an ordered list of EachInterest objects
    interest_array = ndb.LocalStructuredProperty(EachInterest, repeated=True)

class EachInterest(ndb.Model):
    # the information for EachInterst object will go here
    name = ndb.StringProperty(required=True)    # interest name                             ex. League of Legends
    alias = ndb.StringProperty(repeated=True)   # other names for interest                  ex. LoL or LOL
    number_of_users = ndb.IntegerProperty()     # how many people are interested in this    ex. 40

class University(ndb.Model):
    # the ordered list of university names (held as a string) will go here
    university_array = ndb.StringProperty(repeated = True)
