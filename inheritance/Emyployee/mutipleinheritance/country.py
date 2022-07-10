from geographic import Geograhic
from temperature import Temperature

class Contry(Geograhic,Temperature):
    def __init__(self,name,area,pop) -> None:
        super().__init__()
        Geograhic.__intit__(self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.poppulation = pop

    def getPopulationDensity(self):
       return self.population / self.area

    def show_detail(self):
        #ชื่อประเทศ
        print(f'Contry: {self.name}')
       
        #สถานที่ตั้ง
        print(self.getfahernheit())
        
        #แสดงขนาดพื้นที่
        print(f'Area {self.area}')
        print(f'Poppulation: {self.poppulation} Million')
        print(f'Density: {self.getpopulation_density()}')
       
        #time zone
        print(f'TimeZone: {self.gettimezone()}')
        print(f'Clmte: {self.getclimte()}')
        print(f'Temprerature(c): {self.celsius}')
        print(f'Temprerature(F): {self.getfahernheit()}')
        print(f'Weather: {self.getweather()}')
        print