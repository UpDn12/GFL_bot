
import pyautogui
import time

def StarLevel():
    # Ajelar la pantalla de un nivel
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.7)

    Mouse = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.7)
    RefCoor = Mouse
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)

    for i in range(20):
        pyautogui.keyDown('ctrlleft')
        pyautogui.scroll(-99999)
        pyautogui.keyUp('ctrlleft')
    time.sleep(2)
    #==================================================================
    # Mover al Comand Post-----comandPost
    pyautogui.moveTo(RefCoor)
    pyautogui.move(818,-248)
    ComandPost = pyautogui.position()
    pyautogui.moveTo(ComandPost)
    pyautogui.doubleClick(interval=1)
    # Desplegar primer echelon
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    Mouse = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1, interval=0.5)
    time.sleep(2)
    #======================================================================
    # Dezplegar segundo echelon-----Heliport
    pyautogui.moveTo(RefCoor)
    pyautogui.move(411,-190)
    Heliport = pyautogui.position()
    pyautogui.moveTo(Heliport)
    pyautogui.doubleClick(interval=1)
    # Desplegar primer echelon
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    Mouse = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1, interval=0.5)
    time.sleep(2)
    #=======================================================================
    # Empezar el nivel
    Mouse = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.7)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)
    # Resuply Echelon
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\Mision\EndRound.png', confidence = 0.98)
    pyautogui.moveTo(Heliport)
    time.sleep(2)
    pyautogui.click(clicks=2, interval=2)
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    Mouse = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)
    time.sleep(2)
    #Ejerir primer echelon para planificar
    pyautogui.moveTo(ComandPost)
    pyautogui.click(clicks=1)
    #=================================================================================
    # Set up planning mode
    #   planing mode
    Mouse = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.8)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)
    # select plan path
    # 1 node
    pyautogui.move(755, -186)
    pyautogui.click(clicks=1)
    # 2 node
    pyautogui.move(60,118)
    pyautogui.click(clicks=1)
    # 3 node
    pyautogui.move(0,63)
    pyautogui.click(clicks=1)
    # Ejecutar plan
    Select = pyautogui.locateOnScreen('assets\Mision\ExecutePlan.png', confidence = 0.9)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    #==============================================================================
    # Acabar la mision
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\Mision\ReturnToBaseButton.png', confidence = 0.8)
    time.sleep(2)
    pyautogui.click(clicks=1)
# Recibir t-doll
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\Mision\ShareButton.png', confidence = 0.8)
    pyautogui.click(clicks=2, interval=2)

def ChangeEchelon():
    #====================================================================
    #Mover a Echelon Formation
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\RetirarTDoll\AreasBottonSelect.png', confidence = 0.8)
    Mouse = pyautogui.locateOnScreen('assets\RetirarTDoll\AreasBottonSelect.png', confidence = 0.8)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)
    # Ir a Formation
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\RetirarTDoll\EchelonArea.png', confidence = 0.8)
    Mouse = pyautogui.locateOnScreen('assets\RetirarTDoll\EchelonArea.png', confidence = 0.8)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)
    #Cambiar echelon
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\ExMode\IsOnFormation.png', confidence = 0.8)# chequea si esta en la pestaña de formation
    #-------------------------------------------- cambiar de Uzi a Vector
    if (pyautogui.locateOnScreen('assets\ExMode\MicroUzi.png', confidence = 0.8) is not None):

        Mouse = pyautogui.locateOnScreen('assets\ExMode\MicroUzi.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)
        Mouse = None
        while Mouse is None:
            Mouse = pyautogui.locateOnScreen('assets\ExMode\FiltrarPor.png', confidence = 0.8)
        Mouse = pyautogui.locateOnScreen('assets\ExMode\FiltrarPor.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)
        Mouse = None
        while Mouse is None:
            Mouse = pyautogui.locateOnScreen('assets\ExMode\CincoEstrellas.png', confidence = 0.8)
        Mouse = pyautogui.locateOnScreen('assets\ExMode\CincoEstrellas.png', confidence = 0.95)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)

        Mouse = pyautogui.locateOnScreen('assets\ExMode\SMGFiltro.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)

        Mouse = pyautogui.locateOnScreen('assets\ExMode\ConfimBoton.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)
        time.sleep(1.5)

        Mouse = pyautogui.locateOnScreen('assets\ExMode\VectorCard.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)

        Mouse = None
        while Mouse is None:
            Mouse = pyautogui.locateOnScreen('assets\ExMode\Vector.png', confidence = 0.8)
    #-------------------------------------------- Cambiar de vector a Uzi
    elif (pyautogui.locateOnScreen('assets\ExMode\Vector.png', confidence = 0.8) is not None):

        Mouse = pyautogui.locateOnScreen('assets\ExMode\Vector.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)
        Mouse = None
        while Mouse is None:
            Mouse = pyautogui.locateOnScreen('assets\ExMode\FiltrarPor.png', confidence = 0.8)
        Mouse = pyautogui.locateOnScreen('assets\ExMode\FiltrarPor.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)
        Mouse = None
        while Mouse is None:
            Mouse = pyautogui.locateOnScreen('assets\ExMode\CuatroEstrellas.png', confidence = 0.8)
        Mouse = pyautogui.locateOnScreen('assets\ExMode\CuatroEstrellas.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)

        Mouse = pyautogui.locateOnScreen('assets\ExMode\SMGFiltro.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)

        Mouse = pyautogui.locateOnScreen('assets\ExMode\ConfimBoton.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)
        time.sleep(1.5)

        Mouse = pyautogui.locateOnScreen('assets\ExMode\MicroUziCard.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)

        Mouse = None
        while Mouse is None:
            Mouse = pyautogui.locateOnScreen('assets\ExMode\MicroUzi.png', confidence = 0.8)

    #Mover a Battle
    time.sleep(2)
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\RetirarTDoll\AreasBottonSelect.png', confidence = 0.8)
    Mouse = pyautogui.locateOnScreen('assets\RetirarTDoll\AreasBottonSelect.png', confidence = 0.8)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)

    Mouse = None
    while Mouse is None:
            Mouse = pyautogui.locateOnScreen('assets\RetirarTDoll\CombatArea.png', confidence = 0.9)
    Mouse = pyautogui.locateOnScreen('assets\RetirarTDoll\CombatArea.png', confidence = 0.9)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)

def SeleccionarMap():

    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\RetirarTDoll\AreasBottonSelect.png', confidence = 0.9)
    # Comprueba si esta en el modo de dificultad correcta
    if (pyautogui.locateOnScreen('assets\ExMode\EmergencyMod.png', confidence = 0.9) is not None):
        Mouse = pyautogui.locateOnScreen('assets\ExMode\EmergencyMod.png', confidence = 0.9)
        pyautogui.moveTo(Mouse)
        pyautogui.move(-100,0)
        pyautogui.click(clicks=1)
    
    #Seleciona el mapa
    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\ExMode\ExMap.png', confidence = 0.98)
    Mouse = pyautogui.locateOnScreen('assets\ExMode\ExMap.png', confidence = 0.98)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)

    Mouse = None
    while Mouse is None:
        Mouse = pyautogui.locateOnScreen('assets\ExMode\ConfirmBattle.png', confidence = 0.99)
    Mouse = pyautogui.locateOnScreen('assets\ExMode\ConfirmBattle.png', confidence = 0.99)
    pyautogui.moveTo(Mouse)
    pyautogui.click(clicks=1)

def RetireTDoll():
    time.sleep(2)
    # Verificas si aparece la opcion de retirar t-dll
    if (pyautogui.locateOnScreen('assets\RetirarTDoll\RetiriOpcionBoton.png', confidence = 0.8) is not None):
        Retire = pyautogui.locateOnScreen('assets\RetirarTDoll\RetiriOpcionBoton.png', confidence = 0.8)
        pyautogui.moveTo(Retire)
        pyautogui.click(clicks=1)
        # selecionar la opcion de select T-Doll
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\RetirarTDoll\SelectTDoll.png', confidence = 0.8)
        select = pyautogui.locateOnScreen('assets\RetirarTDoll\SelectTDoll.png', confidence = 0.8)
        pyautogui.moveTo(select)
        pyautogui.click(clicks=1)
        # Seleccionar todos los 2* doll
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\RetirarTDoll\SmartSelect.png', confidence = 0.8)
        smartselect = pyautogui.locateOnScreen('assets\RetirarTDoll\SmartSelect.png', confidence = 0.8)
        pyautogui.moveTo(smartselect)
        pyautogui.click(clicks=1)
        #=============3 STAR Tdolsl
        Mouse = pyautogui.locateOnScreen('assets\ExMode\FiltrarPor.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)

        Mouse = None
        while Mouse is None:
            Mouse = pyautogui.locateOnScreen('assets\ExMode\TresEstrellas.png', confidence = 0.8)
        Mouse = pyautogui.locateOnScreen('assets\ExMode\TresEstrellas.png', confidence = 0.95)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)

        Mouse = pyautogui.locateOnScreen('assets\ExMode\ConfimBoton.png', confidence = 0.8)
        pyautogui.moveTo(Mouse)
        pyautogui.click(clicks=1)
        time.sleep(1.5)

        while (pyautogui.locateOnScreen('assets\ExMode\TresEstrellasTDoll.png', confidence = 0.99) is not None):
            Mouse = pyautogui.locateOnScreen('assets\ExMode\TresEstrellasTDoll.png', confidence = 0.99)
            pyautogui.moveTo(Mouse)
            pyautogui.click(clicks=1)
        
        #===============*****************************************************
        # Seleccionar ok botton
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\RetirarTDoll\OkBotton.png', confidence = 0.8)
        okboton = pyautogui.locateOnScreen('assets\RetirarTDoll\OkBotton.png', confidence = 0.8)
        pyautogui.moveTo(okboton)
        pyautogui.click(clicks=1)
        # desmantelar
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\RetirarTDoll\DesmantelarBotton.png', confidence = 0.8)
        desmantelar = pyautogui.locateOnScreen('assets\RetirarTDoll\DesmantelarBotton.png', confidence = 0.8)
        pyautogui.moveTo(desmantelar)
        pyautogui.click(clicks=1)
        time.sleep(1)

        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)
        desmantelar = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)
        pyautogui.moveTo(desmantelar)
        pyautogui.click(clicks=1)
        time.sleep(5)

        # Ir a areas menu
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\RetirarTDoll\AreasBottonSelect.png', confidence = 0.8)
        AreasMenu = pyautogui.locateOnScreen('assets\RetirarTDoll\AreasBottonSelect.png', confidence = 0.8)
        pyautogui.moveTo(AreasMenu)
        pyautogui.click(clicks=1)
        # select ombat area
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\RetirarTDoll\CombatArea.png', confidence = 0.9)
        AreasMenu = pyautogui.locateOnScreen('assets\RetirarTDoll\CombatArea.png', confidence = 0.9)
        pyautogui.moveTo(AreasMenu)
        pyautogui.click(clicks=1)

        SeleccionarMap()


i = 1
while i <= 50:
    StarLevel()
    ChangeEchelon()
    SeleccionarMap()
    RetireTDoll()
    print("loop "+str(i))
    time.sleep(5)
    i+=1
