import pyautogui
import time

from pandas.io.formats.format import return_docstring
from pyautogui import press


def executar_tarefa(perg):
    if perg.lower() == "n":
        print("Retornando ao programa principal.")
        return
while True:
    print("Olá seja Bem-Vindo ao Descomplica Dev")
    print("-------------------------------------")
    print("Abrir Youtube[1]")
    print("Abrir Google[2]")
    print("Abrir ChatGPT[3]")
    print("Abrir VsCode[4]")
    print("Abrir Github[5]")
    print("Sair[6]")
    print("-------------------------------------")
    resp = int(input("Selecione uma opção"))
    if resp == 1:
        pyautogui.press("win")
        pyautogui.write("edge")
        pyautogui.press("enter")
        time.sleep(0.3)
        pyautogui.write("https://www.youtube.com/")
        pyautogui.press("enter")
    elif resp == 2:
        pyautogui.press("win")
        pyautogui.write("edge")
        pyautogui.press("enter")
    elif resp == 3:
        perg = str(input("Deseja pesquisar algo? SIM(S)/NÃO(N)"))
        if perg.lower() == "s":
            con_s = (input(""))
            pyautogui.press("win")
            pyautogui.write("edge")
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.write("https://chatgpt.com/")
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.write(con_s)
            pyautogui.press("enter")

        elif perg.lower() == "n":
            pyautogui.press("win")
            pyautogui.write("edge")
            pyautogui.press("enter")
            time.sleep(0.3)
            pyautogui.write("https://chatgpt.com/")
            pyautogui.press("enter")
    elif resp == 4:
        pyautogui.press("win")
        pyautogui.write("visual studio code")
        pyautogui.press("enter")
    elif resp == 5:
        pyautogui.press("win")
        pyautogui.write("edge")
        pyautogui.press("enter")
        time.sleep(0.3)
        pyautogui.write("https://github.com/rodrigo730")
        pyautogui.press("enter")
    elif resp == 6:
        print("Programa finalizado")
        break
