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
    
    
def validar_notas(alunos):

    for nome, notas in alunos:

        for nota in notas:

            if nota < 0 or nota > 10:
                print("Nota inválida encontrada!")
                return False

    return True

def calcular_media(notas):

    return sum(notas) / len(notas)


def verificar_status(media):

    if media >= 7:
        return "Aprovado"

    elif media >= 5:
        return "Recuperação"

    else:
        return "Reprovado"
    

def processar_alunos(alunos):

    resultados = []

    for nome, notas in alunos:

        media = calcular_media(notas)

        status = verificar_status(media)

        resultados.append((nome, media, status))

    return resultados


def mostrar_resultados(resultados):

    print("\nRESULTADOS\n")

    for nome, media, status in resultados:

        print(nome, "- média:", round(media,2), "-", status)