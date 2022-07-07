class Coche():
  def __init__(self):
    self.puertas = 4
    
  def add_puertas(self):
    self.puertas += 1
    
miCoche = Coche()
miCoche.add_puertas()

print(miCoche.puertas)
