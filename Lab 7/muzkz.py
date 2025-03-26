import pygame
import os

pygame.init()

pl = []
mf = "music"
for song in os.listdir(mf):
    if song.endswith(".mp3"):
        pl.append(os.path.join(mf, song))

sc = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Music Player")
cl = pygame.time.Clock()

backg = pygame.image.load(os.path.join("music elem", "backround.webp"))
plb = pygame.image.load(os.path.join("music elem", "play.png"))
pb = pygame.image.load(os.path.join("music elem", "pause.png"))
nb = pygame.image.load(os.path.join("music elem", "next.png"))
pvb = pygame.image.load(os.path.join("music elem", "back.png"))

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 20)

index = 0
aplay = False

pygame.mixer.music.load(pl[index])
pygame.mixer.music.play(1)
aplay = True

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_LEFT:
                index = (index - 1) % len(pl)
                pygame.mixer.music.load(pl[index])
                pygame.mixer.music.play()
                aplay = True

            elif event.key == pygame.K_RIGHT:
                index = (index + 1) % len(pl)
                pygame.mixer.music.load(pl[index])
                pygame.mixer.music.play()
                aplay = True

    text2 = font2.render(os.path.basename(pl[index]), True, (20, 20, 50))

    sc.blit(backg, (-50, 0))
    sc.blit(bg, (155, 500))
    sc.blit(text2, (365, 520))

    playb_resized = pygame.transform.scale(plb, (70, 70))
    pausb_resized = pygame.transform.scale(pb, (70, 70))
    nextb_resized = pygame.transform.scale(nb, (70, 70))
    prevb_resized = pygame.transform.scale(pvb, (75, 75))

    if aplay:
        sc.blit(pausb_resized, (370, 590))
    else:
        sc.blit(playb_resized, (370, 590))

    sc.blit(nextb_resized, (460, 587))
    sc.blit(prevb_resized, (273, 585))

    pygame.display.update()
    cl.tick(24)
