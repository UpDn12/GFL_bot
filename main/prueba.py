
from pydoc import cli
import time
import pyautogui
    # X:  488 Y:  429



    # Ingresa a la seccion de Combate
def GoCombatSeccion():
    # go to combat seccion
    combat_seccion = pyautogui.locateOnScreen('assets\Lobby\Bombat.png', confidence = 0.9)
    pyautogui.moveTo(combat_seccion)
    pyautogui.click(clicks=1)

    time.sleep(4)

# Selecciona campaña
def GoCampaignSeccion():
    
    Campain_seccion = pyautogui.locateOnScreen('assets\Mision\campaign\CampainMode.png', grayscale = True,confidence = 0.5)
    pyautogui.moveTo(Campain_seccion)
    pyautogui.click(clicks=1)
    time.sleep(3)

# selecciona el capitulo de Isomer
def Isomer_select():
    selectChapter = pyautogui.locateOnScreen('assets\Mision\campaign\DeepDive.png', grayscale = True,confidence = 0.9)
    pyautogui.moveTo(selectChapter)
    pyautogui.scroll(-10000)

    isomer = pyautogui.locateOnScreen('assets\Mision\campaign\Isomero.png', grayscale = True, confidence = 0.9)
    pyautogui.moveTo(isomer)
    pyautogui.click(clicks=1)
    time.sleep(2)

# Entra al capitulo de isomer
def IsomerGame():
    Isomer_game = pyautogui.locateOnScreen('assets\Mision\campaign\Isomero_ch.png', confidence = 0.9)
    pyautogui.moveTo(Isomer_game)
    pyautogui.click(clicks=1)
    time.sleep(5)

# Selecciona el nivel de farm
def Select_LostLevel():
    IsomerLevel = pyautogui.locateOnScreen('assets\Mision\campaign\Level_Isomero.png', confidence = 0.8)
    pyautogui.moveTo(IsomerLevel)
    pyautogui.click(clicks=1)

    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.8)
    ConfirmStar = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.9)
    pyautogui.moveTo(ConfirmStar)
    pyautogui.click(clicks=1)

# lo prepara con el zoom
def StarLevel():
        
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.8)

    PlanMode = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.9)
    pyautogui.moveTo(PlanMode)
    pyautogui.click(clicks=1)

    for i in range(20):
        pyautogui.keyDown('ctrlleft')
        pyautogui.scroll(-99999)
        pyautogui.keyUp('ctrlleft')
    time.sleep(2)
    
    Begin = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.8)
    pyautogui.moveTo(Begin)
    # Mover a ComandPsot
    pyautogui.move(-566,-350)
    pyautogui.click(clicks=1)
        
    # esperar para eljir echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)
    # Ejelir primer echelon por defecto
    OkBotton = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)
    pyautogui.moveTo(OkBotton)
    pyautogui.click(clicks=1)
    #=============================================================
    # Mover a helipueto arriba
    pyautogui.move(-625,-395)
    pyautogui.click(clicks=1)
    # esperar para eljir echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)
    # Ejelir segunto echelon por defecto
    pyautogui.moveTo(OkBotton)
    pyautogui.click(clicks=1)

    #=============================================================
    # Mover a helipueto abajo
    pyautogui.move(-505,-350)
    pyautogui.click(clicks=1)
    # esperar para eljir echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)
        # Ejelir tercer echelon por defecto
    pyautogui.moveTo(OkBotton)
    pyautogui.click(clicks=1)

    Begin = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.8)
    pyautogui.moveTo(Begin)
    pyautogui.click(clicks=1)

    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\EscapeObMision.png', confidence = 0.8)

    Begin = pyautogui.locateOnScreen('assets\Mision\EscapeObMision.png', confidence = 0.8)
    pyautogui.moveTo(Begin)
    pyautogui.click(clicks=1)

    time.sleep(2)

    #  Resuply the echelon
    PlanMode = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.9)
    pyautogui.moveTo(PlanMode)
    pyautogui.move(476,-298)
    pyautogui.click(clicks=2, interval=0.8)
    # esperar resuply botton
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    # resuply echelon
    resuply = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.9)
    pyautogui.moveTo(resuply)
    pyautogui.click(clicks=1)
    time.sleep(2)
    # move to plan mode
    PlanMode = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.9)
    pyautogui.moveTo(PlanMode)
    pyautogui.click(clicks=1)
    # plan path
    # 1 node
    pyautogui.move(290,-174)
    pyautogui.click(clicks=1)
    # 2 node
    pyautogui.move(75,53)
    pyautogui.click(clicks=1)
    # 3 node
    pyautogui.move(-127,-130)
    pyautogui.click(clicks=1)
    # 4 node
    pyautogui.move(207,-105)
    pyautogui.click(clicks=1)
    # esperar para cambiar
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\MoveCambio.png', confidence = 0.8)
    # Cambiar echelones
    CambioEchelon = pyautogui.locateOnScreen('assets\Mision\MoveCambio.png', confidence = 0.9)
    pyautogui.moveTo(CambioEchelon)
    pyautogui.click(clicks=1)
    # ejecutar lo planificado
    CambioEchelon = pyautogui.locateOnScreen('assets\Mision\ExecutePlan.png', confidence = 0.9)
    pyautogui.moveTo(CambioEchelon)
    pyautogui.click(clicks=1)

    # espera hasta el boton ternimar
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\campaign\FinishRround.png', confidence = 0.8)
    # se hubica donde el echelon
    despliege = pyautogui.locateOnScreen('assets\Mision\EndRound.png', confidence = 0.8)
    pyautogui.moveTo(despliege)
    pyautogui.move(-640,-330)
    pyautogui.click(clicks=1)
    # Pulsa retirar
    r = None
    while r is None:
       r = pyautogui.locateOnScreen('assets\Mision\RetirarEchelon.png', confidence = 0.8)

    despliege = pyautogui.locateOnScreen('assets\Mision\RetirarEchelon.png', confidence = 0.8)
    pyautogui.moveTo(despliege)
    pyautogui.click(clicks=1)

    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)

    despliege = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)
    pyautogui.moveTo(despliege)
    pyautogui.click(clicks=1)

    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\TerminateMision.png', confidence = 0.8)

    terminar = pyautogui.locateOnScreen('assets\Mision\TerminateMision.png', confidence = 0.8)
    pyautogui.moveTo(terminar)
    pyautogui.click(clicks=1)

    time.sleep(2)

    pyautogui.move(184,440)
    pyautogui.click(clicks=1)

i = 1
while i <= 10:
    StarLevel()
    print("loop "+str(i))
    time.sleep(10)
    i+=1
    
'''GoCombatSeccion()
GoCampaignSeccion()
Isomer_select()
IsomerGame()
Select_LostLevel()'''