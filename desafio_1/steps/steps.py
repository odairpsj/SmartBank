from behave import given, when, then, step
import requests

api_endpoints = {}
response_codes ={}
response_texts={}
request_bodies = {}
api_url_dummy=None

@given('Definir URL da API REST')
def step_impl(context):
    global api_url_dummy
    api_url_dummy = 'http://dummy.restapiexample.com/api/v1'
    pass

@given('Quando enviando o POST do API endpoint')
def step_impl(context):
    api_endpoints['POST_URL'] = api_url_dummy+'/create'
    pass    

@when('Quando enviar a requisição HTTP POST')
def step_impl(context):
    # sending get request and saving response as response object
    
    url = 'http://dummy.restapiexample.com/api/v1'
    json = {"name": "Andre","salary": "10000", "age": "33"}
    response = requests.get(url)
    response_texts['GET']=response.text
    # extracting response status_code
    statuscode = response.status_code
    response_codes['GET'] = statuscode
    pass

@then('Recebe validação do HTTP da resposta do codigo 200')
def step_impl(context):
    if(response_codes['GET']==200):
        pass

@then('informações da resposta não seja vazio')
def step_impl(context):
    if(response_texts['GET']):
        pass