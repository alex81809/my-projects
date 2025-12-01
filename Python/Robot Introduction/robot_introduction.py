class Robot: 
    def __init__(self, name, bot):
        self.name = name
        self.bot = bot
    
    def show_info(self):
        print(f"Hello, my name is {self.name} and I am the {self.bot}")

robot1 = Robot("Tom", "first robot")
robot1.show_info()

robot2 = Robot("Jerry", "second robot")
robot2.show_info()
