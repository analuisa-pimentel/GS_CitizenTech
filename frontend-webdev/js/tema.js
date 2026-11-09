/* MODO CLARO E ESCURO - PONTO FRESCO */

// Identifica o botão de alteração do tema
const botaoTema = document.getElementById("botao-tema");

// Executa a função quando o botão é clicado
botaoTema.addEventListener("click", alterarTema);

function alterarTema() {

    // Adiciona ou remove a classe do tema escuro
    document.body.classList.toggle("tema-escuro");

    // Verifica qual tema está ativo
    if (document.body.classList.contains("tema-escuro")) {

        botaoTema.setAttribute("aria-pressed", "true");
        botaoTema.setAttribute(
            "aria-label",
            "Ativar modo claro"
        );

    } else {

        botaoTema.setAttribute("aria-pressed", "false");
        botaoTema.setAttribute(
            "aria-label",
            "Ativar modo escuro"
        );

    }
}
