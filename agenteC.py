# Define função do agente com seu comportamento principal
def agenteC_avaliar(resposta: str) -> str:
    if len(resposta.split()) < 4:
# Retorna o(s) bloco(s) mais relevante(s) como contexto
        return "Resposta curta demais. Reavalie."
    if any(p in resposta.lower() for p in ["não sei", "desconhecido", "irrelevante"]):
# Retorna o(s) bloco(s) mais relevante(s) como contexto
        return "Resposta vaga. Solicite nova tentativa."
# Retorna o(s) bloco(s) mais relevante(s) como contexto
    return "Resposta satisfatória."