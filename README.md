# Desafio #1

## Pré Requisitos

1 - Instalar Visual Studio Code (https://visualstudio.microsoft.com/pt-br/downloads/)

2 - Instalar o Behave (https://pypi.org/project/behave/)

## Instruções

1 - Executar o comando 'pip install -r requirements.txt' no prompt comando

2 - Inserir os Imports no Visual Studio Code: 'import given, when, then, step, import requests'

3 - Executar o comando 'Behave' no prompt Comando dentro da pasta 'desafio_1'


## Observações
Efetuei as requests do CRUD e a mesma na maioria das vezes encontrava-se com erro na request de cadastro do empregado, porém, quando executava via postman não dava erro.


# Desafio Smartbank #2
## Pré requisitos


1. Instalar Appium (http://appium.io/downloads.html)
2. Instalar Adnroid Studio (https://developer.android.com/studio?hl=pt-br)
3. Instalar Visual Studio Code (https://code.visualstudio.com/download)


## Instruções

1. Configurar as váriaveis de ambiente: propriedades do sistema > path na váriaveis de ambientes > novo > indicar diretório das váriaveis build-tools
tools, platform-tools (essas váriaveis vão estar dentro do diretório da pasta SDK)
2. Baixar servidor do Appium através do comando: pip install Appium-Python-Client, no terminal
3. Após abrir o Appium configurar o diretório de váriaveis 
4. Startar servidor do Appium e iniciar a sesso do inspector
5. Informar as váriaveis do Desired Capability (preencher com o Json das váriaveis)
6. Ao abrir o Android Studio selecionar a opção Tools > AVD Manager
7. Executar no terminal o comando py.test + (nome do arquivo).py

## Observações

No meu caso ao criar um AVD maneger no Android Studio foi necessário baixar o emulador 8.0 do android que é a ultima verso da APK. 
