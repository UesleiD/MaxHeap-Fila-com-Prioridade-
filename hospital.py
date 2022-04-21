import os, time
from dataclasses import dataclass

class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.chamados = [0]
        self.indice = 999 

    def put(self, item, prioridade):
        self.heap.append((prioridade, self.indice, item))
        self.indice -= 1
        self.__floatUp(len(self.heap) - 1)


    def get(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:  # nao faz nada se for raiz
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)



@dataclass
class Paciente: 
    nomeCompleto : str
    tipoSanguineo : str
    dataNascimento : str
    
    def __init__(self):
            self.nomeCompleto = str(input("Digite seu nome completo: "))
            self.tipoSanguineo = str(input("Digite seu tipo sanguíneo: "))
            self.dataNascimento = str(input("Digite sua data de nascimento: "))

            

            
h = MaxHeap() 


def menu():
    while True:
        escolha = int(input("Escolha uma opção:\n(1) - Adicionar novo paciente\n(2) - Chamar o próximo paciente\n(3) - Mostrar o próximo paciente (sem chamar)\n(4) - Listar os últimos 5 chamados\n(5) - Sair\n---"))
        if escolha == 1:
            #Adição de Paciente
            paciente = Paciente()  
            prioridade = input("Digite sua prioridade de 10 a 1 ") 
            h.put(paciente, prioridade)
            print("Paciente adicionado com sucesso!")   
                
        elif escolha == 2:
            #Chamar próximo paciente
            paciente = h.get()
            h.chamados.append(paciente)
            print(paciente)

        elif escolha == 3:
            #Mostrar próximo paciente
            print(h.peek())
                   
        elif escolha == 4:
            #Mostrar os 5 últimos chamados
            print(*h.chamados[-5:], sep='\n')
        elif escolha == 5:
            quit()
        else:
            print("Opção Inválida!") 
        verNovamente = str(input('Quer escolher outra opção? (s/n)? '))
        if verNovamente == 's':
            print('Aguarde...logo o programa irá reiniciar.')
            time.sleep(2)
            os.system('cls')
        else:
            quit()

menu()

