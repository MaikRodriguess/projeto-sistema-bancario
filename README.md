# Sistema Bancário 🏦

## Objetivo

O objetivo deste projeto é criar um sistema bancário que permita realizar operações básicas como saques, depósitos e visualização de extrato.

## Desafio 
Fomos contratados por um grande banco para desenvolver o seu novo sistema utilizando a linguagem Python. A primeira versão do sistema irá focar em 3 operações principais: depósito, saque e extrato.


### Operação de Depósito
É possível depositar valores positivos na conta bancária.
A versão 1 do projeto trabalha apenas com um usuário, portanto não é necessário informar agência e número da conta.
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Saque
O sistema permite realizar até 3 saques diários.
O valor máximo por saque é de R$ 500,00.
Caso o usuário não possua saldo suficiente na conta, o sistema exibe uma mensagem informando que não é possível efetuar o saque.
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Extrato
Essa operação lista todos os depósitos e saques realizados na conta.
No final da lista, é exibido o saldo atual da conta.
Se não houver movimentações no extrato, a mensagem "Não foram realizadas movimentações" é exibida.
Os valores são exibidos no formato R$ xxx.xx, por exemplo: R$ 1500.45.

🔍[Ver código aqui!](sistema_bancario.py)😁