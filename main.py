import processamento as pr

alunos = pr.adicionar_aluno_nota()

pr.validar_notas(alunos)
print(alunos)

resultados = pr.processar_alunos(alunos)

pr.mostrar_resultados(resultados)

pr.gerar_relatorio(resultados)