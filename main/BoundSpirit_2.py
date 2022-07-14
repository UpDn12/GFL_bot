import pyautogui
import time


def StarLevel():
    # Ajelar la pantalla de un nivel
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.7)

    PlanMode = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.7)
    pyautogui.moveTo(PlanMode)
    pyautogui.click(clicks=1)

    for i in range(20):
        pyautogui.keyDown('ctrlleft')
        pyautogui.scroll(-99999)
        pyautogui.keyUp('ctrlleft')
    time.sleep(2)
    #=============================================
    # Mover al comand post
    Begin = pyautogui.locateOnScreen('assets\Mision\campaign\ComandPostBoSp_25.png', confidence = 0.7)
    pyautogui.moveTo(Begin)
    CoorComandPost = pyautogui.position()
    pyautogui.click(clicks=1)
    # Elejir primer echelon por defecto
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    OkBotton = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    pyautogui.moveTo(OkBotton)
    pyautogui.click(clicks=1)
    #====================================================
    # Empezar el nivel
    Begin = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.7)
    pyautogui.moveTo(Begin)
    pyautogui.click(clicks=1)
    #====================================================
    # resuply primer comand post echelon-----------
    time.sleep(2)
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\EndRound.png', confidence = 0.98)
    time.sleep(2)
    pyautogui.moveTo(CoorComandPost)
    pyautogui.click(clicks=2, interval=1)
    # Resuply primer echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    resuply = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    pyautogui.moveTo(resuply)
    pyautogui.click(clicks=1)
    time.sleep(2)
    # Mover un noda arriba
    pyautogui.moveTo(CoorComandPost)
    pyautogui.move(-40,-78)
    pyautogui.click(clicks=1)
    time.sleep(2)
    # Mover al comand post
    pyautogui.moveTo(CoorComandPost)
    pyautogui.click(clicks=1)
    # seleccionar despliege
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\DeployButton.png', confidence = 0.8)
    deploy = pyautogui.locateOnScreen('assets\Mision\DeployButton.png', confidence = 0.8)
    pyautogui.moveTo(deploy)
    pyautogui.click(clicks=1)
    # Elejir segundo echelon por defecto
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    OkBotton = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    pyautogui.moveTo(OkBotton)
    pyautogui.click(clicks=1)
    # resuply segundo comand post echelon-----------
    time.sleep(2)
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\campaign\BoSp_2\SecondEchelon.png',grayscale =True ,confidence = 0.7)
    secondEchelon = pyautogui.locateOnScreen('assets\Mision\campaign\BoSp_2\SecondEchelon.png',grayscale =True ,confidence = 0.7)
    pyautogui.moveTo(secondEchelon)
    pyautogui.click(clicks=2, interval=1)
    # Resuply primer echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    resuply = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    pyautogui.moveTo(resuply)
    pyautogui.click(clicks=1)
    time.sleep(2)
    # ============================================
    # Set up planning mode
    #   planing mode
    PlanMode = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.8)
    pyautogui.moveTo(PlanMode)
    CoorPlanMode =  pyautogui.position()
    pyautogui.click(clicks=1)
    # select plan path
    # 1 node
    pyautogui.move(811,-82)
    pyautogui.click(clicks=1)
    # Selec first echelon
    pyautogui.move(-316,-222)
    pyautogui.click(clicks=1) 
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\SelectBotton.png', confidence = 0.8)
    Select = pyautogui.locateOnScreen('assets\Mision\SelectBotton.png', confidence = 0.8)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    pyautogui.moveTo(CoorPlanMode)
    # node
    pyautogui.move(380, -287)
    pyautogui.click(clicks=1)
    # 2 node
    pyautogui.move(94, -97)#+++++++++++++++++
    pyautogui.click(clicks=1)
    # Selec Second echelon
    pyautogui.move(66,152)
    pyautogui.click(clicks=1) 
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\SelectBotton.png', confidence = 0.8)
    Select = pyautogui.locateOnScreen('assets\Mision\SelectBotton.png', confidence = 0.8)
    pyautogui.moveTo(Select)
    pyautogui.click(clicks=1)
    pyautogui.moveTo(CoorPlanMode)
    # 3 node
    pyautogui.move(468, 108)
    pyautogui.click(clicks=1)
    # 4 node
    pyautogui.move(118, -53)
    pyautogui.click(clicks=1)
    #=====================================================
    # Ejecutar plan
    ExecutePlan = pyautogui.locateOnScreen('assets\Mision\ExecutePlan.png', confidence = 0.9)
    pyautogui.moveTo(ExecutePlan)
    pyautogui.click(clicks=1)

def FinishAndRestarLevel():
    # Acabar la mision
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\ReturnToBaseButton.png', confidence = 0.8)
    time.sleep(2)
    pyautogui.click(clicks=1)
# Recibir t-doll
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\ShareButton.png', confidence = 0.8)
    pyautogui.click(clicks=2, interval=2)
# Busccar el map
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\campaign\SpiritBotton.png', confidence = 0.8)
    SelecMap = pyautogui.locateOnScreen('assets\Mision\campaign\SpiritBotton.png', confidence = 0.8)
    pyautogui.moveTo(SelecMap)
    pyautogui.click(clicks=1)
#Iniciar mapa
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.8)
    ConfirmStar = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.9)
    pyautogui.moveTo(ConfirmStar)
    pyautogui.click(clicks=1)

def RetireTDoll():
    time.sleep(1)
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
        # delect map EDITABLE
        #   ejelir sharect connexion
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\campaign\ShCnx_Ch.png', confidence = 0.9)
        ShCx = pyautogui.locateOnScreen('assets\Mision\campaign\ShCnx_Ch.png', confidence = 0.9)
        pyautogui.moveTo(ShCx)
        pyautogui.click(clicks=1)
        # Busccar el map
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\campaign\SpiritBotton.png', confidence = 0.8)
        SelecMap = pyautogui.locateOnScreen('assets\Mision\campaign\SpiritBotton.png', confidence = 0.8)
        pyautogui.moveTo(SelecMap)
        pyautogui.click(clicks=1)
        #Iniciar mapa
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.8)
        ConfirmStar = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.9)
        pyautogui.moveTo(ConfirmStar)
        pyautogui.click(clicks=1)
        
def RegresarMenu():
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
    # delect map EDITABLE
    #   ejelir sharect connexion
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\campaign\ShCnx_Ch.png', confidence = 0.9)
    ShCx = pyautogui.locateOnScreen('assets\Mision\campaign\ShCnx_Ch.png', confidence = 0.9)
    pyautogui.moveTo(ShCx)
    pyautogui.click(clicks=1)
    # Busccar el map
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\campaign\SpiritBotton.png', confidence = 0.8)
    SelecMap = pyautogui.locateOnScreen('assets\Mision\campaign\SpiritBotton.png', confidence = 0.8)
    pyautogui.moveTo(SelecMap)
    pyautogui.click(clicks=1)
    #Iniciar mapa
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.8)
    ConfirmStar = pyautogui.locateOnScreen('assets\Mision\CombatLevel.png', confidence = 0.9)
    pyautogui.moveTo(ConfirmStar)
    pyautogui.click(clicks=1)




i = 1
while i <= 20:
    StarLevel()
    FinishAndRestarLevel()
    RetireTDoll()
    print("loop "+str(i))
    time.sleep(10)
    i+=1
