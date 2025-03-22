import pygame
from datetime import datetime

def blitRotate(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, new_rect.topleft)

pygame.init()
screen = pygame.display.set_mode((500, 500))

bg = pygame.transform.scale(pygame.image.load("week7/mickeyclock.png"), (500, 500))

left_arm = pygame.image.load("week7/leftarm.png")
right_arm = pygame.image.load("week7/rightarm.png")

left_arm = pygame.transform.scale(left_arm, (left_arm.get_width() // 6, left_arm.get_height() // 6))
right_arm = pygame.transform.scale(right_arm, (right_arm.get_width() // 6, right_arm.get_height() // 6))

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    angle_min = -6 * minutes - 53
    angle_sec = -6 * seconds

    pos = (screen.get_width() / 2, screen.get_height() / 2)

    blitRotate(screen, left_arm, pos, angle_sec)
    blitRotate(screen, right_arm, pos, angle_min)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()