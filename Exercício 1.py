def cadastrar_estudantes():
    print("\nExercicio 1: ") 
    print("-----------------------------------------------------") 

    estudantes = []

    while True:
        nome = input("Digite o nome do estudante (ou 'PARE' para encerrar): ")
        if nome.upper() == "PARE":
            break    
            estudantes.append(nome)

    print(f"\nQuantidade de estudantes cadastrados: {len(estudantes)}")
    print("Lista de estudantes cadastrados:")

    for estudante in estudantes:
        print(f"{estudante}")

cadastrar_estudantes()