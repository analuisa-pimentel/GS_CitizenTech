/* MODO CLARO E ESCURO - PONTO FRESCO */

// Busca no HTML o botão com id botão-tema e o guarda na variável.
const botaoTema = document.getElementById("botao-tema");

// Quando o usuário clicar no botão, executa a função alterarTema.
botaoTema.addEventListener("click", alterarTema);

// Declara a função responsavel por mudar a aparencia da página.
function alterarTema() {
  // Adiciona a classe tema-escuro ao body; se ja existe, remove a classe.
  document.body.classList.toggle("tema-escuro");

  // Confere se o body possui a classe tema-escuro após a alteracao.
  if (document.body.classList.contains("tema-escuro")) {
    // Informa para acessibilidade que o botão está em estado ativo.
    botaoTema.setAttribute("aria-pressed", "true");
    // Começa a atualizar a descrição acessível do botão.
    botaoTema.setAttribute(
      // Escolhe o atributo aria-label, que da nome ao botão para leitores de tela.
      "aria-label",
      // Define que o próximo clique vai ativar o modo claro.
      "Ativar modo claro",
    );

    // Se o body não tem tema-escuro, o modo claro está ativo.
  } else {
    // Informa para acessibilidade que o botão está em estado desativado.
    botaoTema.setAttribute("aria-pressed", "false");
    // Começa a atualizar a descrição acessível no modo claro.
    botaoTema.setAttribute(
      // Escolhe novamente o atributo aria-label.
      "aria-label",
      // Define que o próximo clique vai ativar o modo escuro.
      "Ativar modo escuro",
    );
  }
}
