import pyautogui
import clipboard
import threading
import keyboard
import os

# Instalar pip install pyautogui

#tempo para arrumar o programa

site1 = "https://nconsig.fenixsoft.com.br/Margem/ConsultaMargem.aspx"



entradas = input('Insira quantidade de elementos da planilia: ')
entradas2 = int(entradas)

def x():
   pyautogui.sleep(20)
   quantidadePlanilia = 0
   while quantidadePlanilia != entradas2 :
      
      pyautogui.keyDown('alt')
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.keyUp('alt')

      pyautogui.sleep(1)
      pyautogui.hotkey('ctrl', 's')
      pyautogui.hotkey('ctrl', 'c')  #pegava o cpf 
      pyautogui.press(['right'])     #e passava pro campo da matricula

      pyautogui.sleep(0.5)

      pyautogui.keyDown('alt')
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.keyUp('alt')

      pyautogui.hotkey('ctrl', 'v') #colava o cpf na pesquisa 
      pyautogui.press(['tab'])

      pyautogui.keyDown('alt')
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.keyUp('alt')

      pyautogui.hotkey('ctrl', 'c')
      pyautogui.press(['right'])

      pyautogui.sleep(0.5)

      pyautogui.keyDown('alt')
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.keyUp('alt')

      pyautogui.hotkey('ctrl', 'v') #colava a matricula na pesquisa

      pyautogui.sleep(0.5)
                        
      contador1 = 0
      while contador1 != 10:
         pyautogui.press(['tab']) #alternava até ficar em cima do botão de pesquisar
         contador1 += 1
      
      pyautogui.sleep(0.5)

      pyautogui.press(['enter']) 

      pyautogui.hotkey('ctrl', 'shift', 'i')
      pyautogui.sleep(1)
      pyautogui.hotkey('ctrl', 'f')
      pyautogui.sleep(1)

      pyautogui.write("Erro de origem")
      pyautogui.sleep(1)
      pyautogui.press('enter')

      pyautogui.sleep(1)

      pyautogui.keyDown('shift')
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.keyUp('shift')

      pyautogui.sleep(2)

      pyautogui.press('enter')

      pyautogui.sleep(1)

      pyautogui.sleep(0.5)
      pyautogui.hotkey('ctrl', 'c')
      pyautogui.sleep(0.5)

      erro = clipboard.paste()
      erro2 = "white"

      if erro == erro2:
         pyautogui.hotkey('ctrl', 'shift', 'i') 
         pyautogui.sleep(1.5)
         pyautogui.hotkey('alt', 'left')
         pyautogui.sleep(0.5)
         pyautogui.pres(['tab'])

         pyautogui.sleep(0.5)
         pyautogui.keyDown('alt')
         pyautogui.sleep(0.5)
         pyautogui.press(['tab'])
         pyautogui.sleep(0.5)
         pyautogui.keyUp('alt')

         pyautogui.sleep(0.5)
         pyautogui.write("Erro")

         pyautogui.hotkey('ctrl', 'left')
         pyautogui.press(['down'])

         pyautogui.sleep(0.5)
         pyautogui.keyDown('alt')
         pyautogui.sleep(0.5)
         pyautogui.press(['tab'])
         pyautogui.sleep(0.5)
         pyautogui.keyUp('alt')
      else:
         pyautogui.sleep(1)

         pyautogui.hotkey('ctrl', 'shift', 'i')
         pyautogui.hotkey('ctrl', 'l')
         pyautogui.sleep(1.5)
         pyautogui.hotkey('ctrl', 'c')
         site = clipboard.paste()
         
         if site == site1:
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])    
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])    
            pyautogui.sleep(0.5)
            pyautogui.press('enter') 

            pyautogui.sleep(0.5)
            pyautogui.press(['tab']) 

            pyautogui.sleep(0.5)
            pyautogui.keyDown('alt')
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.keyUp('alt') 

            pyautogui.write('naocontem')
            pyautogui.hotkey('ctrl', 'left')
            pyautogui.press(['down'])

            pyautogui.sleep(0.5)
            pyautogui.keyDown('alt')
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.keyUp('alt') 
            pass
         else:
            pyautogui.sleep(1)
            contador2 = 0
            
            while contador2 != 17:
             pyautogui.press(['tab']) 
             contador2 += 1
         
      
            pyautogui.sleep(0.5)

            pyautogui.hotkey('ctrl', 'c')
         
            pyautogui.sleep(0.5)
         
            pyautogui.press(['tab']) 
            pyautogui.press('enter') 

            pyautogui.sleep(0.5)
            pyautogui.press(['tab']) 


            pyautogui.keyDown('alt')               
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.keyUp('alt')

            pyautogui.hotkey('ctrl', 'v')

            pyautogui.hotkey('ctrl', 'left')
            pyautogui.press(['down'])

            pyautogui.keyDown('alt')
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.keyUp('alt')

      quantidadePlanilia += 1
   
   
      


# Função que para o programa caso clice na tecla especifica
def y():
   while(True):
      if keyboard.is_pressed('-'):
         pyautogui.hotkey('shift', 'alt')
         os._exit(0)
      
      
             
threading.Thread(target=x).start() ## Roda as duas funções ao mesmo tempo
threading.Thread(target=y).start() ## Roda as duas funções ao mesmo tempo







