class bucles:
  def funcionFor(self):

    #este programa recibe una lista en la variable listaNotas y filtra aquellas notas mayores o iguales a 3

    #lista que vamos a filtrar
    listaNotas = [5,2,3,1,0,3]

    #bucle que recorrera la listaNotas y guardara sus valores en la variable nota
    for nota in listaNotas:

      #condicional que inspeccionara cada nota y imprimira unicamente las mayores  o iguales a 3
      if nota >= 3:
        print(nota)

  def funcionWhile(self):

    #este codigo es un contador que hara que la variable aumente hasta llegar a 9
    
    #variable que aumentara
    contador = 0

    #bucle que se repetira hasta que el contador llegue a 10
    while(contador != 10):
      #imprime la variable y suma uno a la variable
      print(contador)
      contador += 1