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
    #====================================================
    # Mover al comand post
    Begin = pyautogui.locateOnScreen('assets\Mision\StarOperation.png', confidence = 0.7)
    pyautogui.moveTo(Begin)
    # Mover a ComandPsot
    pyautogui.move(-365,-279)
    CoorComandPost = pyautogui.position()
    pyautogui.click(clicks=1)
    # Elejir primer echelon por defecto
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    OkBotton = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    pyautogui.moveTo(OkBotton)
    pyautogui.click(clicks=1)
    
    # Mover al helipuerto
    pyautogui.move(-579,-238)
    CoorHeliport = pyautogui.position()
    pyautogui.click(clicks=1)
    # Ejelir segundo echelon por defecto
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    OkBotton = pyautogui.locateOnScreen('assets\Mision\OkBotton.png', confidence = 0.7)
    pyautogui.moveTo(OkBotton)
    pyautogui.click(clicks=1)
    #====================================================
    # Empaezar el nivel
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
    # resuply segundo comand post echelon------------
    pyautogui.moveTo(CoorHeliport)
    pyautogui.click(clicks=2, interval=1)
    # Resuply segundo echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    resuply = pyautogui.locateOnScreen('assets\Mision\ResuplyBotton.png', confidence = 0.8)
    pyautogui.moveTo(resuply)
    pyautogui.click(clicks=1)
    time.sleep(1)
    # ============================================
    # Set up planning mode
    #     select primer echelon
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\EndRound.png', confidence = 0.98)
    time.sleep(2)
    pyautogui.moveTo(CoorComandPost)
    pyautogui.click(clicks=1)
    #   planing mode
    PlanMode = pyautogui.locateOnScreen('assets\Mision\PlanMode.png', confidence = 0.8)
    pyautogui.moveTo(PlanMode)
    pyautogui.click(clicks=1)
    # select plan path
    # 1 node
    pyautogui.move(742,-425)
    pyautogui.click(clicks=1)
    # 2 node
    pyautogui.move(-182,-76)
    pyautogui.click(clicks=1)
    # 2 node
    pyautogui.moveTo(CoorComandPost)
    pyautogui.click(clicks=1)
    #=====================================================
    # Ejecutar plan
    ExecutePlan = pyautogui.locateOnScreen('assets\Mision\ExecutePlan.png', confidence = 0.9)
    pyautogui.moveTo(ExecutePlan)
    pyautogui.click(clicks=1)
    #===================================================
    # Esperar para retirar
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\Mision\campaign\FinishBoundSpirit_1.png', confidence = 0.8)

    pyautogui.moveTo(CoorComandPost)
    pyautogui.click(clicks=1)

    # Pulsa retirar echelon
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

    # reiniciar mision
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