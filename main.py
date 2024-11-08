class Asiento:
    def __init__(self, color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,x):
        if x in ["rojo","verde","amarillo","negro","blanco"]:
            self.color=x
class Motor:
        def __init__(self, numeroCilindros,tipo,registro):
            self.numeroCilindros=numeroCilindros
            self.tipo=tipo
            self.registro=registro
        def cambiarRegistro(self,x):
             self.registro=x
        def asignarTipo(self,x):
             if x in ["electrico","gasolina"]:
                  self.tipo=x
class Auto:
     cantidadCreados=0
     def __init__(self, modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
     def cantidadAsientos(self,x):
        contador=0
        for i in x:
             if type(i)==Asiento:
                  contador+=1
        return contador
     def verificarIntegridad(self,y):
          if self.registro!=y.registro:
               return "Las piezas no son originales"
          for i in Auto.asientos:
               if type(i)==Asiento:
                    return "Las piezas no son originales"
          return "Auto original"
