import pygame as pg
import os

pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

back = pg.image.load(r'C:\Users\bboya\OneDrive\Desktop\pp2\week7\background.jpg')

pg.font.init()
font = pg.font.Font(None, 36)

music_files = [
    (r"C:\Users\bboya\OneDrive\Desktop\pp2\week7\songs\cirrus-palence.mp3",
     r"C:\Users\bboya\OneDrive\Desktop\pp2\week7\covers\palence.jpg",
     "Cirrus - Palence"),
    
    (r"C:\Users\bboya\OneDrive\Desktop\pp2\week7\songs\Дорадура-Дора.mp3",
     r"C:\Users\bboya\OneDrive\Desktop\pp2\week7\covers\дора.jpeg",
     "Дорадура - Дора"),
    
    (r"C:\Users\bboya\OneDrive\Desktop\pp2\week7\songs\Нас-не-догонят-t.A.T.u.mp3",
     r"C:\Users\bboya\OneDrive\Desktop\pp2\week7\covers\tatu.jpg",
     "Нас не догонят - t.A.T.u")
]

current_track = 0
pg.mixer.music.load(music_files[current_track][0])
# click_sound = pg.mixer.Sound(r"C:\Users\bboya\OneDrive\Desktop\pp2\week7\songs\uletaiu-na-gaiti.mp3") # звук при смене трека
playing = False

def load_cover():
    try:
        return pg.image.load(music_files[current_track][1])
    except pg.error:
        return None

cover_img = load_cover()

def play_music():
    global playing
    pg.mixer.music.play(-1)
    playing = True

def pause_music():
    global playing
    if playing:
        pg.mixer.music.pause()
        playing = False
    else:
        pg.mixer.music.unpause()
        playing = True

def next_track():
    global current_track, cover_img
    # click_sound.play() # воспроизводим звук при смене трека
    current_track = (current_track + 1) % len(music_files)
    pg.mixer.music.load(music_files[current_track][0])
    play_music()
    cover_img = load_cover()

done = False

while not done:
    screen.blit(back, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                play_music()
            elif event.key == pg.K_RIGHT:
                next_track()
            elif event.key == pg.K_p:
                pause_music()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 350 <= x <= 450 and 450 <= y <= 650:
                play_music()
            elif 590 <= x <= 700 and 500 <= y <= 600:
                next_track()
            elif 100 <= x <= 180 and 500 <= y <= 590:
                pause_music()

    # Play triangle
    play_triangle = [(350, 450), (350, 650), (450, 550)]
    pg.draw.polygon(screen, black, play_triangle)

    # Pause button
    pg.draw.rect(screen, black, (150, 500, 30, 90))
    pg.draw.rect(screen, black, (100, 500, 30, 90))

    # Next button
    pg.draw.polygon(screen, black, [(650, 500), (650, 600), (700, 550)], 15)
    pg.draw.polygon(screen, black, [(590, 500), (590, 600), (640, 550)], 15)

    # Track title
    text_surface = font.render(music_files[current_track][2], True, black)
    screen.blit(text_surface, (400 - text_surface.get_width() // 2, 50))

    # Cover image
    if cover_img:
        cover_resized = pg.transform.scale(cover_img, (300, 300))
        screen.blit(cover_resized, (250, 100))

    pg.display.flip()
    clock.tick(60)

pg.quit()
