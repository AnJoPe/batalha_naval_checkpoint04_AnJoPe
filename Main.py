# TAMANHOS
# PEQUENO = 0 4x4
# MÉDIO = 1 5x5
# GRANDE = 2 6x6
from conda.instructions import PRINT

tamanho_mapa = 1

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

numero_submarinos = 0
numero_destroiers = 0
numero_cruzadores = 0
numero_encouracados = 0

posicoes_navios_jogador1 = {

}
posicoes_navios_jogador2 = {

}

identificadores_navios = {
    "Submarino": {
        "Identificador": 1,
        "Tamanho": 1
    },
    "Destróier": {
        "Identificador": 2,
        "Tamanho": 2
    },
    "Cruzador": {
        "Identificador": 3,
        "Tamanho": 3
    },
    "Encouraçado": {
        "Identificador": 4,
        "Tamanho": 4
    }
}


def preparar_partida():

    if tamanho_mapa == 0:
        numero_submarinos = 1
        numero_destroiers = 1
        numero_encouracados = 0
        numero_cruzadores = 0
    elif tamanho_mapa == 1:
        numero_submarinos = 1
        numero_destroiers = 1
        numero_encouracados = 1
        numero_cruzadores = 1
    elif tamanho_mapa == 2:
        numero_submarinos = 1
        numero_destroiers = 2
        numero_encouracados = 2
        numero_cruzadores = 1

    gerar_navios_escolha(numero_submarinos, numero_encouracados, numero_destroiers, numero_cruzadores)

def gerar_navios_escolha(submarinos, encouracados, destroiers, cruzadores):
    """
        -------Pegar a quantidade de navios
        Em ordem, tornar a escolha das posições dos navios para o usuario, clara
        Pedir para o usuário escolher a posição inicial do navio atual
        Checar os lados para os quais o usuario poderá posicionar o resto do navio
        Pedir o lado para qual o navio será colocado
        Posicionar o navio na matriz do jogador
    """
    lista_navios_para_adicionar = {}

    if submarinos > 0:
        lista_navios_para_adicionar["Submarino"] = submarinos
    if encouracados > 0:
        lista_navios_para_adicionar["Encouraçado"] = encouracados
    if destroiers > 0:
        lista_navios_para_adicionar["Destróier"] = destroiers
    if cruzadores > 0:
        lista_navios_para_adicionar["Cruzador"] = cruzadores

    for navio in lista_navios_para_adicionar:
        while lista_navios_para_adicionar[navio] > 0:
            desenhar_mapa()
            posicao_inicial_linha = int(input(f"Insira, por favor, a linha inicial na qual você deseja inserir um {navio}: "))
            posicao_inicial_coluna = int(input(f"Insira, por favor, a coluna inicial na qual você deseja inserir um {navio}: "))
            ###CHECA SE SÃO LINHAS E COLUNAS VÁLIDAS!!!
                ###UMA LINHA E COLUNA VALIDA ESTÁ DENTRO DA MATRIZ E NAO TEM NAVIO NO QUADRADO
                ####TAMBEM NAO É MENOR QUE 1 NENHUM DOS DOIS

            posicao_inicial_linha -= 1 #as listas começam do zero
            posicao_inicial_coluna -= 1 #as listas começam do zero


            matriz_partida[posicao_inicial_linha][posicao_inicial_coluna] = identificadores_navios[navio]["Identificador"]
            # verificar_posicionar_navio([posicao_inicial_linha, posicao_inicial_coluna], identificadores_navios[navio]["Tamanho"])

            desenhar_mapa()
            print(matriz_partida)
            lista_navios_para_adicionar[navio] -= 1

# def verificar_posicionar_navio(posicao_inicial, quantidade_posicoes):



def verificar_existencia_navio(posicao_inicial, quantidade_posicoes, direcao):
    existe_navio = False

    '''
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    '''
    match direcao:
        case 0:
            for pos in range(1, quantidade_posicoes):
                if not matriz_partida[posicao_inicial[0] - pos][posicao_inicial[1]] == 0:
                    existe_navio = True
                    print("EXISTE NAVIO")

        case 1:
            for pos in range(1, quantidade_posicoes):
                if not matriz_partida[posicao_inicial[0]][posicao_inicial[1] + pos] == 0:
                    existe_navio = True
                    print("EXISTE NAVIO")

        case 2:
            for pos in range(1, quantidade_posicoes):
                if not matriz_partida[posicao_inicial[0] + pos][posicao_inicial[1]] == 0:
                    existe_navio = True
                    print("EXISTE NAVIO")

        case 3:
            for pos in range(1, quantidade_posicoes):
                if not matriz_partida[posicao_inicial[0]][posicao_inicial[1] - pos] == 0:
                    existe_navio = True
                    print("EXISTE NAVIO")

    return existe_navio

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
            elif matriz_partida[linha][segunda_parede_quadrado] == 2:
                matriz_desenhada += "|  🚢   | "
            elif matriz_partida[linha][segunda_parede_quadrado] == 3:
                matriz_desenhada += "|  🚢   | "
            elif matriz_partida[linha][segunda_parede_quadrado] == 4:
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

    preparar_partida()

main()