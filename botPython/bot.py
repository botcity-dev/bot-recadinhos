# Import for the Desktop Bot
from botcity.core import DesktopBot

def main():
    
    bot = DesktopBot()

    # abrindo o aplicativo wordpad
    bot.execute(r"C:\Program Files\Windows NT\Accessories\wordpad.exe")
    bot.wait(2000)
    bot.maximize_window()

    # adicionando o seu texto no wordpad
    bot.paste("coloque sua mensagem aqui e, se quiser que seja compartilhada, adicione seu @ e qual é a rede social")

    # aqui você pode escolher a forma que vai executar, deixe apenas uma das funções descomentada
    exemplo_sem_visao_computacional(bot)
    exemplo_com_visao_computacional(bot)

    # aguardar alguns instantes para garantir que o arquivo foi salvo
    bot.wait(2000)
    
    # fechar o wordpad
    bot.alt_f4()
    
    

def exemplo_sem_visao_computacional(bot):  

    # este atalho é o comando para salvar o arquivo, é uma das alternativas para fazer isso
    bot.type_keys(["ctrl", "b"])

    # adicionar o caminho onde vai ser salvo e adicionar o nome no arquivo com extensão .txt
    bot.paste(r"caminho\nome_arquivo.txt")

    # pressiona enter para salvar
    bot.enter()

    # pressiona enter novamente para aceitar a mensagem de que o arquivo está sendo salvo em txt
    bot.enter()

def exemplo_com_visao_computacional(bot):

    if not bot.find( "disketinho", matching=0.97, waiting_time=10000):
        not_found("disketinho")
    bot.click()    
    
    # adicionar o caminho onde vai ser salvo e adicionar o nome no arquivo com extensão .txt
    bot.paste(r"caminho\nome_arquivo.txt")
    
    if not bot.find( "botao_salvar", matching=0.97, waiting_time=10000):
        not_found("botao_salvar")
    bot.click()
    
    if not bot.find( "aceitar_formato", matching=0.97, waiting_time=10000):
        not_found("aceitar_formato")
    bot.click_relative(257, 106)
        

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()

