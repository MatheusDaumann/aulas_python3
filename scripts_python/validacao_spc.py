spc = input('Está no SPC?Digite "s" para SIM e "n" para NÃO')

for i in spc:
    if spc == 's':
        print ('Financiamento negado')
        break
        
    idade = int(input('Qual sua idade?'))
    
    while idade <=17:
        print('Financiamento negado')
        break
    else:
        pass
    
        salario = float(input('Qual o seu salário? R$'))
        valor_carro = float(input('Valor do carro? R$'))
        entrada_carro = float(input('Valor de entrada? R$'))
        vinte=valor_carro * 0.2
        
        while entrada_carro < vinte:
            print('Financiamento negado')
            break
        else:
            pass

        parcelas = int(input('Quantidade de parcelas?máximo 72 parcelas'))
        
        while parcelas >=73:
            print ('Negado limite máximo é de 72 Parcelas')
            break
        else:
            pass
        
            valor_prestacao = (valor_carro / parcelas)
            minimo = (salario * 30 / 100)
            
            while valor_prestacao <= minimo:
                print('Financiamento Aprovado')
                break
            else:
                print ('Financiamento negado')