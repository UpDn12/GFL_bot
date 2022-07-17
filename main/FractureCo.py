import pyautogui
import time


def StarLevel():
    # Ajelar la pantalla de un nivel
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.7)

    Select = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.7)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)

    for i in range(20):
        pyautogui.keyDown('ctrlleft')
        pyautogui.scroll(-99999)
        pyautogui.keyUp('ctrlleft')
    time.sleep(2)
    #====================================================================
    # Mover al comand post-------------------------
    Select = pyautogui.locateOnScreen('assets\Mision\campaign\FractureCop\ComandPost.png', confidence = 0.8)
    pyautogui.moveTo(Select)
    CoorComandPost = Select
    pyautogui.click(clicks=1)
    # Elejir primer echelon por defecto
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    Select = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    time.sleep(1)
    #====================================================================
    # Empezar el nivel
    Select = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.7)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)

    RetireTDoll()# LLamar funcion verificar si hay que retirar t-DOlls***************
    #=====================================================================
    # Resuply Figth Echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\EndRound.png', confidence = 0.98)
    pyautogui.moveTo(CoorComandPost)
    time.sleep(1)
    pyautogui.click(clicks=2, interval=1)
    # Confirm Resuply Echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    Select = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    time.sleep(2)
    #===================================================================
    # Mover un Nodo abajo
    pyautogui.moveTo(CoorComandPost)
    pyautogui.move(46,65)
    pyautogui.click(clicks=1)
    time.sleep(2)
    #======================================================================
    # Elejir segundo echelon por defecto
    pyautogui.moveTo(CoorComandPost)
    pyautogui.click(clicks=1)
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\DeployButton.png', confidence = 0.8)
    deploy = pyautogui.locateOnScreen('assets\Mision\DeployButton.png', confidence = 0.8)
    pyautogui.moveTo(deploy)
    pyautogui.click(clicks=1)
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    Select = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    time.sleep(2)
    # Escojer Primer Echelon
    Select = pyautogui.locateOnScreen('assets\Mision\campaign\FractureCop\FirstEchelon.png', confidence = 0.9)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    #======================================================================
    # Set up planning mode
    #   planing mode
    PlanMode = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.8)
    pyautogui.moveTo(PlanMode)
    CoorPlanMode =  pyautogui.position()
    pyautogui.click(clicks=1)
    # select plan path
    # 1 node
    pyautogui.move(573, -197)
    pyautogui.click(clicks=1)
    # 2 node
    CmPs = pyautogui.move(-110, -32)
    pyautogui.moveTo(CmPs)
    pyautogui.click(clicks=1)
        # esperar para cambiar
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\MoveCambio.png', confidence = 0.8)
    # Cambiar echelones
    CambioEchelon = pyautogui.locateOnScreen('assets\Mision\MoveCambio.png', confidence = 0.9)
    pyautogui.moveTo(CambioEchelon)
    pyautogui.click(clicks=1)
    #========================================================================
    # Ejecutar plan
    Select = pyautogui.locateOnScreen('assets\Mision\ExecutePlan.png', confidence = 0.9)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    #================================================================================
    # Retirar Echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\campaign\FractureCop\FinishAttemp.png', confidence = 0.8)
    # se hubica donde el echelon
    
    pyautogui.moveTo(r)
    time.sleep(2)
    pyautogui.click(clicks=1)
    # Pulsa retirar
    r = None
    while r is None:
       r = pyautogui.locateOnScreen('assets\Mision\RetirarEchelon.png', confidence = 0.8)
    Select = pyautogui.locateOnScreen('assets\Mision\RetirarEchelon.png', confidence = 0.8)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)
    Select = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.8)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    # Repetir Mision
    time.sleep(2)
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\TerminateMision.png', confidence = 0.9)
    Select = pyautogui.locateOnScreen('assets\Mision\TerminateMision.png', confidence = 0.9)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    time.sleep(1)
    pyautogui.move(184,440)
    time.sleep(0.5)
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
        # delect map EDITABLE!!!!!!!!!!!!!!!!!!!!!!!!!
        #   ejelir sharect connexion
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\campaign\PolaLigth.png')
        ShCx = pyautogui.locateOnScreen('assets\Mision\campaign\PolaLigth.png')
        pyautogui.moveTo(ShCx)
        pyautogui.click(clicks=1)
        # Busccar el map Editarrrr1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\campaign\FractureCop\LevelMap.png', confidence = 0.8)
        SelecMap = pyautogui.locateOnScreen('assets\Mision\campaign\FractureCop\LevelMap.png', confidence = 0.8)
        pyautogui.moveTo(SelecMap)
        pyautogui.click(clicks=1)
        #Iniciar mapa
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.8)
        ConfirmStar = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.9)
        pyautogui.moveTo(ConfirmStar)
        pyautogui.click(clicks=1)

        # Ajelar la pantalla de un nivel
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.7)

        Select = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.7)
        pyautogui.moveTo(Select)
        pyautogui.click(clicks=1)

        for i in range(20):
            pyautogui.keyDown('ctrlleft')
            pyautogui.scroll(-99999)
            pyautogui.keyUp('ctrlleft')
        time.sleep(2)
        #===================================================
        # Mover al comand post-------------------------
        Select = pyautogui.locateOnScreen('assets\Mision\campaign\InSigh\CommandPost.png', confidence = 0.8)
        pyautogui.moveTo(Select)
        pyautogui.click(clicks=1)
        # Elejir primer echelon por defecto
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
        Select = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
        pyautogui.moveTo(Select)
        pyautogui.click(clicks=1)
        time.sleep(1)
        # Mover al Helipuerto------------------------
        Select = pyautogui.locateOnScreen('assets\Mision\campaign\InSigh\Heliport.png', confidence = 0.8)
        pyautogui.moveTo(Select)
        Heliport = Select
        pyautogui.click(clicks=1)
        # Elejir segundo echelon por defecto
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
        Select = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
        pyautogui.moveTo(Select)
        pyautogui.click(clicks=1)
        #====================================================
        # Empezar el nivel
        Select = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.7)
        pyautogui.moveTo(Select)
        pyautogui.click(clicks=1)

i = 1
while i <= 30:
    StarLevel()
    print("loop "+str(i))
    time.sleep(10)
    i+=1