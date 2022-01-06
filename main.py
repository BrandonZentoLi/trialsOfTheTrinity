# imports pygame, cv2 and time
import pygame, cv2, sys

# imports button class that we created
from button import Button

# initializes pygame
pygame.init()

# declares clock
clock = pygame.time.Clock()

# sets the caption and icon
pygame.display.set_caption("Trials of The Trinity")

# Assigning colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to width and height variable
capture = cv2.VideoCapture('videos/titlescreen.mp4')
_, image = capture.read()
shape = image.shape[1::-1]

# create the display surface object
# of specific dimension..e(width, height).
screen = pygame.display.set_mode(shape)

instructionsButton = Button('Info', 80, 40, (100, 300), 7)
lessonButton = Button('Lesson', 80, 40, (200, 300), 7)
startButton = Button('Start', 80, 40, (300, 300), 7)
quizButton = Button('Quiz', 80, 40, (400, 300), 7)
quitButton = Button('Quit', 80, 40, (500, 300), 7)

font = pygame.font.Font('fonts/pixel.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render('Trials of the Trinity', True, "#475F77")

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (350, 100)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      capture.release()
      pygame.quit()
      sys.exit()

  success, image = capture.read()
  if success:
    surface = pygame.image.frombuffer(image.tobytes(), shape, "BGR")
    screen.blit(surface, (0, 0))
  else:
    capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

  # copying the text surface object
  # to the display surface object
  # at the center coordinate.
  screen.blit(text, textRect)

  instructionsButton.draw()
  startButton.draw()
  lessonButton.draw()
  quizButton.draw()
  quitButton.draw()

  pygame.display.flip()
  clock.tick(24)