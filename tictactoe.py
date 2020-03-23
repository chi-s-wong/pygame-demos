# Tic-Tac-Toe
# pyGame Demo
# Chi S. Wong

# Installation Instructions
# Download Python 3.6+: https://www.python.org/downloads/
# Install PyGame: https://www.pygame.org/wiki/GettingStarted

# Import important libraries
import pygame
import sys
from pygame.locals import *

# Initialize global variables
# First player starts as X
player = "X"
# Holds the state of the board
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]
# The winner of the game, X or O
winner = None

# ----- Run the game ------
# Start up libraries
pygame.init()
# Window size: 600 x 630 (width x height)
screen = pygame.display.set_mode((600, 630))
# White screen
screen.fill((255, 255, 255))
# Set window title
pygame.display.set_caption("Tic Tac Toe")


# ----- Draw the board and lines ------
# pygame.draw.line(surface, color, start_pos, end_pos, [width])

# Vertical lines
pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600))
pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600))

# Horizontal lines
pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200))
pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400))

# ----- Draw an X or O ------
""" 
pygame.draw.circle(screen, (0, 0, 0), (100, 100), 80, 2)

centerX = 100
centerY = 100
offset = 60
pygame.draw.line(screen, (0, 0, 0), 
                (centerX - offset, centerY - offset), 
                (centerX + offset, centerY + offset), 
                2)
pygame.draw.line(screen, (0, 0, 0), 
                (centerX - offset, centerY + offset), 
                (centerX + offset, centerY - offset), 
                2)

 """

# ----- Draw labels at the top left of each cell -----
def drawLabels(screen):
    labels = []
    for i in range(1, 10):
        font = pygame.font.Font(None, 30)
        labels.append(font.render(str(i), 1, (10,10,10)))
    
    for i in range(3):
        for j in range(3):
            x = (i * 200) + 5
            y = (j * 200) + 5
            # pygame.Surface.fill(color, rect=None, special_flags=0) 
            screen.fill((250, 250, 250), (x, y, 20, 30))
            # pygame.Surface.blit(source, dest, area=None, special_flags=0) 
            screen.blit(labels[i + (j*3)], (x, y))

    # pygame.Rect(left, top, width, height) 
    
""" Draw status bar at the bottom of the board
Reflects the current status of the game
"""


def drawStatus(screen):
    # Gain access to global variables
    global player, winner

    # Determine the status message
    if (winner is None):
        message = player + "'s turn"
    else:
        message = winner + " won!"

    # Render the status message
    # pygame.Font(filename, size)
    font = pygame.font.Font(None, 30)
    # font.render(text, antialias, color)
    text = font.render(message, 1, (10, 10, 10))

    # Copy the rendered message onto the screen
    screen.fill((250, 250, 250), (0, 600, 300, 25))
    screen.blit(text, (10, 600))


""" Returns the mouse position based on which cell in the 3x3 board it belongs to 

       0 100 200 300 400 500 (px)
100      1    |   2   |   3  
         --------------------
300      4    |   5   |   6  
         --------------------
500      7    |   8   |   9 
"""


def boardPos(mouseX, mouseY):
    # Row, Column of cell mouse clicked on
    row = 0
    col = 0

    # Height (y) is 600px high, divide by 3 to mark horizontal lines at 200px intervals
    # Break up mouse up/down position into thirds
    if (mouseY < 200):
        row = 0
    elif (mouseY < 400):
        row = 1
    else:
        row = 2

    # Width (x) is 600px wide, divide by 3 to mark vertical lines at 200px intervals
    # Break up mouse left/right position into thirds
    if (mouseX < 200):
        col = 0
    elif (mouseX < 400):
        col = 1
    else:
        col = 2

    return row, col


""" Draw an X or O depending on cell """


def drawMove(screen, boardRow, boardCol, move):
    symbolColor = pygame.Color(192, 192, 192)
    centerX = (boardCol * 200) + 100
    centerY = (boardRow * 200) + 100

    if (move == "O"):
        # pygame.draw.circle(surface, color, center, radius, width)
        pygame.draw.circle(screen, symbolColor, (centerX, centerY), 80, 2)
    else:
        offset = 60
        pygame.draw.line(screen,
                         symbolColor,
                         (centerX - offset, centerY - offset), # bottom left
                         (centerX + offset, centerY + offset), # top right 
                         3)
        pygame.draw.line(screen,
                         symbolColor,
                         (centerX - offset, centerY + offset), # top left
                         (centerX + offset, centerY - offset), # bottom right
                         3)


""" Change board by drawing move """


def clickBoard():
    # Access global variables
    global board, player

    # Grab position of mouse click
    (mouseX, mouseY) = pygame.mouse.get_pos()
    # Convert into cell clicked
    (row, col) = boardPos(mouseX, mouseY)

    # Assign symbol to cell in board if untouched
    if board[row][col] == None:
        board[row][col] = player
        drawMove(screen, row, col, player)
        if player == "X":
            player = "O"
        else:
            player = "X"


""" Check if winning move has been made 
Draw red line to mark winning formation
Update winner variable for status bar
"""


def checkWinner():
    global board, winner

    if winner is None:
        width = 10
        # Check for winning row
        for row in range(3):
            if (board[row][0] == board[row][1] == board[row][2] and
                    (board[row][0] is not None)):
                # Draw the ilne through winning row
                pygame.draw.line(screen, (250, 0, 0, 128), (0, (row * 200) + 100),
                                 (600, (row*200) + 100), width)
                winner = board[row][0]
                break

        # Check for winning col
        for col in range(3):
            if (board[0][col] == board[1][col] == board[2][col] and
                    (board[0][col] is not None)):
                # Draw the ilne through winning row
                pygame.draw.line(screen, (250, 0, 0, 128), ((col * 200) + 100, 0),
                                 ((col*200) + 100, 600), width)
                winner = board[0][col]
                break

        # Check for top-left to bottom-right diagonal
        if (board[0][0] == board[1][1] == board[2][2] and
                (board[0][0] is not None)):
            # Draw the ilne through winning row
            pygame.draw.line(screen, (250, 0, 0, 128), (0, 0),
                             (600, 600), width)
            winner = board[0][0]

        # Check for bottom-left to top-right diagonal
        if (board[2][0] == board[1][1] == board[0][2] and
                (board[2][0] is not None)):
            # Draw the ilne through winning row
            pygame.draw.line(screen, (250, 0, 0, 128), (0, 600),
                             (600, 0), width)
            winner = board[2][0]


""" Update screen and status bar at bottom """


def updateScreen(screen):
    drawStatus(screen)
    drawLabels(screen)
    pygame.display.update()


""" Start the game 
All of the code in this program runs until user exits program
"""
while True:
    for event in pygame.event.get():
        # If user clicks exit (X) button in window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # If user
        elif event.type is MOUSEBUTTONDOWN:
            # The user clicked; place an X or O
            clickBoard()

    checkWinner()
    updateScreen(screen)
