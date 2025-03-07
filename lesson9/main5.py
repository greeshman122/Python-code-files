class Robot:
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am a robot created to {self.purpose}.")

# Create an instance of Robot
pilot = Robot("Bunty", "assist and provide information to users like you")

# Introduce the robot
pilot.introduce()
