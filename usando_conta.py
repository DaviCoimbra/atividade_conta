from ast import main
from Conta import *

conta_1 = Conta("Banco do Brasil","Davi", "8765-2", 1000)
conta_2 = Conta("Bradesco","Lucas", "3127-8",500)
conta_1.sacar(100)
conta_2.depositar(100)
conta_1.transferir(conta_2,100)

if __name__== '__main__':
    main()