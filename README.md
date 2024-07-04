# Coffee_Machine_Project
Coffee Machine

Este é um projeto simples, o qual simula uma máquina de café em Python.
A máquina oferece três tipos de bebidas: espresso, latte e cappuccino. 
O usuário pode inserir moedas para comprar uma bebida e a máquina verifica se há recursos suficientes para preparar a bebida escolhida.


Relatório: Exibe a quantidade atual de água, leite, café e dinheiro na máquina.
Desligar: Desliga a máquina de café.
Compra de bebidas: Permite ao usuário escolher entre espresso, latte ou cappuccino e pagar com moedas.

Como usar
Iniciar a máquina: Ao iniciar o script running_coffee_machine(), a máquina começará a funcionar e pedirá ao usuário para escolher uma ação.

Escolher uma bebida: O usuário pode escolher entre espresso, latte ou cappuccino.

Inserir moedas: Se a bebida estiver disponível, a máquina pedirá ao usuário para inserir moedas. O usuário deve informar a quantidade de cada tipo de moeda (quarters, dimes, nickels, pennies).

Processamento da transação: A máquina verifica se a quantidade de dinheiro inserida é suficiente para a compra. Se for, a máquina fornece a bebida e o troco, se houver. Se não for, a máquina informa que o dinheiro não é suficiente e devolve as moedas.

Relatório: A qualquer momento, o usuário pode digitar report para ver a quantidade atual de recursos na máquina.

Desligar a máquina: O usuário pode digitar off para desligar a máquina.

Estrutura do Código

Funções
calculate_money(quarters, dimes, nickels, pennies, coins): Calcula o valor total do dinheiro inserido com base nas quantidades de cada tipo de moeda.

check_transaction(value, menu, coffee): Verifica se o valor inserido é suficiente para comprar a bebida escolhida.

process_coins(value, menu, coffee): Calcula e retorna o troco a ser devolvido ao usuário.

print_report(resources, money): Exibe um relatório dos recursos atuais e do dinheiro na máquina.

check_resources(coffee, resources, menu): Verifica se há recursos suficientes para preparar a bebida escolhida.

calculate_resources(coffee, menu, resources): Atualiza os recursos da máquina após a preparação de uma bebida.

running_coffee_machine(): Função principal que controla a execução da máquina de café.

Importações
O código importa o módulo coffee_machine_menu, que defini os recursos iniciais, o menu das bebidas e os valores das moedas.


Estrutura do Menu
O módulo coffee_machine_menu contém um dicionário MENU com a estrutura das bebidas e seus respectivos custos e ingredientes, e um dicionário resources com a quantidade inicial de água, leite e café, e um dicionário coins com os valores das moedas.

