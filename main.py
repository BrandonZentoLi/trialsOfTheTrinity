# import modules
import pygame, sys, cv2

# import our own logic from other ifles
from button import Button
from text_wrap import renderTextCenteredAt

pygame.init()

# display screen
size = (800, 450)
window = pygame.display.set_mode(size)
screen_width, screen_height = pygame.display.get_surface().get_size()

pygame.display.set_caption("Trials of the Trinity")
title_font = pygame.font.Font('fonts/pixel.ttf', 32)
text_font = pygame.font.Font('fonts/pixel.ttf', 15)

text = title_font.render('Trials of the Trinity', True, "#475F77")
textRect = text.get_rect(center = (screen_width // 2, 100))

capture = cv2.VideoCapture('resources/titlescreen.mp4')
_, image = capture.read()
shape = image.shape[1::-1]

# initialize variables
red = 255, 0, 0
fps = capture.get(cv2.CAP_PROP_FPS)

bookOfInsights = pygame.image.load("images/bookofinsights.jpg")
# titlescreen = pygame.image.load("titlescreen.jpg")
# titlescreen = pygame.transform.scale(titlescreen, size)

page_id = 'home'


def update_page_id(id):
    global page_id
    page_id = id


homeButton = Button('Home', 80, 40, (360, 350), 7,
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
    renderTextCenteredAt('Info Page', text_font, '#475F77', 250, 75, window, 200)
    renderTextCenteredAt('Trials of the Trinity is an interactive story in which you are a mortal that has angered the Big Three of the Olympian gods.', text_font, '#475F77', 250, 150, window, 200)
    

    homeButton.draw()


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
    text = title_font.render('Quiz Page', True, "#475F77")
    textRect = text.get_rect(center = (screen_width // 2, 100))
    window.blit(text, textRect)

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