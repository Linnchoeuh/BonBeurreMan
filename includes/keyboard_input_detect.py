keyboard_input = {
    "press" : False,
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
    "ESCAPE" : False,
    "o" : False,
    "b" : False,
    "j" : False,
    "e" : False,
    "c" : False,
    "t" : False,
    "i" : False,
    "n" : False
}
def keyboard_input_fonc(pygame):
    pressing = pygame.key.get_pressed()
    keyboard_input["press"] = False

    #z
    if pressing[pygame.K_z]:
        keyboard_input["z"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["z"] = False
        

    #s
    if pressing[pygame.K_s]:
        keyboard_input["s"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["s"] = False
        

    #q
    if pressing[pygame.K_q]:
        keyboard_input["q"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["q"] = False
        

    #d
    if pressing[pygame.K_d]:
        keyboard_input["d"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["d"] = False
        

    #UP
    if pressing[pygame.K_UP]:
        keyboard_input["UP"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["UP"] = False
        

    #DOWN
    if pressing[pygame.K_DOWN]:
        keyboard_input["DOWN"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["DOWN"] = False
        

    #LEFT
    if pressing[pygame.K_LEFT]:
        keyboard_input["LEFT"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["LEFT"] = False
        

    #RIGHT
    if pressing[pygame.K_RIGHT]:
        keyboard_input["RIGHT"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["RIGHT"] = False
        

    #SPACE
    if pressing[pygame.K_SPACE]:
        keyboard_input["SPACE"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["SPACE"] = False
        

    #LSHIFT
    if pressing[pygame.K_RSHIFT]:
        keyboard_input["RSHIFT"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["RSHIFT"] = False
        

    #RETURN
    if pressing[pygame.K_RETURN]:
        keyboard_input["RETURN"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["RETURN"] = False
        

    #ESCAPE
    if pressing[pygame.K_ESCAPE]:
        keyboard_input["ESCAPE"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["ESCAPE"] = False


    #o
    if pressing[pygame.K_o]:
        keyboard_input["o"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["o"] = False

    #b
    if pressing[pygame.K_b]:
        keyboard_input["b"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["b"] = False

    #j
    if pressing[pygame.K_j]:
        keyboard_input["j"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["j"] = False

    #e
    if pressing[pygame.K_e]:
        keyboard_input["e"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["e"] = False

    #c
    if pressing[pygame.K_c]:
        keyboard_input["c"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["c"] = False

    #t
    if pressing[pygame.K_t]:
        keyboard_input["t"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["t"] = False

    #i
    if pressing[pygame.K_i]:
        keyboard_input["i"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["i"] = False

    #n
    if pressing[pygame.K_n]:
        keyboard_input["n"] = True
        keyboard_input["press"] = True
    else:
        keyboard_input["n"] = False
    
    return keyboard_input


# key_name = [
#     "K_z",
#     "K_s",
#     "K_q",
#     "K_d",
#     "K_UP",
#     "K_DOWN",
#     "K_LEFT",
#     "K_RIGHT",
#     "K_SPACE",
#     "K_RSHIFT",
#     "K_RETURN",
#     "K_ESCAPE"
# ]