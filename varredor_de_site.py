from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os


# Entrado no site
driver = webdriver.Chrome()
driver.get('https://clone-olx-devaprender.netlify.app/')
sleep(5)

# Varrendo os preços
precos = driver.find_elements(By.XPATH,"//span[@class='text-2xl font-bold text-gray-900']")

# Varrendo os produtos
produtos = driver.find_elements(By.XPATH,"//h3[@class='text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]']")

# Percorrendo os preços e produtos do site
for preco, produto in zip(precos, produtos):
    with open('preços.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{preco.text},{produto.text},{os.linesep}')







input('')