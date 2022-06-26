class Car:
    brand = "toyota"
    def __init__(self,model:str,colour:str,year:int,price:int) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price

    def printcardetail(self):
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"colour: {self.colour}")
        print(f"year: {self.year}")
        print(f"price: {self.price:,.2f}")

    def __del__(self):
        print("object was destroyed")
if __name__ == "__main__":
    my_car = Car("cross","white",2022,1500000)
    my_car.printcardetail()