import numpy as np
import random
import time

class VetorNaoOrdenado:#classe para trabalhar com vetores estáticos (sem as listas do Python)

  def __init__(self, capacidade): #método construtor
    self.capacidade = capacidade #quantos elementos vou poder guardar no meu vetor

    self.ultimaPosicao = -1 #pois o vetor começa vazio

    self.valores = np.empty(capacidade, dtype=int)#criando o vetor

  def inserir(self, valor):#insere um elemento no final
    self.ultimaPosicao = self.ultimaPosicao+1
    self.valores[self.ultimaPosicao] = valor

  def imprimir(self):#imprime todo o vetor
    for i in range(self.ultimaPosicao+1):
        print('posição ', i, ' valor ', self.valores[i])

  def ordena_bolha(self): #ordena o vetor pelo método Bubble Sort
    troca = True
    while troca: #repito enquanto houver ao menos uma troca
      troca = False
      for i in range(self.ultimaPosicao):   
        if self.valores[i] > self.valores[i+1]:#se o da esquerda é maior então troca
          aux = self.valores[i]
          self.valores[i] = self.valores[i+1]
          self.valores[i+1] = aux
          troca = True

  def Busca_VetorNaoOrdenado(self, valor):#faz uma busca sequencial até o fim do vetor
    for i in range(self.ultimaPosicao + 1):
      if self.valores[i] == valor:
        return i
      
    return -1#se chegou até aqui não encontrou

  def Busca_VetorOrdenado(self, valor):#faz uma busca sequencial até o fim do vetor
    for i in range(self.ultimaPosicao+1):
      if self.valores[i] == valor:
        return i
      elif self.valores[i] > valor:
        return -1#já não tenho chance de encontrar

    return -1#se chegou até aqui não encontrou

x = VetorNaoOrdenado(9000001)
for i in range(9000000):
  x.inserir(random.randrange(0, 555)) #inserindo valores aleatórios

x.inserir(556)
#x.ordena_bolha()
#x.imprimir()

antes = time.time() #timestamp de antes de chamar a busca
pos = x.Busca_VetorNaoOrdenado(556)

segundos = time.time() - antes
print(f'Levou {segundos} segundos')

if pos >= 0:
  print(f'Valor encontrado na posição {pos}')
else:
  print('Valor não encontrado')

