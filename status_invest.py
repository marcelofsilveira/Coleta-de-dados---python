from selenium import webdriver
from time import sleep

URL = 'https://statusinvest.com.br/acoes/busca-avancada'

print('Fazendo requisição')
driver = webdriver.Chrome()
driver.get(URL)
sleep(1)

print('Buscando Elemento')
button _buscar = driver.find_element_by_xpath('//div/button[contains(@class, "find")]')

button_buscar.click()
sleep(2)

