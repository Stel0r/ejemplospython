#definicion de el constructor de la clase esfero

class esfero:
  #definicion del constructor del esfero
  def __init__(self, color:str, marca:str):
    #variables de clase
    self.colorTinta = color
    self.marca = marca

  #ejemplo de funcion de clase
  def mostrarColor(self):
    print("el color de la tinta es: "+self.colorTinta)


