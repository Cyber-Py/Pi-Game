import os
import time
def printt(string, delay = 0.05):
  for j in string:
    print(j, end="", flush = True)
    time.sleep(delay)
  print('')
def clear():
  os.system('clear')
pidec = [ 4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1,6,9,3,9,9,3,7,5,1,0
  ]
printt('Welcome to the π Game!\n')
time.sleep(2)
clear()
while True:
  global PIFG
  global SOPI
  SOPI = '3.1'
  PIFG = '3.1'
  dl = 2
  for i in pidec:
    if i != pidec[48]:
      printt(f'{SOPI}{i}\n', 0.7)
      printt('Read it carefully')
      g = dl * 1.2
      time.sleep(g)
      clear()
      PIFG = PIFG + str(i)
      SOPI = SOPI + str(i)
      PIEBU = input('>')
      if PIEBU == PIFG:
        clear()
        printt('Correct! Next:\n')
        time.sleep(0.6)
        score = None
        score = SOPI
      elif PIEBU != PIFG:
        printt('Oh noes! You failed to enter the right π digit(s)! :(')
        score = SOPI
        break
    else:
      printt(f'{SOPI}{i}\n', 0.7)
      clear()
      time.sleep(g)
      printt('Just reminding you: Last digit!')
      PIFG = PIFG + str(i)
      SOPI = SOPI + str(i)
      PIEBU = input('>')
      time.sleep(0.5)
      if PIEBU == PIFG:
        printt('Impressive! You finished the game!')
        score = SOPI
        break
      elif PIEBU != PIFG:
        printt('Oh noes! So close! You failed to enter the right π digit(s)! :(')
        score = SOPI
        break
  break
time.sleep(2)
clear()
printt('This is how far you got!:')
print(score)


