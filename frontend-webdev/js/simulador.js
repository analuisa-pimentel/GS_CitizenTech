/* SIMULADOR DO PONTO FRESCO */

// Executa a função quando o botão é clicado
document
  .getElementById("botao-simular")
  .addEventListener("click", simularFuncionamento);

function simularFuncionamento() {
  // Recebe os valores informados
  const valorTemperatura = document.getElementById("temperatura").value;

  const movimentoSelecionado = document.querySelector(
    'input[name="movimento"]:checked',
  );

  const temperatura = Number(valorTemperatura);

  // Elementos que serão atualizados
  const mensagemErro = document.getElementById("mensagem-erro");
  const statusSistema = document.getElementById("status-sistema");
  const caixaStatus = document.getElementById("resultado-simulacao");

  const resultadoTemperatura = document.getElementById("resultado-temperatura");
  const resultadoCondicao = document.getElementById("resultado-condicao");
  const resultadoMovimento = document.getElementById("resultado-movimento");
  const resultadoVentilacao = document.getElementById("resultado-ventilacao");

  mensagemErro.textContent = "";

  // Remove o estado visual da simulação anterior
  caixaStatus.classList.remove(
    "status-normal",
    "status-atencao",
    "status-calor",
    "status-sem-movimento",
  );

  // Campos que serão destacados em caso de erro
  const campoTemperatura = document.getElementById("temperatura");
  const grupoMovimento = document.querySelector(".grupo-movimento");

  // Remove os erros anteriores
  campoTemperatura.classList.remove("campo-erro");
  grupoMovimento.classList.remove("campo-erro");

  // Verifica cada campo separadamente
  const temperaturaInvalida =
    valorTemperatura.trim() === "" ||
    !Number.isFinite(temperatura) ||
    temperatura < 0 ||
    temperatura > 60;

  const movimentoInvalido = movimentoSelecionado === null;

  // Caso exista algum erro
  if (temperaturaInvalida || movimentoInvalido) {
    // Destaca o campo de temperatura
    if (temperaturaInvalida) {
      campoTemperatura.classList.add("campo-erro");
    }

    // Destaca o campo de movimento
    if (movimentoInvalido) {
      grupoMovimento.classList.add("campo-erro");
    }

    // Define a mensagem conforme o erro
    if (temperaturaInvalida && movimentoInvalido) {
      mensagemErro.textContent =
        "Informe uma temperatura entre 0 °C e 60 °C e selecione Sim ou Não.";
    } else if (temperaturaInvalida) {
      mensagemErro.textContent = "Informe uma temperatura entre 0 °C e 60 °C.";
    } else {
      mensagemErro.textContent = "Selecione Sim ou Não para o movimento.";
    }

    // Limpa os resultados anteriores
    statusSistema.textContent = "Aguardando dados válidos";

    resultadoTemperatura.textContent = "—";
    resultadoCondicao.textContent = "—";
    resultadoMovimento.textContent = "—";
    resultadoVentilacao.textContent = "—";

    return;
  }

  const movimento = movimentoSelecionado.value;

  let condicao;
  let ventilacao;
  let status;

  // Classificação da temperatura
  if (temperatura < 30) {
    condicao = "Normal";
  } else if (temperatura < 35) {
    condicao = "Atenção";
  } else {
    condicao = "Calor elevado";
  }

  // Decisão sobre a ventilação
  if (temperatura < 30) {
    ventilacao = "Desligada";
    status = "Condição normal — ventilação desligada";
  } else if (movimento === "nao") {
    ventilacao = "Desligada";
    status = "Sem movimento — ventilação desligada";
  } else if (temperatura < 35) {
    ventilacao = "Modo 1";
    status = "Ventilação acionada — modo 1";
  } else {
    ventilacao = "Modo 2";
    status = "Ventilação acionada — modo 2";
  }

  // Define a aparência do status
  if (temperatura < 30) {
    caixaStatus.classList.add("status-normal");
  } else if (movimento === "nao") {
    caixaStatus.classList.add("status-sem-movimento");
  } else if (temperatura < 35) {
    caixaStatus.classList.add("status-atencao");
  } else {
    caixaStatus.classList.add("status-calor");
  }

  // Atualiza o painel de resultados
  statusSistema.textContent = status;

  resultadoTemperatura.textContent = temperatura + " °C";
  resultadoCondicao.textContent = condicao;

  if (movimento === "sim") {
    resultadoMovimento.textContent = "Detectado";
  } else {
    resultadoMovimento.textContent = "Não detectado";
  }

  resultadoVentilacao.textContent = ventilacao;
}
