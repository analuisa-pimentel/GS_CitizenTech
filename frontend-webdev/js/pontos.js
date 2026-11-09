/* PONTOS ANALISADOS - PONTO FRESCO */

// Seleciona os três botões
const botoesPontos = document.querySelectorAll(".botao-ponto");

// Adiciona o evento de clique em cada botão
for (let i = 0; i < botoesPontos.length; i++) {
  botoesPontos[i].addEventListener("click", function () {
    // Atualiza os dados do ponto selecionado
    mostrarPonto(this.value);

    // Remove a seleção anterior
    for (let j = 0; j < botoesPontos.length; j++) {
      botoesPontos[j].classList.remove("ativo");
      botoesPontos[j].setAttribute("aria-pressed", "false");
    }

    // Destaca o botão selecionado
    this.classList.add("ativo");
    this.setAttribute("aria-pressed", "true");
  });
}

// Função responsável por atualizar os indicadores
function mostrarPonto(ponto) {
  let nome;
  let endereco;
  let cobertura;
  let media;
  let maxima;
  let alertas;
  let prioridade;
  let observacao;

  // Dados simulados de cada ponto
  if (ponto === "A") {
    nome = "Ponto A";
    endereco = "Av. Pastor Martin Luther King, 98";
    cobertura = "Cenário: sem cobertura";
    media = "35,5 °C";
    maxima = "37,1 °C";
    alertas = "100%";
    prioridade = "180";

    observacao =
      "No cenário do Ponto A, todas as seis leituras válidas ficaram nas faixas de atenção ou calor elevado.";
  } else if (ponto === "B") {
    nome = "Ponto B";
    endereco = "Av. Dom Hélder Câmara, 3196";
    cobertura = "Cenário: cobertura parcial";
    media = "34,1 °C";
    maxima = "36,3 °C";
    alertas = "80%";
    prioridade = "90";

    observacao =
      "No cenário do Ponto B, quatro das cinco leituras válidas ficaram em alerta. Uma leitura foi considerada inválida.";
  } else if (ponto === "C") {
    nome = "Ponto C";
    endereco = "Estrada Adhemar Bebiano, 550";
    cobertura = "Cenário: protegido e sombreado";
    media = "32,0 °C";
    maxima = "35,4 °C";
    alertas = "50%";
    prioridade = "30";

    observacao =
      "No cenário do Ponto C, três das seis leituras válidas ficaram nas faixas de atenção ou calor elevado.";
  }

  // Atualiza as informações no HTML
  document.getElementById("ponto-nome").textContent = nome;
  document.getElementById("ponto-endereco").textContent = endereco;
  document.getElementById("ponto-cobertura").textContent = cobertura;

  document.getElementById("ponto-media").textContent = media;
  document.getElementById("ponto-maxima").textContent = maxima;
  document.getElementById("ponto-alertas").textContent = alertas;
  document.getElementById("ponto-prioridade").textContent = prioridade;

  document.getElementById("ponto-observacao").textContent = observacao;
}
