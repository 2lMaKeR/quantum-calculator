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

somando=False
subtraindo=False
multiplicando=False
dividindo=False
potenciacao=False

cont=0


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


# -- -- --
def escolhas():
    global valor1,valor_atual,inp_v1,menos_ant,inp_op,inp_v2,cont
    global somando,subtraindo,multiplicando,dividindo,potenciacao
    if inp_v1==False:
        selec_v1=input(selec_v1_txt)
        if (selec_v1.isdigit())==True:
            if menos_ant==True:
                valor_atual=f'{valor_atual}'+f'{selec_v1}'
                valor1=int(valor_atual)
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
                somando=True
                reset(1)
            case '-':
                inp_op=True
                subtraindo=True
                reset(1)
            case 'x':
                inp_op=True
                multiplicando=True
                reset(1)
            case '%':
                inp_op=True
                dividindo=True
                reset(1)
            case '*':
                inp_op=True
                potenciacao=True
                reset(1)
            case _:
                print('op inval')
                input('reiniciando...')
                reset('erro')
    # -- -- --
    if inp_v2==False:
        selec_v2=int(input(selec_v2_txt))
        valor2=selec_v2
        inp_v2=True
        if somando==True:
            som=int(valor1+valor2)
            res[cont]=som

        if subtraindo==True:
            dim=int(valor1+valor2)
            res[cont]=dim

        if multiplicando==True:
            mult=int(valor1*valor2)
            res[cont]=mult

        if dividindo==True:
            div=int(valor1/valor2)
            res[cont]=div

        if potenciacao==True:
            cont_poten=0
            while cont_poten<selec_v2:
                pot=valor1*valor1
                cont_poten+=1
            res[cont]=pot

        # -- -- --
        valor_atual=res[cont]
        cont+=1
        reset(1)
    # -- -- --
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
#main()

def pot():
    poten=0
    selec_v2=int(input(selec_v2_txt))
    while poten<selec_v2:
        print(1)
        poten+=1
    #print(6*((3-1)*6))
    #print(2*2*2*2*2*2)
# 2 4 8 16 32 64
# 6 36 216 1296
pot()