class RedditPerson(object):
    def __init__(self, name, age, redditUser):
        self.age        = age
        self.name       = name
        self.redditUser = redditUser
    def WhoAmI(self):
        print "Your name is %s, you are %s years old, and your username is %s." % (self.name, self.age, self.redditUser)

name       = raw_input("Enter your name: ")
age        = raw_input("Enter your age: ")
redditUser = raw_input("Enter your Reddit username: ")

person = RedditPerson(name, age, redditUser)
person.WhoAmI()