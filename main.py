class Asiento:
    def __init__(self, color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor():
        x=0
        if x in ["rojo","verde","amarillo","negro","blanco"]:
            Asiento.color=x
class Motor:
        def __init__(self, numeroCilindros,tipo,registro):
            self.numeroCilindros=numeroCilindros
            self.tipo=tipo
            self.registro=registro
        def cambiarRegistro():
             x=0
             Motor.registro=x
        def asignarTipo():
             x=0
             if x in ["electrico","gasolina"]:
                  Motor.tipo=x
class Auto:
     cantidadCreados=0
     def __init__(self, modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
     def cantidadAsientos():
        x=Auto
        contador=0
        for i in x:
             if type(i)==Asiento:
                  contador+=1
        return contador
     def verificarIntegridad():
          y=Motor
          if Auto.registro!=y.registro:
               return "Las piezas no son originales"
          for i in Auto.asientos:
               if type(i)==Asiento:
                    return "Las piezas no son originales"
          return "Auto original"
