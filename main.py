import pygame
pygame.init()


# Create the clock object
clock = pygame.time.Clock()

win = pygame.display.set_mode((830, 600))
img = pygame.image.load('assets/gfx/Inner.png')
smol_img = pygame.Surface([16, 16]).convert()
smol_img.blit(img, (0, 0), (0, 0, 16, 16))
smol_img = pygame.transform.scale(smol_img, (64, 64))



run = True
while run:
    # Limit the framerate to ~120 fps
    clock.tick(120)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    win.blit(smol_img, (0, 0))

for y in range (15):
    for x in range(15):
        win.blit(smol_img, (x * 64,y * 0))
    for x in range(15):
        win.blit(smol_img, (x * 64,y * 64))
    for x in range(15):
        win.blit(smol_img, (x * 64,128))
    for x in range(15):
        win.blit(smol_img, (x * 64,192))
    for x in range(15):
        win.blit(smol_img, (x * 64,256))
    for x in range(15):
        win.blit(smol_img, (x * 64,320))
    for x in range(15):
        win.blit(smol_img, (x * 64,384))
    for x in range(15):
        win.blit(smol_img, (x * 64,448))
    for x in range (15):
        win.blit(smol_img, (x * 64,512))
    for x in range (15):
        win.blit(smol_img, (x * 64,576))


    pygame.display.update()

pygame.quit()