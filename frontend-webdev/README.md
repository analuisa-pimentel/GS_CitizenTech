# Ponto Fresco — Global Solution | Front-End Design e Web Development

## Sobre o Ponto Fresco

O Ponto Fresco é um projeto desenvolvido para pensar em como a tecnologia pode tornar a espera pelo ônibus mais protegida em dias de calor intenso.

Nossa proposta é um abrigo inteligente que combina cobertura para sombra, sensores e ventilação automática sob demanda. O projeto tem como foco a Zona Norte do Rio de Janeiro, e utilizamos três pontos de ônibus em Del Castilho e nas proximidades como referência para as análises.

## Integrantes

Projeto desenvolvido em dupla, por alunas de Engenharia de Software da FIAP:

- **Ana Luisa Rodrigues Pimentel** — RM576025
- **Anna Clara Camillo Rodrigues** — RM575371

## O que desenvolvemos?

**Página Início (`index.html`)**

- Apresentação do problema do calor nos pontos de ônibus e da proposta do Ponto Fresco.
- Cinco seções de conteúdo, além da apresentação inicial.
- Explicação do funcionamento do abrigo, com sombra, sensores e ventilação.
- Acesso às páginas de Simulador, Pontos analisados e Resultados pelo menu e pelos botões.

**Simulador — Fluxo 1 (`html/simulador.html`)**

- Campo para informar a temperatura e seleção de movimento detectado (Sim ou Não).
- Validação dos campos, com mensagens de erro e destaque visual.
- Classificação da temperatura em Normal (abaixo de 30 °C), Atenção (de 30 °C a menos de 35 °C) e Calor elevado (a partir de 35 °C).
- Simulação da ventilação desligada, em modo 1 ou em modo 2, de acordo com a temperatura e o movimento.
- Atualização do painel de resultados sem recarregar a página.

**Pontos analisados — Fluxo 2 (`html/pontos.html`)**

- Seleção entre três pontos de ônibus usados como referência no projeto.
- Exibição da temperatura média, temperatura máxima, percentual de leituras em alerta e índice experimental de prioridade.
- Atualização das informações ao selecionar outro ponto, sem recarregar a página.
- Comparação dos três cenários em um ranking de prioridade.

**Resultados — Fluxo 3 (`html/resultados.html`)**

- Apresentação de indicadores de economia energética estimada.
- Gráficos da modelagem matemática com cenários de temperatura e consumo de energia.
- Explicação dos resultados simulados e acesso à página dos pontos analisados.

**Modo claro e escuro**

- Alternância de tema nas quatro páginas, por um seletor no cabeçalho.
- Atualização das cores da interface com CSS e JavaScript.

## Tecnologias utilizadas

- HTML
- CSS
- JavaScript
- Git e GitHub

## Como visualizar o projeto

Basta baixar ou clonar o repositório e abrir o arquivo `frontend-webdev/index.html` no navegador. Se você estiver acessando apenas a pasta `frontend-webdev`, abra o `index.html` dentro dela.

Pelo menu superior ou pelos botões da página inicial, é possível acessar:

- **Simulador:** informar temperatura e movimento para testar a decisão de ventilação.
- **Pontos:** selecionar os cenários A, B e C e comparar os indicadores.
- **Impacto:** consultar os gráficos e resultados da modelagem matemática.

O projeto funciona diretamente no navegador, sem instalação de bibliotecas ou conexão com banco de dados.

## Importante

O Ponto Fresco é um protótipo acadêmico. Os valores de temperatura, movimento, consumo energético e prioridade apresentados são simulados e não representam medições feitas nos pontos de ônibus.

Os locais de Del Castilho e das proximidades foram escolhidos como referências territoriais. As condições de infraestrutura e os indicadores apresentados no site fazem parte dos cenários de análise, e não de um monitoramento em tempo real.

O simulador demonstra a decisão da ventilação para uma leitura informada pelo usuário. Ele não recebe dados de sensores físicos nem controla um abrigo instalado. O modo claro/escuro pode ser ativado em cada página, mas a preferência não é mantida automaticamente ao navegar para outra.

## Uso de Inteligência Artificial

Utilizamos o ChatGPT como apoio no planejamento das páginas, na organização do HTML, CSS e JavaScript, na revisão do código e na resolução de dúvidas durante o desenvolvimento. A representação visual conceitual do abrigo também contou com o uso de IA.

As informações sobre o uso de inteligência artificial no projeto serão detalhadas no arquivo [AI.md](AI.md).