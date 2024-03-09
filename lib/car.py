from vehicle import Vehicle

# class Car(Vehicle):

    # def __init__(self, wheel_Size,wheel_number): 
    #     self.wheel_Size = wheel_Size
    #     self.wheel_number = wheel_number

    #     def go(self):
    #         return "vrrrrrrooom!"



class  Car(Vehicle):
    def __init__(self, wheel_size, wheel_number):
            self.wheel_size = wheel_size
            self.wheel_number = wheel_number

    def go(self):
            return "vrrrrrrrooom!"

    def fill_up_tank(self):
            return "filling up!"


    #     def fill_up_tank(self):
    #         return "filling up!"

        # def __init__(self,wheel_number):
        #     self.wheel_number = wheel_number
        #     self.wheel_Size = wheel_number

        # def go(self):
        #     return "vrrrrrrrooom!"

        # def fill_up_tank (self):
        #     return "filling up!"

    # def __init__(self, wheel_number, wheel_size):
    #     self.wheel_number = wheel_number
    #     self.wheel_size = wheel_size

    # def go(self):
    #     return "vrrrrrrrooom!"

    # def fill_up_tank(self):
    #     return "filling up!"


    # def __init__(self, wheel_number, wheel_size):
    #     self.wheel_size = wheel_size
    #     self.wheel_number = wheel_number

    # def go(self):
    #     return "vrrrrrrrooom!"

    # def fill_up_tank(self):
    #     return "filling up!"