import math

ang = float(input("digite o ângulo que você deseja"))
seno = math.sin(math.radians(ang))   # converte para radianos antes de calcular o seno
cose = math.cos(math.radians(ang))   # converte para radianos antes de calcular o cosseno
tang = math.tan(math.radians(ang))   # converte para radianos antes de calcular a tangente

print("O ângulo de {} tem seno de {:.2f}".format(ang, seno))
print("O ângulo de {} tem cosseno de {:.2f}".format(ang, cose))
print("O ângulo de {} tem tangente de {:.2f}".format(ang, tang))
