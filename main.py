class Asiento:
    def _init_(self, color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self):
        x=0
        if x in ["rojo","verde","amarillo","negro","blanco"]:
            self.color=x
class Motor:
        def _init_(self, numeroCilindros,tipo,registro):
            self.numeroCilindros=numeroCilindros
            self.tipo=tipo
            self.registro=registro
        def cambiarRegistro(self):
             x=0
             self.registro=x
        def asignarTipo(self):
             x=0
             if x in ["electrico","gasolina"]:
                  self.tipo=x
class Auto:
     cantidadCreados=0
     def _init_(self, modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
     def cantidadAsientos(self):
        x=Auto
        contador=0
        for i in x:
             if type(i)==Asiento:
                  contador+=1
        return contador
     def verificarIntegridad(self):
          y=Motor
          if self.registro!=y.registro:
               return "Las piezas no son originales"
          for i in self.asientos:
               if type(i)==Asiento:
                    return "Las piezas no son originales"
          return "Auto original"
