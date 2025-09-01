# TAMANHOS
# PEQUENO = 0 4x4
# MÉDIO = 1 5x5
# GRANDE = 2 6x6
tamanho_mapa = 0

matriz_partida = []
if tamanho_mapa == 0:
    matriz_partida = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
elif tamanho_mapa == 1:
    matriz_partida = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
elif tamanho_mapa == 2:
    matriz_partida = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

tileset = {
    0: "",
    1: ""
}

def desenhar_mapa():
    matriz_desenhada = ""
    numero_colunas = len(matriz_partida[0])
    numero_linhas = len(matriz_partida)
    for linha in range(numero_linhas):
        for quadrado_coluna in range(numero_colunas):
            matriz_desenhada += "|￣￣￣| "
        matriz_desenhada += "\n"
        for segunda_parede_quadrado in range(numero_colunas):
            matriz_desenhada += "|     | "
        matriz_desenhada += "\n"
    for quadrado_coluna in range(numero_colunas):
        matriz_desenhada += " ￣￣￣  "

    print(matriz_desenhada)

desenhar_mapa()