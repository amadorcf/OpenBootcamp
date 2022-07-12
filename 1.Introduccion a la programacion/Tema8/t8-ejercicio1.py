# ## NOTA ##
# En el siguiente ejemplo he creado tres @property
# para cada atributo de la clase Persona.
# He establecido cada atributo como protegido y he
# expuesto el atributo nombre con un setter, que
# permite cambiar el nombre de la persona pero
# no la edad ni el telefono.

class Persona:

    def __init__(self, edad, nombre, telefono):
        self._nombre = nombre
        self._edad = edad
        self._telefono = telefono

    def presentar_persona(self):
        return f'{self.nombre} tiene {self.edad} años'

    # Atributo nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Atributo edad
    @property
    def edad(self):
        return self._edad

    # Atributo telefono
    @property
    def telefono(self):
        return self._telefono


persona1 = Persona(19, "Paco", 123456789)
print(persona1.presentar_persona())  # Getter

persona1.nombre = "Manolo"  # Setter
print(persona1.presentar_persona())  # Getter
