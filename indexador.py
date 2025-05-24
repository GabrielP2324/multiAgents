import re
import pandas as pd
from sentence_transformers import SentenceTransformer
import hnswlib

# Leitura do texto de entrada
with open("o_alienista.txt", encoding="latin1") as f:
    texto = f.read()

# 🧼 Remove cabeçalho e rodapé do Project Gutenberg
inicio = texto.find("O ALIENISTA")
fim = texto.rfind("FIM")
texto = texto[inicio:fim] if inicio != -1 and fim != -1 else texto

# Inicializa modelo de embeddings
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Divide o texto em blocos a partir dos capítulos
blocos = re.split(r"(?i)cap[íi]tulo\s+\d+", texto)
blocos = [b.strip() for b in blocos if len(b.strip()) > 100]

# Gera os embeddings
embeddings = modelo.encode(blocos, convert_to_numpy=True)

# Cria e popula o índice
index = hnswlib.Index(space="cosine", dim=384)
index.init_index(max_elements=len(blocos), ef_construction=200, M=16)
index.add_items(embeddings)

# Salva o índice e os blocos
index.save_index("indice.bin")
pd.DataFrame({"bloco": blocos}).to_csv("blocos.csv", index=False)

print("Indexação finalizada com sucesso.")
