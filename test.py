temperatura = int(input("Quantos graus está agora?: "))

tipo = str(input("Qual a unidade de medida? (C para Celsius e F para Fahrenheit): "))


temp = 0



if  tipo == "C" :

    conversão = (temperatura * 1.8) + 32 

    temp += 1

else: 

    conversão = (temperatura - 32) / 1.8

if temp == 0:

    temp = "Celsius" 

else:
    temp = "Fahrenheit"


print(f" A temperatura foi transformada em {temp}, assim, a temperatura será {conversão}")


