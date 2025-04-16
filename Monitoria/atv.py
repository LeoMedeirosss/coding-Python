total = 0.0

while True:
    valor = float(input("Digite o valor do produto. Digite 0 para finalizar"))
    
    if(valor == 0):
        break
    elif(valor < 0):
        print("valor invalido")
        continue
    else:
        total = total + valor
        
if total >= 1000:
    desconto = total * 0.1
    total = total - desconto
    print(f"Desconto de R$ {desconto} aplicado")

print(f"total a pagar é: R$ {total}")