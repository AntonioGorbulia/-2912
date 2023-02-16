class Cupboard:
    def __init__(self, name):
        self.name = name
 
    def break(self):
        print(f"Copboard {self.name} break")
 
 
class Table(Cupboard):
    def __init__(self, name):
        super().__init__(name)
 
    def stand(self):
        print(f"Table {self.name} stand")
 
    def break(self):
        print(f"Table {self.name} break")
 
    def old_break(self):
        super().break()

class Chair(Cupboard):
    def __init__(self, name):
        super().__init__(name)
 
    def lie(self):
        print(f"Human {self.name} lie")
 
    def break(self):
        print(f"Human {self.name} break")
 
    def old_break(self):
        super().break()      
 
cupboard = Cupboard("Capybara")
table = Table("Tablet")
chair = Chair("Charry")
cupboard.break()
table.break()
chair.break()
table.old_break()
chair.old_break()
table.stand()
chair.lie()
