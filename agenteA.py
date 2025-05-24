# Importa modelo de embeddings semânticos (SentenceTransformer)
from sentence_transformers import SentenceTransformer
# Biblioteca de indexação vetorial eficiente (HNSW)
import hnswlib
# Biblioteca pandas para manipulação de dados tabulares
import pandas as pd

# Carregamento de modelo e índice
# Carrega o modelo de embedding 'all-MiniLM-L6-v2'
modelo = SentenceTransformer("all-MiniLM-L6-v2")
# Cria o índice de busca baseado em vetores (HNSW)
index = hnswlib.Index(space="cosine", dim=384)
# Carrega o índice vetorial salvo anteriormente
index.load_index("indice.bin")
# Lê o arquivo com os blocos textuais indexados
df = pd.read_csv("blocos.csv")

# Define função do agente com seu comportamento principal
def agenteA_buscar(pergunta: str) -> str:
# Gera embedding da pergunta ou bloco textual
    emb = modelo.encode([pergunta], convert_to_numpy=True)
    k = min(3, index.get_current_count())
    if k == 0:
# Retorna o(s) bloco(s) mais relevante(s) como contexto
        return "Nenhum bloco encontrado. Reexecute o indexador com conteúdo válido."
# Recupera os vetores mais próximos do embedding da pergunta
    idxs, _ = index.knn_query(emb, k=k)
# Retorna o(s) bloco(s) mais relevante(s) como contexto
    return " ".join(df.iloc[i].bloco for i in idxs[0])
