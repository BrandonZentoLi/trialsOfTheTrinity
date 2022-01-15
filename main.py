# import modules
import pygame, cv2
from pygame import mixer

# import our own logic from other ifles
from button import Button
from textWrap import renderTextCenteredAt

pygame.init()

# display screen
size = (800, 450)
window = pygame.display.set_mode(size)
screen_width, screen_height = pygame.display.get_surface().get_size()

pygame.display.set_caption("Trials of the Trinity")
title_font = pygame.font.Font('fonts/pixel.ttf', 32)
text_font = pygame.font.Font('fonts/pixel.ttf', 15)

# playing music
mixer.init()
mixer.music.load('music/celesteMenuMusic.mp3')
mixer.music.play(-1)

# for the book of insight pages:
header_font = pygame.font.Font('fonts/pixel.ttf', 20)

text = title_font.render('Trials of the Trinity', True, "#475F77")
textRect = text.get_rect(center = (screen_width // 2, 100))

capture = cv2.VideoCapture('videos/titlescreen.mp4')
_, image = capture.read()
shape = image.shape[1::-1]

# initialize variables
red = 255, 0, 0
fps = capture.get(cv2.CAP_PROP_FPS)

bookOfInsights = pygame.image.load("images/bookofinsights.jpg")
left_page_x_pos = 250
left_page_y_pos = 125
right_page_x_pos = 550
right_page_y_pos = 125
book_width = 210
# titlescreen = pygame.image.load("titlescreen.jpg")
# titlescreen = pygame.transform.scale(titlescreen, size)

page_id = 'home'


def update_page_id(id):
    global page_id
    page_id = id

homeButton = Button('< Home', 80, 40, (20, 400), 7,
                    window, text_font, 'home', update_page_id)
instructionsButton = Button('Info', 80, 40, (160, 350), 7,
                            window, text_font, 'info', update_page_id)
lessonButton = Button('Lesson', 80, 40, (260, 350), 7,
                      window, text_font, 'lesson', update_page_id)
startButton = Button('Start', 80, 40, (360, 350), 7, window,
                     text_font, 'start', update_page_id)
quizButton = Button('Quiz', 80, 40, (460, 350), 7, window,
                    text_font, 'quiz', update_page_id)
quitButton = Button('Quit', 80, 40, (560, 350), 7, window,
                    text_font, 'quit', update_page_id)
nextPageButton = Button('Next >', 80, 40, (700, 400), 7, window, 
                    text_font, 'next', update_page_id)


# functions


def video_frames():
    success, image = capture.read()
    if success:
        surface = pygame.image.frombuffer(image.tobytes(), shape, "BGR")
        window.blit(surface, (0, 0))
    else:
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

def show_book_of_insights():
  window.blit(bookOfInsights, (0, 0))


def show_home():
    window.blit(text, textRect)
    instructionsButton.draw()
    lessonButton.draw()
    startButton.draw()
    quizButton.draw()
    quitButton.draw()


def show_info():
    renderTextCenteredAt('Info Page', header_font, '#475F77', left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("Trials of the Trinity is an interactive story in which you are a mortal that has angered the Big Three of the Olympian gods. Zeus, the God of the Sky - Poseidon, the God of the Sea - and Hades, the God of the Underworld. To punish you for what you have done, they've decided to give you a trial, and have teleported you to an island.", text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)
    
    renderTextCenteredAt("If you want to make it to tomorrow, you must survive the trials given to you by the gods. Pick your choices wisely, for your fate rests in your hands, mortal.",  text_font, '#475F77', right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    homeButton.draw()
    nextPageButton.draw()

def info_page_two():
  renderTextCenteredAt


def show_lesson():
    text = title_font.render('Lesson Page', True, "#475F77")
    textRect = text.get_rect(center = (screen_width // 2, 100))

    window.blit(text, textRect)

    homeButton.draw()


def show_start():
    text = title_font.render('Start Page', True, "#475F77")
    textRect = text.get_rect(center = (screen_width // 2, 100))

    window.blit(text, textRect)

    homeButton.draw()


def show_quiz():
    show_book_of_insights()
    renderTextCenteredAt('Quiz Page', header_font, '#475F77', left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    homeButton.draw()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        video_frames()
        # window.blit(titlescreen, (0, 0))

        if page_id == 'home':
            show_home()
        elif page_id == 'info':
            show_book_of_insights()
            show_info()
        elif page_id == 'lesson':
            show_book_of_insights()
            show_lesson()
        elif page_id == 'start':
            show_start()
        elif page_id == 'quiz':
            show_quiz()
        elif page_id == 'quit':
            run = False

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()