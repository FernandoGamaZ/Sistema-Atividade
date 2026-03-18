def adicionar_aluno_nota():
    alunos = []
    while True:
        aluno = input("Digite o nome do aluno: ")

        notas = []

        quantidade = int(input("Quantas notas o aluno tem ?: "))
        for i in range(quantidade):
            nota = float(input(f"Nota do aluno: {i+1} "))

            notas.append(nota)
        alunos.append((aluno , notas))
        return alunos
    