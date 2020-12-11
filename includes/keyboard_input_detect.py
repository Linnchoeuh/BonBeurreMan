keyboard_input = {
    "z" : False,
    "s" : False,
    "q" : False,
    "d" : False,
    "UP" : False,
    "DOWN" : False,
    "LEFT" : False,
    "RIGHT" : False,
    "SPACE" : False,
    "RSHIFT" : False,
    "RETURN" : False,
    "ESCAPE" : False
}
def keyboard_input_fonc(pygame):
    pressing = pygame.key.get_pressed()
    #z
    if pressing[pygame.K_z]:
        keyboard_input["z"] = True
    else:
        keyboard_input["z"] = False
        

    #s
    if pressing[pygame.K_s]:
        keyboard_input["s"] = True
    else:
        keyboard_input["s"] = False
        

    #q
    if pressing[pygame.K_q]:
        keyboard_input["q"] = True
    else:
        keyboard_input["q"] = False
        

    #d
    if pressing[pygame.K_d]:
        keyboard_input["d"] = True
    else:
        keyboard_input["d"] = False
        

    #UP
    if pressing[pygame.K_UP]:
        keyboard_input["UP"] = True
    else:
        keyboard_input["UP"] = False
        

    #DOWN
    if pressing[pygame.K_DOWN]:
        keyboard_input["DOWN"] = True
    else:
        keyboard_input["DOWN"] = False
        

    #LEFT
    if pressing[pygame.K_LEFT]:
        keyboard_input["LEFT"] = True
    else:
        keyboard_input["LEFT"] = False
        

    #RIGHT
    if pressing[pygame.K_RIGHT]:
        keyboard_input["RIGHT"] = True
    else:
        keyboard_input["RIGHT"] = False
        

    #SPACE
    if pressing[pygame.K_SPACE]:
        keyboard_input["SPACE"] = True
    else:
        keyboard_input["SPACE"] = False
        

    #LSHIFT
    if pressing[pygame.K_RSHIFT]:
        keyboard_input["RSHIFT"] = True
    else:
        keyboard_input["RSHIFT"] = False
        

    #RETURN
    if pressing[pygame.K_RETURN]:
        keyboard_input["RETURN"] = True
    else:
        keyboard_input["RETURN"] = False
        

    #ESCAPE
    if pressing[pygame.K_ESCAPE]:
        keyboard_input["ESCAPE"] = True
    else:
        keyboard_input["ESCAPE"] = False

    return keyboard_input


key_name = [
    "K_z",
    "K_s",
    "K_q",
    "K_d",
    "K_UP",
    "K_DOWN",
    "K_LEFT",
    "K_RIGHT",
    "K_SPACE",
    "K_RSHIFT",
    "K_RETURN",
    "K_ESCAPE"
]