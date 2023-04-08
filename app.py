from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

# navega para a página do twitter com a pesquisa desejada
driver.get('https://twitter.com/search?q=drive.google.com&src=typed_query')

# aguarda até que a página esteja totalmente carregada
driver.implicitly_wait(10)


search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
search_box.send_keys('drive.google.com')
search_box.submit()

# Aqui você pode navegar pelos resultados da pesquisa
# Por exemplo, encontrar o primeiro link e clicar nele
first_link = driver.find_element('a')
first_link.click()

#dar 10 segundos de espera
driver.implicitly_wait(10)

# Quando terminar, feche a janela do navegador
driver.quit()
"""

# Comandos úteis

#Ir para determinado link

driver.get("link")

# Botão de voltar no navegador 

driver.back() 

# Botão de avançar no navegador 

driver.forward()

# Botão de fechar o navegador

driver.close()

# Botão de atualizar a página

driver.refresh()

"""

