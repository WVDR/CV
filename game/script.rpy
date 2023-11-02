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
image background = "#000"
image background emergea = "images/emergea.png"
image background iotnxt = "images/iotnext.png"
image background homechoice = "images/homechoice.png"
image background WesternCapeGovernment = "WesternCapeGovernment.png"
image background VulcanLabs = "VulcanLabs.png"
image background CapitecBank = "CapitecBank.png"


label maritius:
    show background emergea
    show jobTitle "{size=+20}Senior Solutions Architect{/size}"
    show companyTitle "{size=+10}Emergea{/size}"
    show jobPeriod "{size=-5}{i}Jan 2017 - Oct 2017 · 10 months{/i}{/size}"
    show campanyArea "{size=-5}{i}Cape Town Area, South Africa{/i}{/size}"
    w "Worked on queuing system development: https://www.qmatic.com/ Orchestra development"
    w "This included develop of custom queuing solutions normally in the web patform with the use of AngularJS and some react."
    w "Also completed an android application integration with orchestra and custom orchestra development with AngularJS and socket.io technology stack."
    scene black
    call screen gameMenu

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
        imagebutton auto "CapeTownCBD_%s.png" action [ToggleScreen("capetown"), Jump("CapeTownCBD_WesternCapeGovernment")]
    
    vbox xalign 0.6 yalign 0.1:        
        imagebutton auto "TechnoPark_%s.png" action [ToggleScreen("capetown"), Jump("CapitecBank")]

    vbox xalign 0.1 yalign 0.9:        
        imagebutton auto "WynBerg_%s.png" action [ToggleScreen("capetown"), Jump("HomeChoice")]

    vbox xalign 0.5 yalign 0.9:        
        imagebutton auto "PaardeVlei_%s.png" action [ToggleScreen("capetown"), Jump("VulcanLabs")]

    vbox xalign 0.8 yalign 0.91:        
        imagebutton auto "SouthAfrica_%s.png" action [ToggleScreen("capetown"), Jump("ct_or_jozi")]

label iotnxt:
    show background iotnxt
    menu:
        "Select Role Or Go Back"

        "Senior Software Engineer Team Lead June 2022 - December 2022 (7 months)":
            jump iotnxt_Teamlead

        "Software Engineer March 2022 - Present (1 year 9 months)":
            jump iotnxt_SoftwareEngineer

        "Go Back":
            scene black
            call screen crossroads

label HomeChoice:
    show background homechoice
    menu:
        "Select Role Or Go Back"

        "Senior Software Engineer (Cyberpro Consultant) December 2017 - December 2020":
            jump HomeChoice_SeniorSoftwareEngineer_CyberproConsultant

        "Senior Software Engineer December 2017 - December 2020":
            jump HomeChoice_SeniorSoftwareEngineer

        "Go Back":
            scene black
            call screen capetown

label CapitecBank:
    show background CapitecBank
    menu:
        "Select Role Or Go Back"

        "Application Developer 2012 - 2014 (2 years)":
            jump CapitecBank_ApplicationDeveloper

        "Application Programmer 2009 - 2012 (3 years)":
            jump CapitecBank_ApplicationProgrammer

        "Database Developer 2007 - 2009 (2 years)":
            jump CapitecBank_DatabaseDeveloper

        "Client Care Call Centre Agent 2006 - 2007 (1 year)":
            jump CapitecBank_ClientCareCallCentreAgent

        "Go Back":
            scene black
            call screen capetown

label CapitecBank_ApplicationDeveloper:
    show jobTitle "{size=+20}Application Developer{/size}"
    show companyTitle "{size=+10}Capitec Bank{/size}"
    show jobPeriod "{size=-5}{i}2012 - 2014 (2 years){/i}{/size}"
    show campanyArea "{size=-5}{i}Cape Town, Western Cape, South Africa{/i}{/size}"
    w "Designing and developing of new applications which contribute to the Development of the bank's current/future systems.Primarily Designing/developing the following:"
    w "Web Services,Windows Services,Windows Applications,Banking system components that consisted of very basic web maintenance, WPF, WCF."    
    scene black
    jump CapitecBank

label CapitecBank_ApplicationProgrammer:
    show jobTitle "{size=+20}Application Developer{/size}"
    show companyTitle "{size=+10}Capitec Bank{/size}"
    show jobPeriod "{size=-5}{i}2009 - 2012 (3 years){/i}{/size}"
    show campanyArea "{size=-5}{i}Cape Town, Western Cape, South Africa{/i}{/size}"
    w "Designing and developing of new applications which contribute to the Development of the bank's current/future systems.Primarily Designing/developing the following:"
    w "Web Services,Windows Services,Windows Applications, Banking system components that consisted of very basic web maintenance."
    scene black
    jump CapitecBank

label CapitecBank_DatabaseDeveloper:
    show jobTitle "{size=+20}Database Developer{/size}"
    show companyTitle "{size=+10}Capitec Bank{/size}"
    show jobPeriod "{size=-5}{i}2007 - 2009 (2 years){/i}{/size}"
    show campanyArea "{size=-5}{i}Cape Town, Western Cape, South Africa{/i}{/size}"
    w "Designed and developed Extract, Transform & Load (ETL) processes as well as SQL scripts / procedures to satisfy reporting needs, according to the agreed standards and format."
    w "Perform quality checks and recommend improvements and maintain and modify existing applications and systems."
    scene black
    jump CapitecBank

label CapitecBank_ClientCareCallCentreAgent:
    show jobTitle "{size=+20}Client Care Call Centre Agent{/size}"
    show companyTitle "{size=+10}Capitec Bank{/size}"
    show jobPeriod "{size=-5}{i}2006 - 2007 (1 year){/i}{/size}"
    show campanyArea "{size=-5}{i}Cape Town, Western Cape, South Africa{/i}{/size}"
    w "Team participation with Internet & PC problem resolution for clients via telephonic conversation."
    w "Did some Administration, and also monitored Cellsecure alarm (ATM) system at night."
    w "Granting of card authorization requests."
    scene black
    jump CapitecBank

label VulcanLabs:
    show background VulcanLabs
    show jobTitle "{size=+20}Consultant{/size}"
    show companyTitle "{size=+10}Vulcan Labs{/size}"
    show jobPeriod "{size=-5}{i}2014 - December 2016 (2 years){/i}{/size}"
    show campanyArea "{size=-5}{i}Somerset West Area, South Africa{/i}{/size}"
    w "Designing and developing of new or maintaining existing, web/mobile or frontend applications; requested by external clients as a consultancy/contracting company. Primary focus:"
    w "• Microsoft .Net development"
    w "• Java EE development Project work • Ongoing Java web application maintenance for the Sewells Group web client."
    w "• Research and development of the Microsoft Word document generator and PDF conversion."
    w "• Research and development of the Microsoft Excel conversion to PDF."
    w "• Assistance with the development of the NPAS (Number Plate AdministrationSystem)."
    w "• Front end C# development of the new iPAS (Provincial Accident System).Screen design and prototyping for development of Mobile system using Cordova and html."
    w "• Tour Guide registration system. Maintaining and adding new Functionality of existing VB code base."
    scene black
    call screen capetown

label CapeTownCBD_WesternCapeGovernment:    
    show background WesternCapeGovernment
    show jobTitle "{size=+20}Senior Applications Consultant (Vulcan Labs Consultant){/size}"
    show companyTitle "{size=+10}Vulcan Labs{/size}"
    show jobPeriod "{size=-5}{i}2015 - December 2016 (1 year){/i}{/size}"
    show campanyArea "{size=-5}{i}Cape Town, Western Cape, South Africa{/i}{/size}"
    w "Designing and developing of new or maintaining existing, web/mobile or fronted applications; requested by current client via consultancy/contracting company(Vulcan Labs). Primary focus:"
    w "• Microsoft .Net development"
    w "• Android Development Project work"
    w "• Assistance with the maintenance and deployment of the VisRAMS (Visual Road Road Asset Management System)"
    w "• Assistance with the maintenance and deployment of the RNISVA (Road Network Information System's Visual Assessments) Client Side deployment application to android devices."
    scene black
    call screen capetown


label iotnxt_Teamlead:    
    show jobTitle "{size=+20}Senior Software Engineer Team Lead (Temp){/size}"
    show companyTitle "{size=+10}IoT.nxt{/size}"
    show jobPeriod "{size=-5}{i}June 2022 - December 2022 (7 months){/i}{/size}"
    show campanyArea "{size=-5}{i}South Africa{/i}{/size}"
    w "Managing people with the ability to lead and influence and Mentor them or others."
    w "Leading and managing the delivery of software development projects in a structured environment."
    w "Applied development approaches and methodologies including Agile and/or Waterfall."
    w "Exposure to Product Lifecycle and Management tools."
    scene black
    jump iotnxt

label iotnxt_SoftwareEngineer:
    show jobTitle "{size=+20}Software Engineer{/size}"
    show companyTitle "{size=+10}IoT.nxt{/size}"
    show jobPeriod "{size=-5}{i}March 2022 - Present (1 year 9 months){/i}{/size}"
    show campanyArea "{size=-5}{i}South Africa{/i}{/size}"
    w "Utilized relevant development languages and technologies to design, develop,and maintain software applications."
    w "Identified, installed, and tested software systems we have built from the ground up."
    w "Ranging from internal systems that can help businesses be more efficient to produce systems that can be sold on the open market."
    w "Once the initial software system was delivered; also help in maintaining, and update the system."
    scene black
    jump iotnxt

label HomeChoice_SeniorSoftwareEngineer_CyberproConsultant:    
    show jobTitle "{size=+20}{/size}"
    show companyTitle "{size=+10}HomeChoice{/size}"
    show jobPeriod "{size=-5}{i}December 2017 - December 2020 (3 years 1 month){/i}{/size}"
    show campanyArea "{size=-5}{i}Cape Town, Western Cape, South Africa{/i}{/size}"
    w "Utilized relevant development languages and technologies to design, develop,and maintain software applications."
    w "Identified, installed, and tested software systems we have built from the ground up."
    w "Ranging from internal systems that can help businesses be more efficient to produce systems that can be sold on the open market."
    w "Once the initial software system was delivered; also help in maintaining, and update the system."
    scene black
    jump HomeChoice

label HomeChoice_SeniorSoftwareEngineer:    
    show jobTitle "{size=+20}Senior Software Engineer (Cyberpro Consultant){/size}"
    show companyTitle "{size=+10}HomeChoice{/size}"
    show jobPeriod "{size=-5}{i}January 2021 - March 2022 (1 year 3 months){/i}{/size}"
    show campanyArea "{size=-5}{i}Cape Town, Western Cape, South Africa{/i}{/size}"
    w "Utilized relevant development languages and technologies to design, develop,and maintain software applications."
    w "Identified, installed, and tested software systems we have built from the ground up."
    w "Ranging from internal systems that can help businesses be more efficient to produce systems that can be sold on the open market."
    w "Once the initial software system was delivered; also help in maintaining, and update the system."
    scene black
    jump HomeChoice

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

