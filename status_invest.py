from selenium import webdriver
from time import sleep

URL = 'https://statusinvest.com.br/acoes/busca-avancada'

print('Fazendo requisicao')
driver = webdriver.Chrome()
driver.get(URL)
sleep(1)

print('Buscando Elemento')
button_buscar = driver.find_element_by_xpath(
    '//div/button[contains(@class, "find")]')

button_buscar.click()
sleep(2)

#print('Fechando anuncio')
#button_fechar = driver.find_element_by_class_name('btn-close')
# button_fechar.click()
# sleep(1)

print('Baixando dados...')
button_download = driver.find_element_by_xpath(
    '//div/a[contains(@class, "btn-download")]')

button_download.click()
