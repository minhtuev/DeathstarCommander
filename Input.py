global CurrentEvents
CurrentEvents = []
a = 1

while a == 1:
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_UP):
            CurrentEvents.append("Forward")
        elif (event.type == KEYDOWN and event.key == K_LEFT):
            CurrentEvents.append("Left")
        elif (event.type == KEYDOWN and event.key == K_RIGHT):
            CurrentEvents.append("Right")
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            CurrentEvents.append("Fire")
        elif (event.type == KEYDOWN and event.key == K_ESCAPE):
            a = 0
            sys.exit()
        else:
            pass
