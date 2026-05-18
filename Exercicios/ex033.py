num1 = int(input(' digite o primeiro numero:'))
num2 = int(input(' digite o segundo numero:'))
num3 = int(input(' ditgite o terceiro numero:'))
menor = num1
maior = num1
if num2 > num1 and num2>num3:
       maior = num2
if num3 > num1 and num3>num2:
       maior = num3 
if num2 < num1 and num2<num3:
       menor = num2
if num3 < num1 and num3<num2:
       menor = num3
print(" o maior valor digitado foi {} e o menor {}" .format(maior,menor))      
