#วิธีที่ 1
from cefe.cefe_module import Desserts
from cefe.cefe_module import Drinks
#วิธีที่ 2
#from cefe_module improt Desserts, Drinks

desserts = Desserts()
print(desserts.show_desserts())

drinks = Drinks()
print(drinks.show_drinks())
drinks.add_drink('สมูทตี้')
print(drinks.show_drinks())
drinks.add_drink('น้ำผลไม้')
print(drinks.show_drinks())