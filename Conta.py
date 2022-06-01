class Conta:

  def __init__(self,banco,titular_da_conta,agencia,saldo):
    self.banco = banco
    self.titular_da_conta = titular_da_conta
    self.agencia = agencia
    self.saldo = saldo
  
  #Função Simples para realizar a operação de depósito
  def depositar(self,valor_depostito):
      self.saldo = self.saldo + valor_depostito
      print("depósito realizado com sucesso")
      print("Seu saldo atual é :R$", self.saldo,'\n')
      
  #Função Simples para realizar a operação de saque
  def sacar(self, valor_sacamento):
      if valor_sacamento > self.saldo:
          print("Impossível realizar a operação, o valor do saque é maior que o valor do seu saldo.")
      else:
          self.saldo = self.saldo - valor_sacamento
          print("Saque realizado com sucesso")
          print("Seu saldo atual é :R$", self.saldo,'\n')

  #Função Simples para realizar a operação de transferência
  def transferir(self,conta, valor_transferencia):
      try:
          self.sacar(valor_transferencia)
          conta.depositar(valor_transferencia)
          print("Transferência realizada com sucesso")
      except:
          print('error')