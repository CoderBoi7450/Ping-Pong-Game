import pygame
import random
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

SCORE_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont(("comicsans"), 100)

PLAYER_VEL = 5
PLAYER_WIDTH, PLAYER_HEIGHT = 15, 70
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)






def player1_movemetns(player_1, key_pressed):
    # up
    if key_pressed[pygame.K_w] and player_1.y > 0:
        player_1.y -= PLAYER_VEL
    # down 
    if key_pressed[pygame.K_s] and player_1.y < HEIGHT - player_1.height:
        player_1.y += PLAYER_VEL
        
def player2_movemetns(player_2, key_pressed):
    # up
    if key_pressed[pygame.K_UP] and player_2.y > 0:
        player_2.y -= PLAYER_VEL
    # down 
    if key_pressed[pygame.K_DOWN] and player_2.y < HEIGHT - player_2.height:
        player_2.y += PLAYER_VEL

def draw_win(ball, player_1, player_2, player_1_score, player_2_score):
    WIN.fill(WHITE)

    player_1_text = SCORE_FONT.render(
        "SCORE: " + str(player_1_score), 1, BLACK
    )
    player_2_text = SCORE_FONT.render(
        "SCORE: " + str(player_2_score), 1, BLACK
    )

    WIN.blit(player_1_text, (10, 10))
    WIN.blit(player_2_text, (WIDTH - player_2_text.get_width() - 10, 10))

    pygame.draw.rect(WIN, BLACK, ball)
    pygame.draw.rect(WIN, BLACK, player_1)
    pygame.draw.rect(WIN, BLACK, player_2)

    pygame.display.update()


def draw_winner(winner_text):
    draw_text = WINNER_FONT.render(
        winner_text, 1, BLACK
    )
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(2000)


def main():
    ball_moves_y = [num for num in range(-3,4) if num != 0]
    ball_moves_x = [num for num in range (-8, 9) if num >=5]
    x_rand = random.choice(ball_moves_x)
    y_rand = random.choice(ball_moves_y)

    player_1_score = 0
    player_2_score = 0
    
    ball = pygame.Rect(WIDTH/2 - 10/2, HEIGHT/2, 10, 10)
    player_1 = pygame.Rect(25, HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
    player_2 = pygame.Rect(855, HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)

    


    clock = pygame.time.Clock()
    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        # handle collisions with borders and players
        if ball.y > HEIGHT - ball.height or ball.y < 0:
            y_rand = -y_rand

        if player_1.colliderect(ball):
            x_rand = -x_rand
        elif player_2.colliderect(ball):
            x_rand = -x_rand

        if ball.x < 0:
            player_2_score += 1
            ball.x = WIDTH/2 - 10/2
            ball.y = HEIGHT/2
        if ball.x > WIDTH:
            player_1_score += 1
            ball.x = WIDTH/2 - 10/2
            ball.y = HEIGHT/2

        # moving the ball
        ball.x += x_rand 
        ball.y += y_rand

        # displaying the winner
        winner_text = ""
        if player_1_score == 5:
            winner_text = "Player 1 Wins"
        
        if player_2_score == 5:
            winner_text = "Player 2 Wins"
        
        if winner_text != "":
            draw_winner(winner_text)
            break

        key_pressed = pygame.key.get_pressed()
        
        draw_win(ball, player_1, player_2, player_1_score, player_2_score) 
        player1_movemetns(player_1, key_pressed)
        player2_movemetns(player_2, key_pressed)

    main()
if __name__ == '__main__':
    main()