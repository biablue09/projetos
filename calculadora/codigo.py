numero_1 = float(input("digite 1 numero:"))
numero_2 = float(input( "digite 2 numero:" ))
operacao = input ("operação ( +, -, /, * ) ").strip()

if operacao == "+":
    resultado = numero_1 + numero_2
elif operacao == "-":
     resultado = numero_1 - numero_2
elif operacao == "*":
    resultado = numero_1 * numero_2
elif operacao == "/":
    if numero_2 == 0:
        resultado =  "não é possivel dividir"
    else:
        resultado =  numero_1 / numero_2

else:
    resultado = "operação invalida"

print(f"resultado: {resultado}")



