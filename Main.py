import random, time

# SIGNIFICADO IDENTIFICADORES
    #0 — Água — 🌊
    #1 — Submarino — 🚢
    #2 — Destróier — 🚢
    #3 — Cruzador — 🚢
    #4 — Encouraçado — 🚢
    #5 — Ataque bem-sucedido — 💥
    #6 — Ataque mal-sucedido — ❌

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

matriz_partida_jogador1 = []
matriz_partida_jogador2 = []

matriz_alvo_jogador1 = []

posicoes_navios_jogador1 = {}
posicoes_navios_jogador2 = {}

lista_prioridades_inteligencia_artificial = []
lista_ignorar_inteligencia_artificial = []

# TAMANHOS
    # PEQUENO = 0 4x4
    # MÉDIO = 1 5x5
    # GRANDE = 2 6x6

## FAÇAM AQUI A TAREFA DE PERGUNTAR O TAMANHO DO MAPA
        # usem o time.sleep() e insiram quantos segundos (dentro dos parenteses) querem que o código espere antes de prosseguir
        # façam isso pra dar um tempinho pro usuário digerir as informações do terminal
tamanho_mapa = 1

if tamanho_mapa == 0:
    numero_submarinos = 1
    numero_destroiers = 1
    numero_encouracados = 0
    numero_cruzadores = 0

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
    matriz_alvo_jogador1 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
elif tamanho_mapa == 1:
    numero_submarinos = 1
    numero_destroiers = 1
    numero_encouracados = 1
    numero_cruzadores = 1

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
    matriz_alvo_jogador1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
elif tamanho_mapa == 2:
    numero_submarinos = 1
    numero_destroiers = 2
    numero_encouracados = 2
    numero_cruzadores = 1

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
    matriz_alvo_jogador1 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

#def preparar_mapas()

def preparar_partida():
    time.sleep(1)
    gerar_navios_inimigo_artificial(numero_submarinos, numero_encouracados, numero_destroiers, numero_cruzadores)
    print("O adversário posicionou seus navios.\n")
    time.sleep(1)
    #print(f"POSIÇÕES DOS NAVIOS JOGADOR 2: {posicoes_navios_jogador2}")

    print("Nossa vez de posicionar navios...")
    time.sleep(1)
    gerar_navios_escolha(numero_submarinos, numero_encouracados, numero_destroiers, numero_cruzadores)
    #print(f"POSIÇÕES DOS NAVIOS JOGADOR 1: {posicoes_navios_jogador1}")

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

    print("O mapa da batalha será assim:")
    time.sleep(0.5)
    desenhar_mapa_jogador(matriz_partida_jogador1)
    for navio in lista_navios_para_adicionar:
        while lista_navios_para_adicionar[navio] > 0:
            posicao_valida = False
            while not posicao_valida:
                try:
                    time.sleep(0.5)
                    posicao_inicial_linha = int(input(f"Insira, por favor, a linha inicial na qual você deseja inserir um {navio} (1 a {len(matriz_partida_jogador1)}): "))
                    posicao_inicial_coluna = int(input(f"Insira, por favor, a coluna inicial na qual você deseja inserir um {navio} (1 a {len(matriz_partida_jogador1[0])}): "))
                except:
                    print("Valor inválido, por favor insira um número")

                if posicao_inicial_linha < 1 or posicao_inicial_linha > len(matriz_partida_jogador1):
                    time.sleep(1)
                    print(f"Linha inválida, por favor selecione um posição entre 1 a {len(matriz_partida_jogador1)}.")
                    continue

                if posicao_inicial_coluna < 1 or posicao_inicial_coluna > len(matriz_partida_jogador1[0]):
                    time.sleep(1)
                    print(f"Coluna inválida, por favor selecione um posição entre 1 a {len(matriz_partida_jogador1[0])}.")
                    continue

                posicao_inicial_linha -= 1  # as listas começam do zero
                posicao_inicial_coluna -= 1  # as listas começam do zero

                if not matriz_partida_jogador1[posicao_inicial_linha][posicao_inicial_coluna] == 0:
                    time.sleep(1)
                    print("Posição inválida, há um navio nessa posição! Tente novamente!")
                    continue

                if not navio == "Submarino":
                    if not pode_expandir([posicao_inicial_linha, posicao_inicial_coluna], navio):
                        time.sleep(1)
                        print("O navio não tem espaço para ser posicionado. Tente novamente!")
                        continue
                    #print("Pôde expandir")

                if verificar_e_posicionar_navio([posicao_inicial_linha, posicao_inicial_coluna], navio):
                    posicao_valida = True
                    break
                else:
                    continue
            lista_navios_para_adicionar[navio] -= 1
            time.sleep(0.75)
            print("Navio posicionado com sucesso.")
            time.sleep(0.5)
            desenhar_mapa_jogador(matriz_partida_jogador1)

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
    if navio == "Submarino" and matriz_partida_jogador1[posicao_inicial[0]][posicao_inicial[1]] == 0:
        posicoes_navios_jogador1[f"Navio_{len(posicoes_navios_jogador1) + 1}"] = {
            "Tipo_Navio": navio,
            "Posicoes": [posicao_inicial]
        }
        posicionar_navio(posicao_inicial, navio, 0)
        return True

    elif navio == "Submarino":
        time.sleep(1)
        print("Há um navio nessa posição, impossível posicionar um submarino aqui.")
        return False

    quantidade_posicoes = identificadores_navios[navio]["Tamanho"]

    if not pode_expandir(posicao_inicial, navio):
        time.sleep(2)
        print(f"O {navio} não pode ser colocado nessa posição, pois não há espaço suficiente em nenhuma direção. Tente novamente e escolha outro lugar!")
        return False

    pode_mover_cima = True
    pode_mover_baixo = True
    pode_mover_esquerda = True
    pode_mover_direita = True

    if (posicao_inicial[0] - (quantidade_posicoes - 1) < 0 or
            verificar_existencia_navio(posicao_inicial, navio, 0)):
        pode_mover_cima = False

    if (posicao_inicial[0] + (quantidade_posicoes - 1) >= (len(matriz_partida_jogador1)) or
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
        time.sleep(0.75)
        escolha_direcao = int(input(escolher_direcao_pergunta + "Direção: "))

        if escolha_direcao < 1 or escolha_direcao > 4:
            time.sleep(1)
            print("Direção inválida. Tente novamente!")
            continue

        if escolha_direcao == 1 and not pode_mover_cima:
            time.sleep(1)
            print("Não há espaço para você posicionar o navio direcionado para cima. Tente novamente!")
            continue
        if escolha_direcao == 2 and not pode_mover_direita:
            time.sleep(1)
            print("Não há espaço para você posicionar o navio direcionado para a direita. Tente novamente!")
            continue
        if escolha_direcao == 3 and not pode_mover_baixo:
            time.sleep(1)
            print("Não há espaço para você posicionar o navio direcionado para baixo. Tente novamente!")
            continue
        if escolha_direcao == 4 and not pode_mover_esquerda:
            time.sleep(1)
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
               lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador1[posicao_inicial[0]-pos][posicao_inicial[1]] = identificadores_navios[navio]["Identificador"]
                   lista_posicoes_navio.append([posicao_inicial[0]-pos, posicao_inicial[1]])

               posicoes_navios_jogador1[f"Navio_{len(posicoes_navios_jogador1) + 1}"] = {
                   "Tipo_Navio": navio,
                   "Posicoes": lista_posicoes_navio
               }
           case 1:
               lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador1[posicao_inicial[0]][posicao_inicial[1] + pos] = identificadores_navios[navio][
                       "Identificador"]
                   lista_posicoes_navio.append([posicao_inicial[0], posicao_inicial[1] + pos])

               posicoes_navios_jogador1[f"Navio_{len(posicoes_navios_jogador1) + 1}"] = {
                   "Tipo_Navio": navio,
                   "Posicoes": lista_posicoes_navio
               }
           case 2:
               lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]
               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador1[posicao_inicial[0] + pos][posicao_inicial[1]] = identificadores_navios[navio][
                       "Identificador"]
                   lista_posicoes_navio.append([posicao_inicial[0] + pos, posicao_inicial[1]])

               posicoes_navios_jogador1[f"Navio_{len(posicoes_navios_jogador1) + 1}"] = {
                   "Tipo_Navio": navio,
                   "Posicoes": lista_posicoes_navio
               }
           case 3:
               lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador1[posicao_inicial[0]][posicao_inicial[1] - pos] = identificadores_navios[navio][
                       "Identificador"]
                   lista_posicoes_navio.append([posicao_inicial[0], posicao_inicial[1] - pos])

               posicoes_navios_jogador1[f"Navio_{len(posicoes_navios_jogador1) + 1}"] = {
                   "Tipo_Navio": navio,
                   "Posicoes": lista_posicoes_navio
               }


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
            tentativa_atual = 0

            while not navio_criado_com_sucesso and tentativa_atual < 50:
                navio_criado_com_sucesso = verificar_e_posicionar_navio_inimigo([posicao_inicial_linha, posicao_inicial_coluna], navio, identificadores_navios[navio]["Tamanho"])
                tentativa_atual += 1

            if not navio_criado_com_sucesso:
                #print("NAO CONSEGUI ENCAIXAR O NAVIO, TENTANDO NOVAMENTE")
                continue

            lista_navios_para_adicionar[navio] -= 1

def verificar_e_posicionar_navio_inimigo(posicao_inicial, navio, quantidade_posicoes):
    if navio == "Submarino" and matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1]] == 0:
        posicoes_navios_jogador2[f"Navio_{len(posicoes_navios_jogador2) + 1}"] = {
            "Tipo_Navio": navio,
            "Posicoes": [posicao_inicial]
        }
        posicionar_navio_inimigo(posicao_inicial, navio, 0)
        return True

    elif navio == "Submarino":
        return False

    pode_mover_cima = True
    pode_mover_baixo = True
    pode_mover_esquerda = True
    pode_mover_direita = True

    possibilidades_direcao_navio = [0, 1, 2, 3]

    if (posicao_inicial[0] - (quantidade_posicoes - 1) < 0 or
            verificar_existencia_navio_inimigo(posicao_inicial, quantidade_posicoes, 0)):
        pode_mover_cima = False
        possibilidades_direcao_navio.remove(0)

    if (posicao_inicial[0] + (quantidade_posicoes - 1) >= len(matriz_partida_jogador2) or
            verificar_existencia_navio_inimigo(posicao_inicial, quantidade_posicoes, 2)):
        pode_mover_baixo = False
        possibilidades_direcao_navio.remove(2)

    if (posicao_inicial[1] - (quantidade_posicoes - 1) < 0 or
            verificar_existencia_navio_inimigo(posicao_inicial, quantidade_posicoes, 3)):
        pode_mover_esquerda = False
        possibilidades_direcao_navio.remove(3)

    if (posicao_inicial[1] + (quantidade_posicoes - 1) >= len(matriz_partida_jogador2) or
            verificar_existencia_navio_inimigo(posicao_inicial, quantidade_posicoes, 1)):
        pode_mover_direita = False
        possibilidades_direcao_navio.remove(1)

    if len(possibilidades_direcao_navio) == 0:
        return False

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
                        #print("EXISTE NAVIO")
                        return True

            case 1:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1] + pos] == 0:
                        #print("EXISTE NAVIO")
                        return True

            case 2:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador2[posicao_inicial[0] + pos][posicao_inicial[1]] == 0:
                        #print("EXISTE NAVIO")
                        return True

            case 3:
                for pos in range(1, quantidade_posicoes):
                    if not matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1] - pos] == 0:
                        #print("EXISTE NAVIO")
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
               lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador2[posicao_inicial[0]-pos][posicao_inicial[1]] = identificadores_navios[navio]["Identificador"]
                   lista_posicoes_navio.append([posicao_inicial[0] - pos, posicao_inicial[1]])

               posicoes_navios_jogador2[f"Navio_{len(posicoes_navios_jogador2) + 1}"] = {
                   "Tipo_Navio": navio,
                   "Posicoes": lista_posicoes_navio
               }

           case 1:
               lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1] + pos] = identificadores_navios[navio][
                       "Identificador"]
                   lista_posicoes_navio.append([posicao_inicial[0], posicao_inicial[1] + pos])

               posicoes_navios_jogador2[f"Navio_{len(posicoes_navios_jogador2) + 1}"] = {
                   "Tipo_Navio": navio,
                   "Posicoes": lista_posicoes_navio
               }
           case 2:
               lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador2[posicao_inicial[0] + pos][posicao_inicial[1]] = identificadores_navios[navio][
                       "Identificador"]
                   lista_posicoes_navio.append([posicao_inicial[0] + pos, posicao_inicial[1]])

               posicoes_navios_jogador2[f"Navio_{len(posicoes_navios_jogador2) + 1}"] = {
                   "Tipo_Navio": navio,
                   "Posicoes": lista_posicoes_navio
               }
           case 3:
               lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

               for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                   matriz_partida_jogador2[posicao_inicial[0]][posicao_inicial[1] - pos] = identificadores_navios[navio][
                       "Identificador"]
                   lista_posicoes_navio.append([posicao_inicial[0], posicao_inicial[1] - pos])

               posicoes_navios_jogador2[f"Navio_{len(posicoes_navios_jogador2) + 1}"] = {
                   "Tipo_Navio": navio,
                   "Posicoes": lista_posicoes_navio
               }

       #print(f"Posicionado um {navio} em {posicao_inicial} na direção {direcao}")


def desenhar_minimapa(matriz):
    matriz_desenhada = ""
    numero_colunas = len(matriz[0])
    numero_linhas = len(matriz)
    for linha in range(numero_linhas):
        for coluna_quadrado in range(numero_colunas):
            # print(f"VALOR MATRIZ: {matriz[linha][coluna_quadrado]}")
            if matriz[linha][coluna_quadrado] == 0:
                matriz_desenhada += "[🌊]"
            elif matriz[linha][coluna_quadrado] == 1:
                matriz_desenhada += "[🚢]"
            elif matriz[linha][coluna_quadrado] == 2:
                matriz_desenhada += "[🚢]"
            elif matriz[linha][coluna_quadrado] == 3:
                matriz_desenhada += "[🚢]"
            elif matriz[linha][coluna_quadrado] == 4:
                matriz_desenhada += "[🚢]"
            elif matriz[linha][coluna_quadrado] == 5:
                matriz_desenhada += "[💥]"
            elif matriz[linha][coluna_quadrado] == 6:
                matriz_desenhada += "[❌]"
            else:
                matriz_desenhada += "[]"
        matriz_desenhada += "\n"

    print(matriz_desenhada)

def desenhar_mapa_jogador(matriz):
    matriz_desenhada = ""
    numero_colunas = len(matriz[0])
    numero_linhas = len(matriz)
    for linha in range(numero_linhas):
        for quadrado_coluna in range(numero_colunas):
            matriz_desenhada += " |￣￣￣￣| "
        matriz_desenhada += "\n"

        for segunda_parede_quadrado in range(numero_colunas):
            if segunda_parede_quadrado >= numero_colunas / 2:
                matriz_desenhada += " "
            #print(f"VALOR MATRIZ: {matriz[linha][segunda_parede_quadrado]}")
            if matriz[linha][segunda_parede_quadrado] == 0:
                matriz_desenhada += " |  🌊   | "
            elif matriz[linha][segunda_parede_quadrado] == 1:
                matriz_desenhada += " |  🚢   | "
            elif matriz[linha][segunda_parede_quadrado] == 2:
                matriz_desenhada += " |  🚢   | "
            elif matriz[linha][segunda_parede_quadrado] == 3:
                matriz_desenhada += " |  🚢   | "
            elif matriz[linha][segunda_parede_quadrado] == 4:
                matriz_desenhada += " |  🚢   | "
            elif matriz[linha][segunda_parede_quadrado] == 5:
                matriz_desenhada += " |  💥   | "
            elif matriz[linha][segunda_parede_quadrado] == 6:
                matriz_desenhada += " |  ❌   | "
            else:
                matriz_desenhada += " |       | "
        matriz_desenhada += "\n"

        for terceira_parede_quadrado in range(numero_colunas):
            if terceira_parede_quadrado >= numero_colunas / 2:
                matriz_desenhada += " "
            matriz_desenhada += " |       | "
        matriz_desenhada += "\n"
    for quadrado_coluna in range(numero_colunas):
        matriz_desenhada += "  ￣￣￣￣  "

    print(matriz_desenhada)

def partida_principal():
    while True:
        try:
            time.sleep(1)
            jogador_inicial = int(
                input("Quem irá começar?\n 1 — Jogador;\n 2 — Adversário;\n 3 — Aleatório.\nDecisão: "))
            if 1 <= jogador_inicial <= 3:
                break  # valor válido, sai do loop
            else:
                time.sleep(1)
                print("Opção inválida. Escolha entre 1 e 3.")
        except ValueError:
            time.sleep(1)
            print("Entrada inválida. Digite apenas números inteiros.")

    if jogador_inicial == 3:
        jogador_atual = random.randrange(1, 3)
        time.sleep(1)
        print(f"Seleção aleatória: {jogador_atual}")
    else:
        jogador_atual = jogador_inicial

    time.sleep(1)
    print("\n\nQuem iniciará a partida:")
    time.sleep(0.75)
    if jogador_atual == 1:
        print("Jogador")
    else:
        print("Adversário")

    partida_em_progresso = True

    time.sleep(0.85)
    print("\nBatalha iniciada. Boa Sorte!\n\n")
    time.sleep(1.1)

    while partida_em_progresso:
        match jogador_atual:
            case 1:
                time.sleep(1)
                print("Esse é o mapa de inteligência, ele indicará os seus erros e acertos durante o seu ataque.")
                time.sleep(0.5)
                desenhar_mapa_jogador(matriz_alvo_jogador1)

                posicao_valida = False
                while not posicao_valida:
                    time.sleep(0.75)
                    posicao_ataque_linha = input(f"Insira, por favor, a linha na qual você deseja fazer seu ataque (1 a {len(matriz_alvo_jogador1)}): ")
                    if not posicao_ataque_linha.isdigit():
                        print("Insira apenas números, por favor.")
                        continue

                    posicao_ataque_linha = int(posicao_ataque_linha)

                    posicao_ataque_coluna = input(f"Insira, por favor, a coluna na qual você deseja fazer seu ataque (1 a {len(matriz_alvo_jogador1[0])}): ")
                    if not posicao_ataque_coluna.isdigit():
                        print("Insira apenas números, por favor.")
                        continue

                    posicao_ataque_coluna = int(posicao_ataque_coluna)

                    if posicao_ataque_linha < 1 or posicao_ataque_linha > len(
                            matriz_partida_jogador1):
                        time.sleep(1)
                        print(f"Linha inválida, por favor selecione um posição entre 1 e {len(matriz_alvo_jogador1)}.")
                        continue

                    if posicao_ataque_coluna < 1 or posicao_ataque_coluna > len(
                            matriz_alvo_jogador1[0]):
                        time.sleep(1)
                        print(f"Coluna inválida, por favor selecione um posição entre 1 e {len(matriz_alvo_jogador1[0])}.")
                        continue

                    posicao_ataque_linha -= 1  # as listas começam do zero
                    posicao_ataque_coluna -= 1  # as listas começam do zero

                    posicao_valida = True

                time.sleep(0.75)
                if (matriz_alvo_jogador1[posicao_ataque_linha][posicao_ataque_coluna] == 5 or
                      matriz_alvo_jogador1[posicao_ataque_linha][posicao_ataque_coluna] == 6):

                    print("NOSSA INTELIGÊNCIA INDICA QUE JÁ ATACAMOS ESSAS COORDENADAS!")

                elif (not matriz_partida_jogador2[posicao_ataque_linha][
                            posicao_ataque_coluna] == 0 and
                        not matriz_partida_jogador2[posicao_ataque_linha][
                                posicao_ataque_coluna] == 5 and
                        not matriz_partida_jogador2[posicao_ataque_linha][
                                posicao_ataque_coluna] == 6):

                    print("NOSSA INTELIGÊNCIA DIZ QUE NOSSO ATAQUE FOI UM SUCESSO!")
                    matriz_alvo_jogador1[posicao_ataque_linha][posicao_ataque_coluna] = 5
                    for nav in posicoes_navios_jogador2:
                        for posicao in posicoes_navios_jogador2[nav]["Posicoes"]:
                            if posicao[0] == posicao_ataque_linha and posicao[1] == posicao_ataque_coluna:
                                posicoes_navios_jogador2[nav]["Posicoes"].remove([posicao_ataque_linha, posicao_ataque_coluna])

                else:
                    print("NOSSA INTELIGÊNCIA DIZ QUE NOSSO ATAQUE FOI UM FRACASSO!")
                    matriz_alvo_jogador1[posicao_ataque_linha][posicao_ataque_coluna] = 6

            case 2:
                print("\nO inimigo irá atacar.\n")
                time.sleep(0.75)
                if len(lista_prioridades_inteligencia_artificial) == 0:
                    posicao_valida = False

                    posicao_ataque_linha_jogador_humano = (
                        random.randrange(0, len(matriz_partida_jogador1)))
                    posicao_ataque_coluna_jogador_humano = (
                        random.randrange(0, len(matriz_partida_jogador1[0])))

                    while not posicao_valida:
                        posicao_ataque_linha_jogador_humano = (
                            random.randrange(0, len(matriz_partida_jogador1)))

                        posicao_ataque_coluna_jogador_humano = (
                            random.randrange(0, len(matriz_partida_jogador1[0])))

                        if (posicao_ataque_linha_jogador_humano < 0 or
                                posicao_ataque_linha_jogador_humano > len(matriz_partida_jogador1)):
                            continue

                        if (posicao_ataque_coluna_jogador_humano < 0 or
                                posicao_ataque_coluna_jogador_humano > len(matriz_alvo_jogador1[0])):
                            continue

                        if [posicao_ataque_linha_jogador_humano, posicao_ataque_coluna_jogador_humano] in lista_ignorar_inteligencia_artificial:
                            continue

                        posicao_valida = True

                    ataque_valido = False
                    while not ataque_valido:
                        if (not matriz_partida_jogador1[posicao_ataque_linha_jogador_humano][
                                    posicao_ataque_coluna_jogador_humano] == 0 and
                                not matriz_partida_jogador1[posicao_ataque_linha_jogador_humano][
                                        posicao_ataque_coluna_jogador_humano] == 5 and
                                not matriz_partida_jogador1[posicao_ataque_linha_jogador_humano][
                                        posicao_ataque_coluna_jogador_humano] == 6):
                            time.sleep(0.65)
                            print("O INIMIGO ACERTOU EM CHEIO!")
                            # print(f"inimigo atirou em: [{posicao_ataque_linha_jogador_humano}, {posicao_ataque_coluna_jogador_humano}]")
                            matriz_partida_jogador1[posicao_ataque_linha_jogador_humano][
                                posicao_ataque_coluna_jogador_humano] = 5

                            for nav in posicoes_navios_jogador1:
                                for posicao in posicoes_navios_jogador1[nav]["Posicoes"]:
                                    if posicao[0] == posicao_ataque_linha_jogador_humano and posicao[1] == posicao_ataque_coluna_jogador_humano:
                                        posicoes_navios_jogador1[nav]["Posicoes"].remove(
                                            [posicao_ataque_linha_jogador_humano, posicao_ataque_coluna_jogador_humano])

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ACIMA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [posicao_ataque_linha_jogador_humano - 1,
                                         posicao_ataque_coluna_jogador_humano])

                            if posicao_ataque_linha_jogador_humano < len(
                                    matriz_partida_jogador1) - 2:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ABAIXO
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [posicao_ataque_linha_jogador_humano + 1,
                                         posicao_ataque_coluna_jogador_humano])

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ESQUERDA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [posicao_ataque_linha_jogador_humano,
                                         posicao_ataque_coluna_jogador_humano - 1])

                            if posicao_ataque_linha_jogador_humano > len(
                                    matriz_partida_jogador1[0]) - 2:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - DIREITA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [posicao_ataque_linha_jogador_humano,
                                         posicao_ataque_coluna_jogador_humano + 1])

                        else:
                            time.sleep(0.65)
                            print("O ATAQUE DO INIMIGO FOI EM VÃO! APROVEITEMOS ESSA OPORTUNIDADE!")
                            lista_ignorar_inteligencia_artificial.append([posicao_ataque_linha_jogador_humano, posicao_ataque_coluna_jogador_humano])

                        ataque_valido = True
                else:
                    if not lista_prioridades_inteligencia_artificial:
                        continue

                    posicao_valida = False
                    tentativa = 0
                    prioridade_atacar = random.choice(lista_prioridades_inteligencia_artificial)

                    while not posicao_valida and tentativa <= 50:
                        prioridade_atacar = random.choice(lista_prioridades_inteligencia_artificial)
                        posicao_ataque_linha_jogador_humano = prioridade_atacar[0]
                        posicao_ataque_coluna_jogador_humano = prioridade_atacar[1]

                        if posicao_ataque_linha_jogador_humano < 0 or posicao_ataque_linha_jogador_humano >= len(
                                matriz_partida_jogador1):
                            tentativa += 1
                            continue

                        if posicao_ataque_coluna_jogador_humano < 0 or posicao_ataque_coluna_jogador_humano >= len(
                                matriz_alvo_jogador1[0]):
                            tentativa += 1
                            continue

                        posicao_valida = True

                    if not posicao_valida:
                        lista_prioridades_inteligencia_artificial.remove(prioridade_atacar)
                        continue

                    ataque_valido = False
                    while not ataque_valido:
                        if (not matriz_partida_jogador1[posicao_ataque_linha_jogador_humano][
                                    posicao_ataque_coluna_jogador_humano] == 0 and
                                not matriz_partida_jogador1[posicao_ataque_linha_jogador_humano][
                                        posicao_ataque_coluna_jogador_humano] == 5 and
                                not matriz_partida_jogador1[posicao_ataque_linha_jogador_humano][
                                        posicao_ataque_coluna_jogador_humano] == 6):
                            time.sleep(0.65)
                            print("O INIMIGO ACERTOU EM CHEIO!")
                            # print(f"inimigo atirou em: [{posicao_ataque_linha_jogador_humano}, {posicao_ataque_coluna_jogador_humano}]")
                            matriz_partida_jogador1[posicao_ataque_linha_jogador_humano][
                                posicao_ataque_coluna_jogador_humano] = 5

                            for nav in posicoes_navios_jogador1:
                                for posicao in posicoes_navios_jogador1[nav]["Posicoes"]:
                                    if posicao[0] == posicao_ataque_linha_jogador_humano and posicao[1] == posicao_ataque_coluna_jogador_humano:
                                        posicoes_navios_jogador1[nav]["Posicoes"].remove(
                                            [posicao_ataque_linha_jogador_humano, posicao_ataque_coluna_jogador_humano])

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ACIMA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [posicao_ataque_linha_jogador_humano - 1,
                                         posicao_ataque_coluna_jogador_humano])

                            if posicao_ataque_linha_jogador_humano < len(
                                    matriz_partida_jogador1) - 2:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ABAIXO
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [posicao_ataque_linha_jogador_humano + 1,
                                         posicao_ataque_coluna_jogador_humano])

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ESQUERDA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [posicao_ataque_linha_jogador_humano,
                                         posicao_ataque_coluna_jogador_humano - 1])

                            if posicao_ataque_linha_jogador_humano > len(
                                    matriz_partida_jogador1[0]) - 2:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - DIREITA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [posicao_ataque_linha_jogador_humano,
                                         posicao_ataque_coluna_jogador_humano + 1])

                        else:
                            time.sleep(0.65)
                            print("O ATAQUE DO INIMIGO FOI EM VÃO! APROVEITEMOS ESSA OPORTUNIDADE!")

                        if [posicao_ataque_linha_jogador_humano, posicao_ataque_coluna_jogador_humano] in lista_prioridades_inteligencia_artificial:
                            lista_prioridades_inteligencia_artificial.remove(
                                [posicao_ataque_linha_jogador_humano,
                                 posicao_ataque_coluna_jogador_humano])
                        ataque_valido = True

        if jogador_atual == 1:
            navio_existente = False

            for navio in posicoes_navios_jogador2:
                if len(posicoes_navios_jogador2[navio]["Posicoes"]) > 0:
                    navio_existente = True

            if not navio_existente:
                #print("nao tem navio no jogador 2")
                return 1

        elif jogador_atual == 2:
            navio_existente = False

            for navio in posicoes_navios_jogador1:
                if len(posicoes_navios_jogador1[navio]["Posicoes"]) > 0:
                    navio_existente = True

            if not navio_existente:
                #print("nao tem navio no jogador 1")
                return 2

        time.sleep(1)
        print("\nAqui está um mini-mapa indicando os danos que sofremos:")
        time.sleep(0.5)
        desenhar_minimapa(matriz_partida_jogador1)
        time.sleep(1)

        if jogador_atual == 1: jogador_atual = 2
        elif jogador_atual == 2: jogador_atual = 1
    return None


def main():
    jogo_loopando = True

    while jogo_loopando:
        preparar_partida()

        vencedor = partida_principal()

        time.sleep(1)
        print("\nFIM DA PARTIDA!!!\n")

        time.sleep(1.5)
        print("Aqui está um mini-mapa dos ataques feitos por nós, no inimigo.\n")
        time.sleep(0.5)
        desenhar_minimapa(matriz_alvo_jogador1)

        submarinos_inimigos_afundados = 0
        destroiers_inimigos_afundados = 0
        cruzadores_inimigos_afundados = 0
        encouracados_inimigos_afundados = 0

        submarinos_aliados_afundados = 0
        destroiers_aliados_afundados = 0
        cruzadores_aliados_afundados = 0
        encouracados_aliados_afundados = 0

        for navio in posicoes_navios_jogador2:
            if posicoes_navios_jogador2[navio]["Tipo_Navio"] == "Submarino" and len(
                    posicoes_navios_jogador2[navio]["Posicoes"]) == 0:
                submarinos_inimigos_afundados += 1

            if posicoes_navios_jogador2[navio]["Tipo_Navio"] == "Destróier" and len(
                    posicoes_navios_jogador2[navio]["Posicoes"]) == 0:
                destroiers_inimigos_afundados += 1

            if posicoes_navios_jogador2[navio]["Tipo_Navio"] == "Cruzador" and len(
                    posicoes_navios_jogador2[navio]["Posicoes"]) == 0:
                cruzadores_inimigos_afundados += 1

            if posicoes_navios_jogador2[navio]["Tipo_Navio"] == "Encouraçado" and len(
                    posicoes_navios_jogador2[navio]["Posicoes"]) == 0:
                encouracados_inimigos_afundados += 1

        for navio in posicoes_navios_jogador1:
            if posicoes_navios_jogador1[navio]["Tipo_Navio"] == "Submarino" and len(
                    posicoes_navios_jogador1[navio]["Posicoes"]) == 0:
                submarinos_aliados_afundados += 1

            if posicoes_navios_jogador1[navio]["Tipo_Navio"] == "Destróier" and len(
                    posicoes_navios_jogador1[navio]["Posicoes"]) == 0:
                destroiers_aliados_afundados += 1

            if posicoes_navios_jogador1[navio]["Tipo_Navio"] == "Cruzador" and len(
                    posicoes_navios_jogador1[navio]["Posicoes"]) == 0:
                cruzadores_aliados_afundados += 1

            if posicoes_navios_jogador1[navio]["Tipo_Navio"] == "Encouraçado" and len(
                    posicoes_navios_jogador1[navio]["Posicoes"]) == 0:
                encouracados_aliados_afundados += 1

        time.sleep(1)
        print("\nO vencedor é...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)

        if vencedor == 1:
            print("JOGADOR 1 VENCEU!\n")
            time.sleep(1)

            print(f"Navios Inimigos, afundados por nós:"
                  f"\nSubmarinos: {submarinos_inimigos_afundados};"
                  f"\nDestroiers: {destroiers_inimigos_afundados};"
                  f"\nCruzadores: {cruzadores_inimigos_afundados};"
                  f"\nEncouraçados: {encouracados_inimigos_afundados}.\n")

            time.sleep(1)

            print(f"Nossos navios, afundados pelo Inimigo:"
                  f"\nSubmarinos: {submarinos_aliados_afundados};"
                  f"\nDestroiers: {destroiers_aliados_afundados};"
                  f"\nCruzadores: {cruzadores_aliados_afundados};"
                  f"\nEncouraçados: {encouracados_aliados_afundados}.")

        elif vencedor == 2:
            print("ADVERSÁRIO VENCEU!\n")
            time.sleep(1)

            print(f"Nossos navios, afundados pelo Inimigo:"
                  f"\nSubmarinos: {submarinos_aliados_afundados};"
                  f"\nDestroiers: {destroiers_aliados_afundados};"
                  f"\nCruzadores: {cruzadores_aliados_afundados};"
                  f"\nEncouraçados: {encouracados_aliados_afundados}.")

            time.sleep(1)

            print(f"Navios Inimigos, afundados por nós:"
                  f"\nSubmarinos: {submarinos_inimigos_afundados};"
                  f"\nDestroiers: {destroiers_inimigos_afundados};"
                  f"\nCruzadores: {cruzadores_inimigos_afundados};"
                  f"\nEncouraçados: {encouracados_inimigos_afundados}.\n")

        time.sleep(2)
        print("Depois da batalha, nossa inteligência conseguiu descobrir a antiga localização de todos os navios do inimigo.")
        time.sleep(0.5)
        desenhar_minimapa(matriz_partida_jogador2)

        time.sleep(1)
        decisao = input("\nDeseja jogar uma nova partida? (Sim ou Não): ")
        decisao = decisao.lower().replace(" ", "")

        decisao_nao_feita = True
        while decisao_nao_feita:
            if decisao == "sim" or decisao == "s" or decisao == "si" or decisao == "yes" or decisao == "ye" or decisao == "y":
                time.sleep(1)
                print("Recomeçando partida.")
                time.sleep(0.5)
                print("Recomeçando partida..")
                time.sleep(0.5)
                print("Recomeçando partida...")
                time.sleep(0.5)
                print("Recomeçando partida....")
                time.sleep(1)
                print("\n\n\n")

                decisao_nao_feita = False
                break

            elif decisao == "não" or decisao == "nao" or decisao == "na" or decisao == "n" or decisao == "no":
                time.sleep(1)
                print("Obrigado por jogar!")
                time.sleep(1)
                print("Finalizando o programa.")
                time.sleep(2)

                decisao_nao_feita = False
                jogo_loopando = False
                break

main()