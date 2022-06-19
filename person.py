from dis import show_code
from pkg_resources import working_set


class Person:
    def __init__(self,name,gender,profession) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = 0

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def study(self,hours):
        self.study = hours

    def show(self):
        print(f'name : {self.name} gender: {self.gender} Profession: {self.profession} study: {self.study}')

#person1
jessa = Person('jessa','female','softewre engineer')
jessa.work()
jessa.show()

#person2
jon = Person('jon','mael','doctor')
jon.study = 15
jon.work()
jon.show()
