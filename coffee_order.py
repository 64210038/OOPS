class coffee_order :
    def __init__(self,menu:str,total:float,customer_name:str,num:int,size:str,price:float):
        self.menu = menu
        self.total = total
        self.customer_name = customer_name
        self.num = num
        self.size = size
        self.price = price

def printcardetail(self):
        print(f"coffee: {self.coffee}")
        print(f"menu: {self.menu}")
        print(f"costomer_name: {self.costomer_name}")
        print(f"num: {self.num}")
        print(f"size: {self.size}")
        print(f"price: {self.price:,.2f}")


    def printcardetail(self):
        print(f'costomer_name : {self.costomer_name} menu: {self.menu} size: {self.size} num: {self.num} price: {self.price} total: {self.total}')


def __del__(self):
        print("object was destroyed")

if __name__ == "__main__":

#person1
    coffee = coffee_order (coffee,Espersso,john,1,m,3.00)
    coffee.didplay_detail()

#person2
    coffee = coffee_order (coffee,Americano,Mary,2,L,12.98)
    coffee.didplay_detail()
