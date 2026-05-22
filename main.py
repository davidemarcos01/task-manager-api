tarefas = []

def criar_tarefa(nome):
    tarefas.append(nome)
    print(f"Tarefa '{nome}' criada com sucesso!")

def listar_tarefas():
    print("Lista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

def atualizar_tarefa(indice, novo_nome):
    if 0 <= indice < len(tarefas):
        tarefas[indice] = novo_nome
        print("Tarefa atualizada com sucesso!")
    else:
        print("Tarefa não encontrada.")

def deletar_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa deletada com sucesso!")
    else:
        print("Tarefa não encontrada.")


# Teste simples
criar_tarefa("Estudar Git")
listar_tarefas()
atualizar_tarefa(0, "Estudar Git Flow")
listar_tarefas()
deletar_tarefa(0)
listar_tarefas()
