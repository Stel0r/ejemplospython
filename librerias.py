import time

class libreria:
  def funcion(self,segundos:int):

    #este codigo es un contador que hara que la variable aumente hasta llegar a el argumento dado
    
    #variable que aumentara
    contador = 0

    #bucle que se repetira hasta que el contador llegue a 10
    while(contador != segundos+1):
      #imprime la variable y suma uno a la variable
      print(contador)
      contador += 1
      #hara que el programa espere un segundo (funcion de la libreria time)
      time.sleep(1)
      