# Importa os agentes
from agenteA import agenteA_buscar
from agenteD import agenteD_resumir_blocos
from agenteB import agenteB_responder
from agenteC import agenteC_avaliar

# Lista de perguntas para teste
perguntas = [
    "Por que o personagem Simão Bacamarte decide internar a esposa no hospício?",
    "Quem era Simão Bacamarte?",
    "Qual o objetivo do hospício fundado por Bacamarte?"
]

# Função principal que coordena os quatro agentes para uma pergunta
def executar_fluxo(pergunta):
    print("\n" + "="*80)
    print(f"[Usuário]: {pergunta}")
    
    # Agente A: Recupera contexto
    contexto = agenteA_buscar(pergunta)
    print(f"[AgenteA - ContextRetriever]: Contexto recuperado com {len(contexto)} caracteres")

    # Agente D: Resume contexto
    resumos = agenteD_resumir_blocos([contexto])
    print(f"[AgenteD - Summarizer]: {len(resumos)} resumo(s) gerado(s)")

    # Concatenar os resumos
    contexto_final = " ".join(resumos)
    print(f"[Resumo passado ao Agente B]: {contexto_final[:300]}...")  # Mostra os primeiros 300 caracteres

    # Agente B: Gera resposta com base no resumo
    resposta = agenteB_responder(pergunta, contexto_resumido=contexto_final)
    print(f"[AgenteB - AnswerGenerator]: {resposta}")

    # Agente C: Avalia a resposta
    avaliacao = agenteC_avaliar(resposta)
    print(f"[AgenteC - AnswerEvaluator]: {avaliacao}")

# Execução direta em lote
if __name__ == "__main__":
    for pergunta in perguntas:
        executar_fluxo(pergunta)
