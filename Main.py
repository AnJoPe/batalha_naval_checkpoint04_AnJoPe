import random, time


# Função para ver as regras e mecânicas do jogo
def regras():
    print(
        "\n🌊⚓════════════════════════════════════════════════════════⚓🌊\n\n"
        "📜 REGRAS DA BATALHA NAVAL 📜\n\n"
        "🗺️  O jogo acontece em um tabuleiro 2D.\n"
        "⚔️  Batalha Naval é um clássico jogo de estratégia.\n"
        "🎯  Seu objetivo: afundar os navios inimigos antes que eles afundem os seus!\n"
        "📐  Escolha o tamanho do mapa: 4x4 ou 6x6.\n"
        "🚢  Posicione os navios manualmente ou de forma aleatória.\n\n"
        "📌 Limite de navios por tamanho de mapa:\n\n"
        "\t🚢-----------------------------------------------🚢\n"
        "\t|   Tipo de Navio   |   4x4   |   5x5   |   6x6   |\n"
        "\t🚢-----------------------------------------------🚢\n"
        "\t| ⚔️ Destroier      |    2    |    1    |    2     |\n"
        "\t| 🌊 Submarino     |    1    |    1    |    1     |\n"
        "\t| 🏴‍☠️ Cruzador     |    -    |    1    |    1     |\n"
        "\t| 🛡️ Encouraçado    |    -    |    1    |    2     |\n"
        "\t🚢-----------------------------------------------🚢\n"
        "\n🌊⚓════════════════════════════════════════════════════════⚓🌊\n"
    )



def introducao():
    print(
        "\n🌊⚓~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~⚓🌊\n\n"
        "      🚢  Bem-vindos à grande aventura: BATALHA NAVAL ANJOPE  🚢\n"
        "                      💻 Desenvolvido por:\n"
        "    👨‍💻 André Colombo | 👨‍💻 José Diogo | 👨‍💻 Pedro Miranda\n"
        "\n🌊⚓~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~⚓🌊\n\n"
        "📜 Antes de começar a jogar, deseja ver as Regras? (S/N)"
    )

    ver_regras = input("👉 S - Sim | N - Não: ").lower()

    if ver_regras in ["sim", "s", "si", "yes", "ye", "y"]:
        time.sleep(0.5)
        regras()
    else:
        print(
            "\n🌊⚓~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~⚓🌊\n\n"
            "➡️  Então vamos continuar a aventura, Capitão! 🚢🔥\n"
            "\n🌊⚓~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~⚓🌊\n"
        )


# SIGNIFICADO IDENTIFICADORES
# 0 — Água — 🌊
# 1 — Submarino — 🚢
# 2 — Destróier — 🚢
# 3 — Cruzador — 🚢
# 4 — Encouraçado — 🚢
# 5 — Ataque bem-sucedido — 💥
# 6 — Ataque mal-sucedido — ❌

identificadores_navios = {
    "Submarino": {"Identificador": 1, "Tamanho": 1},
    "Destróier": {"Identificador": 2, "Tamanho": 2},
    "Cruzador": {"Identificador": 3, "Tamanho": 3},
    "Encouraçado": {"Identificador": 4, "Tamanho": 4},
}

lista_prioridades_inteligencia_artificial = []
lista_ignorar_inteligencia_artificial = []


# Função para escolher o tamanho do mapa
def escolher_mapa():
    print(
    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
    "🗺️  Escolha o tamanho do mapa desejado:\n\n"
    "  1️⃣  Pequeno  (4x4)\n"
    "  2️⃣  Médio    (5x5)\n"
    "  3️⃣  Grande   (6x6)\n"
    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
)
    # Variável para verificar se vai rodar o WHILE novamente ou se vai proseguir.
    verificar = 0
    while verificar == 0:
        tamanho_mapa = int(input("👉 Digite sua escolha, Capitão: "))
        match tamanho_mapa:
            case 1:
                print(
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
                    "✅ Você escolheu o mapa: 🗺️  Pequeno (4x4)! 🚢\n"
                    "Prepare-se para a batalha, Capitão! ⚔️🔥\n"
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                )
                return 1
            case 2:
                print(
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
                    "✅ Você escolheu o mapa: 🗺️  Médio (5x5)! ⚓\n"
                    "As águas estão ficando perigosas... mantenha-se atento, Capitão! 🌊👀\n"
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                )
                return 2
            case 3:
                print(
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
                    "✅ Você escolheu o mapa: 🗺️  Grande (6x6)! 🐉🚢\n"
                    "Os mares sombrios aguardam sua coragem... 🌑⚔️\n"
                    "A batalha final está prestes a começar, Capitão! 🔥\n"
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                )
                return 3
            case _:
                print(
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
                    "❌ Valor inválido, Capitão! Escolha apenas entre 1️⃣, 2️⃣ ou 3️⃣! ⚓\n"
                    "Tente novamente e prepare-se para a aventura! 🚢🔥\n"
                    "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                )
                verificar = 0


def preparar_mapas(tamanho_mapa):
    estados_jogo_principal = {
        "matriz_partida_jogador1": [],
        "matriz_partida_jogador2": [],
        "matriz_alvo_jogador1": [],
        "posicoes_navios_jogador1": {},
        "posicoes_navios_jogador2": {},
        "lista_prioridades_ia": [],
        "lista_ignorar_ia": [],
        "numero_submarinos": 0,
        "numero_destroiers": 0,
        "numero_encouracados": 0,
        "numero_cruzadores": 0,
    }

    if tamanho_mapa == 1:
        estados_jogo_principal["numero_submarinos"] = 1
        estados_jogo_principal["numero_destroiers"] = 2
        estados_jogo_principal["numero_encouracados"] = 0
        estados_jogo_principal["numero_cruzadores"] = 0

        estados_jogo_principal["matriz_partida_jogador1"] = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_partida_jogador2"] = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_alvo_jogador1"] = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    elif tamanho_mapa == 2:
        estados_jogo_principal["numero_submarinos"] = 1
        estados_jogo_principal["numero_destroiers"] = 1
        estados_jogo_principal["numero_encouracados"] = 1
        estados_jogo_principal["numero_cruzadores"] = 1

        estados_jogo_principal["matriz_partida_jogador1"] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_partida_jogador2"] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_alvo_jogador1"] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    elif tamanho_mapa == 3:
        estados_jogo_principal["numero_submarinos"] = 1
        estados_jogo_principal["numero_destroiers"] = 2
        estados_jogo_principal["numero_encouracados"] = 2
        estados_jogo_principal["numero_cruzadores"] = 1

        estados_jogo_principal["matriz_partida_jogador1"] = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_partida_jogador2"] = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        estados_jogo_principal["matriz_alvo_jogador1"] = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]

    return estados_jogo_principal


def preparar_partida(estado_jogo):
    time.sleep(1)
    gerar_navios_inimigo_artificial(
        estado_jogo["numero_submarinos"],
        estado_jogo["numero_encouracados"],
        estado_jogo["numero_destroiers"],
        estado_jogo["numero_cruzadores"],
        estado_jogo,
    )
    print(
        "⚓👾 O adversário posicionou seus navios no tabuleiro! 🚢\n"
        "Prepare-se para a batalha, Capitão! ⚔️🔥\n"
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
    )
    time.sleep(1)

    print(
        "🚢⚓ É a nossa vez de posicionar os navios, Capitão! 🗺️\n"
        "Escolha sabiamente suas posições para dominar os mares! 🌊🔥\n"
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
    )
    time.sleep(1)
    gerar_navios_escolha(
        estado_jogo["numero_submarinos"],
        estado_jogo["numero_encouracados"],
        estado_jogo["numero_destroiers"],
        estado_jogo["numero_cruzadores"],
        estado_jogo,
    )


def gerar_navios_escolha(submarinos, encouracados, destroiers, cruzadores, estado_jogo):
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

    print(
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
        "🗺️  O mapa da batalha será exibido assim, Capitão! 🚢⚔️\n"
        "Prepare-se para a estratégia final nos mares! 🌊🔥\n"
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
    )
    time.sleep(0.5)
    desenhar_mapa_jogador(estado_jogo["matriz_partida_jogador1"])
    for navio in lista_navios_para_adicionar:
        while lista_navios_para_adicionar[navio] > 0:
            posicao_valida = False
            while not posicao_valida:
                try:
                    time.sleep(0.5)
                    posicao_inicial_linha = int(
                        input(
                            f"🧭 Capitão, insira a linha inicial para posicionar o navio {navio} 🚢 "
                            f"(1 a {len(estado_jogo['matriz_partida_jogador1'])}): "
                        )
                    )
                    posicao_inicial_coluna = int(
                        input(
                            f"🧭 Capitão, agora insira a coluna inicial para posicionar o navio {navio} 🚢 "
                            f"(1 a {len(estado_jogo['matriz_partida_jogador1'][0])}): "
                        )
                    )
                except:
                    print(
                        "\n❌ Valor inválido, Capitão! Por favor, insira um número válido ⚓🚢\n"
                        "🧭 Use os instrumentos de navegação corretamente e tente novamente! 🌊🔥\n"
                    )

                if posicao_inicial_linha < 1 or posicao_inicial_linha > len(
                    estado_jogo["matriz_partida_jogador1"]
                ):
                    time.sleep(1)
                    print(
                        f"❌ Linha inválida, Capitão! ⚓🚢 "
                        f"Por favor selecione uma posição entre 1 e {len(estado_jogo['matriz_partida_jogador1'])} 🧭🌊\n"
                    )
                    continue

                if posicao_inicial_coluna < 1 or posicao_inicial_coluna > len(
                    estado_jogo["matriz_partida_jogador1"][0]
                ):
                    time.sleep(1)
                    print(
                        f"❌ Coluna inválida, Capitão! ⚓🚢 "
                        f"Por favor selecione uma posição entre 1 e {len(estado_jogo['matriz_partida_jogador1'][0])} 🧭🌊\n"
                    )
                    continue

                posicao_inicial_linha -= 1  # as listas começam do zero
                posicao_inicial_coluna -= 1  # as listas começam do zero

                if (
                    not estado_jogo["matriz_partida_jogador1"][posicao_inicial_linha][
                        posicao_inicial_coluna
                    ]
                    == 0
                ):
                    time.sleep(1)
                    print(
                        "❌ Posição inválida, Capitão! ⚓🚢 "
                        "Já há um navio nessa posição! 🧭🌊 Tente novamente e mantenha a frota segura!\n"
                    )
                    continue

                if not navio == "Submarino":
                    if not pode_expandir(
                        [posicao_inicial_linha, posicao_inicial_coluna],
                        navio,
                        estado_jogo,
                    ):
                        time.sleep(1)
                        print(
                            "❌ Espaço insuficiente, Capitão! ⚓🚢 "
                            "O navio não cabe nessa posição! 🧭🌊 Reavalie sua estratégia e tente novamente!\n"
                        )
                        continue

                if verificar_e_posicionar_navio(
                    [posicao_inicial_linha, posicao_inicial_coluna], navio, estado_jogo
                ):
                    posicao_valida = True
                    break
                else:
                    continue
            lista_navios_para_adicionar[navio] -= 1
            time.sleep(0.75)
            print(
                "\n✅ Navio posicionado com sucesso, Capitão! ⚓🚢\n"
                "A frota está se fortalecendo! 🌊🔥\n"
            )
            time.sleep(0.5)
            desenhar_mapa_jogador(estado_jogo["matriz_partida_jogador1"])


def pode_expandir(posicao_inicial, navio, estado_jogo):
    if navio == "Submarino":
        return True

    tamanho_navio = identificadores_navios[navio]["Tamanho"]

    pode_expandir_cima = True
    pode_expandir_baixo = True
    pode_expandir_esquerda = True
    pode_expandir_direita = True

    # CHECA OS CANTOS PRA VER SE NÃO ESTÁ EM ALGUMA PAREDE
    # TAMBÉM CHECA SE TEM ALGUM CAMINHO SEM NAVIOS
    if (posicao_inicial[0] == 0 or verificar_existencia_navio(
        posicao_inicial, navio, 0, estado_jogo
    ) or (posicao_inicial[0] - tamanho_navio) < 0):
        pode_expandir_cima = False

    if (posicao_inicial[0] == len(estado_jogo["matriz_partida_jogador1"]) - 1 or
            verificar_existencia_navio(posicao_inicial, navio, 2, estado_jogo) or
                (posicao_inicial[0] + tamanho_navio) >= len(estado_jogo["matriz_partida_jogador1"])):
        pode_expandir_baixo = False

    if (posicao_inicial[1] == 0 or
            verificar_existencia_navio(posicao_inicial, navio, 3, estado_jogo) or
                (posicao_inicial[1] - tamanho_navio) < 0):
        pode_expandir_esquerda = False

    if (posicao_inicial[1] == len(estado_jogo["matriz_partida_jogador1"][0]) - 1 or
            verificar_existencia_navio(posicao_inicial, navio, 1, estado_jogo) or
                (posicao_inicial[1] + tamanho_navio) >= len(estado_jogo["matriz_partida_jogador1"])):
        pode_expandir_direita = False

    #print(f"POSSO EXPANDIR CIMA?: {pode_expandir_cima}")
    #print(f"POSSO EXPANDIR BAIXO?: {pode_expandir_baixo}")
    #print(f"POSSO EXPANDIR ESQUERDA?: {pode_expandir_esquerda}")
    #print(f"POSSO EXPANDIR DIREITA?: {pode_expandir_direita}")

    if (
        pode_expandir_cima
        or pode_expandir_baixo
        or pode_expandir_esquerda
        or pode_expandir_direita
    ):
        #print("RETORNEI TRUE")
        return True
    else:
        #print("RETORNEI FALSE")
        return False


def verificar_e_posicionar_navio(posicao_inicial, navio, estado_jogo):
    if (
        navio == "Submarino"
        and estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
            posicao_inicial[1]
        ]
        == 0
    ):
        estado_jogo["posicoes_navios_jogador1"][
            f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
        ] = {"Tipo_Navio": navio, "Posicoes": [posicao_inicial]}
        posicionar_navio(posicao_inicial, navio, 0, estado_jogo)
        return True

    elif navio == "Submarino":
        time.sleep(1)
        print(
            "❌ Capitão! ⚓🚢 Há um navio nessa posição, impossível posicionar o submarino aqui! 🧭🌊\n"
            "Reavalie a estratégia e escolha uma posição segura para sua frota! ⚔️🔥\n"
        )
        return False

    quantidade_posicoes = identificadores_navios[navio]["Tamanho"]

    if not pode_expandir(posicao_inicial, navio, estado_jogo):
        time.sleep(2)
        print(
            f"❌ Capitão! ⚓🚢 O {navio} não pode ser posicionado aqui, "
            "pois não há espaço suficiente em nenhuma direção! 🧭🌊\n"
            "Reavalie sua estratégia e escolha outro local seguro para a frota! ⚔️🔥\n"
        )
        return False

    pode_mover_cima = True
    pode_mover_baixo = True
    pode_mover_esquerda = True
    pode_mover_direita = True

    if posicao_inicial[0] - (quantidade_posicoes - 1) < 0 or verificar_existencia_navio(
        posicao_inicial, navio, 0, estado_jogo
    ):
        pode_mover_cima = False

    if posicao_inicial[0] + (quantidade_posicoes - 1) >= (
        len(estado_jogo["matriz_partida_jogador1"])
    ) or verificar_existencia_navio(posicao_inicial, navio, 2, estado_jogo):
        pode_mover_baixo = False

    if posicao_inicial[1] - (quantidade_posicoes - 1) < 0 or verificar_existencia_navio(
        posicao_inicial, navio, 3, estado_jogo
    ):
        pode_mover_esquerda = False

    if posicao_inicial[1] - (quantidade_posicoes - 1) > (
        len(estado_jogo["matriz_partida_jogador1"])
    ) or verificar_existencia_navio(posicao_inicial, navio, 1, estado_jogo):
        pode_mover_direita = False
    escolher_direcao_pergunta = (
        "\n🧭 Capitão, escolha a direção para posicionar seu navio 🚢:\n\n"
    )
    if pode_mover_cima:
        escolher_direcao_pergunta += "1 — Cima ↑\n"
    if pode_mover_direita:
        escolher_direcao_pergunta += "2 — Direita →\n"
    if pode_mover_baixo:
        escolher_direcao_pergunta += "3 — Baixo ↓\n"
    if pode_mover_esquerda:
        escolher_direcao_pergunta += "4 — Esquerda ←\n"

    direcao_valida = False
    while not direcao_valida:
        time.sleep(0.75)
        escolha_direcao = int(input(escolher_direcao_pergunta + "👉 Capitão, escolha a direção do navio 🚢: "))

        if escolha_direcao < 1 or escolha_direcao > 4:
            time.sleep(1)
            print("❌ Direção inválida, Capitão! ⚓🚢 "
                    "Escolha uma direção correta para o navio 🧭🌊 e tente novamente!\n")
            continue

        if escolha_direcao == 1 and not pode_mover_cima:
            time.sleep(1)
            print(
                "❌ Capitão! ⚓🚢 Não há espaço para posicionar o navio para cima ⬆️🧭🌊\n"
                "Reavalie a estratégia e escolha outra direção segura para a frota! ⚔️🔥\n"
            )
            continue
        if escolha_direcao == 2 and not pode_mover_direita:
            time.sleep(1)
            print(
                "❌ Capitão! ⚓🚢 Não há espaço para posicionar o navio para a direita ➡️🧭🌊\n"
                "Reavalie a estratégia e escolha outra direção segura para a frota! ⚔️🔥\n"
            )
            continue
        if escolha_direcao == 3 and not pode_mover_baixo:
            time.sleep(1)
            print(
                "❌ Capitão! ⚓🚢 Não há espaço para posicionar o navio para baixo ⬇️🧭🌊\n"
                "Reavalie a estratégia e escolha outra direção segura para a frota! ⚔️🔥\n"
            )
            continue
        if escolha_direcao == 4 and not pode_mover_esquerda:
            time.sleep(1)
            print(
                "❌ Capitão! ⚓🚢 Não há espaço para posicionar o navio para a esquerda ⬅️🧭🌊\n"
                "Reavalie a estratégia e escolha outra direção segura para a frota! ⚔️🔥\n"
            )
            continue

        direcao_valida = True

    posicionar_navio(posicao_inicial, navio, escolha_direcao - 1, estado_jogo)
    return True


def verificar_existencia_navio(posicao_inicial, navio, direcao, estado_jogo):
    quantidade_posicoes = identificadores_navios[navio]["Tamanho"]
    """
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    """
    try:
        match direcao:
            case 0:
                for pos in range(1, quantidade_posicoes):
                    if (
                        not estado_jogo["matriz_partida_jogador1"][
                            posicao_inicial[0] - pos
                        ][posicao_inicial[1]]
                        == 0
                    ):
                        return True

            case 1:
                for pos in range(1, quantidade_posicoes):
                    if (
                        not estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
                            posicao_inicial[1] + pos
                        ]
                        == 0
                    ):
                        return True

            case 2:
                for pos in range(1, quantidade_posicoes):
                    if (
                        not estado_jogo["matriz_partida_jogador1"][
                            posicao_inicial[0] + pos
                        ][posicao_inicial[1]]
                        == 0
                    ):
                        return True

            case 3:
                for pos in range(1, quantidade_posicoes):
                    if (
                        not estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
                            posicao_inicial[1] - pos
                        ]
                        == 0
                    ):
                        return True

        return False
    except IndexError:
        return True


def posicionar_navio(posicao_inicial, navio, direcao, estado_jogo):
    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][posicao_inicial[1]] = (
        identificadores_navios[navio]["Identificador"]
    )
    """
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    """
    if identificadores_navios[navio]["Tamanho"] > 1:
        match direcao:
            case 0:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0] - pos][
                        posicao_inicial[1]
                    ] = identificadores_navios[navio]["Identificador"]
                    lista_posicoes_navio.append(
                        [posicao_inicial[0] - pos, posicao_inicial[1]]
                    )

                estado_jogo["posicoes_navios_jogador1"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}
            case 1:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
                        posicao_inicial[1] + pos
                    ] = identificadores_navios[navio]["Identificador"]
                    lista_posicoes_navio.append(
                        [posicao_inicial[0], posicao_inicial[1] + pos]
                    )

                estado_jogo["posicoes_navios_jogador1"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}
            case 2:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]
                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0] + pos][
                        posicao_inicial[1]
                    ] = identificadores_navios[navio]["Identificador"]
                    lista_posicoes_navio.append(
                        [posicao_inicial[0] + pos, posicao_inicial[1]]
                    )

                estado_jogo["posicoes_navios_jogador1"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}
            case 3:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    estado_jogo["matriz_partida_jogador1"][posicao_inicial[0]][
                        posicao_inicial[1] - pos
                    ] = identificadores_navios[navio]["Identificador"]
                    lista_posicoes_navio.append(
                        [posicao_inicial[0], posicao_inicial[1] - pos]
                    )

                estado_jogo["posicoes_navios_jogador1"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador1']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}


def gerar_navios_inimigo_artificial(
    submarinos, encouracados, destroiers, cruzadores, estado_jogo
):
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
            while True:  # SAIRÁ MANUALMENTE PRA PREVENIR SPAWN EM BLOCO INVALIDO
                posicao_inicial_linha = random.randrange(
                    0, len(estado_jogo["matriz_partida_jogador2"])
                )
                posicao_inicial_coluna = random.randrange(
                    0, len(estado_jogo["matriz_partida_jogador2"][0])
                )
                ###CHECA SE SÃO LINHAS E COLUNAS VÁLIDAS!!!
                ###UMA LINHA E COLUNA VALIDA ESTÁ DENTRO DA MATRIZ E NAO TEM NAVIO NO QUADRADO
                ####TAMBEM NAO É MENOR QUE 1 NENHUM DOS DOIS
                #####CHECA TAMBÉM SE O QUADRADO ESCOLHIDO TEM LUGAR PRA EXPANDIR, OU SEJA
                ###TEM ALGUMA DIREÇÃO A SEGUIR CASO O NAVIO TENHA MAIS DE 1 ESPAÇO

                if (
                    not estado_jogo["matriz_partida_jogador2"][posicao_inicial_linha][
                        posicao_inicial_coluna
                    ]
                    == 0
                ):
                    continue
                else:
                    break

            navio_criado_com_sucesso = False
            tentativa_atual = 0

            while not navio_criado_com_sucesso and tentativa_atual < 50:
                navio_criado_com_sucesso = verificar_e_posicionar_navio_inimigo(
                    [posicao_inicial_linha, posicao_inicial_coluna],
                    navio,
                    identificadores_navios[navio]["Tamanho"],
                    estado_jogo,
                )
                tentativa_atual += 1

            if not navio_criado_com_sucesso:
                continue

            lista_navios_para_adicionar[navio] -= 1


def verificar_e_posicionar_navio_inimigo(
    posicao_inicial, navio, quantidade_posicoes, estado_jogo
):
    if (
        navio == "Submarino"
        and estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
            posicao_inicial[1]
        ]
        == 0
    ):
        estado_jogo["posicoes_navios_jogador2"][
            f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
        ] = {"Tipo_Navio": navio, "Posicoes": [posicao_inicial]}
        posicionar_navio_inimigo(posicao_inicial, navio, 0, estado_jogo)
        return True

    elif navio == "Submarino":
        return False

    pode_mover_cima = True
    pode_mover_baixo = True
    pode_mover_esquerda = True
    pode_mover_direita = True

    possibilidades_direcao_navio = [0, 1, 2, 3]

    if posicao_inicial[0] - (
        quantidade_posicoes - 1
    ) < 0 or verificar_existencia_navio_inimigo(
        posicao_inicial, quantidade_posicoes, 0, estado_jogo
    ):
        pode_mover_cima = False
        possibilidades_direcao_navio.remove(0)

    if posicao_inicial[0] + (quantidade_posicoes - 1) >= len(
        estado_jogo["matriz_partida_jogador2"]
    ) or verificar_existencia_navio_inimigo(
        posicao_inicial, quantidade_posicoes, 2, estado_jogo
    ):
        pode_mover_baixo = False
        possibilidades_direcao_navio.remove(2)

    if posicao_inicial[1] - (
        quantidade_posicoes - 1
    ) < 0 or verificar_existencia_navio_inimigo(
        posicao_inicial, quantidade_posicoes, 3, estado_jogo
    ):
        pode_mover_esquerda = False
        possibilidades_direcao_navio.remove(3)

    if posicao_inicial[1] + (quantidade_posicoes - 1) >= len(
        estado_jogo["matriz_partida_jogador2"]
    ) or verificar_existencia_navio_inimigo(
        posicao_inicial, quantidade_posicoes, 1, estado_jogo
    ):
        pode_mover_direita = False
        possibilidades_direcao_navio.remove(1)

    if len(possibilidades_direcao_navio) == 0:
        return False

    escolha_direcao_pergunta = random.choice(possibilidades_direcao_navio)
    posicionar_navio_inimigo(
        posicao_inicial, navio, escolha_direcao_pergunta, estado_jogo
    )
    return True


def verificar_existencia_navio_inimigo(
    posicao_inicial, quantidade_posicoes, direcao, estado_jogo
):
    """
    DIREÇÕES:
        0 - CIMA
        1 - DIREITA
        2 - BAIXO
        3 - ESQUERDA
    """
    try:
        match direcao:
            case 0:
                for pos in range(1, quantidade_posicoes):
                    if (
                        not estado_jogo["matriz_partida_jogador2"][
                            posicao_inicial[0] - pos
                        ][posicao_inicial[1]]
                        == 0
                    ):
                        return True

            case 1:
                for pos in range(1, quantidade_posicoes):
                    if (
                        not estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
                            posicao_inicial[1] + pos
                        ]
                        == 0
                    ):
                        return True

            case 2:
                for pos in range(1, quantidade_posicoes):
                    if (
                        not estado_jogo["matriz_partida_jogador2"][
                            posicao_inicial[0] + pos
                        ][posicao_inicial[1]]
                        == 0
                    ):
                        return True

            case 3:
                for pos in range(1, quantidade_posicoes):
                    if (
                        not estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
                            posicao_inicial[1] - pos
                        ]
                        == 0
                    ):
                        return True

        return False
    except IndexError:
        return True


def posicionar_navio_inimigo(posicao_inicial, navio, direcao, estado_jogo):
    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][posicao_inicial[1]] = (
        identificadores_navios[navio]["Identificador"]
    )
    """
        DIREÇÕES:
            0 - CIMA
            1 - DIREITA
            2 - BAIXO
            3 - ESQUERDA
    """
    if identificadores_navios[navio]["Tamanho"] > 1:
        match direcao:
            case 0:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0] - pos][
                        posicao_inicial[1]
                    ] = identificadores_navios[navio]["Identificador"]
                    lista_posicoes_navio.append(
                        [posicao_inicial[0] - pos, posicao_inicial[1]]
                    )

                estado_jogo["posicoes_navios_jogador2"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}

            case 1:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
                        posicao_inicial[1] + pos
                    ] = identificadores_navios[navio]["Identificador"]
                    lista_posicoes_navio.append(
                        [posicao_inicial[0], posicao_inicial[1] + pos]
                    )

                estado_jogo["posicoes_navios_jogador2"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}
            case 2:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0] + pos][
                        posicao_inicial[1]
                    ] = identificadores_navios[navio]["Identificador"]
                    lista_posicoes_navio.append(
                        [posicao_inicial[0] + pos, posicao_inicial[1]]
                    )

                estado_jogo["posicoes_navios_jogador2"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}
            case 3:
                lista_posicoes_navio = [[posicao_inicial[0], posicao_inicial[1]]]

                for pos in range(1, (identificadores_navios[navio]["Tamanho"])):
                    estado_jogo["matriz_partida_jogador2"][posicao_inicial[0]][
                        posicao_inicial[1] - pos
                    ] = identificadores_navios[navio]["Identificador"]
                    lista_posicoes_navio.append(
                        [posicao_inicial[0], posicao_inicial[1] - pos]
                    )

                estado_jogo["posicoes_navios_jogador2"][
                    f"Navio_{len(estado_jogo['posicoes_navios_jogador2']) + 1}"
                ] = {"Tipo_Navio": navio, "Posicoes": lista_posicoes_navio}


def desenhar_minimapa(matriz):
    matriz_desenhada = ""
    numero_colunas = len(matriz[0])
    numero_linhas = len(matriz)
    for linha in range(numero_linhas):
        for coluna_quadrado in range(numero_colunas):
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
            matriz_desenhada += " |￣￣￣￣|"
        matriz_desenhada += "\n"

        for segunda_parede_quadrado in range(numero_colunas):
            if matriz[linha][segunda_parede_quadrado] == 0:
                matriz_desenhada += " |   🌊   |"
            elif matriz[linha][segunda_parede_quadrado] == 1:
                matriz_desenhada += " |   🚢   |"
            elif matriz[linha][segunda_parede_quadrado] == 2:
                matriz_desenhada += " |   🚢   |"
            elif matriz[linha][segunda_parede_quadrado] == 3:
                matriz_desenhada += " |   🚢   |"
            elif matriz[linha][segunda_parede_quadrado] == 4:
                matriz_desenhada += " |   🚢   |"
            elif matriz[linha][segunda_parede_quadrado] == 5:
                matriz_desenhada += " |   💥   |"
            elif matriz[linha][segunda_parede_quadrado] == 6:
                matriz_desenhada += " |   ❌   |"
            else:
                matriz_desenhada += " |        |"
        matriz_desenhada += "\n"

        for terceira_parede_quadrado in range(numero_colunas):
            matriz_desenhada += " |        |"
        matriz_desenhada += "\n"
    for quadrado_coluna in range(numero_colunas):
        matriz_desenhada += "  ￣￣￣￣ "

    print(matriz_desenhada)


def partida_principal(estado_jogo):
    while True:
        try:
            time.sleep(1)
            print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")
            jogador_inicial = int(
                input(
                    "🧭 Capitão, quem irá iniciar a batalha? ⚔️🚢\n\n"
                    "  1️⃣ — Jogador\n"
                    "  2️⃣ — Adversário 👾\n"
                    "  3️⃣ — Aleatório 🎲\n\n"
                    "👉 Decisão: "
                )
            )
            print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n")
            if 1 <= jogador_inicial <= 3:
                break  # valor válido, sai do loop
            else:
                time.sleep(1)
                print(
                    "❌ Opção inválida, Capitão! ⚓🚢 "
                    "Escolha apenas entre 1️⃣, 2️⃣ ou 3️⃣ 🧭🌊\n"
                    "Tome cuidado e faça a escolha certa para iniciar a batalha! ⚔️🔥\n"
                )
        except ValueError:
            time.sleep(1)
            print(
                "❌ Entrada inválida, Capitão! ⚓🚢 "
                "Digite apenas números inteiros 🧭🌊\n"
                "Use os instrumentos de navegação corretamente e tente novamente! ⚔️🔥\n"
            )

    if jogador_inicial == 3:
        jogador_atual = random.randrange(1, 3)
        time.sleep(1)
        print(
            f"🎲 Seleção aleatória concluída! ⚓🚢\n"
            f"➡️ {jogador_atual} ⚔️🔥\n"
        )
    else:
        jogador_atual = jogador_inicial

    time.sleep(1)
    print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")
    print("🧭 Determinando quem iniciará a partida... ⚔️🚢")
    time.sleep(0.75)
    if jogador_atual == 1:
        print("➡️ O Capitão Jogador irá comandar a primeira jogada! 🔥")
    else:
        print("➡️ O Capitão Adversário assumirá o comando da primeira jogada! 👾⚔️")
    print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")

    partida_em_progresso = True

    time.sleep(0.85)
    print(
        "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n\n"
        "⚔️🚢 A batalha começou, Capitão! 🧭\n"
        "Prepare-se para conquistar os mares e afundar os navios inimigos! 🌊🔥\n\n"
        "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
    )
    time.sleep(1.1)

    while partida_em_progresso:
        match jogador_atual:
            case 1:
                time.sleep(1)
                print(
                    "\n🧭 Capitão, este é o Mapa de Inteligência! ⚓🚢\n"
                    "Ele revelará seus acertos e erros durante os ataques inimigos e os seus! 🌊⚔️\n"
                    "Use-o estrategicamente para dominar os mares! 🔥🗺️\n"
                )
                time.sleep(0.5)
                desenhar_mapa_jogador(estado_jogo["matriz_alvo_jogador1"])

                posicao_valida = False
                while not posicao_valida:
                    time.sleep(0.75)
                    posicao_ataque_linha = input(
                        f"🧭 Capitão, insira a linha para realizar seu ataque 🚢⚔️ "
                        f"(1 a {len(estado_jogo['matriz_alvo_jogador1'])}): "
                    )
                    if not posicao_ataque_linha.isdigit():
                        print(
                            "❌ Entrada inválida, Capitão! ⚓🚢 "
                            "Insira apenas números inteiros 🧭🌊\n"
                            "Use os instrumentos de navegação corretamente e tente novamente! ⚔️🔥\n"
                        )
                        continue

                    posicao_ataque_linha = int(posicao_ataque_linha)

                    posicao_ataque_coluna = input(
                        f"🧭 Capitão, insira a coluna para realizar seu ataque 🚢⚔️ "
                        f"(1 a {len(estado_jogo['matriz_alvo_jogador1'][0])}): "
                    )
                    if not posicao_ataque_coluna.isdigit():
                        print(
                            "❌ Entrada inválida, Capitão! ⚓🚢 "
                            "Insira apenas números inteiros para a coluna 🧭🌊\n"
                            "Use os instrumentos de navegação corretamente e tente novamente! ⚔️🔥\n"
                        )
                        continue

                    posicao_ataque_coluna = int(posicao_ataque_coluna)

                    if posicao_ataque_linha < 1 or posicao_ataque_linha > len(
                        estado_jogo["matriz_partida_jogador1"]
                    ):
                        time.sleep(1)
                        print(
                            f"❌ Linha inválida, Capitão! ⚓🚢 "
                            f"Por favor selecione uma posição entre 1 e {len(estado_jogo['matriz_alvo_jogador1'])} 🧭🌊\n"
                            "Escolha sabiamente e mire com precisão! ⚔️🔥\n"
                        )
                        continue

                    if posicao_ataque_coluna < 1 or posicao_ataque_coluna > len(
                        estado_jogo["matriz_alvo_jogador1"][0]
                    ):
                        time.sleep(1)
                        print(
                            f"❌ Coluna inválida, Capitão! ⚓🚢 "
                            f"Por favor selecione uma posição entre 1 e {len(estado_jogo['matriz_alvo_jogador1'][0])} 🧭🌊\n"
                            "Escolha sabiamente e mire com precisão! ⚔️🔥\n"
                        )
                        continue

                    posicao_ataque_linha -= 1  # as listas começam do zero
                    posicao_ataque_coluna -= 1  # as listas começam do zero

                    posicao_valida = True

                time.sleep(0.75)
                if (
                    estado_jogo["matriz_alvo_jogador1"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ]
                    == 5
                    or estado_jogo["matriz_alvo_jogador1"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ]
                    == 6
                ):

                    print(
                        "❌ Atenção, Capitão! ⚓🚢\n"
                        "Nossa inteligência indica que já atacamos essas coordenadas! 🧭🌊\n"
                        "Escolha um novo alvo com sabedoria para dominar os mares! ⚔️🔥\n"
                    )

                elif (
                    not estado_jogo["matriz_partida_jogador2"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ]
                    == 0
                    and not estado_jogo["matriz_partida_jogador2"][
                        posicao_ataque_linha
                    ][posicao_ataque_coluna]
                    == 5
                    and not estado_jogo["matriz_partida_jogador2"][
                        posicao_ataque_linha
                    ][posicao_ataque_coluna]
                    == 6
                ):

                    print(
                        "\n✅ Capitão! ⚓🚢 Nossa inteligência indica que o ataque foi um sucesso! 🌊⚔️\n"
                        "O inimigo foi atingido! Prepare-se para o próximo movimento estratégico! 🔥🧭\n"
                    )
                    estado_jogo["matriz_alvo_jogador1"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ] = 5
                    for nav in estado_jogo["posicoes_navios_jogador2"]:
                        for posicao in estado_jogo["posicoes_navios_jogador2"][nav][
                            "Posicoes"
                        ]:
                            if (
                                posicao[0] == posicao_ataque_linha
                                and posicao[1] == posicao_ataque_coluna
                            ):
                                estado_jogo["posicoes_navios_jogador2"][nav][
                                    "Posicoes"
                                ].remove([posicao_ataque_linha, posicao_ataque_coluna])

                else:
                    print(
                        "❌ Capitão! ⚓🚢 Nossa inteligência indica que o ataque falhou! 🌊⚔️\n"
                        "O inimigo saiu ileso. Reavalie sua estratégia e prepare o próximo ataque! 🔥🧭\n"
                    )
                    estado_jogo["matriz_alvo_jogador1"][posicao_ataque_linha][
                        posicao_ataque_coluna
                    ] = 6

            case 2:
                print(
                    "\n⚠️ Capitão! O inimigo está prestes a atacar! 🔥🚢\n"
                    "Prepare-se para defender a frota e reagir estrategicamente! 🧭⚔️🌊\n"
                )
                time.sleep(0.75)
                if len(lista_prioridades_inteligencia_artificial) == 0:
                    posicao_valida = False

                    posicao_ataque_linha_jogador_humano = random.randrange(
                        0, len(estado_jogo["matriz_partida_jogador1"])
                    )
                    posicao_ataque_coluna_jogador_humano = random.randrange(
                        0, len(estado_jogo["matriz_partida_jogador1"][0])
                    )

                    while not posicao_valida:
                        posicao_ataque_linha_jogador_humano = random.randrange(
                            0, len(estado_jogo["matriz_partida_jogador1"])
                        )

                        posicao_ataque_coluna_jogador_humano = random.randrange(
                            0, len(estado_jogo["matriz_partida_jogador1"][0])
                        )

                        if (
                            posicao_ataque_linha_jogador_humano < 0
                            or posicao_ataque_linha_jogador_humano
                            > len(estado_jogo["matriz_partida_jogador1"])
                        ):
                            continue

                        if (
                            posicao_ataque_coluna_jogador_humano < 0
                            or posicao_ataque_coluna_jogador_humano
                            > len(estado_jogo["matriz_alvo_jogador1"][0])
                        ):
                            continue

                        if [
                            posicao_ataque_linha_jogador_humano,
                            posicao_ataque_coluna_jogador_humano,
                        ] in lista_ignorar_inteligencia_artificial:
                            continue

                        posicao_valida = True

                    ataque_valido = False
                    while not ataque_valido:
                        if (
                            not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 0
                            and not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 5
                            and not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 6
                        ):
                            time.sleep(0.65)
                            print(
                                "💥 Capitão! ⚓🚢 O inimigo acertou em cheio! 🌊⚔️\n"
                                "A frota sofreu danos! Reorganize suas defesas e prepare o próximo ataque! 🔥🧭\n"
                            )
                            estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano] = 5

                            for nav in estado_jogo["posicoes_navios_jogador1"]:
                                for posicao in estado_jogo["posicoes_navios_jogador1"][
                                    nav
                                ]["Posicoes"]:
                                    if (
                                        posicao[0]
                                        == posicao_ataque_linha_jogador_humano
                                        and posicao[1]
                                        == posicao_ataque_coluna_jogador_humano
                                    ):
                                        estado_jogo["posicoes_navios_jogador1"][nav][
                                            "Posicoes"
                                        ].remove(
                                            [
                                                posicao_ataque_linha_jogador_humano,
                                                posicao_ataque_coluna_jogador_humano,
                                            ]
                                        )

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ACIMA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano - 1,
                                            posicao_ataque_coluna_jogador_humano,
                                        ]
                                    )

                            if (
                                posicao_ataque_linha_jogador_humano
                                < len(estado_jogo["matriz_partida_jogador1"]) - 2
                            ):
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ABAIXO
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano + 1,
                                            posicao_ataque_coluna_jogador_humano,
                                        ]
                                    )

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ESQUERDA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano,
                                            posicao_ataque_coluna_jogador_humano - 1,
                                        ]
                                    )

                            if (
                                posicao_ataque_linha_jogador_humano
                                > len(estado_jogo["matriz_partida_jogador1"][0]) - 2
                            ):
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - DIREITA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano,
                                            posicao_ataque_coluna_jogador_humano + 1,
                                        ]
                                    )

                        else:
                            time.sleep(0.65)
                            print(
                                "✅ Capitão! ⚓🚢 O ataque do inimigo foi em vão! 🌊⚔️\n"
                                "A frota permanece intacta! Aproveitem esta oportunidade para contra-atacar! 🔥🧭\n"
                            )
                            lista_ignorar_inteligencia_artificial.append(
                                [
                                    posicao_ataque_linha_jogador_humano,
                                    posicao_ataque_coluna_jogador_humano,
                                ]
                            )

                        ataque_valido = True
                else:
                    if not lista_prioridades_inteligencia_artificial:
                        continue

                    posicao_valida = False
                    tentativa = 0
                    prioridade_atacar = random.choice(
                        lista_prioridades_inteligencia_artificial
                    )

                    while not posicao_valida and tentativa <= 50:
                        prioridade_atacar = random.choice(
                            lista_prioridades_inteligencia_artificial
                        )
                        posicao_ataque_linha_jogador_humano = prioridade_atacar[0]
                        posicao_ataque_coluna_jogador_humano = prioridade_atacar[1]

                        if (
                            posicao_ataque_linha_jogador_humano < 0
                            or posicao_ataque_linha_jogador_humano
                            >= len(estado_jogo["matriz_partida_jogador1"])
                        ):
                            tentativa += 1
                            continue

                        if (
                            posicao_ataque_coluna_jogador_humano < 0
                            or posicao_ataque_coluna_jogador_humano
                            >= len(estado_jogo["matriz_alvo_jogador1"][0])
                        ):
                            tentativa += 1
                            continue

                        posicao_valida = True

                    if not posicao_valida:
                        lista_prioridades_inteligencia_artificial.remove(
                            prioridade_atacar
                        )
                        continue

                    ataque_valido = False
                    while not ataque_valido:
                        if (
                            not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 0
                            and not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 5
                            and not estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano]
                            == 6
                        ):
                            time.sleep(0.65)
                            print(
                                "💥 Capitão! ⚓🚢 O inimigo acertou em cheio! 🌊⚔️\n"
                                "A frota sofreu danos! Reorganize suas defesas e prepare o próximo ataque! 🔥🧭\n"
                            )
                            estado_jogo["matriz_partida_jogador1"][
                                posicao_ataque_linha_jogador_humano
                            ][posicao_ataque_coluna_jogador_humano] = 5

                            for nav in estado_jogo["posicoes_navios_jogador1"]:
                                for posicao in estado_jogo["posicoes_navios_jogador1"][
                                    nav
                                ]["Posicoes"]:
                                    if (
                                        posicao[0]
                                        == posicao_ataque_linha_jogador_humano
                                        and posicao[1]
                                        == posicao_ataque_coluna_jogador_humano
                                    ):
                                        estado_jogo["posicoes_navios_jogador1"][nav][
                                            "Posicoes"
                                        ].remove(
                                            [
                                                posicao_ataque_linha_jogador_humano,
                                                posicao_ataque_coluna_jogador_humano,
                                            ]
                                        )

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ACIMA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano - 1,
                                            posicao_ataque_coluna_jogador_humano,
                                        ]
                                    )

                            if (
                                posicao_ataque_linha_jogador_humano
                                < len(estado_jogo["matriz_partida_jogador1"]) - 2
                            ):
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ABAIXO
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano + 1,
                                            posicao_ataque_coluna_jogador_humano,
                                        ]
                                    )

                            if posicao_ataque_linha_jogador_humano > 0:
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - ESQUERDA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano,
                                            posicao_ataque_coluna_jogador_humano - 1,
                                        ]
                                    )

                            if (
                                posicao_ataque_linha_jogador_humano
                                > len(estado_jogo["matriz_partida_jogador1"][0]) - 2
                            ):
                                # 60% DE CHANCE DE QUERER TENTAR ATACAR NAVIOS PRÓXIMOS - DIREITA
                                if random.randrange(1, 11) <= 6:
                                    lista_prioridades_inteligencia_artificial.append(
                                        [
                                            posicao_ataque_linha_jogador_humano,
                                            posicao_ataque_coluna_jogador_humano + 1,
                                        ]
                                    )

                        else:
                            time.sleep(0.65)
                            print(
                                "✅ Capitão! ⚓🚢 O ataque do inimigo foi em vão! 🌊⚔️\n"
                                "A frota permanece intacta! Aproveitem esta oportunidade para contra-atacar! 🔥🧭\n"
                            )

                        if [
                            posicao_ataque_linha_jogador_humano,
                            posicao_ataque_coluna_jogador_humano,
                        ] in lista_prioridades_inteligencia_artificial:
                            lista_prioridades_inteligencia_artificial.remove(
                                [
                                    posicao_ataque_linha_jogador_humano,
                                    posicao_ataque_coluna_jogador_humano,
                                ]
                            )
                        ataque_valido = True
                time.sleep(1)
                print(
                    "\n🗺️ Capitão, aqui está o Mini-Mapa de Inteligência da frota! ⚓🚢\n"
                    "Ele indica os danos que sofremos e ajuda a planejar nosso próximo movimento estratégico! 🌊⚔️🔥\n"
                )
                time.sleep(0.5)
                desenhar_minimapa(estado_jogo["matriz_partida_jogador1"])
                time.sleep(1)

        if jogador_atual == 1:
            navio_existente = False

            for navio in estado_jogo["posicoes_navios_jogador2"]:
                if len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) > 0:
                    navio_existente = True

            if not navio_existente:
                return 1

        elif jogador_atual == 2:
            navio_existente = False

            for navio in estado_jogo["posicoes_navios_jogador1"]:
                if len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) > 0:
                    navio_existente = True

            if not navio_existente:
                return 2

        if jogador_atual == 1:
            jogador_atual = 2
        elif jogador_atual == 2:
            jogador_atual = 1
    return None


def main():
    jogo_loopando = True

    while jogo_loopando:
        # TAMANHOS
        # PEQUENO = 1 - 4x4
        # MÉDIO = 2 - 5x5
        # GRANDE = 3 - 6x6

        introducao()
        time.sleep(1.5)
        tamanho_mapa = escolher_mapa()
        estado_jogo = preparar_mapas(tamanho_mapa)

        preparar_partida(estado_jogo)

        vencedor = partida_principal(estado_jogo)

        time.sleep(1)
        print(
            "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            "🏴‍☠️ FIM DA PARTIDA, Capitão! ⚔️🚢\n"
            "A batalha terminou nos mares! 🔥🧭\n"
            "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
        )

        time.sleep(1.5)
        print(
            "\n🗺️ Capitão, aqui está o Mini-Mapa de Inteligência do inimigo! ⚓🚢\n"
            "Ele indica os ataques que realizamos e ajuda a planejar nossos próximos movimentos estratégicos! 🌊⚔️🔥\n"
        )
        time.sleep(0.5)
        desenhar_minimapa(estado_jogo["matriz_alvo_jogador1"])

        submarinos_inimigos_afundados = 0
        destroiers_inimigos_afundados = 0
        cruzadores_inimigos_afundados = 0
        encouracados_inimigos_afundados = 0

        submarinos_aliados_afundados = 0
        destroiers_aliados_afundados = 0
        cruzadores_aliados_afundados = 0
        encouracados_aliados_afundados = 0

        for navio in estado_jogo["posicoes_navios_jogador2"]:
            if (
                estado_jogo["posicoes_navios_jogador2"][navio]["Tipo_Navio"]
                == "Submarino"
                and len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) == 0
            ):
                submarinos_inimigos_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador2"][navio]["Tipo_Navio"]
                == "Destróier"
                and len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) == 0
            ):
                destroiers_inimigos_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador2"][navio]["Tipo_Navio"]
                == "Cruzador"
                and len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) == 0
            ):
                cruzadores_inimigos_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador2"][navio]["Tipo_Navio"]
                == "Encouraçado"
                and len(estado_jogo["posicoes_navios_jogador2"][navio]["Posicoes"]) == 0
            ):
                encouracados_inimigos_afundados += 1

        for navio in estado_jogo["posicoes_navios_jogador1"]:
            if (
                estado_jogo["posicoes_navios_jogador1"][navio]["Tipo_Navio"]
                == "Submarino"
                and len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) == 0
            ):
                submarinos_aliados_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador1"][navio]["Tipo_Navio"]
                == "Destróier"
                and len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) == 0
            ):
                destroiers_aliados_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador1"][navio]["Tipo_Navio"]
                == "Cruzador"
                and len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) == 0
            ):
                cruzadores_aliados_afundados += 1

            if (
                estado_jogo["posicoes_navios_jogador1"][navio]["Tipo_Navio"]
                == "Encouraçado"
                and len(estado_jogo["posicoes_navios_jogador1"][navio]["Posicoes"]) == 0
            ):
                encouracados_aliados_afundados += 1

        time.sleep(1)
        print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")
        print("🧭 Capitão, a tensão nos mares aumenta... Quem será o vencedor? ⚔️🚢")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n")


        if vencedor == 1:
            print("\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                    "🎆🏴‍☠️ PARABÉNS, Capitão Jogador 1! ⚔️🚢\n"
                    "Você conquistou os mares e afundou a frota inimiga! 🌊🔥🧭\n"
                    "🌊⚓═══════════════════════════════════════════════⚓🌊\n")
            time.sleep(1)

            print(
                "🛳️⚓ Resumo da Batalha ⚓🛳️\n"
                f"Submarinos inimigos afundados: {submarinos_inimigos_afundados} 🐋\n"
                f"Destroiers inimigos afundados: {destroiers_inimigos_afundados} 🚢\n"
                f"Cruzadores inimigos afundados: {cruzadores_inimigos_afundados} ⛴️\n"
                f"Encouraçados inimigos afundados: {encouracados_inimigos_afundados} 🛳️\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )

            time.sleep(1)

            print(
                "⚔️🛡️ Relatório de Danos da Frota ⚓🚢\n"
                f"Submarinos aliados afundados: {submarinos_aliados_afundados} 🐋\n"
                f"Destroiers aliados afundados: {destroiers_aliados_afundados} 🚢\n"
                f"Cruzadores aliados afundados: {cruzadores_aliados_afundados} ⛴️\n"
                f"Encouraçados aliados afundados: {encouracados_aliados_afundados} 🛳️\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )

        elif vencedor == 2:
            print(
                "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
                "💀🏴‍☠️ ALERTA, Capitão! O adversário venceu! ⚔️🚢\n"
                "Nossa frota foi derrotada nos mares! 🌊🔥🧭\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )
            time.sleep(1)

            print(
                "⚔️🛡️ Relatório de Perdas da Frota ⚓🚢\n"
                f"Submarinos aliados afundados: {submarinos_aliados_afundados} 🐋\n"
                f"Destroiers aliados afundados: {destroiers_aliados_afundados} 🚢\n"
                f"Cruzadores aliados afundados: {cruzadores_aliados_afundados} ⛴️\n"
                f"Encouraçados aliados afundados: {encouracados_aliados_afundados} 🛳️\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )

            time.sleep(1)

            print(
                "🛳️⚓ Relatório de Conquistas ⚓🛳️\n"
                f"Submarinos inimigos afundados: {submarinos_inimigos_afundados} 🐋\n"
                f"Destroiers inimigos afundados: {destroiers_inimigos_afundados} 🚢\n"
                f"Cruzadores inimigos afundados: {cruzadores_inimigos_afundados} ⛴️\n"
                f"Encouraçados inimigos afundados: {encouracados_inimigos_afundados} 🛳️\n"
                "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            )

        time.sleep(2)
        print(
            "\n🌊⚓═══════════════════════════════════════════════⚓🌊\n"
            "🧭 Capitão, após a batalha, nossa inteligência revelou a antiga localização de todos os navios inimigos! ⚓🚢\n"
            "Use essas informações para planejar futuras estratégias e dominar os mares! 🌊⚔️🔥\n"
            "🌊⚓═══════════════════════════════════════════════⚓🌊\n"
        )
        time.sleep(0.5)
        desenhar_minimapa(estado_jogo["matriz_partida_jogador2"])

        time.sleep(1)
        decisao = input("🧭 Capitão, deseja zarpar novamente para uma nova batalha? ⚓🚢 (Sim ou Não): ")
        decisao = decisao.lower().replace(" ", "")

        decisao_nao_feita = True
        while decisao_nao_feita:
            if (
                decisao == "sim"
                or decisao == "s"
                or decisao == "si"
                or decisao == "yes"
                or decisao == "ye"
                or decisao == "y"
            ):
                time.sleep(1)
                print("🌊⚓ Recomeçando a batalha. ⚓🚢")
                time.sleep(0.5)
                print("🌊⚓ Recomeçando a batalha.. ⚓🚢")
                time.sleep(0.5)
                print("🌊⚓ Recomeçando a batalha... ⚓🚢")
                time.sleep(0.5)
                print("🌊⚓ Recomeçando a batalha.... ⚓🚢")
                time.sleep(1)
                print("\n\n\n")

                decisao_nao_feita = False
                break

            elif (
                decisao == "não"
                or decisao == "nao"
                or decisao == "na"
                or decisao == "n"
                or decisao == "no"
            ):
                time.sleep(1)
                print("⚓🚢 Obrigado por jogar, Capitão! 🌊🧭")
                time.sleep(1)
                print("⚓ Finalizando a batalha e recolhendo a frota... ⚔️🔥")
                time.sleep(2)

                decisao_nao_feita = False
                jogo_loopando = False
                break


main()