## Desafio

Para participar do desafio você deverá criar um bot que abre o wordpad e deixa uma mensagem sobre o evento, deixando o seu @ e rede social caso permita compartilhar sua mensagem.

> Para ver a lista completa de funções para desenvolver o seu bot, acesse a [documentação](https://documentation.botcity.dev/pt/frameworks/desktop/python/).

## Dicas

### Template
Disponibilizamos um template para você começar a desenvolver o seu bot, com algumas configurações prontas.

### Sugestão de implementação
- ### abrir o app wordpad
    - encontrar o executável do spotify e usar o comando `bot.execute(r"caminho/app.exe")`
    - usar a função `bot.wait(2000)` para aguardar o app abrir
    - usar a função `bot.maximize_window()` para maximizar a janela do app

- ### digitar uma mensagem
    - usar a função `bot.type_keys("message")` para digitar cada caractere da mensagem 
    - usar a função `bot.paste("message")` para colar a mensagem inteira

- ### salvar a mensagem por atalho
    - usar a função `bot.type_keys(["ctrl", "b"])` para salvar a mensagem
    - usar a função `bot.paste(r"caminho\nome_arquivo.txt")` para definir o caminho e nome do arquivo
    - usar a função `bot.enter()` para confirmar o salvamento
    - usar a função `bot.alt_f4()` para fechar o app

- ### salvar mensagem por visão computacional
    - usar o BotCity Studio para encontrar os elementos ([Guia rápido de uso](STUDIO.md))
    - buscar e clicar o icone disquete para salvar (ação click)
    - usar a função `bot.paste(r"caminho\nome_arquivo.txt")` para definir o caminho e nome do arquivo
    - buscar e clicar o botão de salvar (ação click)
    - buscar e clicar o icone de fechar (ação click)
