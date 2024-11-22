class Superhero:
    def __init__(self, name, power, alias):
        self.name = name      # Real name of the superhero
        self.power = power    # The superpower they possess
        self.alias = alias    # Superhero alias (e.g., "Spider-Man")
    
    def introduce(self):
        return f"Hi, I am {self.alias}, but my real name is {self.name}. I have the power of {self.power}!"
    
    def use_power(self):
        return f"{self.alias} is using {self.power} to save the day!"
    
    def __str__(self):
        return f"Superhero: {self.alias}, Real Name: {self.name}, Power: {self.power}"

# Creating an instance of Superhero
superhero = Superhero("Peter Parker", "Web-Slinging", "Spider-Man")
print(superhero.introduce())
print(superhero.use_power())
