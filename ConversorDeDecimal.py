curso = "Analise e Desenvolvimento de sistema "
componentes_do_grupo = ["Renan Saran", "Lucas Givando", "Rodrigo"]
disciplinas_envolvidas = ["Programação de Computadores", "Organização e Arquitetura de computadores"]
versao_do_aplicativo = "1.2"



def exibir_menu():
    
    print("1. Converter decimal")
    print("2. Curso")
    print("3. Componentes do Grupo")
    print("4. Diciplinas")
    print("5. Versão")
    print("6. Sair")
    
    
def decimal_para_binario(decimal):
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

def decimal_para_hexadecimal(decimal):
    if decimal == 0:
        return '0'
    hexadecimal = ''
    while decimal > 0:
        resto = decimal % 16
        if resto < 10:
            hexadecimal = str(resto) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + resto - 10) + hexadecimal
        decimal = decimal // 16
    return hexadecimal

def decimal_para_octal(decimal):
    if decimal == 0:
        return '0'
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal
    

def main():
    exibir_menu()

    opcao = int(input("\nEscolha uma opção: "))
    

    
    if opcao == 1:
        converterPara = int(input(" \n1. Binario \n2. Hexadecimal \n3. OctaDecimal \nConverter para: "))
        decimal = int(input("\nDigite o decimal a ser convertido: "))
        if converterPara == 1:
            print("O decimal", decimal, "equivale a:", decimal_para_binario(decimal), "em Binario")
        elif converterPara == 2:
            print("O decimal", decimal, "equivale a:", decimal_para_hexadecimal(decimal), "em Hexadecimal")
        elif converterPara == 3:
            print("O decimal", decimal, "equivale a:", decimal_para_octal(decimal), "em OctaDecimal")
            
    elif opcao == 2:
        print(curso)
        
    elif opcao == 3:
        for componentes in componentes_do_grupo:
                print("- " + componentes)
    
    elif opcao == 4:
        for disciplina in disciplinas_envolvidas:
                print("- " + disciplina)
    
    elif opcao == 5:
        print(versao_do_aplicativo)
        
   
        


main()
        

    
    
    
    