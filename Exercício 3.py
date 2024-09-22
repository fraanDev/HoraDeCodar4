def remover_frutas():
    print("\nExercicio 3: ") 
    print("-----------------------------------------------------") 
    
    frutas = ['PERA', 'LARANJA', 'MORANGO', 'MAÇA', 'BANANA']

    print("Lista completa:")
    print(frutas)

    while frutas:
        fruta_escolhida = input("\nDigite o nome de um produto para remover (sem acentos.): ").upper()

        if fruta_escolhida in frutas:
            frutas.remove(fruta_escolhida)  
            print(f"A fruta '{fruta_escolhida}' foi retirada da lista.") 
        else:
            print("Produto indisponível no nosso mercado.") 

        print("Lista atual:", frutas)

    print("\nTodos os produtos foram removidos da lista.")

remover_frutas()