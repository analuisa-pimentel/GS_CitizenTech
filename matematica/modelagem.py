"""
CITIZENTECH - PONTO FRESCO - MATEMÁTICA/CÁLCULO - DADOS SIMULADOS
Modelagem da temperatura ao longo do dia (função trigonométrica), dos períodos
de ventilação (inequação) e do consumo de energia (E = P x t).
"""

import numpy as np                 # função de temperatura; inequação; vetor de horas do dia
import matplotlib.pyplot as plt    # seção de gráficos
import os                          # criar a pasta dos gráficos

""" -- CONSTANTES -- """
PERIODO = 24
T_PICO = 14
LIMITE_ATENCAO = 30
LIMITE_ELEVADO = 35
POTENCIAS_W = [0, 10, 20]
INICIO_OPERACAO = 5
FIM_OPERACAO = 23
DT = 1/60
DEMANDAS = [1, 0.6]

# Cada cenário: [nome, M (média, °C), A (amplitude, °C)]
# Cenários SIMULADOS de dias de verão no Rio · não são medições
CENARIOS = [
    ['Dia ameno', 27, 4],         # mínima 23 °C, máxima 31 °C
    ['Dia quente', 30.5, 5.5],    # mínima 25 °C, máxima 36 °C
    ['Onda de calor', 32, 6],     # mínima 26 °C, máxima 38 °C
]

# CORES DA IDENTIDADE VISUAL DO PROJETO
AZUL_ESCURO = '#0B2E4F'
AZUL_TRANSPARENTE = '#0B2E4F33'
LARANJA = '#F28C28'

PASTA_GRAFICOS = 'graficos'

""" -- SEÇÃO DE CÁLCULOS (ANALÍTICO) -- """

def temperatura(t, M, A):
    return M + A * np.cos(2 * np.pi / PERIODO * (t - T_PICO))


def intervalo_acima(L, M, A):
    # Resolve T(t) >= L. Retorna: duração (h), início e fim (h)
    k = (L - M) / A
    if k >= 1:
        return 0, None, None      # o limiar nunca é atingido
    elif k <= -1:
        return 24, None, None     # acima do limiar o dia inteiro
    else:
        meio = (12 / np.pi) * np.arccos(k)
        return 2 * meio, T_PICO - meio, T_PICO + meio
                          # início          # fim


def formatar_hora(h):
    hora_inteira = int(h)
    minutos = round((h - int(h)) * 60)
    if minutos == 60:
        minutos = 0
        hora_inteira += 1
    return f'{hora_inteira:02d}:{minutos:02d}'


""" -- SEÇÃO DE SIMULAÇÃO (NUMÉRICO) -- """

def classificar(temp):
    if temp < LIMITE_ATENCAO:
        return 0
    elif temp < LIMITE_ELEVADO:
        return 1
    else:
        return 2


def decidir_ventilacao(estado, hora):
    if hora < INICIO_OPERACAO or hora >= FIM_OPERACAO or estado == 0:
        return 0
    elif estado == 1:
        return 1
    else:
        return 2


def simular_dia(M, A):
    horas = np.arange(0, 24, DT)
    temps = temperatura(horas, M, A)
    tempo_m1 = tempo_m2 = 0

    for i in range(len(horas)):
        estado = classificar(temps[i])
        modo = decidir_ventilacao(estado, horas[i])
        if modo == 1:
            tempo_m1 += DT
        elif modo == 2:
            tempo_m2 += DT

    return tempo_m1, tempo_m2


def energia(t_m1, t_m2, d):
    energia_demanda = d * (POTENCIAS_W[1] * t_m1 + POTENCIAS_W[2] * t_m2)
    energia_continua = POTENCIAS_W[2] * (FIM_OPERACAO - INICIO_OPERACAO)
    energia_economia = (energia_continua - energia_demanda) / energia_continua * 100

    return energia_demanda, energia_continua, energia_economia


def potencia_no_dia(M, A):
    # Potência da ventilação em cada minuto do dia (para o Gráfico 3)
    horas = np.arange(0, 24, DT)
    temps = temperatura(horas, M, A)
    potencias = []

    for i in range(len(horas)):
        estado = classificar(temps[i])
        modo = decidir_ventilacao(estado, horas[i])
        potencias.append(POTENCIAS_W[modo])

    return horas, potencias


""" -- SEÇÃO DE GRÁFICOS -- """

def configurar_grafico(titulo, rotulo_x, rotulo_y, eixo_horas=True):
    plt.title(titulo, color=AZUL_ESCURO, fontweight='bold')
    plt.xlabel(rotulo_x, color=AZUL_ESCURO)
    plt.ylabel(rotulo_y, color=AZUL_ESCURO)
    plt.grid(color=AZUL_TRANSPARENTE)
    plt.tick_params(colors=AZUL_ESCURO)
    if eixo_horas:
        plt.xticks(range(0, 25, 2))
        plt.xlim(0, 24)


def salvar_grafico(nome_arquivo):
    plt.legend()
    plt.savefig(f'{PASTA_GRAFICOS}/{nome_arquivo}', dpi=200, bbox_inches='tight')
    plt.close()


def grafico_cenarios():
    # Gráfico 1: temperatura ao longo do dia nos três cenários
    horas = np.arange(0, 24, DT)
    estilos = [':', '--', '-']    # ameno, quente, onda de calor

    plt.figure(figsize=(9, 5))
    for i in range(len(CENARIOS)):
        nome = CENARIOS[i][0]
        M = CENARIOS[i][1]
        A = CENARIOS[i][2]
        temps = temperatura(horas, M, A)
        plt.plot(horas, temps, color=AZUL_ESCURO, linestyle=estilos[i], linewidth=2, label=nome)

    plt.axhline(LIMITE_ATENCAO, color=LARANJA, linestyle='--', label='Limiar Atenção (30 °C)')
    plt.axhline(LIMITE_ELEVADO, color=LARANJA, linestyle='-.', label='Limiar Calor elevado (35 °C)')

    configurar_grafico('Temperatura ao longo do dia (cenários simulados)', 'Hora do dia (h)', 'Temperatura (°C)')
    salvar_grafico('1_temperatura_cenarios.png')


def grafico_onda_calor():
    # Gráfico 2: períodos de ventilação no cenário de onda de calor
    nome = CENARIOS[2][0]
    M = CENARIOS[2][1]
    A = CENARIOS[2][2]
    horas = np.arange(0, 24, DT)
    temps = temperatura(horas, M, A)

    plt.figure(figsize=(9, 5))
    plt.plot(horas, temps, color=AZUL_ESCURO, linewidth=2, label=nome)

    # Sombreia entre o limiar e a curva, só onde a condição do where é verdadeira
    plt.fill_between(horas, LIMITE_ATENCAO, temps,
                     where=(temps >= LIMITE_ATENCAO) & (temps < LIMITE_ELEVADO),
                     color=AZUL_TRANSPARENTE, label='Modo 1 (Atenção)')
    plt.fill_between(horas, LIMITE_ELEVADO, temps,
                     where=(temps >= LIMITE_ELEVADO),
                     color=AZUL_ESCURO, alpha=0.35, label='Modo 2 (Calor elevado)')

    plt.axhline(LIMITE_ATENCAO, color=LARANJA, linestyle='--', linewidth=1)
    plt.axhline(LIMITE_ELEVADO, color=LARANJA, linestyle='-.', linewidth=1)

    # Resultado analítico: início e fim do período acima de 35 °C
    duracao, inicio, fim = intervalo_acima(LIMITE_ELEVADO, M, A)
    plt.axvline(inicio, color=LARANJA, linestyle='--', linewidth=1.5,
                label=f'T ≥ 35 °C: {formatar_hora(inicio)} às {formatar_hora(fim)}')
    plt.axvline(fim, color=LARANJA, linestyle='--', linewidth=1.5)

    configurar_grafico('Onda de calor: períodos de ventilação (cenário simulado)', 'Hora do dia (h)', 'Temperatura (°C)')
    salvar_grafico('2_onda_calor_ventilacao.png')


def grafico_potencia():
    # Gráfico 3: potência ao longo do dia, sob demanda x contínua
    M = CENARIOS[2][1]
    A = CENARIOS[2][2]
    horas, potencias = potencia_no_dia(M, A)

    potencia_continua = []
    for h in horas:
        if INICIO_OPERACAO <= h < FIM_OPERACAO:
            potencia_continua.append(POTENCIAS_W[2])
        else:
            potencia_continua.append(0)

    plt.figure(figsize=(9, 5))
    plt.step(horas, potencia_continua, where='post', color=LARANJA, linewidth=1.5, linestyle='--', label='Contínua (sempre no Modo 2)')
    plt.step(horas, potencias, where='post', color=AZUL_ESCURO, linewidth=2, label='Sob demanda')
    plt.fill_between(horas, 0, potencias, step='post', color=AZUL_TRANSPARENTE)
    plt.ylim(0, 25)

    configurar_grafico('Potência da ventilação na onda de calor (cenário simulado)', 'Hora do dia (h)', 'Potência (W)')
    salvar_grafico('3_potencia_dia.png')


def grafico_energia():
    # Gráfico 4: energia por cenário (d = 1)
    nomes = []
    e_demanda = []
    e_continua = []
    economias = []
    for cenario in CENARIOS:
        t_m1, t_m2 = simular_dia(cenario[1], cenario[2])
        ed, ec, eco = energia(t_m1, t_m2, 1)
        nomes.append(cenario[0])
        e_demanda.append(ed)
        e_continua.append(ec)
        economias.append(eco)

    posicoes = np.arange(len(CENARIOS))

    plt.figure(figsize=(9, 5))
    plt.bar(posicoes - 0.2, e_demanda, width=0.4, color=AZUL_ESCURO, label='Sob demanda')
    plt.bar(posicoes + 0.2, e_continua, width=0.4, color=AZUL_TRANSPARENTE, edgecolor=AZUL_ESCURO, label='Contínua')

    for i in range(len(posicoes)):
        plt.text(posicoes[i] - 0.2, e_demanda[i] + 6, f'{e_demanda[i]:.0f} Wh', color=AZUL_ESCURO, ha='center')
        plt.text(posicoes[i], e_continua[i] + 22, f'economia {economias[i]:.1f}%', color=LARANJA, ha='center', fontweight='bold')

    plt.ylim(0, 480)
    configurar_grafico('Energia diária estimada (cenários simulados, d = 1)', 'Cenário', 'Energia (Wh)', eixo_horas=False)
    plt.xticks(posicoes, nomes)
    salvar_grafico('4_energia_cenarios.png')


def grafico_limiar():
    # Gráfico 5: duração acima do limiar em função do limiar escolhido
    limiares = np.arange(28, 38.05, 0.1)
    estilos = [':', '--', '-']

    plt.figure(figsize=(9, 5))
    for i in range(len(CENARIOS)):
        nome = CENARIOS[i][0]
        M = CENARIOS[i][1]
        A = CENARIOS[i][2]
        duracoes = []
        for L in limiares:
            duracao, inicio, fim = intervalo_acima(L, M, A)
            duracoes.append(duracao)
        plt.plot(limiares, duracoes, color=AZUL_ESCURO, linestyle=estilos[i], linewidth=2, label=nome)

    plt.axvline(LIMITE_ATENCAO, color=LARANJA, linestyle='--', label='Limiar Atenção (30 °C)')
    plt.axvline(LIMITE_ELEVADO, color=LARANJA, linestyle='-.', label='Limiar Calor elevado (35 °C)')

    configurar_grafico('Horas acima do limiar conforme o limiar escolhido (cenários simulados)',
                       'Limiar de acionamento (°C)', 'Horas acima do limiar (h)', eixo_horas=False)
    plt.xticks(range(28, 39, 1))
    salvar_grafico('5_efeito_limiar.png')


""" -- SEÇÃO DE RESULTADOS -- """

def mostrar_resultados(nome, M, A):
    print(f'\n--- {nome.upper()} (M = {M} °C, A = {A} °C) ---')
    print(f'Mínima: {M - A:.1f} °C às 02:00 | Máxima: {M + A:.1f} °C às 14:00')

    # Analítico
    d30, ini30, fim30 = intervalo_acima(LIMITE_ATENCAO, M, A)
    d35, ini35, fim35 = intervalo_acima(LIMITE_ELEVADO, M, A)
    for L, d, ini, fim in [[LIMITE_ATENCAO, d30, ini30, fim30], [LIMITE_ELEVADO, d35, ini35, fim35]]:
        if ini is None:
            if d == 0:
                print(f'T ≥ {L} °C: nunca atinge')
            else:
                print(f'T ≥ {L} °C: o dia inteiro')
        else:
            print(f'T ≥ {L} °C: das {formatar_hora(ini)} às {formatar_hora(fim)} ({d:.2f} h)')

    # Numérico x analítico
    t_m1, t_m2 = simular_dia(M, A)
    print(f'Modo 1 · analítico: {d30 - d35:.2f} h | numérico: {t_m1:.2f} h')
    print(f'Modo 2 · analítico: {d35:.2f} h | numérico: {t_m2:.2f} h')

    # Energia
    for d in DEMANDAS:
        ed, ec, eco = energia(t_m1, t_m2, d)
        print(f'Energia (d = {d}): {ed:.1f} Wh sob demanda x {ec:.1f} Wh contínua · economia de {eco:.1f}%')


""" -- MAIN -- """

def main():
    print('Modelagem Matemática · Ponto Fresco (cenários simulados)')
    for cenario in CENARIOS:
        nome = cenario[0]
        M = cenario[1]
        A = cenario[2]
        mostrar_resultados(nome, M, A)

    os.makedirs(PASTA_GRAFICOS, exist_ok=True)
    grafico_cenarios()
    grafico_onda_calor()
    grafico_potencia()
    grafico_energia()
    grafico_limiar()
    print(f'\nGráficos salvos na pasta "{PASTA_GRAFICOS}/".')


if __name__ == "__main__":
    main()