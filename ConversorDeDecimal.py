curso = "Analise e Desenvolvimento de sistema "
componentes_do_grupo = ["Renan Saran", "Lucas Givando", "Rodrigo"]
disciplinas_envolvidas = ["Programação de Computadores", "Organização e Arquitetura de computadores"]
versao_do_aplicativo = "1.1"



def exibir_menu():
    
    print("1. Converter decimal")
    print("2. Curso")
    print("3. Componentes do Grupo")
    print("4. Diciplinas")
    print("5. Versão")
    print("6. Sair")
    
    
def decimal_para_binario(decimal):
  
    return 

def decimal_para_hexadecimal(decimal):
 
    return 

def decimal_para_octal(decimal):
   
    return 
    

def main():
    exibir_menu()

    opcao = int(input("\nEscolha uma opção: "))
    

    
    if opcao == 1:
        converterPara = int(input(" \n1. Binario \n2. Hexadecimal \n3. OctaDecimal \nConverter para:"))
        decimal = int(input("\nDigite o decimal a ser convertido: "))
        if converterPara == 1:
            resultado = decimal_para_binario(decimal)
        elif converterPara == 2:
            resultado == decimal_para_hexadecimal(decimal)
        elif converterPara == 3:
            resultado == decimal_para_octal(decimal)
            
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
        

    
    
    
    