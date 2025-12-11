import sys
from MemoriaCache import MemoriaCache

CPU_DEBUG = True

registrador_cp = 0x00
registrador_ax = 0x00
registrador_bx = 0x00
registrador_cx = 0x00
registrador_dx = 0x00

flag_zero = False

#memoria = MemoriaCache('C:/Users/renan/Downloads/ProjetoArq_1/ProjetoArq_1/arquivos_memoria/mov_mov_add.bin')
#memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
memoria = MemoriaCache("C:/Users/renan.biavati/Downloads/ProjetoArq_1/ProjetoArq_1/ProjetoArq_1/arquivos_memoria/fibonacci_10.bin")

def buscarEDecodificarInstrucao():
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    instrucao = memoria.getValorMemoria(registrador_cp)

    print(instrucao)

    if CPU_DEBUG == False:
            print("Instruções inválidas.")
    else:
        if instrucao == 0x00:
            print('ID da instrução: 0 - instrução ADD Registrador e Byte')
            return instrucao
        elif instrucao == 0x01:
            print('ID da instrução: 1 - instrução ADD Reg, Reg')
            return instrucao
        elif instrucao == 0x10:
            print('ID da instrução: 2 - instrução INC Reg')
            return instrucao
        elif instrucao == 0x20:
            print('ID da instrução: 3 - instrução DEC Reg')
            return instrucao
        elif instrucao == 0x30:
            print('ID da instrução: 4 - instrução SUB Reg, Byte')
            return instrucao
        elif instrucao == 0x31:
            print('ID da instrução: 5 - instrução SUB Reg, Reg')
            return instrucao
        elif instrucao == 0x40:
            print('ID da instrução: 6 - instrução MOV Reg, Byte')
            return instrucao
        elif instrucao == 0x41:
            print('ID da instrução: 7 - instrução MOV Reg, Reg')
            return instrucao
        elif instrucao == 0x50:
            print('ID da instrução: 8 - instrução JMP Byte')
            return instrucao
        elif instrucao == 0x60:
            print('ID da instrução: 9 - instrução CMP Reg, Byte')
            return instrucao
        elif instrucao == 0x61:
            print('ID da instrução: 10 - instrução CMP Reg, Reg')
            return instrucao
        elif instrucao == 0x70:
            print('ID da instrução: 11 - instrução JZ Byte')
            return instrucao
        else:
            print("Instruções inválidas..")
    return -1

def lerOperadoresExecutarInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    #add reg-byte
    if idInstrucao == 0x00:
        # busca operadores
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:  # Para o registrador AX
            registrador_ax = registrador_ax + 1
            print('Adicionando 1 em:', registrador_ax)
        elif operador1 == 0x03:  # Para o registrador BX
            registrador_bx = registrador_bx + 1
            print('Adicionando 1 em:', registrador_bx)
        elif operador1 == 0x04:  # Para o registrador CX
            registrador_cx = registrador_cx + 1
            print('Adicionando 1 em:', registrador_cx)
        elif operador1 == 0x05:  # Para o registrador DX
            registrador_dx = registrador_dx + 1
            print('Adicionando 1 em:', registrador_dx)

    #add reg-reg
    elif idInstrucao == 0x01:
        #busca operadores
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax = registrador_ax+registrador_ax
                print('somando 0x02 em', registrador_ax)
            elif operador2 == 0x03:
                registrador_ax = registrador_ax+registrador_bx
                print('somando 0x03 em', registrador_ax)
            elif operador2 == 0x04:
                registrador_ax = registrador_ax+registrador_cx
                print('somando 0x04 em', registrador_ax)
            elif operador2 == 0x05:
                registrador_ax = registrador_ax+registrador_dx
                print('somando 0x05 em', registrador_ax)
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx = registrador_bx+registrador_ax
                print('somando 0x02 em', registrador_bx)
            elif operador2 == 0x03:
                registrador_bx = registrador_bx+registrador_bx
                print('somando 0x03 em', registrador_bx)
            elif operador2 == 0x04:
                registrador_bx = registrador_bx+registrador_cx
                print('somando 0x04 em', registrador_bx)
            elif operador2 == 0x05:
                registrador_bx = registrador_bx+registrador_dx
                print('somando 0x05 em', registrador_bx)
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx = registrador_cx+registrador_ax
                print('somando 0x02 em', registrador_cx)
            elif operador2 == 0x03:
                registrador_cx = registrador_cx+registrador_bx
                print('somando 0x03 em', registrador_cx)
            elif operador2 == 0x04:
                registrador_cx = registrador_cx+registrador_cx
                print('somando 0x04 em', registrador_cx)
            elif operador2 == 0x05:
                registrador_cx = registrador_cx+registrador_dx
                print('somando 0x05 em', registrador_cx)
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx = registrador_dx+registrador_ax
                print('somando 0x02 em', registrador_dx)
            elif operador2 == 0x03:
                registrador_dx = registrador_dx+registrador_bx
                print('somando 0x03 em', registrador_dx)
            elif operador2 == 0x04:
                registrador_dx = registrador_dx+registrador_cx
                print('somando 0x04 em', registrador_dx)
            elif operador2 == 0x05:
                registrador_dx = registrador_dx+registrador_dx
                print('somando 0x05 em', registrador_dx)
        
    #inc    
    elif idInstrucao == 0x10:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:
            registrador_ax += 1
            print('incrementando ', registrador_ax, "em 0x02")
        elif operador1 == 0x03:
            registrador_bx += 1
            print('incrementando ', registrador_bx, "em 0x03")
        elif operador1 == 0x04:
            registrador_cx += 1
            print('incrementando ', registrador_cx, "em 0x04")
        elif operador1 == 0x05:
            registrador_dx += 1
            print('incrementando ', registrador_dx, "em 0x05")

    #dec
    elif idInstrucao == 0x20:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:
            registrador_ax -= 1
            print('decrementando ', registrador_ax, "em 0x02")
        elif operador1 == 0x03:
            registrador_bx -= 1
            print('decrementando ', registrador_bx, "em 0x03")
        elif operador1 == 0x04:
            registrador_cx -= 1
            print('decrementando ', registrador_cx, "em 0x04")
        elif operador1 == 0x05:
            registrador_dx -= 1
            print('decrementando ', registrador_dx, "em 0x05")

    #sub reg-byte
    if idInstrucao == 0x30:
        # busca operadores
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if operador1 == 0x02:  # Para o registrador AX
            registrador_ax = registrador_ax - 1
            print('Subtraindo 1 em:', registrador_ax)
        elif operador1 == 0x03:  # Para o registrador BX
            registrador_bx = registrador_bx - 1
            print('Subtraindo 1 em:', registrador_bx)
        elif operador1 == 0x04:  # Para o registrador CX
            registrador_cx = registrador_cx - 1
            print('Subtraindo 1 em:', registrador_cx)
        elif operador1 == 0x05:  # Para o registrador DX
            registrador_dx = registrador_dx - 1
            print('Subtraindo 1 em:', registrador_dx)

    #sub reg-reg
    elif idInstrucao == 0x31:
        #busca operadores
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            if operador2 == 0x02:
                registrador_ax = registrador_ax-registrador_ax
                print('Subtraindo 0x02 em', registrador_ax)
            elif operador2 == 0x03:
                registrador_ax = registrador_ax-registrador_bx
                print('Subtraindo 0x03 em', registrador_ax)
            elif operador2 == 0x04:
                registrador_ax = registrador_ax-registrador_cx
                print('Subtraindo 0x04 em', registrador_ax)
            elif operador2 == 0x05:
                registrador_ax = registrador_ax-registrador_dx
                print('Subtraindo 0x05 em', registrador_ax)
        elif operador1 == 0x03:
            if operador2 == 0x02:
                registrador_bx = registrador_bx-registrador_ax
                print('Subtraindo 0x02 em', registrador_bx)
            elif operador2 == 0x03:
                registrador_bx = registrador_bx-registrador_bx
                print('Subtraindo 0x03 em', registrador_bx)
            elif operador2 == 0x04:
                registrador_bx = registrador_bx-registrador_cx
                print('Subtraindo 0x04 em', registrador_bx)
            elif operador2 == 0x05:
                registrador_bx = registrador_bx-registrador_dx
                print('Subtraindo 0x05 em', registrador_bx)
        elif operador1 == 0x04:
            if operador2 == 0x02:
                registrador_cx = registrador_cx-registrador_ax
                print('Subtraindo 0x02 em', registrador_cx)
            elif operador2 == 0x03:
                registrador_cx = registrador_cx-registrador_bx
                print('Subtraindo 0x03 em', registrador_cx)
            elif operador2 == 0x04:
                registrador_cx = registrador_cx-registrador_cx
                print('Subtraindo 0x04 em', registrador_cx)
            elif operador2 == 0x05:
                registrador_cx = registrador_cx-registrador_dx
                print('Subtraindo 0x05 em', registrador_cx)
        elif operador1 == 0x05:
            if operador2 == 0x02:
                registrador_dx = registrador_dx-registrador_ax
                print('Subtraindo 0x02 em', registrador_dx)
            elif operador2 == 0x03:
                registrador_dx = registrador_dx-registrador_bx
                print('Subtraindo 0x03 em', registrador_dx)
            elif operador2 == 0x04:
                registrador_dx = registrador_dx-registrador_cx
                print('Subtraindo 0x04 em', registrador_dx)
            elif operador2 == 0x05:
                registrador_dx = registrador_dx-registrador_dx
                print('Subtraindo 0x05 em', registrador_dx)

    #mov reg-byte
    elif idInstrucao == 0x40:
        #busca operadores
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            registrador_ax = operador2
            print('atribuindo 0x02 em', registrador_ax)
        elif operador1 == 0x03:
            registrador_bx = operador2
            print('atribuindo 0x03 em', registrador_bx)
        elif operador1 == 0x04:
            registrador_cx = operador2
            print('atribuindo 0x04 em', registrador_cx)
        elif operador2 == 0x05:
            registrador_dx = operador2
            print('atribuindo 0x05 em', registrador_dx)

    #mov reg-reg
    elif idInstrucao == 0x41:
        #busca operadores
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        operador2 = memoria.getValorMemoria(registrador_cp + 2)
        if operador1 == 0x02:
            registrador_ax = operador2
            print('atribuindo 0x02 em', registrador_ax)
        elif operador1 == 0x03:
            registrador_bx = operador2
            print('atribuindo 0x03 em', registrador_bx)
        elif operador1 == 0x04:
            registrador_cx = operador2
            print('atribuindo 0x04 em', registrador_cx)
        elif operador2 == 0x05:
            registrador_dx = operador2
            print('atribuindo 0x05 em', registrador_dx)

    #jmp
    elif idInstrucao == 0x50:
        operador1 = memoria.getValorMemoria(registrador_cp + 1) 
        registrador_cp = operador1

    #cmp reg-byte
    elif idInstrucao == 0x60:  # id da instrução CMP
    # Busca os operadores
        operador1 = memoria.getValorMemoria(registrador_cp + 1)  # Primeiro operando
        operador2 = memoria.getValorMemoria(registrador_cp + 2)  # Segundo operando

        # Verificar qual tipo de comparação será feita
        if operador1 == 0x02:  # Comparar com AX
            valor1 = registrador_ax
        elif operador1 == 0x03:  # Comparar com BX
            valor1 = registrador_bx
        elif operador1 == 0x04:  # Comparar com CX
            valor1 = registrador_cx
        elif operador1 == 0x05:  # Comparar com DX
            valor1 = registrador_dx
        else:
            valor1 = operador1  # Se for um valor imediato

        valor2 = operador2 

        # Comparação (simulando a subtração)
        resultado = valor1 - valor2

        # Flags baseadas no resultado
        if resultado == 0:
            print('Resultado da CMP: Zero flag set')
            flag_zero = True
        else:
            flag_zero = False

    #cmp reg-reg
    elif idInstrucao == 0x61:  # id da instrução CMP
    # Busca os operadores
        operador1 = memoria.getValorMemoria(registrador_cp + 1)  # Primeiro operando
        operador2 = memoria.getValorMemoria(registrador_cp + 2)  # Segundo operando

        # Verificar qual tipo de comparação será feita
        if operador1 == 0x02:  # Comparar com AX
            valor1 = registrador_ax
        elif operador1 == 0x03:  # Comparar com BX
            valor1 = registrador_bx
        elif operador1 == 0x04:  # Comparar com CX
            valor1 = registrador_cx
        elif operador1 == 0x05:  # Comparar com DX
            valor1 = registrador_dx
        else:
            valor1 = operador1  # Se for um valor imediato

        if operador2 == 0x02:  # Comparar com AX
            valor2 = registrador_ax
        elif operador2 == 0x03:  # Comparar com BX
            valor2 = registrador_bx
        elif operador2 == 0x04:  # Comparar com CX
            valor2 = registrador_cx
        elif operador2 == 0x05:  # Comparar com DX
            valor2 = registrador_dx
        else:
            valor2 = operador2  # Se for um valor imediato

        # Comparação (simulando a subtração)
        resultado = valor1 - valor2

        # Flags baseadas no resultado
        if resultado == 0:
            print('Resultado da CMP: Zero flag set')
            flag_zero = True
        else:
            flag_zero = False

    #jz byte        
    elif idInstrucao == 0x70:
        operador1 = memoria.getValorMemoria(registrador_cp + 1)
        if flag_zero: 
            registrador_cp = operador1     
        else:
            registrador_cp = registrador_cp + 2
    else:
        print("ID da instrução inválido")

def calcularProximaInstrucao(idInstrucao):
    global registrador_ax
    global registrador_bx
    global registrador_cp
    global registrador_cx
    global registrador_dx
    global flag_zero

    if CPU_DEBUG == True:
        # 2 OPERADORES
        if idInstrucao == 0X00:
            registrador_cp = registrador_cp + 3
            print('mudando CP para ', registrador_cp)
        elif idInstrucao == 0x01:
            registrador_cp = registrador_cp + 3
            print('mudando CP para ', registrador_cp)
        elif idInstrucao == 0x30:
            registrador_cp = registrador_cp + 3
            print('mudando CP para ', registrador_cp)
        elif idInstrucao == 0x31:
            registrador_cp = registrador_cp + 3
            print('mudando CP para ', registrador_cp)
        elif idInstrucao == 0x40:
            registrador_cp = registrador_cp + 3
            print('mudando CP para ', registrador_cp)    
        elif idInstrucao == 0x41:
            registrador_cp = registrador_cp + 3
            print('mudando CP para ', registrador_cp)
        elif idInstrucao == 0x60:
            registrador_cp = registrador_cp + 3
            print('mudando CP para ', registrador_cp)
        elif idInstrucao == 0x61:
            registrador_cp = registrador_cp + 3
            print('mudando CP para ', registrador_cp)
    
        # 1 OPERADOR
        elif idInstrucao == 0x10:
            registrador_cp = registrador_cp + 2
            print('mudando CP para ', registrador_cp)
        elif idInstrucao == 0x20:
            registrador_cp = registrador_cp + 2
            print('mudando CP para ', registrador_cp)
        elif idInstrucao == 0x50:
            print('mudando CP para ', registrador_cp)
        elif idInstrucao == 0x70:
            print('mudando CP para ', registrador_cp)
        else:
            ('Erro no cálculo da próxima instrução.')
    else:
        ('Erro no cálculo da próxima instrução.')


def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] \
            AX[{registrador_ax:02X}]  \
            BX[{registrador_bx:02X}]  \
            CX[{registrador_cx:02X}]  \
            DX[{registrador_dx:02X}]  \
            ZF[{flag_zero}] ')

if __name__ == '__main__':
    while (True):
        #Unidade de Controle
        idInstrucao = buscarEDecodificarInstrucao()

        #ULA
        lerOperadoresExecutarInstrucao(idInstrucao)  

        dumpRegistradores() 

        #Unidade de Controle
        calcularProximaInstrucao(idInstrucao)

        #apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)
    
