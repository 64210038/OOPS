
class Person:
    def __init__(self,name,gender,profession,study:int) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def show(self):
        print(f'name : {self.name} gender: {self.gender} Profession: {self.profession} study: {self.study}')

    def __del__(self):
        print("object was destroyed")

if __name__ == "__main__":

    #person1
    jessa = Person('jessa','female','softewre engineer',10)
    jessa.work()
    jessa.show()

    #person2
    jon = Person('jon','mael','doctor',15)
    jon.work()
    jon.show()

    #person3
    lisa = Person( 'lisa','female','korean singer',10)
    lisa.work()
    lisa.show()