import pyautogui as pg
import keyboard as kb
import time

positionList = []
addKey = ""
startKey = ""

while True:
  if kb.is_pressed(addKey):
    positionList.append(pg.position())
    print("position added")
    time.sleep(0.1)
    continue
  if kb.is_pressed(startKey):
    print(str(len(positionList)) + " " + "positions enregistrées")
    print(positionList)
    break

while True:
  for i in positionList:
    pg.moveTo(i.x, i.y)
    pg.click()
    time.sleep(5)