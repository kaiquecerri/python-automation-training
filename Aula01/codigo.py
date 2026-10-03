import pyautogui
import time
import pandas

pyautogui.PAUSE = 1
#VARIAVEIS
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "email@email.com"
senha = "senha1234"

tabela = pandas.read_csv("produtos.csv")


#ABRIR O NAVEGADOR
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

#ACESSAR A PAGINA
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1)

#LOGAR NA CONTA -> feito sem ver a aula
# pyautogui.press("tab")
# pyautogui.write(email)
# pyautogui.press("tab")
# pyautogui.write(senha)
# pyautogui.press("tab")
# pyautogui.press("enter")

#LOGAR NA CONTA
pyautogui.click(895, 325)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

#CADASTRAR ITENS
pyautogui.PAUSE = 0.1
for linha in tabela.index:
    pyautogui.click(844, 207)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))

   
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

