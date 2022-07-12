import pyautogui
import time
from prueba import *

def Open_Game():
    # ubicacion de la imagen del juego para abrirlo
    game_coor = pyautogui.locateOnScreen('assets\OpenGame\Icon_Game.png', confidence = 0.8)
    pyautogui.moveTo(game_coor)
    pyautogui.click(clicks=1)

def IniciarLobby():
    
    r = None
    while r is None:
        r = pyautogui.locateOnScreen('assets\OpenGame\Game_Start.png', confidence = 0.8)
    pyautogui.click(clicks=1)





GoCombatSeccion()
GoCampaignSeccion()
Isomer_select()
IsomerGame()
Select_LostLevel()

for i in range (1,3):
    StarLevel()
    Stablish()
    BeginOp()
    PlanningMode()
    TerminarTurno()
    RepetirBatalla()
