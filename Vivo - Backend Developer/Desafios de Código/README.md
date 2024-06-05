# Desafios de Projeto Bootcamp Python 

Este repositório contém desafios de projeto destinados a aprimorar minhas habilidades de programação e resolução de problemas. Cada desafio é projetado para abordar tópicos específicos e testar minha capacidade de escrever código funcional na linguagem Python. Sinta-se à vontade para explorar esses desafios.

## Desafio 1: Verificador de Planos de Internet

- **Descrição**: Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

Planos Oferecidos:

- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

  **Entrada**: Como entrada solicite o consumo médio mensal de dados em GB (float).

  **Saída**: Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.

## Desafio 2: Lista de Equipamentos

- **Descrição**: Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

  **Entrada**: O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

  **Saída**: Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.

## Desafio 3: Validando Número de Telefone

- **Descrição**: magine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

Formato esperado:
O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. Lembre-se de respeitar os espaços entre os números quando preciso.

  **Entrada**: Uma string representando o número de telefone.

  **Saída**: Uma mensagem indicando se o número de telefone é válido ou inválido.

  ## Desafio 4: Classe de Usuário

- **Descrição**: Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

  **Entrada**: Nome do usuário, número de telefone e plano.
  
  **Saída**: Mensagem indicando que o usuário foi criado com sucesso.

  ## Desafio 5: Funcionalidades ao Plano

- **Descrição**: Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano. Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada' para gerar uma mensagem personalizada.

Condições da verificação do saldo:
- Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
- Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
- Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

  **Entrada**: Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.
  
  **Saída**: Mensagem personalizada de acordo o saldo do cliente.

  ## Desafio 6: Realizando Chamadas

- **Descrição**: Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto. Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e duracao como parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.

  **Entrada**: Número do usuário, número do telefone, saldo inicial, número do destinatário e a duração da chamada em minutos.

  **Saída**: Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.

