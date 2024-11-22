class Superhero:
    def __init__(self, name, power, alias):
        self.name = name      # name of the superhero
        self.power = power    # superpower they possess
        self.alias = alias    # Superhero alias 
    

class Villain(Superhero):
    def __init__(self, name, power, alias, evil_plan):
        super().__init__(name, power, alias)
        self.evil_plan = evil_plan
    
    def reveal_plan(self):
        return f"{self.alias}'s evil plan is: {self.evil_plan}"

    def superpower(self):
        return f"{self.alias} is using {self.power} to cause chaos!"

# Creating an instance of Villain
villain = Villain("Norman Osborn", "Super Strength", "Green Goblin", "Take over the city!")
print(villain.reveal_plan())
print(villain.superpower())