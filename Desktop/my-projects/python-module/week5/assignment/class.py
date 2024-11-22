class Superhero:
    def __init__(self, name, power, alias):
        self.name = name      # name of the superhero
        self.power = power    # superpower they possess
        self.alias = alias    # Superhero alias 
    
    def introduce(self):
        return f"Hi, I am {self.alias}, but my real name is {self.name}. I have the power of {self.power}!"
    
    def use_power(self):
        return f"{self.alias} is using {self.power} to save the day!"
    
    def __str__(self):
        return f"Superhero: {self.alias}, Real Name: {self.name}, Power: {self.power}"

# Lets create an instance of Superhero
superhero = Superhero("Peter Parker", "Web-Slinging", "Spider-Man")
print(superhero.introduce())
print(superhero.use_power())

class Villain(Superhero):
    def __init__(self, name, power, alias, evil_plan):
        super().__init__(name, power, alias)
        self.evil_plan = evil_plan
    
    def reveal_plan(self):
        return f"{self.alias}'s evil plan is: {self.evil_plan}"

    def use_power(self):
        return f"{self.alias} is using {self.power} to cause chaos!"

# Creating an instance of Villain
villain = Villain("Norman Osborn", "Super Strength", "Green Goblin", "Take over the city!")
print(villain.reveal_plan())
print(villain.use_power())

