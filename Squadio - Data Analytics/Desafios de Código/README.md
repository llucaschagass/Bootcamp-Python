# Desafios de Projeto Bootcamp Python 

Este repositório contém desafios de projeto destinados a aprimorar minhas habilidades de programação e resolução de problemas. Cada desafio é projetado para abordar tópicos específicos e testar minha capacidade de escrever código funcional na linguagem Python. Sinta-se à vontade para explorar esses desafios.

## Desafio 1: A Aventura do Explorador

- **Descrição**: Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

  **Entrada**: Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta.

  **Saída**: O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

## Desafio 2: Lista de itens

- **Descrição**: Neste desafio, você deve criar um programa que permita cadastrar uma lista de itens que o usuário possui. A lista deve conter um número fixo de itens e deve ser exibida na tela.

  **Entrada**: O programa deve solicitar ao usuário o nome dos itens que deseja cadastrar. Cada item deve ser cadastrado separadamente.

  **Saída**: Após receber os itens cadastrados pelo usuário, o programa deve exibir na tela a lista de itens que o usuário possui. Cada item deve ser cadastrado separadamente.

## Desafio 3: Armazenamento de Dados

- **Descrição**: Neste desafio, você deve criar um programa que permita calcular a nova capacidade total de armazenamento de dados após um aumento percentual específico.

  **Entrada**: Dois valores inteiros positivos, representando a capacidade atual total de armazenamento em teraflops e o aumento percentual, separados por espaço.

  **Saída**: A nova capacidade total de armazenamento em teraflops, após o aumento percentual especificado.

  ## Desafio 4: O Grande Depósito

- **Descrição**: Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro. O programa deve solicitar apenas uma vez o valor de depósito.

  **Entrada**: O programa deve receber o valor de depósito digitado pelo cliente. Os valor pode ser decimal, representando valor em reais.
  
  **Saída**: O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado. Se o valor for "0", deverá imprimir uma mensagem encerrando o programa. Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro solicitando um novo valor.

  ## Desafio 5: Estrutura de Dados

- **Descrição**: Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancaria, foi identificado a necessidade de uma nova funcionalidade para otimizar os processos e melhorias da experiência dos usuários. Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

  **Entrada**: A primeira entrada consiste em um número inteiro que representa a  quantidade de ativos que o usuário possui. Em seguida, o usuário deverá informar, em linhas separadas, os tipos (strings) dos respectivos ativos.
  
  **Saída**:Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. Cada ativo deve ser apresentado em uma linha separada.

  ## Desafio 6: Validando a Força de Senhas

- **Descrição**: Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS, e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários no IAM são fracas e podem representar um risco à segurança dos dados da empresa. Para resolver esse problema, foi solicitado que você desenvolva um programa capaz de analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.

  **Entrada**: A entrada será uma única string representando a senha que precisa ser validada.

  **Saída**: Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não, juntamente com um feedback explicativo sobre os critérios considerados.

  ## Desafio 7: Robô inteligente

- **Descrição**: Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero. Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

O programa deve ser executado continuamente, permitindo que o usuário insira vários números. Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente. Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos.

  **Entrada**: A entrada deve receber valores inteiros.

  **Saída**: O código deverá retornar uma mensagem (string) informando se o número é positivo ou não. Ao receber o valor 0, ele deverá encerrar o e informar quantos números foram positivos e negativos.

   ## Desafio 8: Classificação Frutífera

- **Descrição**: Nesta missão, sua tarefa é mais desafiadora do que nunca! Em um pomar mágico, as frutas têm características únicas que as diferenciam. Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características: peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo de fruta tem limites específicos para essas características.

  **Entrada**: Seu código deve receber as seguintes entradas do usuário: Peso da fruta, Textura da fruta e Cor da fruta

  **Saída**: O código deve produzir uma saída indicando a classificação da fruta com base nas características fornecidas.

    ## Desafio 9: Afinidade Elemental
  
- **Descrição**: No reino mágico onde cada feiticeiro possui uma afinidade elemental única, seu desafio é criar um modelo de machine learning para prever essa afinidade. Os feiticeiros podem pertencer a um dos quatro elementos mágicos: Fogo, Água, Terra ou Ar. A predição será baseada em cinco atributos mágicos: intensidade do feitiço, presença de componente raro, fase lunar, idade do feiticeiro e afinidade com animais mágicos.

  **Entrada**: Seu código deve receber as seguintes entradas do usuário: Intensidade do feitiço, Componente raro, Fase lunar, Idade do feiticeiro e Afinidade com animais mágicos.

  **Saída**: O código deve produzir uma saída indicando a afinidade elemental prevista do feiticeiro com base nos atributos fornecidos.
