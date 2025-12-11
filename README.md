# Simulador de CPU Hipotética em Python

Este projeto é uma implementação em Python de um simulador de CPU simples. Ele emula o ciclo de **Busca (Fetch)**, **Decodificação (Decode)** e **Execução (Execute)**, manipulando registradores, flags e memória simulada através da leitura de arquivos binários.

## 📂 Estrutura do Projeto

  * **`main.py`**: O núcleo do simulador. Contém a lógica da Unidade Central de Processamento (CPU), incluindo:
      * **Unidade de Controle:** Decide a próxima instrução (`calcularProximaInstrucao`).
      * **Decodificador:** Identifica qual operação deve ser realizada (`buscarEDecodificarInstrucao`).
      * **ULA (Unidade Lógica e Aritmética):** Executa operações matemáticas e lógicas (`lerOperadoresExecutarInstrucao`).
      * **Registradores:** Armazena o estado atual da CPU.
  * **`MemoriaCache.py`**: Simula a memória RAM.
      * Lê um arquivo binário do disco.
      * Carrega os bytes em uma lista (array).
      * Fornece métodos para leitura (`getValorMemoria`) e escrita (`setValorMemoria`).

## ⚙️ Arquitetura do Sistema

### Registradores

O simulador possui 5 registradores principais e 1 flag de estado:

| Registrador | Descrição | Endereço Interno (Hex) |
| :--- | :--- | :--- |
| **CP** | Contador de Programa (Instruction Pointer) | - |
| **AX** | Registrador de Propósito Geral | `0x02` |
| **BX** | Registrador de Propósito Geral | `0x03` |
| **CX** | Registrador de Propósito Geral | `0x04` |
| **DX** | Registrador de Propósito Geral | `0x05` |
| **ZF** | Zero Flag (Verdadeiro se o resultado da última operação CMP for 0) | - |

### Conjunto de Instruções (Instruction Set)

O simulador reconhece os seguintes *Opcodes* (códigos de operação):

| ID (Hex) | Mnemônico | Operandos | Descrição |
| :--- | :--- | :--- | :--- |
| `0x00` | **ADD** | Reg, Byte | Soma um valor imediato a um registrador. |
| `0x01` | **ADD** | Reg, Reg | Soma o valor de dois registradores. |
| `0x10` | **INC** | Reg | Incrementa (+1) o valor de um registrador. |
| `0x20` | **DEC** | Reg | Decrementa (-1) o valor de um registrador. |
| `0x30` | **SUB** | Reg, Byte | Subtrai um valor imediato de um registrador. |
| `0x31` | **SUB** | Reg, Reg | Subtrai o valor de um registrador de outro. |
| `0x40` | **MOV** | Reg, Byte | Move um valor imediato para um registrador. |
| `0x41` | **MOV** | Reg, Reg | Move o valor de um registrador para outro. |
| `0x50` | **JMP** | Endereço | Salto incondicional para um endereço de memória. |
| `0x60` | **CMP** | Reg, Byte | Compara um registrador com um valor (define ZF). |
| `0x61` | **CMP** | Reg, Reg | Compara dois registradores (define ZF). |
| `0x70` | **JZ** | Endereço | Salto condicional (Jump if Zero) se ZF for True. |

## 🚀 Como Executar

### Pré-requisitos

  * Python 3.x instalado.
  * Um arquivo binário (`.bin`) contendo o código de máquina válido.

### Configuração

Antes de rodar, é necessário apontar o caminho do arquivo de memória no código.

1.  Abra o arquivo `main.py`.
2.  Localize a linha de instanciação da memória (aprox. linha 18):
    ```python
    memoria = MemoriaCache("caminho/para/seu/arquivo.bin")
    ```
3.  Altere o caminho para o local do seu arquivo binário (ex: `fibonacci_10.bin`).

### Execução

No terminal, execute:

```bash
python main.py
```

O programa entrará em um loop onde:

1.  Lê e exibe a instrução atual.
2.  Executa a lógica.
3.  Imprime o estado dos registradores (`dumpRegistradores`).
4.  Pausa e aguarda um "Enter" do usuário para ir para o próximo ciclo de clock (`sys.stdin.read(1)`).

## 🛠 Debugging

A variável `CPU_DEBUG` no início do `main.py` controla a verbosidade do simulador:

  * `True`: Exibe detalhes passo a passo, dumps de memória e transições de estado.
  * `False`: Exibe apenas mensagens de erro essenciais.
