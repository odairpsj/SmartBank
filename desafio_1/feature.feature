Feature: Desafio1

    Scenario: Cadastro Empregado

    Given Definir URL da API REST

    Given Quando enviando o POST do API endpoint
	When Quando enviar a requisição HTTP POST
    Then Recebe validação do HTTP da resposta do codigo 200
	And informações da resposta não seja vazio