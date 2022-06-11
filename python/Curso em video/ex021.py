import pygame
pygame.init()
pygame.mixer.music.load('test.mkv')
pygame.mixer.music.play()
pygame.event.wait()