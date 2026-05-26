"""
Operador    Função
+           soma
-           subtração
*           multiplicação
/           divisão
//          divisão inteira
%           resto divisão
**          potência
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


soma = num1 + num2
print(f"Soma: {soma}")

sub = num1 - num2
print(f"Subtração: {sub}")

mult = num1 * num2
print(f"Multiplicação: {mult}")

div = num1 / num2
print(f"Divisão: {div}")

div_int = num1 % num2
print(f"Divisão inteira: {div_int}")

resto = div
print(f"Resto: {resto}")

pot = num1 ** num2
print(f"Potência: {pot}")

