from google.appengine.ext import ndb
from google.appengine.api import users  # allows access to Google ID for log-in purposes

class Interest(ndb.Model):
    # the information for Interst object will go here
    name = ndb.StringProperty(required=True)    # interest name                ex. League of Legends
    alias = ndb.StringProperty()   # other names for interest                  ex. LoL or LOL

class User(ndb.Model):
    # user's name will be entered here
    name = ndb.StringProperty()

    # user's email MUST be entered when it is created, and it goes here
    email = ndb.StringProperty()

    social_media = ndb.StringProperty()
    #the image location will be entered here
    image = ndb.StringProperty()

    # A list of Interest objects... need to find how they are compared. Will they be separate? Will that matter?
    interests = ndb.StructuredProperty(Interest, repeated = True)

    #the index of the user's university will be here
    university = ndb.StringProperty()

    major = ndb.StringProperty()

    def compare_interests(self, other_user):
        # count counts how much these users have in common. 3 is best, 0 is worst
        count = 0
        # let's loop through each of your interests ex. tennis, swimming, camping; rn we're checking tennis
        for each_interest in self.interests:
            # has that user's specific interest been found?
            found_yet = False
            # now let's loop through the other person's interests
            for each_other_interest in other_user.interests:
                # if tennis already matches to one thing in that user... it probably won't match to another LOL
                # so let's save us some processing
                if found_yet:
                    pass
                # if your interest name matches... you win a point!
                # now you've got another common intrest with another scumbag!
                # and since that interest is matched, it likely won't match again
                # after all, who writes "beating dogs" for TWO out of their three interests?
                # only pathetic people, and we won't try to recommend them
                if each_interest.name == each_other_interest.name:
                    count += 1
                    found_yet = True
        # return your common-interest index!
        return count

# Stuff that is no longer useful, but make cool notes
    # will hold an ordered list of EachInterest objects
    # LocalStructuredProperty means EachInterest will be a "blob"
    # so EachInterest will look like {'name': "somestring", 'alias': ["somestring", "someotherstring"], etc}
    # aka its values go into dictionary format (which is what I want)
