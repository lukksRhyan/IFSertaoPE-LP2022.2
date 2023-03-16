import json
#esse aqui eu fui muito pro, isso aqui le o arquivo alunos.json e salva em html a situacao da turma
def media(aluno):
    return (aluno['nota1'] + aluno['nota2']) / 2

def situacao(aluno):
    nota_final = media(aluno)

    if nota_final < 4:
        return 'reprovado'
    elif nota_final >= 4 and nota_final < 7:
        return 'em recuperação'
    elif nota_final > 7:
        return 'aprovado'
def ver_aluno(aluno):
    print(f"Nome: {aluno['aluno']}\nMédia: {media(aluno)}\n{situacao(aluno)}")

with open('alunos.json', 'r') as alunos:
    notas = json.load(alunos)
    reprovados = 0
    aprovados = 0
    recuperacao = 0

    for aluno in notas:
        ver_aluno(aluno)

with open('SituacaoTurma.html', 'w') as quadro_geral:
    for aluno in notas:
        if situacao(aluno) == 'reprovado':
            reprovados += 1
        elif situacao(aluno) == 'em recuperação':
            recuperacao += 1
        elif situacao(aluno) == 'aprovado':
            aprovados +=1
    texto = f"""<html>
<head>
    <title>Quadro Geral</title>
</head>
<body>
    <h1>Situacao da turma</h1>
    <p>Reprovados:{reprovados}</p>
    <p>Aprovados:{aprovados}</p>
    <p>Em recuperacao:{recuperacao}</p>
</body>
</html>"""
    quadro_geral.write(texto)