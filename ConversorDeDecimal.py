curso = "CST em Analise e Desenvolvimento de sistema "
componentes_do_grupo = ["Renan Saran", "Lucas Givando", "Rodrigo Silva"]
disciplinas_envolvidas = ["Programação de Computadores", "Organização e Arquitetura de computadores"]
versao_do_aplicativo = "1.4"


#exibe apenas as opcoes do menu 
def exibir_menu():
    print("\nMenu")
    print("1. Converter decimal")
    print("2. Curso")
    print("3. Componentes do Grupo")
    print("4. Diciplinas")
    print("5. Versão")
    print("6. Sair")
    
#realiza a conversao dos numeros hexadecimais para as letras 
def letras_hexadecimal(resto):
    
        if resto == 10:
            return "A"
        if resto == 11:
            return "B"
        if resto == 12:
            return "C"
        if resto == 13:
            return "D"
        if resto == 14:
            return "E"
        if resto == 15:
            return "F"
    
#realiza a conversao de decimal para binario 
def decimal_para_binario(decimal):
   
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

#realiza a conversao de decimal para hexadecimal 
def decimal_para_hexadecimal(decimal):
  
    hexadecimal = ''
    while decimal > 0:
        resto = decimal % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
             hexadecimal = letras_hexadecimal(resto) + hexadecimal
        decimal = decimal // 16
    return hexadecimal

#realiza a conversao de decimal para octadecimal 
def decimal_para_octal(decimal):
  
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal

#exibe as opcoes de conversao, e chama as funcoes de conversao de acordo com o selecionado
def exibir_opcao_conversao():
    converterPara = int(input(" \n1. Binario \n2. Hexadecimal \n3. OctaDecimal \nConverter para: "))
    decimal = int(input("\nDigite o decimal a ser convertido: "))

    if decimal == 0:
        print("0 equivale a ele mesmo em qualque base...")
    else:
        if converterPara == 1:
            print("O decimal", decimal, "equivale a:", decimal_para_binario(decimal), "em Binario")
        elif converterPara == 2:
            print("O decimal", decimal, "equivale a:", decimal_para_hexadecimal(decimal), "em Hexadecimal")
        elif converterPara == 3:
            print("O decimal", decimal, "equivale a:", decimal_para_octal(decimal), "em OctaDecimal")
        
#funcao princial, onde o programa e iniciado invocando as outras funcoes/funcionalidades
def main():

    opcao = 0    

    while opcao != 6:
        exibir_menu()
        opcao = int(input("\nEscolha uma opção: "))
        if opcao == 1:
            
            exibir_opcao_conversao()
                
        elif opcao == 2:
            print(curso)

        elif opcao == 3:
            for componentes in componentes_do_grupo:
                    print("- " + componentes)

        elif opcao == 4:
            for disciplina in disciplinas_envolvidas:
                    print("- " + disciplina)

        elif opcao == 5:
            print("v",versao_do_aplicativo)
        
        elif opcao == 6: 
            print("Encerrando a aplicação...")
        
        else: 
             print("Opção inválida. Por favor, escolha novamente.")
        
main()
        

    
    
    
    