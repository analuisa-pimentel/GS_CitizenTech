/* PONTOS ANALISADOS - PONTO FRESCO */

// Seleciona os três botões
const botoesPontos = document.querySelectorAll(".botao-ponto");

// Adiciona o evento de clique em cada botão
for (let i = 0; i < botoesPontos.length; i++) {
  // Associa a cada botão uma função executada quando ele for clicado.
  botoesPontos[i].addEventListener("click", function () {
    // Atualiza os dados do ponto selecionado
    mostrarPonto(this.value);

    // Remove a seleção anterior
    for (let j = 0; j < botoesPontos.length; j++) {
      // Retira a classe ativo, que controla o destaque visual do botão.
      botoesPontos[j].classList.remove("ativo");
      // Informa que este botão não está pressionado/selecionado para acessibilidade.
      botoesPontos[j].setAttribute("aria-pressed", "false");
    }

    // Adiciona a classe ativo somente ao botão que o usuário clicou.
    this.classList.add("ativo");
    // Informa que o botão clicado está selecionado para tecnologias assistivas.
    this.setAttribute("aria-pressed", "true");
  });
}

// Função responsável por atualizar os indicadores
function mostrarPonto(ponto) {
  // Guarda temporariamente o nome que aparecera no painel.
  let nome;
  // Guarda o endereço de referência do ponto escolhido.
  let endereco;
  // Guarda a descrição da cobertura do cenário.
  let cobertura;
  // Guarda a temperatura média simulada.
  let media;
  // Guarda a temperatura máxima simulada.
  let maxima;
  // Guarda a porcentagem de leituras em alerta.
  let alertas;
  // Guarda o índice experimental de prioridade.
  let prioridade;
  // Guarda o texto explicativo do ponto.
  let observacao;

  // Confere se o usuário selecionou o Ponto A.
  if (ponto === "A") {
    // Define o nome correspondente ao Ponto A.
    nome = "Ponto A";
    // Define o endereço usado como referência para o Ponto A.
    endereco = "Av. Pastor Martin Luther King, 98";
    // Indica que o cenário A foi modelado sem cobertura.
    cobertura = "Cenário: sem cobertura";
    // Define a média de temperatura simulada do Ponto A.
    media = "35,5 °C";
    // Define a temperatura máxima simulada do Ponto A.
    maxima = "37,1 °C";
    // Indica que todas as leituras válidas do Ponto A ficaram em alerta.
    alertas = "100%";
    // Define o índice de prioridade calculado para o Ponto A.
    prioridade = "180";

    // Inicia a atribuicao da observacao do Ponto A.
    observacao =
      // Registra a explicação dos resultados simulados para o Ponto A.
      "No cenário do Ponto A, todas as seis leituras válidas ficaram nas faixas de atenção ou calor elevado.";

    // Se não for o Ponto A, verifica se a opção selecionada foi B.
  } else if (ponto === "B") {
    // Define o nome correspondente ao Ponto B.
    nome = "Ponto B";
    // Define o endereço de referência do Ponto B.
    endereco = "Av. Dom Hélder Câmara, 3196";
    // Indica que o cenário B considera cobertura parcial.
    cobertura = "Cenário: cobertura parcial";
    // Define a média de temperatura simulada do Ponto B.
    media = "34,1 °C";
    // Define a temperatura máxima simulada do Ponto B.
    maxima = "36,3 °C";
    // Define a proporção de leituras válidas em alerta no Ponto B.
    alertas = "80%";
    // Define o índice de prioridade calculado para o Ponto B.
    prioridade = "90";

    // Inicia a atribuicao da observacao do Ponto B.
    observacao =
      // Explica que uma das leituras de B foi considerada inválida.
      "No cenário do Ponto B, quatro das cinco leituras válidas ficaram em alerta. Uma leitura foi considerada inválida.";

    // Se não for A nem B, verifica se a opção selecionada foi C.
  } else if (ponto === "C") {
    // Define o nome correspondente ao Ponto C.
    nome = "Ponto C";
    // Define o endereço de referência do Ponto C.
    endereco = "Estrada Adhemar Bebiano, 550";
    // Indica que o cenário C possui protecao e sombra.
    cobertura = "Cenário: protegido e sombreado";
    // Define a média de temperatura simulada do Ponto C.
    media = "32,0 °C";
    // Define a temperatura máxima simulada do Ponto C.
    maxima = "35,4 °C";
    // Define a proporção de leituras válidas em alerta no Ponto C.
    alertas = "50%";
    // Define o índice de prioridade calculado para o Ponto C.
    prioridade = "30";

    // Inicia a atribuicao da observacao do Ponto C.
    observacao =
      // Explica quantas leituras válidas do Ponto C ficaram em alerta.
      "No cenário do Ponto C, três das seis leituras válidas ficaram nas faixas de atenção ou calor elevado.";
  }

  // Procura no HTML o elemento ponto-nome e altera o texto com o nome selecionado.
  document.getElementById("ponto-nome").textContent = nome;
  // Atualiza no HTML o endereço de referência exibido.
  document.getElementById("ponto-endereco").textContent = endereco;
  // Atualiza no HTML a descrição da cobertura do cenário.
  document.getElementById("ponto-cobertura").textContent = cobertura;

  // Atualiza o indicador de temperatura média.
  document.getElementById("ponto-media").textContent = media;
  // Atualiza o indicador de temperatura máxima.
  document.getElementById("ponto-maxima").textContent = maxima;
  // Atualiza a porcentagem de leituras em alerta.
  document.getElementById("ponto-alertas").textContent = alertas;
  // Atualiza o índice experimental de prioridade.
  document.getElementById("ponto-prioridade").textContent = prioridade;

  // Atualiza a observacao explicativa do ponto selecionado.
  document.getElementById("ponto-observacao").textContent = observacao;
}
