# import modules
import pygame
import cv2
from pygame import mixer

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

# playing music
mixer.init()
mixer.music.load('music/celesteMenuMusic.mp3')
mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# for the book of insight pages:
header_font = pygame.font.Font('fonts/pixel.ttf', 20)

text = title_font.render('Trials of the Trinity', True, "#475F77")
textRect = text.get_rect(center=(screen_width // 2, 100))

capture = cv2.VideoCapture('resources/titlescreen.mp4')
_, image = capture.read()
shape = image.shape[1::-1]

# initialize variables
red = 255, 0, 0
fps = capture.get(cv2.CAP_PROP_FPS)

bookOfInsights = pygame.image.load("resources/bookofinsights.jpg")
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

#Home Buttons
homeButtonOne = Button('< Home', 80, 40, (20, 400), 7,
                    window, text_font, 'home', update_page_id)
homeButtonTwo = Button('Home >', 80, 40, (700, 400), 7, window,
                           text_font, 'home', update_page_id)

#Info Buttons
infoPageOneButton = Button('Info', 80, 40, (160, 350), 7,
                            window, text_font, 'info_page_one', update_page_id)
infoPageTwoButton = Button('Next >', 80, 40, (700, 400), 7, window,
                        text_font, 'info_page_two', update_page_id)

#Book of Insights 
bookPageOneButton = Button('Lesson', 80, 40, (260, 350), 7,
                      window, text_font, 'book_page_one', update_page_id)
bookPageOneBackButton = Button('< Back', 80, 40, (20, 400), 7,
                      window, text_font, 'book_page_one', update_page_id)
bookPageTwoNextButton = Button('Next >', 80, 40, (700, 400), 7, window,
                           text_font, 'book_page_two', update_page_id)
bookPageTwoBackButton = Button('< Back', 80, 40, (20, 400), 7,
                      window, text_font, 'book_page_two', update_page_id)
bookPageThreeNextButton = Button('Next >', 80, 40, (700, 400), 7, window,
                             text_font, 'book_page_three', update_page_id)
bookPageThreeBackButton = Button('< Back', 80, 40, (20, 400), 7,
                      window, text_font, 'book_page_three', update_page_id)
bookPageFourNextButton = Button('Next >', 80, 40, (700, 400), 7, window,
                             text_font, 'book_page_four', update_page_id)
bookPageFourBackButton = Button('< Back', 80, 40, (20, 400), 7,
                      window, text_font, 'book_page_four', update_page_id)
bookPageFiveNextButton = Button('Next >', 80, 40, (700, 400), 7, window,
                             text_font, 'book_page_five', update_page_id)
bookPageFiveBackButton = Button('< Back', 80, 40, (20, 400), 7,
                      window, text_font, 'book_page_five', update_page_id)
bookPageSixNextButton = Button('Next >', 80, 40, (700, 400), 7, window,
                             text_font, 'book_page_six', update_page_id)
bookPageSixBackButton = Button('< Back', 80, 40, (20, 400), 7,
                      window, text_font, 'book_page_six', update_page_id)
bookPageSevenNextButton = Button('Next >', 80, 40, (700, 400), 7, window,
                             text_font, 'book_page_seven', update_page_id)

#Game Buttons
startButton = Button('Start', 80, 40, (360, 350), 7, window,
                     text_font, 'start', update_page_id)

#Quiz Buttons
quizButton = Button('Quiz', 80, 40, (460, 350), 7, window,
                    text_font, 'quiz', update_page_id)

#Quit Button
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
    infoPageOneButton.draw()
    bookPageOneButton.draw()
    startButton.draw()
    quizButton.draw()
    quitButton.draw()

#Info Pages
def info_page_one():

    show_book_of_insights()

    renderTextCenteredAt('Info Page', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("Trials of the Trinity is an interactive story in which you are a mortal that has angered the Big Three of the Olympian gods. Zeus, the God of the Sky - Poseidon, the God of the Sea - and Hades, the God of the Underworld. To punish you for what you have done, they've decided to give you a trial, and have teleported you to an island.",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)

    renderTextCenteredAt('Info Page', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("If you want to make it to tomorrow, you must survive the trials given to you by the gods. Pick your choices wisely, for your fate rests in your hands, mortal.",
                         text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width,)

    homeButtonOne.draw()
    infoPageTwoButton.draw()


def info_page_two():

    show_book_of_insights()

    renderTextCenteredAt('Info Page', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("There will be five different natural disasters you must conquer. Each disaster will ask for a choice. This decision will affect the overall outcome, sometimes with lasting effects.",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)

    renderTextCenteredAt('Info Page', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("In addition to choosing the right choice, the user will be prompted with a special item of their choice, courtesy of the gods - they grant you a guaranteed pass to the next level. While you can use these items at any point during the game, it is crucial you use it at the appropriate level. There is a chance that the item does absolutely nothing, so be prepared for that as well.",  text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width,)

    homeButtonOne.draw()


#Book of Insights Pages
def lessonOne():

    show_book_of_insights()

    renderTextCenteredAt('Book of', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("Welcome to the Book of Insights.", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)

    renderTextCenteredAt('Insights', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("Here, you can learn all about natural disasters to help overcome obstacles in the interactive story. Let’s get started!",
                         text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width,)

    homeButtonOne.draw()
    bookPageTwoNextButton.draw()


def lessonTwo():

    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("The tornado is the first natural disaster we’re going to explore. A violent rotating column of air, a tornado is deadly to anything that gets in the way. The column extends from the base of a thunderstorm down to the ground. Oftentimes, tornadoes are just a result of the four Anemoi having a fight amongst themselves. They have a pretty bad temper!",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)

    renderTextCenteredAt('Tornados', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("The best way to survive a tornado is to hide and stay in a sturdy building. Stay away from windows and doors, and get to the lowest floor (such as a basement). Always avoid being inside a vulnerable shelter, like a car or tent. In addition, get under something heavy within your shelter for extra protection.",
                         text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width,)

    bookPageOneBackButton.draw()
    bookPageThreeNextButton.draw()


def lessonThree():

    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("A volcano is an opening in the Earth’s crust through which an avalanche of lava, volcanic ash, and gases escape. One of the deadliest disasters, volcanoes are catastrophic during both the actual eruption phase, and the aftermath. Volcanic ash can cause damage thousands of kilometers away, including destroying crops, contaminating water supplies, while also causing respiratory problems for anyone with the misfortune of being caught in the ash.",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)

    renderTextCenteredAt('Volcanos', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("If you are caught in the initial wave of pyroclastic flow, there is little you could do.  However, you should always be aware of the residing ash in the air, which can be lethal to humans when inhaled. It’s advised to wear a mask or to cover your mouth during and after a volcanic eruption. Also, geothermal lands are especially prone to collapsing during a volcanic eruption, so avoid those at all costs!",
                         text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width,)

    bookPageTwoBackButton.draw()
    bookPageFourNextButton.draw()


def lessonFour():

    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("When the Earth rumbles and shakes, you know something is about to happen. Earthquakes are classified as days when the tectonic plates below us get into a fight. But one lingering question you might have is, who sent it? Was it Poseidon, the earthshaker - or was it Hades, the god of the underworld? It’s difficult to tell, so all you can do is flip a coin and hope you prayed to the right god!",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)

    renderTextCenteredAt('Earthquakes', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("Earthquakes are destructive natural disasters that are deadliest in a dense and civilized area. Buildings topple, cracks form - and you are left to wonder what you have done. Get somewhere as low as possible, like a basement, and hide under something heavy so falling debris is unlikely to hit you.",
                         text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width,)

    bookPageThreeBackButton.draw()
    bookPageFiveNextButton.draw()


def lessonFive():

    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("The tsunami is a natural disaster that occurs when tectonic plates under water get into an argument. I know, these tectonic plates are so troublesome and naughty!",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)

    renderTextCenteredAt('Tsunamis', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("Tsunamis are a wall of water rushing towards the shore. So what do you do? Get as far away from the water as possible, even if you can’t outrun it. Getting to as high of an elevation as possible might also be helpful. If you are dragged into the current, your best chance at survival is to find something floating and cling onto it. Your fate’s been sealed if Poseidon is having a bad hair day!",
                         text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width,)

    bookPageFourBackButton.draw()
    bookPageSixNextButton.draw()


def lessonSix():

    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("It’s not a good idea to make both Zeus and Poseidon mad! Forming over tropical waters, hurricanes (tropical cyclones) are a mixture of water and wind. They strengthen when it feeds on unstable air, such as turbulence and rising motion.",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)

    renderTextCenteredAt('Hurricanes', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("The safest place during a hurricane is the eye of the storm. It’s the calmest part during the storm, with light winds and fair weather. Stay away from any objects that can be lifted off the ground, and make sure to avoid drowning in water. That would be unfortunate.",
                         text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width,)

    bookPageFiveBackButton.draw()
    bookPageSevenNextButton.draw()


def lessonSeven():
    
    show_book_of_insights()

    renderTextCenteredAt('Book of', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("Congratulations! You made it through the Book of Insights.",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width,)

    renderTextCenteredAt('Insights', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width,)

    renderTextCenteredAt("The gods were betting you wouldn't be able to. By the way, Athena always had faith you would. She’s the goddess of wisdom for a reason.",
                         text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width,)

    bookPageSixBackButton.draw()
    homeButtonTwo.draw()


def show_start():
    text = title_font.render('Start Page', True, "#475F77")
    textRect = text.get_rect(center=(screen_width // 2, 100))

    window.blit(text, textRect)

    homeButtonOne.draw()


def show_quiz():
    text = title_font.render('Quiz Page', True, "#475F77")
    textRect = text.get_rect(center=(screen_width // 2, 100))
    window.blit(text, textRect)

    homeButtonOne.draw()


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

        #Info Pages 
        elif page_id == 'info_page_one':
            info_page_one()
        elif page_id == 'info_page_two':
            info_page_two()
        
        #Book of Insights Pages
        elif page_id == 'book_page_one':
            lessonOne()
        elif page_id == 'book_page_two':
            lessonTwo()
        elif page_id == 'book_page_three':
            lessonThree()
        elif page_id == 'book_page_four':
            lessonFour()
        elif page_id == 'book_page_five':
            lessonFive()
        elif page_id == 'book_page_six':
            lessonSix()
        elif page_id == 'book_page_seven':
            lessonSeven()
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
