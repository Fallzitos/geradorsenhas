import random
import time
print("BEM VINDO AO GERADOR DE SENHAS")
time.sleep(2)
espaco = ("")
minus = "minus"
verifi = ["minus"]
#---------------------------------------------------------------------
respostaM = print("Digite 1 para sim\nDigite 2 para não")
perguntaM = int(input("Sua senha deve conter letras MAIUSCULAS?"))
if perguntaM == 1:
    maiu = "maiu"
    verifi.append(maiu)
else:
    maiu = False
time.sleep(2)
print("(--------------------------------------)")
#---------------------------------------------------------------------
repostaN = print("Digite 1 para sim\nDigite 2 para não")
perguntaN = int(input("Sua senha deve conter NÚMEROS?"))
if perguntaN == 1:
    nume = "nume"
    verifi.append(nume)
else:
    nume = False
time.sleep(2)
print("(--------------------------------------)")
#---------------------------------------------------------------------
respostaS = print("Digite 1 para sim\nDigite 2 para não")
perguntaS = int(input("Sua senha deve conter Caracteres Especiais?"))

if perguntaS == 1:
    cara = "cara"
    verifi.append(cara)
else:
    cara = False
time.sleep(2)
print("(--------------------------------------)")
#---------------------------------------------------------------------
print("Está sendo gerado uma senha de 12 caracteres...")
cara1 = random.choice(verifi)

alfaminus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfamaius = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alfanume = ["1","2","3","4","5","6","7","8","9","0"]
alfacara = ["!","@","#","*"]

cara1 = random.choice(verifi)

if cara1 == maiu:
    cara1 = random.choice(alfamaius)
elif cara1 == nume:
    cara1 = random.choice(alfanume)
elif cara1 == cara:
    cara1 = random.choice(alfacara)
elif cara1 == minus:
    cara1 = random.choice(alfaminus)
    
cara2 = random.choice(verifi)

if cara2 == maiu:
    cara2 = random.choice(alfamaius)
elif cara2 == nume:
    cara2 = random.choice(alfanume)
elif cara2 == cara:
    cara2 = random.choice(alfacara)
elif cara2 == minus:
    cara2 = random.choice(alfaminus)

cara3 = random.choice(verifi)

if cara3 == maiu:
    cara3 = random.choice(alfamaius)
elif cara3 == nume:
    cara3 = random.choice(alfanume)
elif cara3 == cara:
    cara3 = random.choice(alfacara)
elif cara3 == minus:
    cara3 = random.choice(alfaminus)

cara4 = random.choice(verifi)

if cara4 == maiu:
    cara4 = random.choice(alfamaius)
elif cara4 == nume:
    cara4 = random.choice(alfanume)
elif cara4 == cara:
    cara4 = random.choice(alfacara)
elif cara4 == minus:
    cara4 = random.choice(alfaminus)

cara5 = random.choice(verifi)

if cara5 == maiu:
    cara5 = random.choice(alfamaius)
elif cara5 == nume:
    cara5 = random.choice(alfanume)
elif cara5 == cara:
    cara5 = random.choice(alfacara)
elif cara5 == minus:
    cara5 = random.choice(alfaminus)
    
cara6 = random.choice(verifi)

if cara6 == maiu:
    cara6 = random.choice(alfamaius)
elif cara6 == nume:
    cara6 = random.choice(alfanume)
elif cara6 == cara:
    cara6 = random.choice(alfacara)
elif cara6 == minus:
    cara6 = random.choice(alfaminus)
    
cara7 = random.choice(verifi)

if cara7 == maiu:
    cara7 = random.choice(alfamaius)
elif cara7 == nume:
    cara7 = random.choice(alfanume)
elif cara7 == cara:
    cara7 = random.choice(alfacara)
elif cara7 == minus:
    cara7 = random.choice(alfaminus)
    
cara8 = random.choice(verifi)

if cara8 == maiu:
    cara8 = random.choice(alfamaius)
elif cara8 == nume:
    cara8 = random.choice(alfanume)
elif cara8 == cara:
    cara8 = random.choice(alfacara)
elif cara8 == minus:
    cara8 = random.choice(alfaminus)
    
cara9 = random.choice(verifi)

if cara9 == maiu:
    cara9 = random.choice(alfamaius)
elif cara9 == nume:
    cara9 = random.choice(alfanume)
elif cara9 == cara:
    cara9 = random.choice(alfacara)
elif cara9 == minus:
    cara9 = random.choice(alfaminus)
    
cara10 = random.choice(verifi)

if cara10 == maiu:
    cara10 = random.choice(alfamaius)
elif cara10 == nume:
    cara10 = random.choice(alfanume)
elif cara10 == cara:
    cara10 = random.choice(alfacara)
elif cara10 == minus:
    cara10 = random.choice(alfaminus)
    
cara11 = random.choice(verifi)

if cara11 == maiu:
    cara11 = random.choice(alfamaius)
elif cara11 == nume:
    cara11 = random.choice(alfanume)
elif cara11 == cara:
    cara11 = random.choice(alfacara)
elif cara11 == minus:
    cara11 = random.choice(alfaminus)
    
cara12 = random.choice(verifi)

if cara12 == maiu:
    cara12 = random.choice(alfamaius)
elif cara12 == nume:
    cara12 = random.choice(alfanume)
elif cara12 == cara:
    cara12 = random.choice(alfacara)
elif cara12 == minus:
    cara12 = random.choice(alfaminus)
    
senhafinal = cara1+cara2+cara3+cara4+cara5+cara6+cara7+cara8+cara9+cara10+cara11+cara12
senga = open("senha.txt", "w")
senga.write(senhafinal)
