from secrets import choice
from tkinter.colorchooser import Chooser
from measure import Measure

if __name__ == '__main__':
    mobj = Measure()
    #ให้ user เลือกได้ว่าต้องการแปลงเป็น inch หรือ cm
    choice = input(f'Choose menu (1: inch, 2:cm)')
    #รับค่าตัวเลขจาก user ได้
    number = float(input('Enter number : '))

    if choice == '1':
        print(f'{number} cm = {mobj.cm_inch(number):.2f} inch')
    elif choice == '2':
        print(f'{number} inch = {mobj.cm_inch(number):.2f} cm')
    else:
        print('choose wrong menu')

    #print(f'5 cm = {mobj.cm_inch(5):.2f} inch') #1.07
    #print(f'18.5 inch  = {mobj.inch_cm(18.5):.2f} cm') #46.99
