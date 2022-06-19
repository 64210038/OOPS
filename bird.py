class Bird:
    global bird_type #global variable #ถ้าไม่ใช่คำว่า global ตัวแปร bird_type จะกลายเป็น class veriable
    bird_type = 'porrot'
    bird_name = 'Lori' #class variable


    def __init__(self,color) -> None:
        self.color = color #instance variable
        name = 'peter' #local variable
        print(f'{name} in init') #call local variable

if __name__ == '__main__':
    my_bird = Bird('Green,Blue')

    #call instance variable ชื่อวัตถุ .instance variable
    print(my_bird.color)

     #call class variable #ชื่อคลาส class_variable
    print(Bird.bird_name)

    #call global variable #เรียกชื่อตัวแปรได้เลย
    print(bird_type)

    #error 
    #พยายามเรียก local variable
    #print(name) # NameError : name 'name' is not defined
    
    #พยายามเรียก global variable ผ่าน class
    #print(Bird.bird_type)
    #type object 'Bird' has no attribute 'bird_type'.