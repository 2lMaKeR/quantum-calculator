import os
# -- -- --
# vars
res=[0,1,2,3,4,5,6,7,8,9]
valor1=0
valor2=0
valor_atual=0

espaco=2

menos_ant=False

inp_v1=False
inp_op=False
inp_v2=False

# -- -- --
# vars de texto
divisorias='-'*31
titulo=('Quantum Calculator'.center(31))

selec_v1_txt='Digite o primeiro valor: '
selec_op_txt='Digite a operação que deseja realizar: '
selec_v2_txt='Digite o segundo valor: '

final='Resultado armazenado, reiniciando cálculo...'


# -- -- --
def visor():
    print(titulo)
    print(divisorias)
    print(f'{valor_atual}'.center(31))
    print(divisorias)


# -- -- --
def operacoes():
    print('|  +  |'.ljust(espaco),'|  -  |'.ljust(espaco),'|  x  |'.ljust(espaco),'|  %  |'.ljust(espaco))
    print('| sin |'.ljust(espaco),'| cos |'.ljust(espaco),'| tan |'.ljust(espaco),'|  *  |'.ljust(espaco))
    print(' '.ljust(3*espaco+1),'|  =  |'.ljust(espaco),'|  AC |')
    print(divisorias)

def escolhas():
    global valor1,valor_atual,inp_v1,menos_ant,inp_op,inp_v2
    if inp_v1==False:
        selec_v1=input(selec_v1_txt)
        if (selec_v1.isdigit())==True:
            if menos_ant==True:
                valor_atual=f'{valor_atual}'+f'{selec_v1}'
                valor1=int(selec_v1)
            else:
                valor1=selec_v1
                valor_atual=selec_v1
            inp_v1=True
            reset(1)
        else: 
            match selec_v1:
                case 'ac':
                    reset('erro')
                case 'AC':
                    reset('erro')
                case '+':
                    valor_atual=selec_v1
                    reset(1)
                case '-':
                    valor_atual=selec_v1
                    menos_ant=True
                    reset(1)
                case _:
                    print('op inval')
                    input('reiniciando...')
                    reset('erro')
    # -- -- --
    if inp_op==False:
        selec_op=str(input(selec_op_txt))
        match selec_op:
            case 'ac':
                reset('erro')
            case 'AC':
                reset('erro')
            case '+':
                inp_op=True
                reset(1)
            case '-':
                inp_op=True
                reset(1)
            case _:
                print('op inval')
                input('reiniciando...')
                reset('erro')
     # -- -- --
    if inp_v2==False:         
        selec_v2=int(input(selec_v2_txt))
        valor2=selec_v2                              # continuar configurando o final da função e a seleção de operação
        res[1]=int(valor1+valor2)
        valor_atual=res[1]
        inp_v2=True
        reset(1)

    input(final)
    reset('erro')


# -- -- --
def cleaner():
    os.system('cls')


# -- -- --
def reset(chave): # adicionar todas os outro bools
    global inp_v1,valor_atual
    if chave=='erro':
        inp_v1=False
        valor_atual=0
    main()


# -- -- --
def main():
    cleaner()
    visor()
    operacoes()
    escolhas()


# -- -- --
main()