# import modules
import pygame
import cv2
import random
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
main_channel = mixer.Channel(0)
main_music = mixer.Sound('music/celesteMenuMusic.mp3')
main_channel.set_volume(0.1)
main_channel.play(main_music, loops=-1)

start_channel = mixer.Channel(1)
start_music = mixer.Sound('music/emeraldStoryMusic.mp3')
start_channel.set_volume(0.1)

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

itemPage = pygame.image.load('resources/items.jpg')
stick = pygame.image.load('resources/stick.png')
fence = pygame.image.load('resources/fence.png')
vacuum = pygame.image.load('resources/vacuum.png')
board = pygame.image.load('resources/skateboard.png')
bubble = pygame.image.load('resources/bubble.png')
bookOfInsights = pygame.image.load("resources/bookofinsights.png")
left_page_x_pos = 250
left_page_y_pos = 125
right_page_x_pos = 550
right_page_y_pos = 125
book_width = 210

page_id = 'home'


def update_page_id(id):
    global page_id
    page_id = id


def choice1C_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.25:
        page_id = 'secret ending one'
    else:
        page_id = 'level two'


def choice2A_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.15:
        page_id = 'volcano ending one'
    else:
        page_id = 'level three'


def choice2B_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.75:
        page_id = 'volcano ending two'
    else:
        page_id = 'level three'

#FIX THIS 
def choice3A_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.25:
        page_id = 'level four'
    else:
        page_id = 'level four'


def choice3B_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.30:
        page_id = 'secret ending two'
    else:
        page_id = 'level four'


def choice3C_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.25:
        page_id = 'earthquake ending'
    elif chance >= 0.50:
        page_id = 'secret ending one'
    else:
        page_id = 'level four'


def choice4A_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.50:
        page_id = 'tsunami ending'
    else:
        page_id = 'level five'


def choice4B_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.30:
        page_id = 'tsunami ending'
    else:
        page_id = 'level five'


def choice4C_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.25:
        page_id = 'tsunami ending'
    else:
        page_id = 'level five'


def choice4E_chance():
    global page_id
    chance = random.uniform(0, 1)
    if chance <= 0.20:
        page_id = 'secret ending three'
    else:
        page_id = 'survival ending one'


# Home Buttons
homeButtonOne = Button('< Home', 80, 40, (20, 400), 7,
                       window, text_font, 'home', update_page_id)
homeButtonTwo = Button('Home >', 80, 40, (700, 400), 7,
                       window, text_font, 'home', update_page_id)

# Info Buttons
infoPageOneNextButton = Button(
    'Info', 80, 40, (160, 350), 7, window, text_font, 'info_page_one', update_page_id)
infoPageOneBackButton = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'info_page_one', update_page_id)
infoPageTwoButton = Button('Next >', 80, 40, (700, 400),
                           7, window, text_font, 'info_page_two', update_page_id)

# Book of Insights
bookPageOneButton = Button('Lesson', 80, 40, (260, 350),
                           7, window, text_font, 'book_page_one', update_page_id)
bookPageOneBackButton = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_one', update_page_id)
bookPageTwoNextButton = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_two', update_page_id)
bookPageTwoBackButton = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_two', update_page_id)
bookPageThreeNextButton = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_three', update_page_id)
bookPageThreeBackButton = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_three', update_page_id)
bookPageFourNextButton = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_four', update_page_id)
bookPageFourBackButton = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_four', update_page_id)
bookPageFiveNextButton = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_five', update_page_id)
bookPageFiveBackButton = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_five', update_page_id)
bookPageSixNextButton = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_six', update_page_id)
bookPageSixBackButton = Button(
    '< Back', 80, 40, (20, 400), 7, window, text_font, 'book_page_six', update_page_id)
bookPageSevenNextButton = Button(
    'Next >', 80, 40, (700, 400), 7, window, text_font, 'book_page_seven', update_page_id)

# Game Buttons
startButton = Button('Start', 80, 40, (360, 350), 7,
                     window, text_font, 'start', update_page_id)
stickButton = Button('Stick', 80, 40, (165, 230), 7,
                     window, text_font, 'stick', update_page_id)
fenceButton = Button('Fence', 80, 40, (268, 230), 7,
                     window, text_font, 'fence', update_page_id)
vacuumButton = Button('Vacuum', 80, 40, (375, 230), 7,
                      window, text_font, 'vacuum', update_page_id)
boardButton = Button('Board', 80, 40, (480, 230), 7,
                     window, text_font, 'board', update_page_id)
bubbleButton = Button('Bubble', 80, 40, (585, 230), 7,
                      window, text_font, 'bubble', update_page_id)

# Level One Buttons
levelOneButton = Button('Begin! >', 80, 40, (700, 400),
                        7, window, text_font, 'level one', update_page_id)
choice1A = Button('', 215, 150, (47, 250), 7, window,
                  text_font, 'tornado ending', update_page_id)
choice1B = Button('', 215, 150, (297, 250), 7, window,
                  text_font, 'level two', update_page_id)
choice1C = Button('', 215, 150, (547, 250), 7, window, text_font,
                  None, update_page_id, choice1C_chance)

# Level Two Buttons
choice2A = Button('', 215, 150, (100, 250), 7, window,
                  text_font, None, update_page_id, choice2A_chance)
choice2B = Button('', 215, 150, (500, 250), 7, window,
                  text_font, None, update_page_id, choice2B_chance)

# Level Three Buttons
choice3A = Button('', 215, 150, (47, 250), 7, window,
                  text_font, None, update_page_id, choice3A_chance)
choice3B = Button('', 215, 150, (297, 250), 7, window,
                  text_font, None, update_page_id, choice3B_chance)
choice3C = Button('', 215, 150, (547, 250), 7, window,
                  text_font, None, update_page_id, choice3C_chance)

# Level Four Buttons
choice4A = Button('', 250, 150, (150, 125), 7, window,
                  text_font, None, update_page_id, choice4A_chance)
choice4B = Button('', 250, 150, (410, 125), 7, window,
                  text_font, None, update_page_id, choice4B_chance)
choice4C = Button('', 215, 150, (47, 280), 7, window,
                  text_font, None, update_page_id, choice4C_chance)
choice4D = Button('', 215, 150, (297, 280), 7, window,
                  text_font, None, update_page_id)
choice4E = Button('', 215, 150, (547, 280), 7, window,
                  text_font, None, update_page_id, choice4E_chance)

# Quiz Buttons
quizButton = Button('Quiz', 80, 40, (460, 350), 7, window,
                    text_font, 'quiz', update_page_id)

# Question 1 Options
q1option1 = Button('Basement', 170, 30, (465, 150), 7, window,
                   text_font, 'question_2', update_page_id)
q1option2 = Button('On top of a mountain', 170, 30, (465, 200),
                   7, window, text_font, 'question_2', update_page_id)
q1option3 = Button('The Ocean', 170, 30, (465, 250), 7,
                   window, text_font, 'question_2', update_page_id)
q1option4 = Button('Underwater', 170, 30, (465, 300), 7,
                   window, text_font, 'question_2', update_page_id)

# Question 2 Options
q2option1 = Button('Go underwater', 170, 30, (465, 150), 7,
                   window, text_font, 'question_3', update_page_id)
q2option2 = Button('Hold on to something', 170, 30, (465, 200),
                   7, window, text_font, 'question_3', update_page_id)
q2option3 = Button('Swim away', 170, 30, (465, 250), 7,
                   window, text_font, 'question_3', update_page_id)

# Question 3 Options
q3option1 = Button('True', 170, 30, (465, 150), 7, window,
                   text_font, 'question_4', update_page_id)
q3option2 = Button('False', 170, 30, (465, 200), 7, window,
                   text_font, 'question_4', update_page_id)

# Question 4 Options
q4option1 = Button('Yes', 170, 30, (465, 150), 7, window,
                   text_font, 'question_5', update_page_id)
q4option2 = Button('No', 170, 30, (465, 200), 7, window,
                   text_font, 'question_5', update_page_id)
q4option3 = Button('Maybe??', 170, 30, (465, 250), 7, window,
                   text_font, 'question_5', update_page_id)

# Question 5 Options
q5option1 = Button('Eye of the Storm', 170, 30, (465, 150),
                   7, window, text_font, 'result', update_page_id)
q5option2 = Button('Through the hurricane', 170, 30, (465, 200),
                   7, window, text_font, 'result', update_page_id)
q5option3 = Button('Underwater again', 170, 30, (465, 250),
                   7, window, text_font, 'resul', update_page_id)
q5option4 = Button("I don't know??", 170, 30, (465, 300), 7,
                   window, text_font, 'resul', update_page_id)

# Quit Button
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


def show_items():
    window.blit(itemPage, (0, 0))


def show_home():
    window.blit(text, textRect)
    infoPageOneNextButton.draw()
    bookPageOneButton.draw()
    startButton.draw()
    quizButton.draw()
    quitButton.draw()


# Info Pages
def info_page_one():
    show_book_of_insights()

    renderTextCenteredAt('Info Page', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "Trials of the Trinity is an interactive story in which you are a mortal that has angered the Big Three of the Olympian gods. Zeus, the God of the Sky - Poseidon, the God of the Sea - and Hades, the God of the Underworld. To punish you for what you have done, they've decided to give you a trial, and have teleported you to an island.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt('Info Page', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "If you want to make it to tomorrow, you must survive the trials given to you by the gods. Pick your choices wisely, for your fate rests in your hands, mortal.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    homeButtonOne.draw()
    infoPageTwoButton.draw()


def info_page_two():
    show_book_of_insights()

    renderTextCenteredAt('Info Page', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "There will be five different natural disasters you must conquer. Each disaster will ask for a choice. This decision will affect the overall outcome, sometimes with lasting effects.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt('Info Page', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "In addition to choosing the right choice, the user will be prompted with a special item of their choice, courtesy of the gods - they grant you a guaranteed pass to the next level. While you can use these items at any point during the game, it is crucial you use it at the appropriate level. There is a chance that the item does absolutely nothing, so be prepared for that as well.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    infoPageOneBackButton.draw()
    homeButtonTwo.draw()


# Book of Insights Pages
def lessonOne():
    show_book_of_insights()

    renderTextCenteredAt('Book of', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt("Welcome to the Book of Insights.", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt('Insights', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "Here, you can learn all about natural disasters to help overcome obstacles in the interactive story. Let's get started!",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    homeButtonOne.draw()
    bookPageTwoNextButton.draw()


def lessonTwo():
    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "The tornado is the first natural disaster we're going to explore. A violent rotating column of air, a tornado is deadly to anything that gets in the way. The column extends from the base of a thunderstorm down to the ground. Oftentimes, tornadoes are just a result of the four Anemoi having a fight amongst themselves. They have a pretty bad temper!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt('Tornados', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "The best way to survive a tornado is to hide and stay in a sturdy building. Stay away from windows and doors, and get to the lowest floor (such as a basement). Always avoid being inside a vulnerable shelter, like a car or tent. In addition, get under something heavy within your shelter for extra protection.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    bookPageOneBackButton.draw()
    bookPageThreeNextButton.draw()


def lessonThree():
    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "A volcano is an opening in the Earth's crust through which an avalanche of lava, volcanic ash, and gases escape. One of the deadliest disasters, volcanoes are catastrophic during both the actual eruption phase, and the aftermath. Volcanic ash can cause damage thousands of kilometers away, including destroying crops, contaminating water supplies, while also causing respiratory problems for anyone with the misfortune of being caught in the ash.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt('Volcanos', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "If you are caught in the initial wave of pyroclastic flow, there is little you could do.  However, you should always be aware of the residing ash in the air, which can be lethal to humans when inhaled. It's advised to wear a mask or to cover your mouth during and after a volcanic eruption. Also, geothermal lands are especially prone to collapsing during a volcanic eruption, so avoid those at all costs!",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    bookPageTwoBackButton.draw()
    bookPageFourNextButton.draw()


def lessonFour():
    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "When the Earth rumbles and shakes, you know something is about to happen. Earthquakes are classified as days when the tectonic plates below us get into a fight. But one lingering question you might have is, who sent it? Was it Poseidon, the earthshaker - or was it Hades, the god of the underworld? It’s difficult to tell, so all you can do is flip a coin and hope you prayed to the right god!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt('Earthquakes', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "Earthquakes are destructive natural disasters that are deadliest in a dense and civilized area. Buildings topple, cracks form - and you are left to wonder what you have done. Get somewhere as low as possible, like a basement, and hide under something heavy so falling debris is unlikely to hit you.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    bookPageThreeBackButton.draw()
    bookPageFiveNextButton.draw()


def lessonFive():
    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "The tsunami is a natural disaster that occurs when tectonic plates under water get into an argument. I know, these tectonic plates are so troublesome and naughty!",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt('Tsunamis', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "Tsunamis are a wall of water rushing towards the shore. So what do you do? Get as far away from the water as possible, even if you can’t outrun it. Getting to as high of an elevation as possible might also be helpful. If you are dragged into the current, your best chance at survival is to find something floating and cling onto it. Your fate’s been sealed if Poseidon is having a bad hair day!",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    bookPageFourBackButton.draw()
    bookPageSixNextButton.draw()


def lessonSix():
    show_book_of_insights()

    renderTextCenteredAt('Surviving', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "It's not a good idea to make both Zeus and Poseidon mad! Forming over tropical waters, hurricanes (tropical cyclones) are a mixture of water and wind. They strengthen when it feeds on unstable air, such as turbulence and rising motion.",
        text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt('Hurricanes', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "The safest place during a hurricane is the eye of the storm. It's the calmest part during the storm, with light winds and fair weather. Stay away from any objects that can be lifted off the ground, and make sure to avoid drowning in water. That would be unfortunate.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    bookPageFiveBackButton.draw()
    bookPageSevenNextButton.draw()


def lessonSeven():
    show_book_of_insights()

    renderTextCenteredAt('Book of', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt("Congratulations! You made it through the Book of Insights.",
                         text_font, '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt('Insights', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    renderTextCenteredAt(
        "The gods were betting you wouldn't be able to. By the way, Athena always had faith you would. She's the goddess of wisdom for a reason.",
        text_font, '#475F77', right_page_x_pos, right_page_y_pos, window, book_width)

    bookPageSixBackButton.draw()
    homeButtonTwo.draw()


# Story Pages
def show_start():
    show_items()

    renderTextCenteredAt('Items', title_font, '#475F77',
                         screen_width // 2, left_page_y_pos - 40, window, book_width)

    stickButton.draw()
    fenceButton.draw()
    vacuumButton.draw()
    boardButton.draw()
    bubbleButton.draw()


def stick_page():
    renderTextCenteredAt('Stick turns into... a Lightning Rod!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    levelOneButton.draw()
    window.blit(stick, (200, 200))


def fence_page():
    renderTextCenteredAt('Fence turns into... a Durable Wall!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    levelOneButton.draw()
    window.blit(fence, (250, 150))


def vacuum_page():
    renderTextCenteredAt('Vacuum turns into... a Powerful Broom!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    levelOneButton.draw()
    window.blit(vacuum, (250, 150))


def board_page():
    renderTextCenteredAt('Board turns into... a Hoverboard!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    levelOneButton.draw()
    window.blit(board, (250, 150))


def bubble_page():
    renderTextCenteredAt('Bubble turns into an... Indestructible Shield!', title_font, '#475F77',
                         screen_width // 2, 75, window, 800)

    levelOneButton.draw()
    window.blit(bubble, (250, 150))


def level_one():

    renderTextCenteredAt(
        "Welcome to the beginning of the end. Zeus, unhappy with your actions, sends a large tornado hurtling your direction. What do you do?",
        header_font, '#475F77', 400, 50, window, 800)

    choice1A.draw()
    choice1B.draw()
    choice1C.draw()

    renderTextCenteredAt('Save a monkey!', header_font, '#FFFFFF', 154, 310, window, 200)
    renderTextCenteredAt('Explore a creepy shack', header_font, '#FFFFFF', 407, 310, window, 200)
    renderTextCenteredAt('Hide in a hole', header_font, '#FFFFFF', 655, 310, window, 200)


def level_two():
    renderTextCenteredAt("Woah! The volcano suddenly became active, and the ash hurries your way! Quick, make a choice!",
                         header_font, '#475F77', 400, 50, window, 800)
    choice2A.draw()
    choice2B.draw()

    renderTextCenteredAt('Craft a mask!', header_font, '#FFFFFF', 208, 310, window, 200)
    renderTextCenteredAt('Run from the ash', header_font, '#FFFFFF', 610, 310, window, 200)


def level_three():
    renderTextCenteredAt("That was close one. Gasping for air, you plead to the gods saying that you've learned your lesson, but no response comes. And to make matters worse, the ground below you starts shaking uncontrollably as you realize you are now being challenged with an earthquake.",
                         header_font, '#475F77', 400, 50, window, 800)

    choice3A.draw()
    choice3B.draw()
    choice3C.draw()

    renderTextCenteredAt('Hide in the shack', header_font, '#FFFFFF', 154, 310, window, 200)
    renderTextCenteredAt('Go into the dark cave', header_font, '#FFFFFF', 407, 310, window, 200)
    renderTextCenteredAt('Stop, drop, pray', header_font, '#FFFFFF', 655, 310, window, 200)   

def level_four():
    renderTextCenteredAt("After the earthquake, the ensuing aftershocks create a tsunami. Without warning, the first wave of the tsunami comes and submerges the land, and you are caught in it. There is no telling if a main wave will still rush towards you. What do you do?",
                         header_font, '#475F77', 400, 50, window, 800)

    choice4A.draw()
    choice4B.draw()
    choice4C.draw()
    choice4D.draw()
    choice4E.draw()

    renderTextCenteredAt('Swim to shore!', header_font, '#FFFFFF', 270, 175, window, 200)
    renderTextCenteredAt('Hang onto a drifting wood piece', header_font, '#FFFFFF', 538, 175, window, 200)   
    renderTextCenteredAt('Climb to the top of a palm tree', header_font, '#FFFFFF', 154, 340, window, 200)
    renderTextCenteredAt('Collect drifting materials', header_font, '#FFFFFF', 407, 340, window, 200)
    renderTextCenteredAt('Crawl to peak of volcano!', header_font, '#FFFFFF', 655, 340, window, 200)   


def tornado_ending():
    renderTextCenteredAt("You chose to go save the monkey. As you reach him, you pick him up and also realize that you're being picked up. Turns out, the tornado had caught up to you guys, so as you're flying through the air while cuddling with the baby monkey, some final thoughts flow through your head. I hope you end up meeting the Wizard of Oz!",
                         header_font, '#475F77', 400, 50, window, 800)


def volcano_ending_one():
    renderTextCenteredAt("After inhaling too much volcanic ash, you start coughing, and coughing, until you start losing consciousness. And slowly, as you leave this world, the last thought you will ever have is praying pathetically to the gods. A fiery blaze engulfs you, as the land below you reveals itself to be a dangerous geothermal area.",
                         header_font, '#475F77', 400, 50, window, 800)


def volcano_ending_two():
    renderTextCenteredAt("You die a fiery death, but at least you went down in style, by drowning in a pool of burning lava! The lava was a comfortable 1250°, just a little over your average hot tub. Yet again, you realize you shouldn't have stolen the Hades's pet dog, Cerberus.",
                         header_font, '#475F77', 400, 50, window, 800)


def earthquake_ending():
    renderTextCenteredAt("The ground below you cracks open and you fall into an endless pit. And that was when you realized you probably shouldn't have taken Hades' favourite helmet!",
                         header_font, '#475F77', 400, 50, window, 800)


def tsunami_ending():
    renderTextCenteredAt("Navigating the fully submerged island, you hear a loud sound as you turn around and discover a huge wave of water building up. With one final look at the sun, you apologize to the gods as you choke on water.",
                         header_font, '#475F77', 400, 50, window, 800)


def hurricane_ending():
    renderTextCenteredAt("The endless swirls of water, rain, and thunder eventually was too much for you to handle.",
                         header_font, '#475F77', 400, 50, window, 800)


def survival_ending_one():
    renderTextCenteredAt("You reach the peak of the volcano, but also carefully avoid falling in. And suddenly, a plane flies past you. Waving your hands like a madman, the pilot sees you and picks you up. You survived!",
                         header_font, '#475F77', 400, 50, window, 800)


def survival_ending_two():
    renderTextCenteredAt("The hurricane passes and you finally open your eyes. Hooray! You survived! The gods congratulate you and you go back to your normal life. This time, you shouldn't anger the gods.",
                         header_font, '#475F77', 400, 50, window, 800)


def secret_ending_one():
    renderTextCenteredAt("Praying, you beg Zeus to spare you. And suddenly, you are at Mount Olympus. You get on your knees, thanking the gods when you realize Zeus had something else in mind.",
                         header_font, '#475F77', 400, 50, window, 800)


def secret_ending_two():
    renderTextCenteredAt("Hiding in the cave, you think you are safe when you hear a low, grumbling voice behind you. Slowly turning around, you see the monstrosity which is the Minotaur. The two-horned creature grabs you and eats you for dinner. And that, kids, is why you should never enter a dark cave!",
                         header_font, '#475F77', 400, 50, window, 800)


def secret_ending_three():
    renderTextCenteredAt("Wondering how water levels could rise so high, you are submerged underwater where it is revealed that Poseidon has taken a liking towards you. You are made into an immortal and forced to work for Poseidon for the rest of your eternal life.",
                         header_font, '#475F77', 400, 50, window, 800)


def secret_ending_four():
    renderTextCenteredAt("You decided that you wanted to get revenge against the god, and with the supercharged lightning rod you attempted to attack Zeus. You realize at the last moment that Zeus is actually the god of lightning, and regret not taking the chance to live a peaceful life when you had the opportunity to.",
                         header_font, '#475F77', 400, 50, window, 800)

# Quiz Pages
def show_quiz():
    show_book_of_insights()

    renderTextCenteredAt('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt("Question 1: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt("Where is the best place to go when there's a tornado? ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    renderTextCenteredAt('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q1option1.draw()
    q1option2.draw()
    q1option3.draw()
    q1option4.draw()

    homeButtonOne.draw()


def show_question2():
    show_book_of_insights()

    renderTextCenteredAt('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt("Question 2: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt("When in water during a tsunami, what's the best course of action? ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    renderTextCenteredAt('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q2option1.draw()
    q2option2.draw()
    q2option3.draw()


    homeButtonOne.draw()


def show_question3():
    show_book_of_insights()

    renderTextCenteredAt('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt("Question 3: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt("True or False: Geothermal land is safe to cross during a volcanic eruption.", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    renderTextCenteredAt('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q3option1.draw()
    q3option2.draw()


    homeButtonOne.draw()


def show_question4():
    show_book_of_insights()

    renderTextCenteredAt('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt("Question 4: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt("In the event of an Earthquake, is it safe to take cover underneath a sturdy table?", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    renderTextCenteredAt('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q4option1.draw()
    q4option2.draw()
    q4option3.draw()


    homeButtonOne.draw()

def show_question5():
    show_book_of_insights()

    renderTextCenteredAt('Question:', header_font, '#475F77',
                         left_page_x_pos, left_page_y_pos - 40, window, book_width)

    renderTextCenteredAt("Question 5: ", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos, window, book_width)

    renderTextCenteredAt("If you're already caught in a hurricane, what's the safest place to head towards?", text_font,
                         '#475F77', left_page_x_pos, left_page_y_pos + 20, window, book_width)

    renderTextCenteredAt('Answers:', header_font, '#475F77',
                         right_page_x_pos, right_page_y_pos - 40, window, book_width)

    q5option1.draw()
    q5option2.draw()
    q5option3.draw()
    q5option4.draw()


    homeButtonOne.draw()


def main():
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        video_frames()
        # window.blit(titlescreen, (0, 0))

        if page_id == 'home':
            show_home()

        # Info Pages
        elif page_id == 'info_page_one':
            info_page_one()
        elif page_id == 'info_page_two':
            info_page_two()

        # Book of Insights Pages
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

        # Game Pages
        elif page_id == 'start':
            show_start()
        elif page_id == 'stick':
            stick_page()
        elif page_id == 'fence':
            fence_page()
        elif page_id == 'vacuum':
            vacuum_page()
        elif page_id == 'board':
            board_page()
        elif page_id == 'bubble':
            bubble_page()
        elif page_id == 'level one':
            level_one()
        elif page_id == 'level two':
            level_two()
        elif page_id == 'level three':
            level_three()
        elif page_id == 'level four':
            level_four()
        elif page_id == 'level five':
            pass
        elif page_id == 'tornado ending':
            tornado_ending()
        elif page_id == 'volcano ending one':
            volcano_ending_one()
        elif page_id == 'volcano ending two':
            volcano_ending_two()
        elif page_id == 'earthquake ending':
            earthquake_ending()
        elif page_id == 'tsunami ending':
            tsunami_ending()
        elif page_id == 'hurricane ending':
            hurricane_ending()
        elif page_id == 'survival ending one':
            survival_ending_one()
        elif page_id == 'survival ending two':
            survival_ending_two()
        elif page_id == 'secret ending one':
            secret_ending_one()
        elif page_id == 'secret ending two':
            secret_ending_two()
        elif page_id == 'secret ending three':
            secret_ending_three()
        elif page_id == 'secret ending four':
            secret_ending_four()

        # Quiz pages
        elif page_id == 'quiz':
            show_quiz()
        elif page_id == 'question_2':
            show_question2()
        elif page_id == 'question_3':
            show_question3()
        elif page_id == 'question_4':
            show_question4()
        elif page_id == 'question_5':
            show_question5()
        # Quit Page
        elif page_id == 'quit':
            run=False

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
