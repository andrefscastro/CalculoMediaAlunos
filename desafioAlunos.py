import json

##programa para calcular a media dos alunos buscandos os dados em um arquivo JSON

with open('AlunosNota.json', 'r', encoding="utf-8") as file:
    dados = json.load(file)

for estudante in dados['Alunos']:
    notas = estudante["notas"]
    mediaNotas = sum(notas)/len(notas)
    estudante["media"] = mediaNotas

with open('AlunosNota.json', 'w', encoding="utf-8") as file:
    json.dump(dados, file, indent=2)


##gravar dados de estudantes aprovados e reprovados

with open('AlunosAprovados.json', 'w') as fileabove, \
    open('AlunosReprovados.json', 'w') as filebelow:

    estudantesAprovados = [s for s in dados["Alunos"] if s["media"] >= 70]
    estudantesReprovados = [s for s in dados["Alunos"] if s["media"] < 70]

    json.dump({"Alunos": estudantesAprovados}, fileabove, indent=2)
    json.dump({"Alunos": estudantesReprovados}, filebelow, indent=2)
