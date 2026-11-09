/* SIMULADOR DO PONTO FRESCO */

// Executa a função quando o botão é clicado
document
  // Localiza o botão que possui o id botao-simular.
  .getElementById("botao-simular")
  // Quando o botão for clicado, executa a função simularFuncionamento.
  .addEventListener("click", simularFuncionamento);

// Localiza o formulário pelo id form-simulador e começa a configurar um evento.
document.getElementById("form-simulador").addEventListener(
  // O evento submit acontece ao enviar o formulário, inclusive com Enter.
  "submit",
  // Cria a função que será executada quando ocorrer esse evento.
  function (evento) {
    // Impede o envio tradicional do formulário e o recarregamento da página.
    evento.preventDefault();
    // Executa a mesma simulação que é iniciada pelo clique no botão.
    simularFuncionamento();
  },
);

// Declara a função principal que valida as entradas e decide a ventilação.
function simularFuncionamento() {
  // Recebe os valores informados
  // Lê o texto digitado no campo de temperatura.
  const valorTemperatura = document.getElementById("temperatura").value;

  // Procura qual das duas opções de movimento está marcada.
  const movimentoSelecionado = document.querySelector(
    // Seleciona somente o input de movimento que estiver checked.
    'input[name="movimento"]:checked',
  );

  // Converte o valor digitado de texto para número, permitindo comparações.
  const temperatura = Number(valorTemperatura);

  // Guarda o elemento que mostra mensagens de erro do formulário.
  const mensagemErro = document.getElementById("mensagem-erro");
  // Guarda o elemento que mostra o status geral da simulação.
  const statusSistema = document.getElementById("status-sistema");
  // Guarda a caixa do resultado para atualizar suas classes de cor.
  const caixaStatus = document.getElementById("resultado-simulacao");

  // Guarda o elemento que mostrará a temperatura informada.
  const resultadoTemperatura = document.getElementById("resultado-temperatura");
  // Guarda o elemento que mostrará a faixa térmica identificada.
  const resultadoCondicao = document.getElementById("resultado-condicao");
  // Guarda o elemento que mostrará se houve movimento.
  const resultadoMovimento = document.getElementById("resultado-movimento");
  // Guarda o elemento que mostrará o modo da ventilação.
  const resultadoVentilacao = document.getElementById("resultado-ventilacao");

  // Apaga eventual mensagem de erro exibida na simulação anterior.
  mensagemErro.textContent = "";

  // Começa a remover as classes de status que podem ter ficado da última simulação.
  caixaStatus.classList.remove(
    // Remove a classe visual usada para temperatura normal.
    "status-normal",
    // Remove a classe visual usada para a faixa de atenção.
    "status-atencao",
    // Remove a classe visual usada para calor elevado.
    "status-calor",
    // Remove a classe visual usada quando não há movimento.
    "status-sem-movimento",
  );

  // Guarda o campo de temperatura para destacar erros, se necessário.
  const campoTemperatura = document.getElementById("temperatura");
  // Guarda o grupo de opções de movimento para destacar erros.
  const grupoMovimento = document.querySelector(".grupo-movimento");

  // Retira a borda de erro da temperatura antes de uma nova validação.
  campoTemperatura.classList.remove("campo-erro");
  // Retira o destaque de erro do movimento antes de uma nova validação.
  grupoMovimento.classList.remove("campo-erro");

  // Cria uma variável booleana que indica se a temperatura é inválida.
  const temperaturaInvalida =
    // Considera inválido deixar o campo vazio ou preenchido só com espaços.
    valorTemperatura.trim() === "" ||
    // Considera inválido um valor que não seja um número finito.
    !Number.isFinite(temperatura) ||
    // Não aceita temperaturas abaixo de 0 graus no formulário.
    temperatura < 0 ||
    // Não aceita temperaturas acima de 60 graus no formulário.
    temperatura > 60;

  // Verifica se o usuário deixou as duas opções de movimento desmarcadas.
  const movimentoInvalido = movimentoSelecionado === null;

  // Entra no bloco de erro quando pelo menos um dos dois campos é inválido.
  if (temperaturaInvalida || movimentoInvalido) {
    // Destaca o campo de temperatura
    // Confere especificamente se o erro está no campo de temperatura.
    if (temperaturaInvalida) {
      // Adiciona a classe campo-erro para destacar a temperatura no CSS.
      campoTemperatura.classList.add("campo-erro");
    }

    // Confere especificamente se o erro está na seleção de movimento.
    if (movimentoInvalido) {
      // Destaca o grupo de movimento usando a classe campo-erro.
      grupoMovimento.classList.add("campo-erro");
    }

    // Verifica se os dois campos apresentam erro ao mesmo tempo.
    if (temperaturaInvalida && movimentoInvalido) {
      // Começa a definir a mensagem de erro mostrada ao usuário.
      mensagemErro.textContent =
        // Exibe uma mensagem solicitando as duas informações obrigatorias.
        "Informe uma temperatura entre 0 °C e 60 °C e selecione Sim ou Não.";
      // Se apenas a temperatura estiver inválida, entra neste caso.
    } else if (temperaturaInvalida) {
      // Exibe uma mensagem solicitando temperatura dentro do intervalo permitido.
      mensagemErro.textContent = "Informe uma temperatura entre 0 °C e 60 °C.";
      // Se a temperatura estiver valida, resta o erro na seleção de movimento.
    } else {
      // Exibe uma mensagem pedindo que o usuário selecione Sim ou Não.
      mensagemErro.textContent = "Selecione Sim ou Não para o movimento.";
    }

    // Substitui o status antigo por um aviso de dados invalidos.
    statusSistema.textContent = "Aguardando dados válidos";

    // Limpa a temperatura do resultado anterior, mostrando um traço.
    resultadoTemperatura.textContent = "—";
    // Limpa a condicao do resultado anterior.
    resultadoCondicao.textContent = "—";
    // Limpa a informação de movimento do resultado anterior.
    resultadoMovimento.textContent = "—";
    // Limpa a ventilação do resultado anterior.
    resultadoVentilacao.textContent = "—";

    // Encerra a função agora para não calcular com dados invalidos.
    return;
  }

  // Obtem o valor da opção selecionada: sim ou não.
  const movimento = movimentoSelecionado.value;

  // Reserva uma variável para a classificação da temperatura.
  let condicao;
  // Reserva uma variável para o modo de ventilação.
  let ventilacao;
  // Reserva uma variável para a mensagem geral de status.
  let status;

  // Verifica se a temperatura está abaixo de 30 graus.
  if (temperatura < 30) {
    // Classifica temperaturas abaixo de 30 graus como Normal.
    condicao = "Normal";
    // Se não for Normal, verifica se está abaixo de 35 graus.
  } else if (temperatura < 35) {
    // Classifica temperaturas de 30 até menos de 35 graus como Atenção.
    condicao = "Atenção";
    // Se chegou aqui, a temperatura é de pelo menos 35 graus.
  } else {
    // Classifica temperaturas de 35 graus ou mais como Calor elevado.
    condicao = "Calor elevado";
  }

  // Primeiro verifica se a temperatura é Normal, independente de movimento.
  if (temperatura < 30) {
    // Mantem a ventilação desligada quando não há necessidade térmica.
    ventilacao = "Desligada";
    // Define a mensagem explicando o desligamento por temperatura normal.
    status = "Condição normal — ventilação desligada";
    // Caso esteja quente, verifica se não foi detectado movimento.
  } else if (movimento === "nao") {
    // Desliga a ventilação porque não há movimento detectado.
    ventilacao = "Desligada";
    // Define a mensagem que explica o desligamento por falta de movimento.
    status = "Sem movimento — ventilação desligada";
    // Com movimento detectado, verifica se a temperatura e menor que 35 graus.
  } else if (temperatura < 35) {
    // Ativa o Modo 1 para temperaturas de Atenção com movimento.
    ventilacao = "Modo 1";
    // Define a mensagem informando o acionamento do Modo 1.
    status = "Ventilação acionada — modo 1";
    // Se nenhuma regra anterior se aplica, há calor elevado e movimento.
  } else {
    // Ativa o Modo 2 de ventilação.
    ventilacao = "Modo 2";
    // Define a mensagem informando o acionamento do Modo 2.
    status = "Ventilação acionada — modo 2";
  }

  // Verifica se deve exibir a cor correspondente a condicao Normal.
  if (temperatura < 30) {
    // Adiciona a classe usada pelo CSS para o status Normal.
    caixaStatus.classList.add("status-normal");
    // Em temperaturas mais altas, verifica ausencia de movimento.
  } else if (movimento === "nao") {
    // Adiciona a classe que representa o sistema desligado por falta de movimento.
    caixaStatus.classList.add("status-sem-movimento");
    // Se há movimento, verifica se a faixa térmica e Atenção.
  } else if (temperatura < 35) {
    // Adiciona a classe de destaque visual da faixa Atenção.
    caixaStatus.classList.add("status-atencao");
    // Se chegou aqui, o estado visual é Calor elevado.
  } else {
    // Adiciona a classe de destaque visual para Calor elevado.
    caixaStatus.classList.add("status-calor");
  }

  // Mostra a mensagem de status calculada no painel de resultados.
  statusSistema.textContent = status;

  // Mostra a temperatura informada com a unidade de graus Celsius.
  resultadoTemperatura.textContent = temperatura + " °C";
  // Mostra a classificação térmica calculada.
  resultadoCondicao.textContent = condicao;

  // Verifica se o usuário selecionou Sim para movimento.
  if (movimento === "sim") {
    // Exibe Detectado quando houve movimento.
    resultadoMovimento.textContent = "Detectado";
    // Caso contrario, o usuário selecionou Não.
  } else {
    // Exibe Não detectado quando não houve movimento.
    resultadoMovimento.textContent = "Não detectado";
  }

  // Por último, mostra se a ventilação está desligada, em Modo 1 ou Modo 2.
  resultadoVentilacao.textContent = ventilacao;
}
