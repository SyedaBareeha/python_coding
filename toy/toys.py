class CuddlyToy:
    
    def __init__(self,type, size, colour, job):
        self.type=type
        self.size = size
        self.colour = colour
        self.job = job

    def make_noise(self):
        pass

    def describe(self):
        print(f"I am a{self.type} and i am of {self.size} and my color is  {self.colour} additionally I work as a {self.job}.")

class Teddy(CuddlyToy):
    def __init__(self, type, size, colour, job):
        super().__init__(type, size, colour, job)
    
     

    def make_noise(self):
        print("Growl!")

class Bunny(CuddlyToy):
   ## def __init__(self, size, colour, job):
     #   CuddlyToy.__init__(self,size, colour, job)

    def make_noise(self):
        print("Squeak!")

class EngineDriver(Teddy):
    def __init__(self, type, size, colour, job,speed):
        super().__init__(type, size, colour, job)
    
        self.speed=speed
    def show(self):
        print(f"I am driving train at a speed of {self.speed}.")    
            
class Gardener(Teddy):
    def __init__(self, size, colour, job):
        super().__init__(size, colour, job)
    
class Clown(Bunny):
    pass
    
class BankManager(Bunny):
    pass


