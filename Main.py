import random

# TAMANHOS
# PEQUENO = 0 4x4
# MÉDIO = 1 5x5
# GRANDE = 2 6x6

tamanho_mapa = 1

matriz_partida_jogador1 = []
matriz_partida_jogador2 = []

if tamanho_mapa == 0:
    matriz_partida_jogador1 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    matriz_partida_jogador2 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
elif tamanho_mapa == 1:
    matriz_partida_jogador1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    matriz_partida_jogador2 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
elif tamanho_mapa == 2:
    matriz_partida_jogador1 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    matriz_partida_jogador2 = [
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
    # gerar_navios_inimigo_artificial(numero_submarinos, numero_encouracados, numero_destroiers, numero_cruzadores)

def gerar_navios_escolha(submarinos, encouracados, destroiers, cruzadores):
    """
        XX Pegar a quantidade de navios
        XX Em ordem, tornar a escolha das posições dos navios para o usuario, clara
        XX Pedir para o usuário escolher a posição inicial do navio atual
        XX Checar os lados para os quais o usuario poderá posicionar o resto do navio
        XX Pedir o lado para qual o navio será colocado
        XX Posicionar o navio na matriz do jogador
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
        desenhar_mapa_jogador()

        while lista_navios_para_adicionar[navio] > 0:
            posicao_valida = False
            while not posicao_valida:
                posicao_inicial_linha = int(input(f"Insira, por favor, a linha inicial na qual você deseja inserir um {navio} (1 a {len(matriz_partida_jogador1)}): "))
                posicao_inicial_coluna = int(input(f"Insira, por favor, a coluna inicial na qual você deseja inserir um {navio} (1 a {len(matriz_partida_jogador1[0])}): "))

                if posicao_inicial_linha < 1 or posicao_inicial_linha > len(matriz_partida_jogador1):
                    print(f"Linha inválida, por favor selecione um posição entre 1 a {len(matriz_partida_jogador1)}.")
                    continue

                if posicao_inicial_coluna < 1 or posicao_inicial_coluna > len(matriz_partida_jogador1[0]):
                    print(f"Coluna inválida, por favor selecione um posição entre 1 a {len(matriz_partida_jogador1[0])}.")
                    continue

                posicao_inicial_linha -= 1  # as listas começam do zero
                posicao_inicial_coluna -= 1  # as listas começam do zero

                if not matriz_partida_jogador1[posicao_inicial_linha][posicao_inicial_coluna] == 0:
                    print("Posição inválida, há um navio nessa posição! Tente novamente!")
                    continue

                if not navio == "Submarino":
                    if not pode_expandir([posicao_inicial_linha, posicao_inicial_coluna], navio):
                        print("O navio não tem espaço para ser posicionado. Tente novamente!")
                        continue
                    print("Pôde expandir")

                if verificar_e_posicionar_navio([posicao_inicial_linha, posicao_inicial_coluna], navio):
                    posicao_valida = True
                    break
                else:
                    continue
            #print(matriz_partida_jogador2)
            lista_navios_para_adicionar[navio] -= 1

def pode_expandir(posicao_inicial, navio):
    if navio == "Submarino": return True

    tamanho_navio = identificadores_navios[navio]["Tamanho"]

    pode_expandir_cima = True
    pode_expandir_baixo = True
    pode_expandir_esquerda = True
    pode_expandir_direita = True

    #CHECA OS CANTOS PRA VER SE NÃO ESTÁ EM ALGUMA PAREDE
    #TAMBÉM CHECA SE TEM ALGUM CAMINHO SEM NAVIOS
    if posicao_inicial[0] == 0 or verificar_existencia_navio(posicao_inicial, navio, 0): pode_expandir_cima = False
    if posicao_inicial[0] == len(matriz_partida_jogador1) - 1 or verificar_existencia_navio(posicao_inicial, navio, 2): pode_expandir_baixo = False
    if posicao_inicial[1] == 0 or verificar_existencia_navio(posicao_inicial, navio, 3): pode_expandir_esquerda = False
    if posicao_inicial[1] == len(matriz_partida_jogador1[0]) - 1 or verificar_existencia_navio(posicao_inicial, navio, 1): pode_expandir_direita = False

    #print(f"CIMA: {pode_expandir_cima}")
    #print(f"BAIXO: {pode_expandir_baixo}")
    #print(f"ESQUERDA: {pode_expandir_esquerda}")
    #print(f"DIREITA: {pode_expandir_direita}")

    if pode_expandir_cima or pode_expandir_baixo or pode_expandir_esquerda or pode_expandir_direita: return True
    else: return False

def verificar_e_posicionar_navio(posicao_inicial, navio):
    if navio == "Submarino":
        posicionar_navio(posicao_inicial, navio, 0)
        return True

    quantidade_posicoes = identificadores_navios[navio]["Tamanho"]

    if not pode_expandir(posicao_inicial, navio):
        print(f"O {navio} não pode ser colocado nessa posição, pois não há espaço em nenhuma direção. Tente novamente e escolha outro lugar!")
        return False

    pode_mover_cima = True
    pode_mover_baixo = True
    pode_mover_esquerda = True
    pode_mover_direita = True

    if (posicao_inicial[0] - (quantidade_posicoes - 1) < 0 or
            verificar_existencia_navio(posicao_inicial, navio, 0)):
        pode_mover_cima = False

    if (posicao_inicial[0] + (quantidade_posicoes - 1) > (len(matriz_partida_jogador1)) or
            verificar_existencia_navio(posicao_inicial, navio, 2)):
        pode_mover_baixo = False

    if (posicao_inicial[1] - (quantidade_posicoes - 1) < 0 or
            verificar_existencia_navio(posicao_inicial, navio, 3)):
        pode_mover_esquerda = False

    if (posicao_inicial[1] - (quantidade_posicoes - 1) > (len(matriz_partida_jogador1)) or
            verificar_existencia_navio(posicao_inicial, navio, 1)):
        pode_mover_direita = False

    escolher_direcao_pergunta = "Escolha a direção na qual você quer posicionar o seu navio:\n"
    if pode_mover_cima:
        escolher_direcao_pergunta += "1 — Cima\n"
    if pode_mover_direita:
        escolher_direcao_pergunta += "2 — Direita\n"
    if pode_mover_baixo:
        escolher_direcao_pergunta += "3 — Baixo\n"
    if pode_mover_esquerda:
        escolher_direcao_pergunta += "4 — Esquerda\n"

    direcao_valida = False
    while not direcao_valida:
        escolha_direcao = int(input(escolher_direcao_pergunta + "Direção: "))

        if escolha_direcao < 1 or escolha_direcao > 4:
            print("Direção inválida. Tente novamente!")
            continue

        if escolha_direcao == 1 and not pode_mover_cima:
            print("Não há espaço para você posicionar o navio direcionado para cima. Tente novamente!")
            continue
        if escolha_direcao == 2 and not pode_mover_direita:
            print("Não há espaço para você posicionar o navio direcionado para a direita. Tente novamente!")
            continue
        if escolha_direcao == 3 and not pode_mover_baixo:
            print("Não há espaço para você posicionar o navio direcionado para baixo. Tente novamente!")
            continue
        if escolha_direcao == 4 and not pode_mover_esquerda:
            print("Não há espaço para você posicionar o navio direcionado para a esquerda. Tente novamente!")
            continue

        direcao_valida = True

    posicionar_navio(posicao_inicial, navio, escolha_direcao - 1)
    return True

def verificar_existencia_navio(posicao_inicial, navio, direcao):
    #print(f"Parâmetros: {posicao_inicial} : {navio} : {direcao}")
    quantidade_posicoes = identificadores_navios[navio]["Tamanho"]
    '''
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    '''
    try:
        match direcao:
            case 0:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador1[posicao_inicial[0] - pos][posicao_inicial[1]] == 0:
                        #print("EXISTE NAVIO PARA CIMA")
                        return True

            case 1:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador1[posicao_inicial[0]][posicao_inicial[1] + pos] == 0:
                        #print("EXISTE NAVIO PARA DIREITA")
                        return True

            case 2:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador1[posicao_inicial[0] + pos][posicao_inicial[1]] == 0:
                        #print("EXISTE NAVIO PARA BAIXO")
                        return True

            case 3:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador1[posicao_inicial[0]][posicao_inicial[1] - pos] == 0:
                        #print("EXISTE NAVIO PARA ESQUERDA")
                        return True

        return False
    except IndexError:
        return True

def posicionar_navio(posicao_inicial, navio, direcao):
    matriz_partida_jogador1[posicao_inicial[0]][posicao_inicial[1]] = identificadores_navios[navio]["Identificador"]
    '''
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    '''
    if identificadores_navios[navio]["Tamanho"] > 1:
       match direcao:
           case 0:
               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador1[posicao_inicial[0]-pos][posicao_inicial[1]] = identificadores_navios[navio]["Identificador"]
           case 1:
               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador1[posicao_inicial[0]][posicao_inicial[1] + pos] = identificadores_navios[navio][
                       "Identificador"]
           case 2:
               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador1[posicao_inicial[0] + pos][posicao_inicial[1]] = identificadores_navios[navio][
                       "Identificador"]
           case 3:
               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador1[posicao_inicial[0]][posicao_inicial[1] - pos] = identificadores_navios[navio][
                       "Identificador"]


def gerar_navios_inimigo_artificial(submarinos, encouracados, destroiers, cruzadores):
    """
            XX Pegar a quantidade de navios
            XX Em ordem, tornar a escolha das posições dos navios para o usuario, clara
            XX Pedir para o usuário escolher a posição inicial do navio atual
            XX Checar os lados para os quais o usuario poderá posicionar o resto do navio
            XX Pedir o lado para qual o navio será colocado
            XX Posicionar o navio na matriz do jogador
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
            while True: #SAIRÁ MANUALMENTE PRA PREVENIR SPAWN EM BLOCO INVALIDO
                posicao_inicial_linha = random.randrange(0, len(matriz_partida_jogador2))
                posicao_inicial_coluna = random.randrange(0, len(matriz_partida_jogador2[0]))
                ###CHECA SE SÃO LINHAS E COLUNAS VÁLIDAS!!!
                    ###UMA LINHA E COLUNA VALIDA ESTÁ DENTRO DA MATRIZ E NAO TEM NAVIO NO QUADRADO
                    ####TAMBEM NAO É MENOR QUE 1 NENHUM DOS DOIS
                    #####CHECA TAMBÉM SE O QUADRADO ESCOLHIDO TEM LUGAR PRA EXPANDIR, OU SEJA
                        ###TEM ALGUMA DIREÇÃO A SEGUIR CASO O NAVIO TENHA MAIS DE 1 ESPAÇO

                if not matriz_partida_jogador2[posicao_inicial_linha][posicao_inicial_coluna] == 0:
                    continue
                else:
                    break

            navio_criado_com_sucesso = False

            while not navio_criado_com_sucesso:
                navio_criado_com_sucesso = verificar_e_posicionar_navio_inimigo([posicao_inicial_linha, posicao_inicial_coluna], navio, identificadores_navios[navio]["Tamanho"])

            desenhar_mapa_jogador()
            print(matriz_partida_jogador2)
            lista_navios_para_adicionar[navio] -= 1

def verificar_e_posicionar_navio_inimigo(posicao_inicial, navio, quantidade_posicoes):
    if navio == "Submarino":
        posicionar_navio_inimigo(posicao_inicial, navio, 0)
        return True

    pode_mover_cima = True
    pode_mover_baixo = True
    pode_mover_esquerda = True
    pode_mover_direita = True

    possibilidades_direcao_navio = [0, 1, 2, 3]

    if (posicao_inicial[0] - (quantidade_posicoes - 1) < 0 or
            verificar_existencia_navio_inimigo(posicao_inicial, quantidade_posicoes, 0)):
        pode_mover_cima = False
        possibilidades_direcao_navio.remove(0)

    if (posicao_inicial[0] + (quantidade_posicoes - 1) > (len(matriz_partida_jogador2)) or
            verificar_existencia_navio_inimigo(posicao_inicial, quantidade_posicoes, 2)):
        pode_mover_baixo = False
        possibilidades_direcao_navio.remove(2)

    if (posicao_inicial[1] - (quantidade_posicoes - 1) < 0 or
            verificar_existencia_navio_inimigo(posicao_inicial, quantidade_posicoes, 3)):
        pode_mover_esquerda = False
        possibilidades_direcao_navio.remove(3)

    if (posicao_inicial[1] - (quantidade_posicoes - 1) > (len(matriz_partida_jogador2)) or
            verificar_existencia_navio_inimigo(posicao_inicial, quantidade_posicoes, 1)):
        pode_mover_direita = False
        possibilidades_direcao_navio.remove(1)

    if len(possibilidades_direcao_navio) == 0:
        return False
    else:
        escolha_direcao_pergunta = random.choice(possibilidades_direcao_navio)

    posicionar_navio_inimigo(posicao_inicial, navio, escolha_direcao_pergunta)
    return True

def verificar_existencia_navio_inimigo(posicao_inicial, quantidade_posicoes, direcao):
    '''
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    '''
    try:
        match direcao:
            case 0:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador2[posicao_inicial[0] - pos][posicao_inicial[1]] == 0:
                        print("EXISTE NAVIO")
                        return True

            case 1:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1] + pos] == 0:
                        print("EXISTE NAVIO")
                        return True

            case 2:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador2[posicao_inicial[0] + pos][posicao_inicial[1]] == 0:
                        print("EXISTE NAVIO")
                        return True

            case 3:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1] - pos] == 0:
                        print("EXISTE NAVIO")
                        return True

        return False
    except IndexError:
        return True

def posicionar_navio_inimigo(posicao_inicial, navio, direcao):
    matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1]] = identificadores_navios[navio]["Identificador"]
    '''
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    '''
    if identificadores_navios[navio]["Tamanho"] > 1:
       match direcao:
           case 0:
               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador2[posicao_inicial[0]-pos][posicao_inicial[1]] = identificadores_navios[navio]["Identificador"]
           case 1:
               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1] + pos] = identificadores_navios[navio][
                       "Identificador"]
           case 2:
               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador2[posicao_inicial[0] + pos][posicao_inicial[1]] = identificadores_navios[navio][
                       "Identificador"]
           case 3:
               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1] - pos] = identificadores_navios[navio][
                       "Identificador"]
       #print(f"Posicionado um {navio} em {posicao_inicial} na direção {direcao}")


def desenhar_mapa_jogador():
    matriz_desenhada = ""
    numero_colunas = len(matriz_partida_jogador1[0])
    numero_linhas = len(matriz_partida_jogador1)
    for linha in range(numero_linhas):
        for quadrado_coluna in range(numero_colunas):
            matriz_desenhada += "|￣￣￣￣| "
        matriz_desenhada += "\n"

        for segunda_parede_quadrado in range(numero_colunas):
            if segunda_parede_quadrado >= numero_colunas / 2:
                matriz_desenhada += " "
            #print(f"VALOR MATRIZ: {matriz_partida[linha][segunda_parede_quadrado]}")
            if matriz_partida_jogador1[linha][segunda_parede_quadrado] == 1:
                matriz_desenhada += "|  🚢   | "
            elif matriz_partida_jogador1[linha][segunda_parede_quadrado] == 2:
                matriz_desenhada += "|  🚢   | "
            elif matriz_partida_jogador1[linha][segunda_parede_quadrado] == 3:
                matriz_desenhada += "|  🚢   | "
            elif matriz_partida_jogador1[linha][segunda_parede_quadrado] == 4:
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