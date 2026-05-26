"""
op1             lógico      op2
operação1       >           operação2
operação1       >=          operação2
operação1       <           operação2
operação1       <=          operação2
operação1       ==          operação2
operação1       not         operação2
operação1       and         operação2
operação1       or          operação2
Resultador valor True/False
"""

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print(f"O valor {num1} é maior que o valor {num2}")
elif num1 >= num2:
    print(f"O valor {num1} é maior ou igual ao valor {num2}")
elif num1 < num2:
    print(f"O valor {num1} é menor que o valor {num2}")
elif num1 <= num2:
    print(f"O valor {num1} é menor ou igual ao valor {num2}")
elif num1 == num2:
    print(f"O valor {num1} é igual ao valor {num2}")
else:
    print("Insira os valores!")

