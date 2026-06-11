"""
Desafio: A empresa solicita uma demanda para o controle de transações bancárias, onde deverão ser apresentadas as principais operações como 

saque, depósito, transferência, entre contas. 



Projeto Integrado Python 

Sistema Bancário Orientado a Objetos 

Contexto do Projeto 

Uma instituição financeira precisa de um sistema simples para controlar transações bancárias entre clientes. O sistema deverá permitir: 

    Criar contas bancárias  

    Realizar depósitos  

    Efetuar saques  

    Fazer transferências entre contas  

    Exibir extrato  

    Trabalhar com diferentes tipos de contas  

O projeto foi elaborado para praticar: 

    ✅ Classes 

    ✅ Objetos 

    ✅ Métodos 

    ✅ Herança 

    ✅ Encapsulamento 

    ✅ Métodos Especiais (__init__, __str__) 

    
Requisitos do Sistema 

Cliente 

    -Nome  

    -CPF  

Conta 

    -Número da conta  

    -Titular  

    -Saldo  

Operações 

    -Depositar  

    -Sacar  

    -Transferir  

    -Consultar saldo  

Conta Corrente 

    -Possui limite extra para saque. 

Conta Poupança 

    -Não possui limite extra. 
"""


class Cliente:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf


    def __str__(self):
        return f"\nCadastro realizado!\nCliente: {self.nome}\nCPF: {self.cpf}\n"




class Conta:
    def __init__(self,numero_conta,titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f"\nCliente: {self.titular.nome} depositou {valor:.2f}\nSaldo atual: {self.saldo}\n") # :.2f = o valor com mais duas casas decimais, exemplo: 250.00
        else:
            print("Valor inválido")

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"\nCliente: {self.titular.nome} sacou R${valor:.2f}\nSaldo atual: {self.saldo}\n")
        else:
            print("Saldo insuficiente")
    

    def transferir(self,destinatario,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"\nCliente: {self.titular.nome} transferiu R${valor:.2f}")
        else:
            print("Saldo insuficiente")
        
    def exibir_saldo(self):
        print(f"Saldo atual: {self.saldo}")


    def __str__(self):
        return f"\nNúmero da conta: {self.numero_conta}\nTitular: {self.titular}\nSaldo atual: {self.saldo}\n"


class ContaCorrente(Conta):
    def __init__(self,numero_conta,titular,limite):
        super().__init__(numero_conta,titular)
        self.limite = limite

    def sacar(self, valor):
        if valor <=(self.saldo + self.limite):
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado")
        else:
            print("Saldo insuficiente")

    def __str__(self):
        return f"\nConta Corrente:\nNúmero da conta: {self.numero_conta}\nTitular: {self.titular.nome}\nSaldo atual: {self.saldo}\nLimite disponível: {self.limite}\n"
    

class ContaPoupanca(Conta):
    def __str__(self):
        return f"\nConta Poupança:\nNúmero da conta: {self.numero_conta}\nTitular: {self.titular.nome}\nSaldo atual: {self.saldo}\n"
    


cliente1 = Cliente("Jefferson","183.543.624-04")
cliente2 = Cliente("Soares","177.018.576-02")

conta1 = ContaCorrente(1001,cliente1,500)
conta2 = ContaPoupanca(1002,cliente2)


print("\n=====Depósito=====")
conta1.depositar(1200)

print("\n=====Saque=====")
conta1.sacar(200)

print("\n=====Transferência=====")
conta1.transferir(conta2,200)

print("\n=====Saldos=====")
conta1.exibir_saldo()