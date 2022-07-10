class Temperature:
    def setcelsius(self,time):
        self.celsius = celsius
   
    def getfahernheit(self):
        return self.celsius * 1.8 + 32
    
    def getweather(self):
        if self.celsius <= 0:
            return 'freezing'
        elif self.celsius <= 18:
            return 'cold'
        elif self.celsius <= 28:
            return 'warm'
        else:
            return 'hot'

