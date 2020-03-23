# Tic-Tac-Toe
# pyGame Demo
# Chi S. Wong

# Installation Instructions
# Download Python 3.6+: https://www.python.org/downloads/
# Install PyGame: https://www.pygame.org/wiki/GettingStarted

# import important libraries
import pygame
import sys
from pygame.locals import *

# initialize global variables
# X starts first
player = "X"
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]
winner = None 

# ----- Run the game ------
# Start up libraries
pygame.init()
# Window size: 600 x 630 (width x height)
screen = pygame.display.set_mode((600, 630))
# Black screen
screen.fill((255, 255, 255))
# Set window title
pygame.display.set_caption("Tic Tac Toe")


# ----- Draw the board and lines ------
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
 
# ----- Status bar -----
def drawStatus(board):
    # gain access to global variables
    global player, winner

    # determine the status message
    if (winner is None):
        message = player + "'s turn"
    else:
        message = winner + " won!"
        
    # render the status message
    font = pygame.font.Font(None, 30)
    text = font.render(message, 1, (10, 10, 10))

    # copy the rendered message onto the board
    board.fill ((250, 250, 250), (0, 600, 300, 25))
    board.blit(text, (10, 600))    


 # ----- Get clicked board position -----
def boardPos(mouseX, mouseY):
    row = 0
    col = 0

    if (mouseX < 200):
        col = 0
    elif (mouseX < 400):
        col = 1
    else:
        col = 2

    if (mouseY < 200):
        row = 0
    elif (mouseY < 400):
        row = 1
    else:
        row = 2
    
    # print(row +  col)
    return row, col

# ----- Draw an X or O depending on cell -----
def drawMove(screen, boardRow, boardCol, move):
    centerX = (boardCol * 200) + 100
    centerY = (boardRow * 200) + 100

    if (move == "O"):
        pygame.draw.circle(screen, (0, 0, 0), (centerX, centerY), 80, 2)
    else:
        offset = 60
        pygame.draw.line(screen, (0, 0, 0), 
                        (centerX - offset, centerY - offset), 
                        (centerX + offset, centerY + offset), 
                        3)
        pygame.draw.line(screen, (0, 0, 0), 
                        (centerX - offset, centerY + offset), 
                        (centerX + offset, centerY - offset), 
                        3)

# ----- Change grid to reflect move -----
def clickBoard():
    global board, player

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos(mouseX, mouseY)

    if board[row][col] == None:
        board[row][col] = player
        drawMove(board, row, col, player)
        if player == "X":
            player = "O"
        else:
            player = "X"
       

# ----- Check if winning move has been made ------    
def checkWinner():
    global board, winner 

    if winner is None:
        for row in range(3):
            if (board[row][0] == board[row][1] == board[row][2] and \
                (board[row][0] is not None)):
                # Draw the ilne through winning row
                pygame.draw.line(screen, (250, 0, 0, 128), (0, (row * 200) + 100), \
                                (600, (row*200) + 100))
                winner = board[row][0]
                break

        for col in range(3):
            if (board[0][col] == board[1][col] == board[2][col] and \
                (board[0][col] is not None)):
                # Draw the ilne through winning row
                pygame.draw.line(screen, (250, 0, 0, 128), ((col * 200) + 100, 0), \
                                ((col*200) + 100, 600))
                winner = board[0][col]
                break
        
        if (board[0][0] == board[1][1] == board[2][2] and \
            (board[0][0] is not None)):
                # Draw the ilne through winning row
                pygame.draw.line(screen, (250, 0, 0, 128), (0, 0), \
                                (600, 600))
                winner = board[0][0]
        
        if (board[2][0] == board[1][1] == board[0][2] and \
            (board[2][0] is not None)):
                # Draw the ilne through winning row
                pygame.draw.line(screen, (250, 0, 0, 128), (0, 600), \
                                (600, 0))
                winner = board[2][0]    


# ----- Start game -----
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            clickBoard()

    drawStatus(screen)

    checkWinner()
    pygame.display.update()


# initialize board
# check if game is won
# change board on click
