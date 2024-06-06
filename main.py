import os
# -- -- --
# vars
res=[]
valor1=0
valor2=0
valor_atual=0

espaco=2

inp_v1=False


# -- -- --
# vars de texto
divisorias='-'*31
titulo=('Quantum Calculator'.center(31))

selec_v1_txt='Digite o primeiro valor: '
selec_op_txt='Digite a operação que deseja realizar: '
selec_v2_txt='Digite o primeiro valor: '


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
    global valor1,valor_atual,inp_v1
    if inp_v1==False:
        #global valor1,valor_atual
        selec_v1=int(input(selec_v1_txt))  # resolver BO e verificar se é int ou str
        if selec_v1=='ac' and selec_v1=='AC':
            reset()
        elif selec_v1!=int:
            print('op inval')
            input('reiniciando...')
            reset()
        else:
            valor1=selec_v1
            valor_atual=selec_v1
            inp_v1=True
            main()
    # -- -- --
    selec_op=str(input(selec_op_txt))
    selec_v2=int(input(selec_v2_txt))


# -- -- --
def cleaner():
    os.system('cls')


# -- -- --
def reset(): # adicionar todas os outro bools
    global inp_v1
    inp_v1=False
    main()


# -- -- --
def main():
    cleaner()
    visor()
    operacoes()
    escolhas()


# -- -- --
main()