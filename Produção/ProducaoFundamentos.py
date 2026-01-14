# ProducaoFundamentos.py
# Produção (CLI) — Fundamentos de Python
# Autor: (Marcos Alvarães)
# Execução: python 

from __future__ import annotations
import json

CRITERIOS_SITUACAO = ("Reprovado", "Aprovado")  


def ler_int(mensagem: str, minimo: int | None = None, maximo: int | None = None) -> int:
    """Lê um inteiro com validação de intervalo (opcional)."""
    idade_int = 0

    while idade_int <= 0:
        idade_int = int(input(mensagem))
        if idade_int <= 0:
            print("Número inválido, tente inserir acima de 0.")
        return idade_int

def ler_string(mensagem: str) -> str:
    """Lê uma string não vazia (após strip)."""
    ler_str = ""

    while ler_str == "": 
        ler_str = str(input(mensagem))
        if ler_str == "":
            print("Nome inválido.")
    return ler_str

def ler_float(mensagem: str, minimo: float | None = None, maximo: float | None = None) -> float:
    """Lê um float com validação de intervalo (opcional). Aceita vírgula ou ponto."""
    lerAltura = 0
    while lerAltura < 1.0:
        lerAltura = float(input(mensagem))
        if lerAltura < 1.0:
            print("Altura inválida.")
    return lerAltura


def ler_nota(mensagem: str) -> float:
    """Lê uma nota (0 a 20)."""
    lerFloatNota = float(input(mensagem))
    return lerFloatNota

def calcular_media(notas: list[float]) -> float:
    """Calcula a média de uma lista de notas."""
    contador = 0
    media = 0

    for nota in notas:
        media = media + nota
        contador = contador + 1
    
    resultado_media = media / contador
    return resultado_media
    
def obter_situacao(media: float) -> str:
    """Determina Aprovado/Reprovado usando o tuplo CRITERIOS_SITUACAO."""

    if media < 10: 
        return CRITERIOS_SITUACAO[0] # Reprovado
    else: 
        return CRITERIOS_SITUACAO[1] # Aprovado

def obter_aproveitamento(media: float) -> str:
    """Classifica aproveitamento por intervalos."""
    aproveitamento = ""

    if media >= 14:
        aproveitamento = "Bom"
    elif media >= 10 and media < 14:
        aproveitamento = "Regular"
    else: 
        aproveitamento = "Insuficiente"
    return aproveitamento
    
def gravar_dict_to_json(alunos: list[dict]) -> None:
    """Grava o dicionario como um ficheiro json"""
    #print("[Função gravar_dict_to_json por implementar]")
    with open('06_Leonardo_0125_10793.json', 'w') as fp:
        json.dump(alunos, fp)
    print("Salvo com sucesso.")


##########################################################################################    

def criar_aluno() -> dict:
    """Recolhe dados, valida e devolve um dicionário com o aluno."""
    print("\n--- Adicionar Aluno ---")
    nome = ler_string("Nome do aluno: ")
    idade = ler_int("Idade: ", minimo=0)
    altura = ler_float("Altura (ex.: 1.65): ", minimo=0.3, maximo=2.5)

    notas: list[float] = []
    print("Introduza 3 notas (0 a 20).")
    for i in range(1, 4):
        nota = ler_nota(f"Nota {i}: ")
        notas.append(nota)

    media = calcular_media(notas)
    situacao = obter_situacao(media)
    aproveitamento = obter_aproveitamento(media)

    aluno = {
        "nome": nome,
        "idade": idade,
        "altura": altura,
        "notas": notas,
        "media": media,
        "situacao": situacao,
        "aproveitamento": aproveitamento,
    }
    print("Aluno registado com sucesso.\n")
    return aluno


def listar_alunos(alunos: list[dict]) -> None:
    """Lista alunos com informação resumida."""
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Sem alunos registados.")
        return

    for idx, a in enumerate(alunos, start=1):
        print(f"{idx:>2}. {a['nome']} | Média: {a['media']:.2f} | {a['situacao']} | {a['aproveitamento']}")


def estatisticas(alunos: list[dict]) -> None:
    """Mostra estatísticas globais da turma."""
    print("\n--- Estatísticas da Turma ---")
    if not alunos:
        print("Sem alunos registados.")
        return

    medias = [a["media"] for a in alunos]
    media_turma = calcular_media(medias)
    melhor_media = max(medias)
    pior_media = min(medias)

    aprovados = sum(1 for a in alunos if a["situacao"] == "Aprovado")
    reprovados = len(alunos) - aprovados

    dist = {"Bom": 0, "Regular": 0, "Insuficiente": 0}
    for a in alunos:
        dist[a["aproveitamento"]] += 1

    # Nomes dos melhores/piores (pode haver empate)
    melhores = [a["nome"] for a in alunos if a["media"] == melhor_media]
    piores = [a["nome"] for a in alunos if a["media"] == pior_media]

    print(f"Total de alunos: {len(alunos)}")
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Melhor média: {melhor_media:.2f} ({', '.join(melhores)})")
    print(f"Pior média: {pior_media:.2f} ({', '.join(piores)})")
    print(f"Aprovados: {aprovados} | Reprovados: {reprovados}")
    print("Distribuição por aproveitamento:")
    print(f"  Bom: {dist['Bom']}")
    print(f"  Regular: {dist['Regular']}")
    print(f"  Insuficiente: {dist['Insuficiente']}")


def menu() -> None:
    alunos: list[dict] = []

    while True:
        print("\n===== Gestor de Alunos =====")
        print("1) Adicionar aluno")
        print("2) Listar alunos")
        print("3) Estatisticas da turma")
        print("4) Gravar o Dict para json")
        print("5) Sair")

        opcao = ler_int("Escolha uma opção: ", minimo=1, maximo=5)
        #opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            aluno = criar_aluno()
            alunos.append(aluno)
            
        elif opcao == 2:
            listar_alunos(alunos)
            
        elif opcao == 3:
            estatisticas(alunos)
            
        elif opcao == 4:
            if not alunos:
                print("\nSem alunos registados para gravar.")
            else:
                gravar_dict_to_json(alunos)
        elif opcao == 5:
            print("\nA terminar. Obrigado.")
            break


if __name__ == "__main__":
    menu()
