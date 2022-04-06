import pygame
import sys
import random

pygame.init()

font = pygame.font.SysFont(None, 50)
windowheight = 500
windowwidth = 450
boardcolor = (189, 189, 189)
black = (0, 0, 0)
screen = pygame.display.set_mode((windowwidth, windowheight))
clock = pygame.time.Clock()
pygame.display.set_caption("Sudoku")

class sudoku:

    def __init__(self):
        self.board = ([""]*81)

    def main(self):
        screen.fill(boardcolor)
        activekey = "1"

        while True:
            pygame.display.update()
            self.drawboard()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        activekey = "1"
                    elif event.key == pygame.K_2:
                        activekey = "2"
                    elif event.key == pygame.K_3:
                        activekey = "3"
                    elif event.key == pygame.K_4:
                        activekey = "4"
                    elif event.key == pygame.K_5:
                        activekey = "5"
                    elif event.key == pygame.K_6:
                        activekey = "6"
                    elif event.key == pygame.K_7:
                        activekey = "7"
                    elif event.key == pygame.K_8:
                        activekey = "8"
                    elif event.key ==  pygame.K_9:
                        activekey = "9"
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for x in range(0, 450, 50):
                        for y in range(0, 450, 50):
                            if pos[0] in range(x, x+50):
                                if pos[1] in range(y, y+50):
                                    print(f"x: {x}, y: {y}, x/50: {x/50}, y/50: {y/50}")
                                    if self.valid(((x, y)), activekey):
                                        self.drawmove((x, y), activekey)

    def valid(self, move, key):
        x = move[0]
        y = move[1]
        idx = x // 50 + y // 50 * 9
        board = self.board
        board[idx] = key
        print(board)
        return True

    def drawmove(self, pos, key):
        board = self.board
        board
        img = font.render(f"{key}", True, black)
        screen.blit(img, (pos[0]+8, pos[1]+5))
        pygame.display.update()

    def drawboard(self):
        pygame.draw.line(screen, black, (150, 0), (150, 450), 5)
        pygame.draw.line(screen, black, (300, 0), (300, 450), 5)
        pygame.draw.line(screen, black, (0, 150), (450, 150), 5)
        pygame.draw.line(screen, black, (0, 300), (450, 300), 5)
        blocksize = 50
        for x in range(0, windowwidth, blocksize):
            for y in range(0, 450, blocksize):
                rect = pygame.Rect(x, y, blocksize, blocksize)
                pygame.draw.rect(screen, black, rect, 1)
        for i in range(10):
            img = font.render(f"{i}", True, black)
            screen.blit(img, (5+i*45, 455))

if __name__ == "__main__":
    start = sudoku()
    start.main()    