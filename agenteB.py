# agenteB.py
from transformers import pipeline

# Usa modelo de Perguntas e Respostas em português
qa_pipeline = pipeline("question-answering", model="pierreguillou/bert-base-cased-squad-v1.1-portuguese", device="cuda")

# Função do Agente B recebe pergunta e contexto resumido (concatenado)
def agenteB_responder(pergunta: str, contexto_resumido: str) -> str:
    try:
        resposta = qa_pipeline(question=pergunta, context=contexto_resumido)
        return resposta["answer"]
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"
