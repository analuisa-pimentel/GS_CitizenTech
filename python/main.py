"""
CITIZENTECH - PONTO FRESCO - PYTHON - DADOS SIMULADOS
"""

""" -- CONSTANTES -- """
LIMITE_ATENCAO = 30
LIMITE_ELEVADO = 35
INTERVALO_MIN = 30

# Listas paralelas: o índice do estado é o mesmo da mensagem
ESTADOS = ['Normal', 'Atenção', 'Calor elevado', 'Falha de leitura']
MENSAGENS = [
    'Condição confortável para a espera.',
    'Atenção ao calor: procure a sombra do abrigo.',
    'Calor elevado: fique na sombra e mantenha-se hidratado.',
    'Sensor com falha: leitura indisponível.'
]

# Listas paralelas: o índice do modo é o mesmo da potência
VENTILACAO = ['Desligada', 'Modo 1', 'Modo 2']
POTENCIAS_W = [0, 10, 20]


""" -- LISTAS -- """
# Cada ponto: [letra, descrição, fator de infraestrutura]
# Fator: 0 = coberto e sombreado; 0.5 = proteção parcial; 1 = sem cobertura
PONTOS = [
    ['A', 'Ponto sem cobertura', 1], 
    ['B', 'Ponto com cobertura parcial', 0.5], 
    ['C', 'Ponto coberto e sombreado', 0]
    ] 

# Cada leitura: [ponto, hora, temperatura (°C), umidade (%), movimento recente]
# Dados SIMULADOS · janela de observação: 11:00 às 13:30, a cada 30 min
LEITURAS = [
    ['A', '11:00', 33.8, 62, True],
    ['A', '11:30', 35.2, 60, True],
    ['A', '12:00', 36.4, 58, False],
    ['A', '12:30', 37.1, 57, True],
    ['A', '13:00', 36.0, 59, True],
    ['A', '13:30', 34.5, 61, True],

    ['B', '11:00', 29.5, 65, True],
    ['B', '11:30', 34.6, 63, False],
    ['B', '12:00', 35.8, 61, True],
    ['B', '12:30', 36.3, 60, True],
    ['B', '13:00', None, 62, True],
    ['B', '13:30', 34.1, 64, False],

    ['C', '11:00', 28.6, 68, True],
    ['C', '11:30', 29.8, 66, True],
    ['C', '12:00', 34.2, 65, True],
    ['C', '12:30', 35.4, 63, True],
    ['C', '13:00', 34.8, 64, False],
    ['C', '13:30', 29.4, 66, True],
]

# Simulações feitas na opção 5. Ficam separadas: não alteram LEITURAS e somem quando o programa é fechado
simulacoes = []

""" -- FUNÇÕES DE ENTRADA E VALIDAÇÃO -- """
def ler_opcao(valor):
    if valor in ['0', '1', '2', '3', '4', '5']:
        return valor
    else:
        return None


def escolher_ponto():
    print('Escolha um ponto. \n' \
    'OPÇÕES DISPONÍVEIS: \n' \
    'A - Av. Pastor Martin Luther King, 98 \n' \
    'B - Av. Dom Hélder Câmara, 3196 \n' \
    'C - Estrada Adhemar Bebiano, 550 \n' \
    'T - TODOS')
    while True:
        ponto_escolhido = input('OPÇÃO ESCOLHIDA: ').strip().upper()
        valores_disponiveis = ['A', 'B', 'C', 'T']
        if ponto_escolhido in valores_disponiveis:
            return ponto_escolhido
        else:
            print('Valor não disponível! Tente novamente.')


def ler_numero(mensagem, minimo, maximo):
    while True:
        texto = input(mensagem).replace(",", ".")
        try:
            valor = float(texto)
        except ValueError:
            print("Valor inválido. Digite um número, ex.: 34.5")
            continue

        if minimo <= valor <= maximo:
            return valor
        else:
            print(f'Valor fora da faixa esperada ({minimo} a {maximo}).')


def ler_movimento():
    while True:
        movimento = input('Há movimento no ponto? (s/n): ').strip().upper()
        if movimento == 'S':
            return True
        elif movimento == 'N':
            return False
        else:
            print('Valor não aceito! Digite s ou n.')


def menu():
    print('\n=== Ponto Fresco · Zona Norte (dados simulados) ===')
    print('1 - Consultar medições de um ponto')
    print('2 - Resumo das condições')
    print('3 - Prioridade dos pontos')
    print('4 - Estimar energia dos pontos')
    print('5 - Simular uma leitura')
    print('0 - Sair')

    opcao = input('Opção escolhida: ').strip()
    return ler_opcao(opcao)


""" -- FUNÇÕES DE LÓGICA -- """
def classificar(temperatura):
    if temperatura is None:
        return 3
    elif temperatura < LIMITE_ATENCAO:
        return 0
    elif temperatura < LIMITE_ELEVADO:
        return 1
    else:
        return 2

    
def decidir_ventilacao(estado, movimento):
    if movimento == False or estado == 0 or estado == 3:
        return 0
    elif estado == 1:
        return 1
    else:
        return 2


def filtrar_por_ponto(leituras, ponto):
    if ponto == 'T':
        return leituras

    selecionadas = []
    for leitura in leituras:
        if leitura[0] == ponto:
            selecionadas.append(leitura)
    return selecionadas


def calcular_resumo(leituras, ponto):
    # Alerta = estados "Atenção" ou "Calor elevado" (indices 1 e 2)
    selecionadas = filtrar_por_ponto(leituras, ponto)
    soma = qtd_alerta = validas = falhas = 0
    valor_maximo = None
    hora_maximo = ''
    ponto_maximo = ''

    for leitura in selecionadas:
        if leitura[2] is None:
            falhas += 1
            continue
        else:
            validas += 1
            soma += leitura[2]

        if classificar(leitura[2]) in [1, 2]:
            qtd_alerta += 1

        if valor_maximo is None or leitura[2] > valor_maximo:
            valor_maximo = leitura[2]
            hora_maximo = leitura[1]
            ponto_maximo = leitura[0]

    media = soma/validas
    porcentagem_alerta = qtd_alerta/validas*100

    return media, valor_maximo, hora_maximo, ponto_maximo, porcentagem_alerta, qtd_alerta, validas, falhas


def minutos_exposicao(leituras):
    #Conta leituras em “Calor elevado” com movimento × INTERVALO_MIN
    exposicao = 0
    for leitura in leituras:
        indice = classificar(leitura[2])
        if indice == 2 and leitura[4] == True:
            exposicao += 1

    return exposicao * INTERVALO_MIN


def buscar_fator(ponto):
    fator = 0
    for item in PONTOS:
        if item[0] == ponto:
            fator = item[2]

    return fator


def calcular_prioridade(ponto):
    # Prioridade = minutos de calor elevado com movimento x (1 + fator)
    selecionadas = filtrar_por_ponto(LEITURAS, ponto)
    minutos_calor_elevado = minutos_exposicao(selecionadas)
    fator = buscar_fator(ponto)

    return minutos_calor_elevado * (1+fator)


def estimar_energia(leituras, ponto):
    # Automática: potência do modo decidido x 0.5h (cada leitura = 30 min)
    # Contínua: ventilador sempre no modo 2, para comparação

    selecionadas = filtrar_por_ponto(leituras, ponto)
    energia = energia_continua = 0

    for leitura in selecionadas:
        i = classificar(leitura[2])
        modo = decidir_ventilacao(i, leitura[4])
        energia += POTENCIAS_W[modo] * (INTERVALO_MIN/60)
        energia_continua += POTENCIAS_W[2] * (INTERVALO_MIN/60)

    return energia, energia_continua


""" -- FUNÇÕES DE EXIBIÇÃO -- """
def mostrar_medicoes():
    ponto = escolher_ponto()
    selecionadas = filtrar_por_ponto(LEITURAS, ponto)

    print('\n--- MEDIÇÕES (dados simulados) ---')
    n = 1
    for leitura in selecionadas:
        i = classificar(leitura[2])
        modo = decidir_ventilacao(i, leitura[4])

        if leitura[2] is None:
            temperatura = '---'
        else:
            temperatura = f'{leitura[2]:.1f} °C'

        if leitura[4]:
            movimento = 'sim'
        else:
            movimento = 'não'

        print(f'{n}. Ponto {leitura[0]} · {leitura[1]} · {temperatura} · {leitura[3]}% · movimento: {movimento}')
        print(f'   Estado: {ESTADOS[i]} | Ventilação: {VENTILACAO[modo]}')
        print(f'   {MENSAGENS[i]}')
        n += 1


def exibir_resumo(titulo, ponto):
    media, valor_maximo, hora_maximo, ponto_maximo, porcentagem_alerta, qtd_alerta, validas, falhas = calcular_resumo(LEITURAS, ponto)
    minutos = minutos_exposicao(filtrar_por_ponto(LEITURAS, ponto))
 
    print(f'\n-- {titulo} --')
    print(f'Média das temperaturas: {media:.1f} °C')
    print(f'Maior temperatura: {valor_maximo:.1f} °C (ponto {ponto_maximo}, {hora_maximo})')
    print(f'Leituras em alerta: {qtd_alerta} de {validas} ({porcentagem_alerta:.1f}%)')
    print(f'Minutos em calor elevado com demanda: {minutos} min')
    if falhas > 0:
        print(f'Leituras com falha (fora do cálculo): {falhas}')


def mostrar_resumo():
    print('\n--- RESUMO DAS CONDIÇÕES (dados simulados · 11:00 às 13:30) ---')
    print('Alerta = estados "Atenção" ou "Calor elevado"')
 
    for item in PONTOS:
        exibir_resumo(f'PONTO {item[0]} · {item[1]}', item[0])
 
    exibir_resumo('GERAL · TODOS OS PONTOS', 'T')


def mostrar_prioridade():
    print('\n--- RANKING EXPERIMENTAL DE PRIORIDADE ---')
    print('Prioridade = minutos de calor elevado com movimento × (1 + fator de infraestrutura)')
 
    # [pontuação, letra]: o sorted ordena pelo primeiro elemento
    ranking = []
    for item in PONTOS:
        ranking.append([calcular_prioridade(item[0]), item[0]])
    ranking = sorted(ranking, reverse=True)
 
    posicao = 1
    for item in ranking:
        letra = item[1]
        minutos = minutos_exposicao(filtrar_por_ponto(LEITURAS, letra))
        fator = buscar_fator(letra)
        print(f'{posicao}º - Ponto {letra}: {item[0]:.0f} pontos ({minutos} min × {1 + fator})')
        posicao += 1
 
    print(f'Ponto {ranking[0][1]} deve receber melhorias primeiro: combina mais tempo de calor com passageiros e menor proteção.')


def ranking_energia():
    print('\n--- ENERGIA ESTIMADA (dados simulados) ---')
    print('Automática: ventilação por demanda | Contínua: sempre no modo 2')
 
    for item in PONTOS:
        energia, energia_continua = estimar_energia(LEITURAS, item[0])
        economia = (energia_continua - energia) / energia_continua * 100
        print(f'Ponto {item[0]}: {energia:.1f} Wh (automática) x {energia_continua:.1f} Wh (contínua) · economia de {economia:.1f}%')


def simular_leitura():
    print('\n--- SIMULAR UMA LEITURA ---')
    print('Apenas demonstra a lógica: não altera os dados do projeto.')
 
    ponto = escolher_ponto()
    temp = ler_numero('Temperatura (°C): ', -10, 60)
    umid = ler_numero('Umidade (%): ', 0, 100)
    movim = ler_movimento()
 
    # Mesmo formato das leituras, sem horário
    simulacoes.append([ponto, 'sem horário', temp, umid, movim])
 
    i = classificar(temp)
    modo = decidir_ventilacao(i, movim)
    print(f'\nPonto {ponto} (simulação)')
    print(f'Estado: {ESTADOS[i]}')
    print(f'Ventilação: {VENTILACAO[modo]}')
    print(MENSAGENS[i])


""" -- MAIN() -- """
def main():
    while True:
        valor = menu()
        match valor:
            case '1':
                mostrar_medicoes()
            case '2':
                mostrar_resumo()
            case '3':
                mostrar_prioridade()
            case '4':
                ranking_energia()
            case '5':
                simular_leitura()
            case '0':
                print('Obrigada pela participação! Saindo...')
                break
            case _:
                print('Valor inválido! Tente novamente.')


if __name__ == "__main__":
    main()