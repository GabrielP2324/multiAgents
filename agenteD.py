from transformers import pipeline

# Carrega o modelo de sumarização
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Divide blocos grandes em partes menores
def dividir_texto_em_partes(texto, max_chars=1500):
    return [texto[i:i+max_chars] for i in range(0, len(texto), max_chars)]

# Função principal do agente D
def agenteD_resumir_blocos(blocos, max_length=130, min_length=30):
    resumos = []

    for bloco in blocos:
        partes = dividir_texto_em_partes(bloco)  # divide o bloco grande
        for parte in partes:
            if len(parte.strip()) > 0:
                try:
                    resumo = summarizer(parte, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
                    resumos.append(resumo)
                except Exception as e:
                    print(f"[AgenteD] Erro ao resumir parte: {e}")
    
    return resumos
