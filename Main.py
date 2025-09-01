# TAMANHOS
# PEQUENO = 0 4x4
# MÉDIO = 1 5x5
# GRANDE = 2 6x6
tamanho_mapa = 1

matriz_partida = []
if tamanho_mapa == 0:
    matriz_partida = [
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ]
elif tamanho_mapa == 1:
    matriz_partida = [
        [0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
elif tamanho_mapa == 2:
    matriz_partida = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]

posicoes_navios_jogador1 = {

}

def preparar_partida():
    gerar_navios_escolha()

def gerar_navios_escolha(submarinos, encouracados, destroiers, cruzadores):
    '''
        Pegar a quantidade de navios
        Em ordem, tornar a escolha das posições dos navios para o usuario, clara
        Pedir para o usuário escolher a posição inicial do navio atual
        Checar os lados para os quais o usuario poderá posicionar o resto do navio
        Pedir o lado para qual o navio será colocado
        Posicionar o navio na matriz do jogador
    '''


def desenhar_mapa():
    matriz_desenhada = ""
    numero_colunas = len(matriz_partida[0])
    numero_linhas = len(matriz_partida)
    for linha in range(numero_linhas):
        for quadrado_coluna in range(numero_colunas):
            matriz_desenhada += "|￣￣￣￣| "
        matriz_desenhada += "\n"

        for segunda_parede_quadrado in range(numero_colunas):
            if segunda_parede_quadrado >= numero_colunas / 2:
                matriz_desenhada += " "
            #print(f"VALOR MATRIZ: {matriz_partida[linha][segunda_parede_quadrado]}")
            if matriz_partida[linha][segunda_parede_quadrado] == 1:
                matriz_desenhada += "|  🚢   | "
            else:
                matriz_desenhada += "|       | "
        matriz_desenhada += "\n"

        for terceira_parede_quadrado in range(numero_colunas):
            if terceira_parede_quadrado >= numero_colunas / 2:
                matriz_desenhada += " "
            matriz_desenhada += "|       | "
        matriz_desenhada += "\n"
    for quadrado_coluna in range(numero_colunas):
        matriz_desenhada += " ￣￣￣￣  "

    print(matriz_desenhada)

def main():

    desenhar_mapa()

main()