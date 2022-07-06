import urllib
import easygui
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")
texto = easygui.enterbox("Qual Mensagem deseja enviar?")
quantidade = easygui.enterbox("Para quantos números deseja enviar a mensagem?")

i = 0
while i < int(quantidade):

    numero = easygui.enterbox("Qual o número?")

    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"

    navegador.get(link)
    time.sleep(5)
    navegador.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)

    i = i + 1
    time.sleep(5)
