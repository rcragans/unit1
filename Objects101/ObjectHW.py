class Person(object):
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
    def greet(self, other_person):
        print "Hello %s, I am %s!" % (other_person.name, self.name)
    def print_contact_info(self):
        print "%s\'s email: " % self.name + self.email + ', ' + "%s\'s phone: " % self.name + self.phone
    def add_friend(self, friend):
        self.friends.append(friend)
    def num_friends(self):
        print len(self.friends)
    def greeting_count(self):
        greeting_count = 0
        if self.greet > 0:
            greeting_count += 1
            print greeting_count
sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')
sonny.add_friend("Julie")
sonny.add_friend("Jordan")
sonny.num_friends()
sonny.greet(jordan)
jordan.greet(sonny)
sonny.greeting_count()
sonny.print_contact_info()
jordan.print_contact_info()

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print self.make, self.model, self.year
myCar = Vehicle('Nissan', 'Altima', '2013')
myCar = Vehicle('Ford', 'Fairlane', '1972')
myCar.print_info()



