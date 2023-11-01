# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define w = Character("Werner", image="werner")
image werner:
    "images/werner.png"
image jobTitle = ParameterizedText(xalign=0.22, yalign=0.1)
image companyTitle = ParameterizedText(xalign=0.2, yalign=0.17)
image jobPeriod = ParameterizedText(xalign=0.2, yalign=0.25)
image campanyArea = ParameterizedText(xalign=0.2, yalign=0.30)


label maritius:
    show image "images/emergea.png"
    show jobTitle "{size=+20}Senior Solutions Architect{/size}"
    show companyTitle "{size=+10}Emergea{/size}"
    show jobPeriod "{size=-5}{i}Jan 2017 - Oct 2017 · 10 months{/i}{/size}"
    show campanyArea "{size=-5}{i}Cape Town Area, South Africa{/i}{/size}"
    w "Worked on queuing system development: https://www.qmatic.com/ Orchestra development"
    w "This included develop of custom queuing solutions normally in the web patform with the use of AngularJS and some react."
    w "Also completed an android application integration with orchestra and custom orchestra development with AngularJS and socket.io technology stack."    
    show screen gameMenu

screen gameMenu():    
    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.game_menu_background

    vbox xalign 0.45 yalign 0.72:        
        imagebutton auto "SouthAfrica_%s.png" action [ToggleScreen("gameMenu"), Jump("ct_or_jozi")]

    vbox xalign 0.7 yalign 0.72:        
        imagebutton auto "Mauritius_%s.png" action [ToggleScreen("gameMenu"), Jump("maritius")]

    vbox xalign 0.47 yalign 0.49:
        text "{size=+30}World Map{/size}"
        text "(click on flags"
        text "to navigate)"

screen crossroads():
    ## This ensures that any other menu screen is replaced.
    tag menu
    image Movie(size=(1600,1080),play="images/background_game_branch.webm")
        
    vbox xalign 0.337 yalign 0.403:        
        imagebutton auto "CBD_left_%s.png" action [ToggleScreen("crossroads"), Jump("ct")]        

    vbox xalign 0.473 yalign 0.333:                
        imagebutton auto "CBD_Right_%s.png" action [ToggleScreen("crossroads"), Jump("iotnxt")]

    vbox xalign 0.39 yalign 0.70:        
        imagebutton auto "SouthAfrica_%s.png" action [ToggleScreen("crossroads"), Jump("start")]

    vbox xalign 0.39 yalign 0.25:
        text "{size=+30}Cross Roads{/size}"        

screen capetown():
    ## This ensures that any other menu screen is replaced.
    tag menu
    image "capetownJobs.png"
        
    vbox xalign 0.1 yalign 0.1:        
        imagebutton auto "CapeTownCBD_%s.png" action [ToggleScreen("capetown"), Jump("ct_or_jozi")]
    
    vbox xalign 0.6 yalign 0.1:        
        imagebutton auto "TechnoPark_%s.png" action [ToggleScreen("capetown"), Jump("ct_or_jozi")]

    vbox xalign 0.1 yalign 0.9:        
        imagebutton auto "WynBerg_%s.png" action [ToggleScreen("capetown"), Jump("ct_or_jozi")]

    vbox xalign 0.5 yalign 0.9:        
        imagebutton auto "PaardeVlei_%s.png" action [ToggleScreen("capetown"), Jump("ct_or_jozi")]

    vbox xalign 0.8 yalign 0.91:        
        imagebutton auto "SouthAfrica_%s.png" action [ToggleScreen("capetown"), Jump("ct_or_jozi")]

label iotnxt:
    show image "images/iotnext.png"
    show jobTitle "{size=+20}Senior Software Engineer Team Lead (Temp){/size}"
    show companyTitle "{size=+10}IoT.nxt{/size}"
    show jobPeriod "{size=-5}{i}Jun 2022 - Dec 2022 · 7 months{/i}{/size}"
    show campanyArea "{size=-5}{i}South Africa{/i}{/size}"
    w "Managing people with the ability to lead and influence and Mentor them or others."
    w "Leading and managing the delivery of software development projects in a structured environment."
    w "Applied development approaches and methodologies including Agile and/or Waterfall."
    w "Exposure to Product Lifecycle and Management tools."
    show screen gameMenu

label splashscreen:
    scene black
    with Pause(1)

    show text "Werner Presents..." with dissolve
    hide text with dissolve
    with Pause(1)

    show text "CV" with dissolve
    hide text with dissolve
    with Pause(1)

    return

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    call screen gameMenu
    # These display lines of dialogue.

    # This ends the game.
    return

label ct_or_jozi:
    call screen crossroads

label ct:
    call screen capetown

