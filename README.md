# Ponto Fresco Ativo

**Global Solution 2026.2 · FIAP · CitizenTech** · Engenharia de Software, 1º ano

Abrigos inteligentes para tornar a espera pelo ônibus mais protegida do calor e orientar melhorias nos pontos de ônibus da Zona Norte do Rio.

## Ficha da CitizenTech

| Campo | Definição |
|---|---|
| **Nome da CitizenTech** | Ponto Fresco Ativo |
| **Cidade e bairro** | Rio de Janeiro · Del Castilho, Zona Norte |
| **Cidadão beneficiado** | Passageiros de ônibus que esperam o transporte expostos ao calor e têm pouca alternativa a essa espera, especialmente trabalhadores, idosos e pessoas com mobilidade reduzida |
| **Problema, em uma frase** | Passageiros esperam ônibus sob calor intenso em pontos com pouca proteção, e faltam uma proteção que funcione na hora certa e dados para decidir quais pontos melhorar primeiro |
| **Como funciona** | Um abrigo com sombra e sensores de temperatura, umidade e movimento: quando há calor e passageiros esperando, a ventilação liga sozinha, sem precisar de celular ou internet. Os dados de cada ponto mostram onde a cidade deve investir primeiro |
| **O que cada parte faz** | Sensor e circuito decidem e acionam a ventilação no abrigo; programa em Python analisa as leituras e ordena os pontos por prioridade; site apresenta a solução e simula seu funcionamento; matemática estima o calor ao longo do dia e a energia gasta (detalhes por disciplina abaixo) |
| **Link do repositório** | `https://github.com/analuisa-pimentel/GS_CitizenTech/` |
| **Indicador de impacto** | Minutos de calor com passageiros esperando em cada ponto, energia economizada pela ventilação sob demanda e compreensão dos avisos pelos usuários |
| **ODS conectados** | 11 · Cidades e comunidades sustentáveis · 13 · Ação contra a mudança do clima · 10 · Redução das desigualdades · 3 · Saúde e bem-estar |

**Quem participa do ecossistema:** passageiros e moradores, Prefeitura, concessionária de mobiliário urbano, equipes técnicas de manutenção, órgãos e iniciativas sobre calor (SMAC, COR) e universidades.

> Todos os dados usados nos protótipos são simulados. As faixas de temperatura são valores experimentais da equipe e não equivalem aos níveis oficiais de calor do COR.

## O projeto em cada disciplina

### Edge Computing & Computer Systems
Circuito no Wokwi com ESP32, sensor de temperatura e umidade (DHT22) e sensor de movimento (PIR). Classifica o calor em Normal, Atenção e Calor elevado, aciona a ventilação no modo correspondente quando há passageiros, sinaliza o estado com LEDs e trata falhas do sensor.
📁 [`edge/`](edge/)

### Computational Thinking with Python
Programa de terminal que analisa leituras simuladas de três pontos de ônibus, classifica cada leitura, decide o modo da ventilação, calcula média, maior temperatura e % em alerta, estima a energia e monta um ranking experimental de prioridade.
📁 [`python/`](python/)

### Matemática
Modelagem da temperatura ao longo do dia com uma função senoidal, estimativa do tempo de ventilação e da energia (E = P × t) e comparação entre ventilação sob demanda e contínua.
📁 [`matematica/`](matematica/)

### Front-End Design
Landing page em HTML e CSS que apresenta o problema do calor nos pontos de ônibus, a solução, o funcionamento e o impacto esperado.
📁 [`site/`](site/)

### Web Development
Interações em JavaScript na mesma página: simulador de temperatura e movimento com a mesma regra do circuito e do Python, ranking dos pontos simulados e modo claro/escuro.
📁 [`site/`](site/)

### Software & Total Experience Design
Escopo da solução, jornada do passageiro e do gestor público, requisitos funcionais, não funcionais e regras de negócio, e backlog com histórias de usuário priorizadas.
📁 [`software-tx/`](software-tx/)

### Storytelling
Videopitch de até 3 minutos que apresenta o problema, a solução, o ecossistema, o impacto e o protótipo funcionando.
🎬 [Link do vídeo](https://link-do-video)

## Equipe

| Nome completo | RM |
|---|---|
| Ana Luisa Rodrigues Pimentel | RM576025 |
| Anna Clara Camillo Rodrigues | RM575371 |
