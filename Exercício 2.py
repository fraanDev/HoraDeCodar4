def verificar_planeta():
    print("\nExercicio 2: ") 
    print("-----------------------------------------------------") 

    planetas = ['TERRA', 'MARTE', 'PLUTAO', 'VENUS', 'JUPITER', 'SATURNO']

    planeta_escolhido = input("Digite o nome de um planeta (sem acento): ").upper()

   
    if planeta_escolhido in planetas:
        
        print(f"O planeta {planeta_escolhido} está na lista!")

    else:
        print(f"O planeta {planeta_escolhido} NÃO está na lista.") 

verificar_planeta()