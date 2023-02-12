class Monkey:
    def __init__(self, name):
        self.name = name
 
    def jump(self):
        print(f"Monkey {self.name} jump")
 
 
class Human(Monkey):
    def __init__(self, name):
        super().__init__(name)
 
    def build(self):
        print(f"Human {self.name} build home")
 
    def jump(self):
        print(f"Human {self.name} jump")
 
    def old_jump(self):
        super().jump()
 
 
monkey = Monkey("Money")
human = Human("Stepan")
monkey.jump()
human.jump()
human.old_jump()
human.build()
 
