#วิธีที่1
from my_math import sqrt,circle_area

print(f'aqart of 5 = {sqrt(5)}')
print(f'circle_area = {circle_area(2):,.2f}')

#วิธีที่2
import my_math as my
print("****วิธีที่2****")
print(f'aqart of 5 = {my.sqrt(5)}')
print(f'circle_area = {my.circle_area(2):,.2f}')