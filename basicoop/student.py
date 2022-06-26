class Student :
    def __init__(self,id:str,name:str,major="it"):
        self.id = id
        self.name = name
        self.major = major
  
    def didplay_detail(self):
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"major: {self.major}")

def __del__(self):
        print("object was destroyed")

if __name__ == "__main__":

    #person1
    my_student = Student(111,"jessica","it")
    my_student.didplay_detail()

    #person2
    my_student = Student(112,"john","mkt")
    my_student.didplay_detail()

    #person2
    james = Student("113","james",)
    james.didplay_detail()