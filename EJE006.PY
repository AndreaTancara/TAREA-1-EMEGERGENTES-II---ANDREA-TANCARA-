#Sentencias 

temperatura = int(input("Indiquela temperatura: "))

if temperatura > 28:
    print("Hace calor")
else:
    print("Hace frío")  

if temperatura > 28:
    print("Hace calor")
elif temperatura > 20:
    print("Hace templado")
elif temperatura > 10:
    print("Hace fresco")
else:
    print("Hace frío")  
    
print("Fin del programa")