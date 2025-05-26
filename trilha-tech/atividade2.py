# Lista para armazenar as tarefas 
tarefas = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    print("\n>>> ADICIONANDO NOVA TAREFA")
    descricao = input("Digite a nova tarefa: ")
    tarefa = {"descricao": descricao, "status": "pendente"}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!\n")


# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("\n>>> LISTA DE TAREFAS:")
        print("Nenhuma tarefa encontrada.\n")
    else:
        print("\n>>> LISTA DE TAREFAS:")
        #  Mostra cada tarefa com um número começando do 1
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa['descricao']} - {tarefa['status']}")
        print()

# Função para remover uma tarefa
def remover_tarefa():
    print("\n>>> REMOVENDO TAREFA")
    listar_tarefas()
    if tarefas:
        try:
            numero = int(input("Digite o número da tarefa que deseja remover: "))
            if 1 <= numero <= len(tarefas):
                removida = tarefas.pop(numero - 1)
                print(f"Tarefa '{removida['descricao']}' removida com sucesso!\n")
            else:
                print("Número inválido.\n")
        except ValueError:
            print("Por favor, digite um número válido.\n")

# Função para marcar como concluída
def marcar_como_concluida():
    print("\n>>> MARCAR TAREFA COMO CONCLUÍDA")
    listar_tarefas()
    if tarefas:
        try:
            numero = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
            if 1 <= numero <= len(tarefas):
                tarefas[numero - 1]["status"] = "concluída"
                print("Tarefa marcada como concluída!\n")
            else:
                print("Número inválido.\n")
        except ValueError:
            print("Por favor, digite um número válido.\n")

# Função para marcar como pendente
def marcar_como_pendente():
    print("\n>>> MARCAR TAREFA COMO PENDENDE")
    listar_tarefas()
    if tarefas:
        try:
            numero = int(input("Digite o número da tarefa que deseja marcar como pendente: "))
            if 1 <= numero <= len(tarefas):
                tarefas[numero - 1]["status"] = "pendente"
                print("Tarefa marcada como pendente!\n")
            else:
                print("Número inválido.\n")
        except ValueError:
            print("Por favor, digite um número válido.\n")

# Loop principal
while True:
    print("""

°°°°°°°°°°° AGENDA ONLINE °°°°°°°°°°
             
    1. Adicionar tarefa
    2. Listar tarefas
    3. Remover tarefa
    4. Marcar tarefa como pendente
    5. Marcar tarefa como concluída
    6. Sair
          
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°          
""")


    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        marcar_como_pendente()
    elif opcao == "5":
        marcar_como_concluida()
    elif opcao == "6":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
