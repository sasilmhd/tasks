class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
    def drive(self,Km):
        self.odometer=self.odometer+Km
    def get_info(self):
    
        print(f"The car travelled {self.odometer}km{"s" if self.odometer>1 else ""}")
car1=Car("BMW","M4",2024)
car2=Car("Benz","G-Wagon", 2024)
car1.drive(1)
car1.drive(0)
car2.drive(10)
car2.drive(0)
print(f"The Car Covered {car1.odometer}km{"s" if car1.odometer>1 else ""}")
car1.get_info()
car2.get_info()
