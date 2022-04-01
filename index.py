import pyautogui
from PIL import ImageGrab


print("Monitor Size: ", pyautogui.size())
print("Mouse Position: ", pyautogui.position())

# pyautogui.moveTo(294, 627)
# pyautogui.click() 

# with pyautogui.hold('ctrl'):
#   pyautogui.press('n')

# pyautogui.write('Hello world!')

# pyautogui.alert('Finish')

y_position = 650
x_position = 140

initialClick = (300, 770)
lines = 100
columns = 200
sheetColor = (124, 113, 44)
REGION = x_position, y_position, columns+x_position, lines+y_position

click = 'left'

pyautogui.click(x=initialClick[0], y=initialClick[1])
pyautogui.click(x=initialClick[0], y=initialClick[1])

for i in range(20):
  im = ImageGrab.grab(bbox=REGION)
  # im.save('test{}.png'.format(i))
  # print(im)
  forBreak = False
  for l in range(lines):
    for c in range(columns):
      if im.getpixel((c, l)) == sheetColor:
        print("c", c)
        if c < columns / 2:
          click = 'right'
        else:
          click = 'left'
        forBreak = True
        break
    if forBreak == True:
      break
  if click == 'left':
    pyautogui.click(x=x_position, y=y_position)
  else:
    pyautogui.click(x=x_position + columns, y=y_position)
  print("click", click)
  # print('test{}.png'.format(i))
