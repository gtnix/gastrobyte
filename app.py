import os

restaurantes = [{"nome":"Boa praça","categoria":"Brasileira","ativo":False}, 
                {"nome":"Pizza Suprema","categoria":"Pizza","ativo":True},
                {"nome":"Cantina da Nona","categoria":"Italiana","ativo":False}]

def exibir_nome():

    """Exibe o nome estilizado do programa na tela."""

    print("🇸​​​​​🇦​​​​​🇧​​​​​🇴​​​​​🇷​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇷​​​​​🇪​​​​​🇸​​​​​🇸​​​​​\n") 

def exibir_opcoes():

    """
    Mostra as opções disponíveis no menu principal do sistema.

    O menu oferece funcionalidades para:
    1. Cadastrar novos restaurantes.
    2. Listar todos os restaurantes.
    3. Alterar o status (ativo/inativo) de um restaurante.
    4. Encerrar o programa. 
    """

    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar status do restaurante")
    print("4. Sair\n")

def finalizar_app():

    """
    Finaliza a execução do aplicativo exibindo uma mensagem de encerramento.

    Utiliza a função exibir_subtitulo() para manter o padrão visual do sistema.
    """

    exibir_subtitulo("Finalizando o aplicativo.")

def voltar_menu_principal():

    """
    Aguarda uma entrada do usuário e retorna ao menu principal do sistema.

    Usada como pausa após a execução de qualquer funcionalidade antes de reiniciar o ciclo do menu.
    """

    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

def opcao_invalida():

    """
    Exibe uma mensagem de erro quando o usuário digita uma opção inválida.

    Garante retorno ao menu principal após o erro.
    """

    print("Opção inválida\n")
    voltar_menu_principal()

def exibir_subtitulo(texto):

    """
    Exibe um texto centralizado entre linhas de asteriscos como subtítulo.

    Parâmetros:
    texto (str): Texto que será formatado como título da seção atual.

    Essa função é usada para manter a consistência visual e separar seções no terminal.
    """

    os.system("clear")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():

    """
    Solicita ao usuário o nome e a categoria de um novo restaurante e o adiciona à lista.

    O restaurante é adicionado com status 'ativo = False' por padrão.
    Após o cadastro, exibe uma mensagem de confirmação e retorna ao menu.
    """

    exibir_subtitulo("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante.upper()} foi cadastrado com sucesso!\n")
    voltar_menu_principal()

def listar_restaurantes():

    """
    Lista todos os restaurantes cadastrados com seus nomes, categorias e status de atividade.

    Utiliza a função `ljust()` para alinhar visualmente os dados no terminal.
    Após a listagem, retorna ao menu principal.
    """

    exibir_subtitulo("Listando os restaurantes...\n")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")    #função ljust() do Python alinha uma string à esquerda, adicionando preenchimento à direita.

    voltar_menu_principal()

def alterar_status_restaurante():

    """
    Altera o status (ativo/inativo) de um restaurante a partir do nome informado pelo usuário.

    Se o restaurante for encontrado, seu status é invertido.
    Caso não seja localizado, uma mensagem de erro é exibida.
    Em ambos os casos, retorna ao menu principal ao final.
    """

    exibir_subtitulo("Alterando status do restaurante...")
    nome_restaurante = input("Digite o nome do Restaurante que deseja alterar o status: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso."    #Aplicação de função ternária, permite escrever declaração condicional em uma única linha.
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")

    voltar_menu_principal()

def escolher_opcao():

    """
    Recebe a entrada do usuário e direciona para a função correspondente.

    Controla a navegação do menu com tratamento de erro para entradas não numéricas.
    Garante que qualquer exceção ou número inválido leve de volta ao menu.
    """

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    
    """
    Função principal do sistema.

    Limpa o terminal, exibe o nome do programa, apresenta as opções e aguarda a escolha do usuário.
    Executa continuamente até que o usuário escolha a opção de sair.
    """

    os.system("clear")
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()  
