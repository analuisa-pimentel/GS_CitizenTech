### FERRAMENTA: ChatGPT, da OpenAI | Novembro de 2026

**Disciplinas:** Front-End Design e Web Development — Global Solution CitizenTech 2026.2  
**Projeto:** Ponto Fresco — Abrigo Inteligente  
**Integrantes:** Ana Luisa Rodrigues Pimentel (RM576025) e Anna Clara Camillo Rodrigues (RM575371)

## PLANEJAMENTO DO SITE E ORGANIZAÇÃO DAS PÁGINAS

**Pedido consolidado (resumo de várias mensagens):** usamos os requisitos das disciplinas de Front-End Design e Web Development e o documento-base do Ponto Fresco para planejar um site único, que apresentasse o problema e a solução, tivesse cinco seções na landing page e oferecesse pelo menos duas interações em JavaScript, além do modo claro/escuro. Também pedimos que a implementação respeitasse o conteúdo estudado em aula, sem frameworks ou integrações externas.

**Resposta:** a IA ajudou a organizar a estrutura com quatro páginas:
1. `index.html` — apresentação do projeto, com cinco seções de conteúdo;
2. `simulador.html` — interação com temperatura e detecção de movimento;
3. `pontos.html` — comparação dos três pontos usados como referência;
4. `resultados.html` — indicadores e gráficos das simulações.

Também sugeriu separar os arquivos em pastas de HTML, CSS, JavaScript e imagens, com um cabeçalho e um rodapé padronizados.

**O que fizemos:** adotamos a estrutura de quatro páginas, unificamos as entregas das duas disciplinas e fomos construindo e testando cada parte antes de avançar para a seguinte.

---

## IDENTIDADE VISUAL E IMAGEM DO ABRIGO

**Mensagem**
> Vamos criar um prototipo de como seria o abrigo inteligente do Ponto Fresco para que eu possa utilizar no projeto

> Eu quero que você faça mais no estilo do primeiro, de ser um ponto realista. Mas eu quero que siga o nosso guia na parte que tenha a identidade visual

> Preciso apenas da foto, sem as infos e textos

> Remova o fundo branco, deixando em png

**Resposta:** a IA auxiliou na criação e nos ajustes de uma representação visual conceitual do abrigo, incluindo sua cobertura, o painel solar e a aplicação da identidade do Ponto Fresco. Também orientou a utilização da imagem sem fundo na página inicial.

**O que fizemos:** escolhemos a representação que mais combinava com o projeto, pedimos mudanças na imagem e usamos a versão com fundo transparente no `index.html`. A identidade visual seguida no site já havia sido definida e aprovada por nós, incluindo a marca Ponto Fresco, o descritor “Abrigo Inteligente”, as cores e as fontes Sora e Inter.

---

## CONSTRUÇÃO E AJUSTES DA LANDING PAGE

**Pedido consolidado (resumo de várias mensagens):** desenvolver a página inicial seguindo nossa identidade visual, com uma apresentação do abrigo e cinco seções que explicassem o problema, a solução, o simulador, os pontos analisados e os resultados. Ao longo da construção, pedimos mudanças de tamanho, espaçamento e organização para evitar informações repetidas ou elementos visualmente exagerados.

**Resposta:** a IA sugeriu estruturas de HTML e regras de CSS para o hero, os cartões, os botões de navegação, as seções e o rodapé. Também orientou o uso da imagem do abrigo ao lado do texto principal e a criação de links para as outras páginas.

**O que fizemos:** avaliamos a aparência no navegador, enviamos capturas de tela e ajustamos os componentes até chegar ao layout aprovado. Mantivemos as cinco seções exigidas no Front-End, além da área inicial de destaque.

---

## SIMULADOR DE TEMPERATURA E VENTILAÇÃO

**Pedido consolidado (resumo de várias mensagens):** criar uma página em que a pessoa informa a temperatura e seleciona se existe movimento no abrigo. O sistema deve validar os dados, classificar a condição térmica e mostrar a decisão da ventilação, usando as mesmas regras definidas para o projeto nas outras disciplinas.

**Resposta:** a IA forneceu sugestões de HTML, CSS e JavaScript para:
1. ler a temperatura e a opção de movimento;
2. verificar campos vazios e temperaturas fora da faixa de entrada do protótipo;
3. classificar temperaturas abaixo de 30 °C como **Normal**, de 30 °C a menos de 35 °C como **Atenção** e a partir de 35 °C como **Calor elevado**;
4. manter a ventilação desligada quando não houver movimento; com movimento, utilizar modo 1 na faixa de Atenção e modo 2 em Calor elevado;
5. atualizar o resultado na própria página, sem recarregá-la;
6. apresentar mensagens de erro e estados visuais diferentes.

**O que fizemos:** aplicamos e testamos o simulador, incluindo cenários de erro, navegação por teclado e as faixas de temperatura. A página representa uma decisão pontual com dados informados pelo usuário: não consulta sensores físicos, não cria registros de monitoramento e não implementa temporizador de inatividade.

---

## COMPARAÇÃO DOS TRÊS PONTOS ANALISADOS

**Pedido consolidado (resumo de várias mensagens):** mostrar os pontos A, B e C em uma página comparativa, permitindo escolher um deles e visualizar seus indicadores, além de apresentar um ranking de prioridade. Os dados precisavam estar de acordo com o trabalho de Python e com a proposta do Ponto Fresco.

**Resposta:** a IA orientou a criação dos três botões de seleção, dos campos de informação atualizados pelo JavaScript e de um ranking visual. O código do `pontos.js` utiliza eventos de clique, condicionais e `textContent` para modificar o conteúdo exibido, sem carregar outra página.

**O que fizemos:** testamos a seleção dos três pontos e mantivemos os dados como cenários simulados. Os endereços são referências territoriais, mas as temperaturas, condições de cobertura, percentuais e índices de prioridade não correspondem a medições reais nesses locais.

---

## RESULTADOS E GRÁFICOS DA MODELAGEM MATEMÁTICA

**Pedido consolidado (resumo de várias mensagens):** criar a página de resultados com os indicadores de economia de energia e os gráficos que já tinham sido produzidos na parte de Matemática, sem gerar números novos ou criar uma biblioteca de gráficos em JavaScript.

**Resposta:** a IA sugeriu cartões com os três percentuais de economia energética estimada (84,7%, 51,8% e 37,2%) e a inclusão das imagens dos gráficos de consumo de energia e temperatura. Também forneceu ajustes de CSS para controlar o tamanho das imagens.

**O que fizemos:** inserimos os gráficos já existentes, ajustamos suas dimensões e centralização depois de conferir a página no navegador e comparamos os números apresentados com os trabalhos de Python e Matemática. A página exibe resultados de simulações, não dados coletados em tempo real.

---

## MODO CLARO E ESCURO

**Mensagem**
> Ainda não fiz a parte do modo claro/escuro, na questão do botão que vai ativar dá para fazer algo no estilo da foto? Ou seria conteudo alem do que aprendi?

**Resposta:** a IA propôs um seletor com símbolos de sol e lua, construído com HTML e CSS, e um arquivo `tema.js` compartilhado entre as quatro páginas. A mudança de cores utiliza `classList.toggle()`, `if/else` e classes CSS aplicadas ao `body`.

**AJUSTES VISUAIS**

Após testar no navegador, percebemos que o seletor estava maior e menos alinhado do que gostaríamos. Pedimos ajustes no tamanho, na posição e no espaçamento. Também identificamos que uma diferença visual no Simulador era causada pelo zoom do navegador, não pelo CSS.

**O que fizemos:** diminuímos e alinhamos o seletor ao menu, removemos a regra desnecessária de margem e testamos os temas nas quatro páginas. Não utilizamos `localStorage`: a escolha do tema não fica salva ao navegar para outra página.

---

## REVISÃO FINAL DO HTML, CSS E JAVASCRIPT

**Mensagem**
> Já fiz a limpeza do bloco duplicado e fiz o pequeno ajuste na linha 720 e 731 do css, testei a responsividade em todos os tamanhos sugeridos, fiz a comparação dos valores de python e matematica.

**Resposta:** a IA analisou os arquivos ZIP do projeto e apontou pequenos ajustes, como a remoção de um bloco CSS duplicado no Simulador e a aplicação de um seletor mais específico para o campo numérico. Também organizou testes de navegação, funcionamento das interações e responsividade.

**O que fizemos:** corrigimos os trechos indicados, conferimos a responsividade nas larguras de 375 px, 768 px e 1366 px e comparamos os valores do site com os materiais de Python e Matemática. Mantivemos as páginas e funcionalidades que já estavam funcionando, sem reconstruir partes desnecessariamente.

**COMENTÁRIOS EXPLICATIVOS NOS ARQUIVOS JS**

> Ok, alteração feita. Antes de fazermos o AI.md, quero colocar comentarios do que cada linha do js faz, igual o professor de web pediu num trabalho que fizemos anteriormente

**Resposta:** a IA acrescentou comentários explicativos nos arquivos `simulador.js`, `pontos.js` e `tema.js`, explicando instruções como eventos de clique, condicionais, validações, alterações no DOM, atributos de acessibilidade e `preventDefault()`.

**O que fizemos:** solicitamos que a lógica original fosse preservada, para facilitar a leitura e a explicação do código sem acrescentar funcionalidades novas.

---

## OBSERVAÇÃO SOBRE O USO DA IA

A IA foi utilizada para sugerir estruturas, fornecer e explicar trechos de HTML, CSS e JavaScript, apoiar a criação da imagem conceitual do abrigo, ajudar na identificação de erros e revisar a documentação. A dupla definiu o escopo, escolheu a identidade visual, avaliou as sugestões, integrou os arquivos, testou as páginas e decidiu quais ajustes manter.

Os indicadores exibidos são provenientes das simulações acadêmicas do projeto. O site não está integrado a sensores reais ou a um banco de dados.

Este registro reúne os principais pedidos relacionados à entrega conjunta de **Front-End Design e Web Development**. Não documenta os prompts utilizados separadamente no desenvolvimento do programa de Python.
