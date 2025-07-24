# Sistema Bancário Modularizado - SYS_BANKV2.py

Este projeto consiste em um sistema bancário simples, modularizado em Python, implementado no arquivo `SYS_BANKV2.py`. Ele contempla funcionalidades básicas para manipulação de contas correntes e usuários, e tem como objetivo exercitar conceitos importantes da linguagem como modularização, passagem de parâmetros (positional only, keyword only), listas de dados e organização do código.

---

## Desafio e Objetivo

O desafio principal deste projeto foi modularizar as operações bancárias em funções independentes e bem definidas, seguindo regras específicas para passagem de parâmetros. Além disso, foi necessário criar funções para gerenciamento de usuários e contas bancárias, mantendo a integridade dos dados.

---

## Estrutura do Programa

### Funções de operações bancárias

- **depositar(saldo, valor, extrato, /)**  
  - Argumentos posicional-only (`/`), ou seja, só podem ser passados por posição.  
  - Valida o valor e atualiza saldo e extrato, retornando os valores atualizados.

- **sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)**  
  - Argumentos keyword-only (`*`), devem ser passados com nomes explícitos.  
  - Faz validações de saldo, limite, número máximo de saques e atualiza saldo, extrato e contador de saques.  
  - Retorna saldo, extrato e número de saques atualizados.

- **exibir_extrato(saldo, /, *, extrato)**  
  - Mistura argumentos posicional-only e keyword-only.  
  - Exibe o histórico das transações e o saldo atual.

---

### Funções para gerenciamento de usuários e contas

- **criar_usuario(usuarios)**  
  - Solicita dados do usuário: nome, nascimento, CPF (somente números) e endereço.  
  - Evita duplicidade de CPF.  
  - Armazena o usuário em uma lista.

- **criar_conta(agencia, numero_conta, usuarios)**  
  - Solicita o CPF para vincular a conta a um usuário existente.  
  - Cria uma conta com agência fixa e número sequencial.  
  - Retorna o dicionário da conta criada.

- **listar_contas(contas)**  
  - Lista todas as contas cadastradas com dados básicos.

---

## Fluxo do Programa (`main()`)

1. Inicializa variáveis de controle: saldo, extrato, limite de saque, contador de saques, listas de usuários e contas.

2. Exibe um menu interativo no terminal para o usuário escolher a operação desejada.

3. Chama as funções correspondentes às opções, atualizando o estado do sistema conforme necessário.

4. Permite múltiplas operações até o usuário optar por sair.

---

## Como o código implementa o desafio

- **Modularização clara**: cada função tem responsabilidade única.  
- **Regras de passagem de parâmetros** aplicadas conforme solicitado no desafio:  
  - Positional-only para depósito.  
  - Keyword-only para saque.  
  - Mistura para extrato.  
- **Controle de usuários e contas** com verificações e vínculos corretos.  
- **Interação via terminal** simples e didática.

---

## Como usar

1. Certifique-se de ter Python 3 instalado.  
2. Salve o código no arquivo `SYS_BANKV2.py`.  
3. Execute no terminal com:

```bash
python SYS_BANKV2.py

```