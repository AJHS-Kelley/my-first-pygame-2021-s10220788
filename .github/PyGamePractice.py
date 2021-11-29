


















# Setup Fonts
basicFont = pygame.font.SysFont(None, 48)

# Setup Text
text = basicFont.render('Hello, world!',True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centrex = windowSurface.get_rect().centrex
textRect.centery = windowSurface.get_rect().centery

# Draw background polygon onto the surface.
windowSurface.fill(WHITE)

# Draw a green polygon onto the surface.
pygame.draw.polyogn(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0,  106)))

# Draw blue lines on the windowSurface


