# Uso de IA · Matemática (Differentiated Problem Solving)

**Projeto:** Ponto Fresco · Global Solution 2026.2 · FIAP CitizenTech
**Ferramenta:** Claude (Anthropic)
**Período:** novembro de 2026
**Equipe:** Ana Luisa Rodrigues Pimentel (RM576025) · Anna Clara Camillo Rodrigues (RM575371)

A IA foi usada como apoio na escolha e justificativa do modelo matemático, na estruturação e revisão do código (`modelagem.py`) e na redação do relatório técnico em PDF. Os prompts abaixo estão transcritos como foram enviados; as respostas estão resumidas.

---

## DEFINIÇÃO E GERAÇÃO DO PROBLEMA

> agora de acordo com o programa feito em python e o nosso documento base para o projeto/solução, precisamos montar a parte/entrega de matemática do projeto, anexei as 2 fotos disponibilizadas para os estudantes esclarecendo o que precisamos fazer nesta parte (já tenho salvo no meu vs code alguns exemplo de como gerar equações, inequações, expressões e funções de 1,2 e 3 grau, além da parte de geração de gráficos, mas podemos escolher outro tipo de função também); Pra começar, precisamos Escolher e justificar uma função matemática (pensei em função trigonométrica para representar a variação térmica ao longo do dia, mas aceito outras ideias também), Definir variáveis, parâmetros e hipóteses (explicar temperatura, tempo, amplitude, período e o que a função não representa), Criar o código .py da modelagem (Implementar cálculos e simulações numéricas coerentes com o Ponto Fresco), Gerar gráficos legíveis (mostrar a curva da temperatura e o comportamento para diferentes cenários),  Analisar o tempo de ventilação (relacionar limiar de acionamento aos períodos de uso simulados), Comparar consumo energético estimado (Usar E = potência × tempo e comparar ventilação contínua e sob demanda), Interpretar os resultados e limites (explicar o que os gráficos mostram sem apresentar dados simulados como medições reais), preparar o relatório técnico em PDF (Incluir problema, modelo escolhido, gráficos, resultados e interpretação)

**Resposta:** a IA confirmou a escolha da função trigonométrica e propôs o modelo completo: função cosseno com período de 24 h e pico às 14h, variáveis, parâmetros, hipóteses, o que o modelo não representa e três cenários de dia (ameno, quente e onda de calor). Também resolveu a inequação T(t) ≥ L, definiu a comparação de energia entre ventilação sob demanda e contínua, calculou os resultados esperados para conferirmos depois e sugeriu os gráficos e a estrutura do relatório.

> não, primeiro monta o pdf base com tudo isso, depois vamos para o código e posteriormente com o código pronto você vai revisar o pdf novamente

**Resposta:** a IA montou o PDF base do relatório com o modelo, as hipóteses, o desenvolvimento analítico, as tabelas de resultados marcadas como preliminares e espaços reservados para os gráficos, que seriam gerados pelo nosso código.

---

## DEFINIÇÃO E DESENVOLVIMENTO DO CÓDIGO

> beleza, agora de acordo com isso, me ajude a saber estruturar o código, sem montar pra mim, mas me dizendo quais bibliotecas eu vou chamar no começo do código e quando irei usar elas, como estruturar o calculo de uma função trigonometrica em python e quais cenários meu código precisa calcular, por último vamos fazer a geração dos gráficos de acordo com a identidade visual do nosso projeto (valores e linhas em azul escuro, grade em um azul mais transparente, linha dos valores de resultado em laranja), me ajude a montar o esqueleto/ordem do projeto; a gente vai dividir um arquivo pra cada coisa (cálculos, simulações e gráficos) ou deixar tudo no mesmo?

**Resposta:** a IA recomendou um arquivo único dividido em seções e explicou quais bibliotecas usar (numpy e matplotlib) e quando, os cuidados com radianos e com o domínio do `arccos`, o que o código precisava calcular em cada cenário, os comandos do matplotlib para cada tipo de gráfico e a ordem do arquivo. O código ficou sob minha responsabilidade.

> ok, estruturei o esqueleto do arquivo py de acordo com isso então da seguinte forma: cabeçalho -> imports -> constantes -> seção de cálculos (analítico) -> seção de simulação (numérico) -> seção de gráficos -> seção de resultados -> main; agora de acordo com isso, me diz o que eu preciso incluir dentro de cada função, o que ela deve fazer/retornar especificamente, e quais ferramentas devo usar para cada uma; lembrando que precisa abranger os conhecimentos aprendidos nessa matéria: lidar com funções/expressões matemáticas de forma computacional que retornem resultados reais e mostrá-los em gráfico, tudo em python (em constantes, preciso que vc gere alguns cenários pra mim, e me ensine como declarar as cores nele)

**Resposta:** a IA escreveu o bloco de constantes com a lista `CENARIOS` e as cores da identidade visual, explicou como declarar cores com transparência em hexadecimal e descreveu cada função na ordem do esqueleto: o que recebe, o que faz, o que retorna, as ferramentas e um teste para conferir. Com essa orientação, escrevi as funções de cálculo, simulação e energia.

---

## REVISÃO DO CÓDIGO, DÚVIDAS E REFINAMENTO

> ok, fiz tudo que eu consegui do código e colei aqui, as funções estão feitas, por favor revise elas, veja se tem algum erro e me avise se necessário, como aplicar a fórmula trigonométrica do modelo em python na função temperatura(t, M, A)? não entendi como fazer a fórmula potencia_no_dia(M, A); moneti a função de configurar gráfico, mas ainda nn entendi como os dados vão vim pra ca exatamente, invés de x e y eu deveria usar M e A no caso? 

**Resposta:** a IA apontou os erros do código (erro de digitação no import do matplotlib, uso desnecessário do sympy, retorno errado no `intervalo_acima`, conflito de nome entre a função `temperatura` e o parâmetro do `classificar`, índice no lugar da temperatura no `simular_dia` e parênteses errados no cálculo da economia), mostrou como escrever a fórmula da `temperatura` em Python, explicou a lógica do `potencia_no_dia` e como os dados chegam aos gráficos pelo `plt.plot(x, y)`. Também mostrou o primeiro gráfico completo como modelo e os comandos principais dos outros. Corrigi o que consegui a partir dessas explicações.

> revise a nova versão do meu código completa, ajustando o que ainda estiver errado e me explicando quais foram as mudanças; além disso, me ajuda a montar a seção de gráficos diretamente no código, preenchendo as funções que determinei mas não consegui terminar de preencher, essa foi a única parte que tive dúvida ao aplicar as ferramentas e escopo sugerido

**Resposta:** a IA devolveu o `modelagem.py` corrigido e completo. Corrigiu os erros que ainda restavam (sympy ainda presente, parâmetro inválido no `decidir_ventilacao`, linha que sobrescrevia a função `temperatura` no `simular_dia` e no `potencia_no_dia`, textos fixos no `configurar_grafico`), escreveu a seção de gráficos (os cinco gráficos) e as funções `potencia_no_dia`, `salvar_grafico` e `mostrar_resultados`, rodou o código e conferiu que os resultados batiam com o relatório. Revisei cada função para entender os comandos usados.

---

## RELATÓRIO TÉCNICO FINAL

> agora de acordo com o código final completo, o resultado da execução, o print do terminal pós rodar o programa, os prints enviados dos graficos e o pdf base que tínhamos com o que planejavamos incluir no programa, revise o pdf e faça as mudanças necessárias para se enquadrar na nossa versão final e sólida, com suas devidas explicações (pode incluir a imagem dos gráficos, explicando os resultados encontrados em cada um), lembrando que esses eram os requisitos entregáveis desta matéria: " Código-fonte dos cálculos, simulações e gráficos (.py). Relatório Técnico em PDF (.pdf) contendo descrição do problema, modelo matemático, gráficos gerados e interpretação dos resultados. "

**Resposta:** a IA atualizou o PDF com os resultados da execução, inseriu os gráficos gerados pelo nosso código com a interpretação de cada um, acrescentou a comparação entre o método analítico e o numérico e atualizou a descrição do código. Também sugeriu trocar `plt.ylim(0, 420)` por `plt.ylim(0, 480)` no Gráfico 4, porque a legenda cobria o texto da economia. Apliquei a mudança no código.

---

## REVISÃO DO PROMPTS.MD

> sobre a parte do uso de IA, eu fiz o arquivo prompts.md separado do pdf, pode revisar o que vc acha dele? pensei em deixar o resumo geral sobre uso da IA no pdf igual já está, e deixar a conversa mais detalhada no prompts.md passando por cada parte do projeto que montamos junto
