#Kuruma Musume v0.101




#Resource Definitions

#characters
define tb = Character("[name]", color="F6D295")
define sil = Character("Silvie", color="#63D2FA")
define mia = Character("Mia", color="FF2626")
define lan = Character("Lanna", color="AFAFAF")
define she = Character("Shelby", color='556B2F')

define sta = Character("Staci", color="91BF5D")

#backgrounds
#Places
image bg mg = "images/Scenes/work_garage.jpg"
image bg coffee = "images/Scenes/coffee_shop.jpg"
image bg cafeexd = "images/Scenes/cafeoutside.jpg"
image bg cafeexn = "images/Scenes/cafeoutside-night.jpg"
image bg bed = "images/Scenes/bedroom.jpg"
image bg park = "images/Scenes/park.jpg"
image bg foodcourt = "images/Scenes/foodcourt.jpg"
image bg miastore = "images/Scenes/mias_store.jpg"
image bg silviestore = "images/Scenes/silvies_store.jpg"
image bg lannastore = "images/Scenes/game_store.jpg"
image bg itally = "images/Scenes/fancy_restaurant.jpg"
image bg p4u = "images/Scenes/p4u.jpg"
#Cars
image bg sil = "images/Scenes/s13_parked.jpg"
image bg silin = "images/Scenes/s13_int.jpg"
image bg miain = "images/Scenes/miain.jpg"
image bg miap = "images/Scenes/mia_parked.jpg"
image bg lanin = "images/Scenes/lan_evo_int.jpeg"
image bg tbin = "images/Scenes/tbcar_int.jpg"
image bg stang ="images/Scenes/stang_parked.jpg"
image bg shein ="images/Scenes/shein.jpg"

#Misc
image black = "images/Scenes/black.png"
image title = "title_screen2.png"


#character images
image silvia = "images/Characters/Silvie.png"
image mia = "images/Characters/mia-neutral.png"
image lanna = "images/Characters/Lanna-Evolina.png"
image mustang ="images/Characters/Shelby.png"

image staci = "images/Characters/thot.png"



#The following is an example of animated images
#for future reference
#image silvia_transform:
#    "silvia"
#    pause .5
#    "mia"
#    pause .5
#    repeat


#Transformations

#Slide Left
transform slideleft:
    linear 0.5 xalign 0.0




#CGs
#[To Be Filled In Later]

#Music
define audio.heartbeat = "music/heartbeat.mp3"
define audio.running = "music/running.mp3"
define audio.cantstop = "music/cantstop.mp3"
define audio.bed = "music/noonesleep.mp3"
define audio.burning = "music/burningdesire.mp3"
define audio.mia = "music/burninglove.mp3"
define audio.mall = "music/seventeen.mp3"
define audio.forget = "music/forget.mp3"
define audio.park = "music/fantasy.mp3"
define audio.fallapart = "music/fallapart.mp3"
define audio.kisstokiss = "music/kisstokiss.mp3"
define audio.restaurant = "music/yellow.mp3"
define audio.tbcar = "music/hero.mp3"
define audio.p4u = "music/face.mp3"
define audio.she = "music/rockin.mp3"


#sounds
define audio.cell = "sounds/cellget.wav"
define audio.wrench = "sounds/wrench.mp3"
define audio.kick = "sounds/kick.wav"
define audio.spunch = "sounds/soft-punch.wav"


#Initial Flags:


init:

#Phone Numbers
    $   mia_number = False
    $   lanna_number = False
    $   shelby_number = False
    $   staci_number = False

#Calls
    $   call_silvie = False
    $   call_mia = False
    $   call_shelby = False

    $   call_staci = False
#Dates
    $   first_date = False
    $   day2_date = False

#Locations
    $   coffee_date = False

#Unique Scenarios
    #Key:
    # 0=No one
    # 1=Silvie
    # 2=Mia
    # 3=Lanna
    # 4=Shelby
    $   mall_date = 0

#Girlfriend
    $   gf = False

#Rejections
    $   sil_rejection = 0
    $   mia_rejection = 0
    $   lan_rejection = 0
    $   she_rejection = 0

    $   sta_rejection = 0

#With Girls
    $   with_mia = False
    $   with_sil = False
    $   with_lan = False
    $   with_she = False

    $   with_sta = False
    $   solo = True

#Relationships
    $   sil_rel = 0
    $   mia_rel = 0
    $   lan_rel = 0
    $   hac_rel = 0
    $   rox_rel = 0
    $   mr2_rel = 0
    $   she_rel = 0

    $   sta_rel = 0

#day
    $   day = 1

#Silvie Flags
    $   sil_date = 0
    $   sil_date1 = False
    $   s_coffee_day_2 = False
    $   sil_first_drive = False

#Mia Flags
    $   mia_met = False
    $   mia_date = 0
    $   mia_date1 = False
    $   mia_first_drive = False
    $   ms_help = False

#Shelby Flags
    $   shelby_met =False
    $   shelby_date = 0

#Lanna Flags
    $   lan_met = False
    $   lan_date = 0
    $   lan_date1 = False
    $   lan_first_drive = False

#RX-7 Flags

#AE86 Flags

#Staci Flags
    $   sta_date = 0


#Character Variables
    $   Silvie = "{color=#63D2FA}Silvie{/color}"
    $   Mia = "{color=FF2626}Mia{/color}"
    $   Lanna = "{color=AFAFAF}Lanna{/color}"
    $   Shelby = "{color=556B2F}Shelby{/color}"

    $   Staci = "{color=91BF5D}Staci{/color}"


#Misc Variables


# GAME START

label start:


    play music heartbeat fadein 1.5

    #Day 0
    python:
        name = renpy.input("My name is...")

        name = name.strip() or "Tofuboy"

    $   PC = "{color=F6D295}" + name + "{/color}"
    "I've been working as a mechanic ever since my senior year of high school. It's the only job I ever wanted."
    "Ever since I was a kid, cars have fascinated me. The sounds, the smells, and of course the sensation of being behind the wheel."
    "Despite all of the time I've spent under the hood of cars and all of the knowledge I have, nothing could have prepared me for that day."

    #$   day = 2


    #$   renpy.jump("dstart_" + str(day))

    scene bg mg with dissolve

    show silvia with dissolve
    $   with_sil = True
    "Sick Customer" "*Cough* *Cough*"

    tb "Need a cough drop, ma'am?"
    "Sick Customer" "No thanks. *Cough* I'll be fine. Can you please just fix me?"
    tb "Uh, sure. So we're going to need to replace-"
    "Sick Customer" "I don't care what it is or how much it costs, please- *Cough* *Cough* fix it."
    tb "Alright. Alright. I'll let you know when it's done."

    hide silvia

    "This poor car has been through a lot it seems. Right now it needs a new catalytic converter but it will need a lot more before too long."
    play sound wrench
    "She seems in a hurry, though, so I doubt I'll convince her to let me fix anything that isn't urgent."

    tb "Ma'am, you're all set."

    show silvia

    "Without warning, the woman leaped on me and wraped her arms around me."
    "Customer" "Thank you so much! You saved my life! I don't know how I can ever repay you."
    tb "Calm down. It's really no big deal. Just my job."
    "Strangely, this woman is looking remarkably better."
    tb "You really seem healthier all of a sudden."
    "Customer" "It's all thanks to you! We cars rarely find such amazing mechanics."
    "I think this woman might actually be crazy."
    "Customer" "Wait, did I just say that?"
    tb "Look ma'am, you're welcome and all, but I've got other cars to work on, so if you'd just pay, you can go."
    "Customer" "No, I've said too much.{w} What do I do?{w} What do I do?"
    tb "You pay your bill and go on with your day. Seriously, lady, I just fixed your car. It's not a big deal."
    "She took me by the hand and lead me out to her car."

    scene bg sil with dissolve
    show silvia with dissolve

    "Customer" "Look, I need to explain something to you. I'm-"
    "She paused and got in the car, looking up at me with concerned eyes."

    hide silvia

    "Without warning, she vanished! She just disappeared right in front of my eyes."
    "I opened the door and looked inside. Obviously she couldn't just be hiding somewhere; I watched her disappear."
    "Customer" "What are you looking for?"
    "I turned around, thinking this was some bizarre magic trick and I'd find her standing behind me."
    "Customer" "I'm right here, silly."
    "That's when I realized that her voice was coming from the speakers."
    "Customer" "Get in, please."
    "What choice did I have? I opened the door and sat down in the driver's seat."

    scene bg silin with dissolve
    pause 1
    show silvia

    "Suddenly, she appeared in the seat next to me."
    "Customer" "As you probably already guessed, I'm not really a human."
    "I definitely had not guessed that. In fact, that's the last thing I would have guessed."
    "And here I was thinking she was the crazy one, but apparently {i}I'm{/i} going crazy."
    "Customer" "Look, I shouldn't be telling you this. We prefer to blend in with humans and we're afraid of what you'd do if you found out about us-"
    "Customer" "But I trust you. I've been to a lot of mechanics throughout my life and I've never had one who treated me with so much love and care."
    "Customer" "Occasionally we make exceptions to the rule about no one knowing, and I decided that you were worth it."
    "Customer" "Also, I already kind of gave myself away inside, so..."
    "I was at a loss for words. What is this insanity? Is she trying to tell me that she's literally the car?"
    tb "Are you saying what I think you are."
    "Customer" "Please be my personal mechanic forever!"
    "She reached across and hugged me again."

    menu:
        "Alright, I will.":
            $   solo = False
            $   with_sil = True
            jump bemechanic_yes

        "This is all too much. I think I've lost my mind.":
            jump bemechanic_no

    label bemechanic_no:
    tb "I'm sure with copious amounts of alcohol and a good long rest, I'll forget this crazy nightmare."
    "And so I closed the shop early that day without warning."
    "Whatever trouble I'd end up in for delaying several other customers waiting for me to fix their cars, it would be worth it just to forget this."
    "I never saw that strange woman again."
    return

    label bemechanic_yes:

    tb "This is absolutely the craziest thing to ever happen to me, but I'm fascinated all the same."
    tb "I have a question, though."
    "Customer" "Yeah?"
    tb "What's your name?"
    sil "You can call me [Silvie]."
    "From that moment on, my life changed forever."
    stop music fadeout 1.5

    pause 1.5

    scene title with dissolve
    play music running fadein 1.5

    pause

    "{i}Insert cool opening video thing here{/i}"

    scene bg mg with dissolve

    play music cantstop fadein 1.5


#Days

    #Day 1
    "That day changed my life"
    "Over the next few days, we met each other after I finished with work."

    scene bg silin with dissolve

    show silvia with dissolve

    sil "It's weird, but it actually feels good that a human knows about me."
    tb "You think so?"
    sil "Yeah! Normally we keep ourselves pretty secret. Sometimes even we can't recognize each other."
    "She lets out a long, contented sigh."
    sil "It's kind of a relief just to have someone know who I really am."
    tb "So, I've gotta know something."
    tb "How are you, uh, car-girls born?"
    sil "No one really knows exactly. We just kind of exist suddenly."
    sil "What we do know is that it seems to have something to do with someone putting their heart and soul into making us."
    sil "It's like a little piece of their soul creates a new soul for their car!"
    tb "So if someone spends a lot of time working on you, suddenly you're a person?"
    sil "It's the only theory I've ever heard that makes any sense."
    tb "Are you really all girls?"
    sil "Yup. We're still trying to figure that one out too, but we suspect that the same thing used to happen with ships back when it took a lot more work to build them."
    sil "It would explain why boats are always called she."
    tb "I guess it would."
    tb "So how do you recognize other car girls?"
    sil "We like the term {i}Kuruma Musume{/i}."
    sil "When you know enough about cars, you can start recognizing what Kuruma Musumes look like. We always look a little like the cars we're born from."
    sil "Not to mention the fact that we aren't able to get too far away from our car selves, so someone who won't walk far from her car probably is the car."
    sil "It's probably easier for us to tell than it is for humans, but I'm sure you'd learn to recognize us if you met some more."
    tb "You should introduce me to some others then. This is fascinating."
    sil "Maybe."
    sil "We're usually pretty shy, so I don't know if any others will want to meet you."
    sil "N-not that I'd be jealous of you talking to someone else!"
    "Oh no. I hope she's not one of {i}those{/i} types."
    tb "Oh well. If I have you around, I'm sure I'm bound to meet another car at some point anyway."
    sil "We'll see."
    sil "So, we've been seeing each other for a few days now, but we never really do anything. So I was wondering, do you want to go get coffee or something?"
    "Wait, is a car asking me out on a date?"

    menu:
        "I'd love to!":
            $   sil_rel += 2
            "[Silvie] exhales as if she were holding her breath waiting for my answer."
            sil "Great! There's a little coffee shop a few blocks down that I go to a lot. You'll love it!"
            jump sil_coffee_date1

        "Maybe some other time.":
            $   sil_rejection += 1
            jump nosildate1



    label dnight_1:

    stop music fadeout 1.5

    scene bg bed with dissolve

    play music bed fadein 1.5

    "What a crazy day."
    if first_date:
        "I think I just went on a date with a car."
        jump dend_1
    else:
        jump dend_1

    label dend_1:
    "I should get some rest. These past few days have been exhausting."

    #Day 2
    label dstart_2:

    $ day += 1
    show bg bed with fade
    "DEBUG: Day 2 start | Actually Day [day]"
    "It's great to have the day off."
    "What should I do?"

    menu:
        "Call [Silvie]":
            $   call_silvie = True
            $   renpy.jump("sil_dc" + str(sil_date + 1))
            "I guess I should call Silvie."
            sil "Hello?"
            "DEBUG: sil_date=[sil_date]"
            if sil_date == 1:
                tb "Hey, Silvie. Are you busy today?"
                sil "Not at all! Would you like to meet up?"
                tb "Sure. Where should we meet?"
                sil "I'd like to go to that little park downtown, if you don't mind."
                $   sil_rel += 3
                jump sil_park_date1

            else:
                tb "Hey, Silvie. I was wondering if you'd like to go for that coffee today?"
                sil "Of course! Do you want to meet there or should I come pick you up?"
                tb "I'll meet you there. It's fine."
                $   sil_rel += 3
                $   s_coffee_day_2 = True
                $   call_silvie = True
                jump sil_coffee_date1

        "Go somewhere":
            "Where should I go?"
            menu:
                "Coffee shop":
                    if first_date:
                        "I feel like visiting that coffee shop again."
                        jump mia_coffee_date1
                    else:
                        "I should try that coffee shop near work."
                        $   s_coffee_day_2 = True
                        jump sil_coffee_date1
                "Park":
                    "It's so nice outside today. I should go visit the park downtown."
                    jump park
                "Parts 4 U":
                    jump she_d2_date





    label park:


    scene bg park

    if sil_date == 1:
        jump sil_park_date1

    else:
        jump evo_park_date1











    $   renpy.jump("dend_" + str(day))



    #Mall Scenario

    #Mall Solo
    label solo_mall1:
    $   solo = True
    $   mall_date = 0
    if day2_date:
        "Speaking of shopping, I do need to go pick up some things from the mall before it closes. I'll just head over there really quick."
    else:
        "I should really do some shopping before I head home. I guess I'll head to the mall."
    stop music fadeout 1.5
    scene bg foodcourt with dissolve
    play music mall fadein 1.5
    "I quickly went between stores, buying what I needed, and then decided to grab a quick bite of food at the food court."
    jump day_2_mall_event


    #Mia Day 2 Mall
    label mia_mall1:

    $   mall_date = 2
    if mia_first_drive:
        mia "Great! You can drive yourself if you're too scared after last time with me."
        tb "Nah, I'll be fine."
        "[Mia]'s driving was much more gentle this time around. It was actually pretty relaxing."

    else:
        mia "Great! I'll give you a ride."
        scene bg miain with dissolve
        show mia at right with dissolve
        stop music fadeout 1.5
        play music mia fadein 1.5

        "[Mia] took me to her car - herself - and for some reason I trusted this girl who looked like a small child to drive."
        "She really was a skilled driver, though. It was honestly the smoothest ride I'd ever been given."
        tb "You're pretty good at this."
        mia "Thanks. I guess I just really know myself better than a human could. It makes driving much easier."
        tb "I've spent my life around cars and don't think I've met anyone quite as skilled."
        mia "I'm not surprised. Humans don't compare to Kuruma Musumes when it comes to driving skill, and the only other car you've met is Silvie."
        "We arrived at the mall and found parking."


    mia "This won't take long. You sure you don't mind coming with me?"
    tb "Of course not. It's been really fun getting to know you."
    "She lead me inside the mall to her favorite store."

    stop music fadeout 1.5
    scene bg miastore with dissolve
    play music mall fadein 1.5
    show mia with dissolve

    "Unsurprisingly, it was a children's clothing store."
    mia "One nice thing about looking like a kid is just how cute all the clothes are!"
    mia "Also, if anyone thinks you're my dad, just play along. It's easier that way."
    "Shopkeeper" "Hi! Welcome to Not-Justice! Can I help you find anything?"
    mia "Nah, we're just looking."
    "Shopkeeper" "Well, let me know if you need any help."
    tb "Thanks, we will."
    "[Mia] browsed through the shirts before focussing on one particular shirt covered in multi-colored hearts."
    mia "Oh! This one's cute! What do you think?"
    tb "Hmm. {w}I think it suits you."
    mia "You're just saying that because you have no clue."
    tb "Okay, yeah."
    mia "Ha-haha! It's fine. I don't really care what you think anyway. It's like my popups. If I like 'em, I'm keeping them. Screw what anyone thinks."
    tb "Your headlights? Do people actually tell you to get rid of them?"
    mia "All the time. I go to car meets pretty regularly and there's always a few people who tell me they don't like the popups."
    mia "It's like, \"then take 'em off {b}YOUR{/b} car.\" Popups are cute and I want to be cute."
    "I've never been a huge fan of popups myself, but I better not tell her that."
    tb "They should respect the build."
    mia "Right?"
    mia "People just can't get that through their heads.{w} It's my car, {i}me{/i}, and I'll make it look how I want it."
    tb "So how much have you done to yourself since you were on your own?"
    mia "Wow!{w} That's an incredibly private question. Do you normally ask girls about what surgeries they've had or what their boyfriends didn't do to them?"
    tb "Oh.{w} Sorry, I just kind of assumed that cars would like to talk about their modifications."
    mia "Well, you know what they say about assuming."
    mia "It's not really that big of a deal, but you should still be a little more considerate. A car's worth more than her parts, ya know."
    tb "You're right. Thanks for the advice."
    #show mia smiling
    mia "I think I'm done here. Want to go get some dinner? It's food court food, but it's food."
    "[Mia] paid for her clothes while the shopkeeper gave me strange looks, then we headed over to the food court."
    jump day_2_mall_event


    #Silvie Day 2 Mall

    label sil_mall1:
    $   mall_date = 1
    play music mall fadein 1.5
    scene bg silviestore with dissolve
    show silvia with dissolve
    "[Silvie], it turned out, preferred to do her clothes shopping at the big department stores."
    "I've never cared much for them because of their manipulative marketing tactics, but if that's the clothes [Silvie] likes, what can I say?"
    sil "I don't go shopping a lot. I usually just go with [Mia], but she usually shops at other stores. It's nice to have someone who doesn't mind going to my favorites."
    tb "Does [Mia] not come with you?"
    sil "She will, but she always complains."
    tb "I guess that's just how she is."
    sil "I don't really mind it. She's been my closest friend since we met, so it's not a big deal."
    tb "Do you have a lot of friends?"
    sil "Well, I probably know most of the Kuruma Musumes in town. I'm not really friends with any humans though."
    sil "Except you, of course."
    tb "But are you actually close to any of them?"
    sil "Not really. We'll talk sometimes, and I'm always happy to race them, but I guess we aren't all that close."
    sil "It's okay, though. I don't have to be close friends with everyone, but I always have people I can call."
    tb "I guess that's a good way to look at it."
    "To be honest, I've never had many close friends either."
    sil "But if you ask Mia, she'd say I'm friends with the whole city!"
    tb "You do seem like the social type."
    sil "It's just great to know I'm not alone."
    sil "Hey, do you want to go get something to eat? This place has a really nice food court."
    tb "Yeah, that'd be great."
    jump day_2_mall_event


    #Lanna Day 2 Mall

    label lan_mall1:
    $   mall_date = 3
    play music mall fadein 1.5
    scene bg foodcourt with dissolve
    show lanna with dissolve
    "After a quick stop by the restroom and much teasing from Lanna for it, we started strolling through the mall."
    scene bg lannastore with dissolve
    show lanna with dissolve
    "Lanna stopped us when we reached the game store."
    lan "Yo. I wanna see if they've got any new racing sims in yet."
    "Store Employee" "Welcome to Games to Go. Need any help finding something?"
    lan "Yeah, you got the new Gran Autismo or Horza Forizon in?"
    "Store Employee" "Sorry, we just sold out of Horza and GA doesn't come out for another month."
    lan "Damn."
    "Store Employee" "We have a few coppies of the new Plumber Kart if you're looking for racing games."
    lan "Ha{w} ha{w} ha{w} ha.{w} Obviously I'm looking for a real racing game, not some dumb cartoon for kids."
    "Store Employee" "I'm so sorry. I meant no offense!"
    lan "What else do you have that's new?"
    "Store Employee" "Do you like shooters?"
    lan "I guess."
    "This poor employee probably isn't being paid enough to deal with [Lanna]."
    "They talk for a few minutes, the employee desparate to find some way to appease a car who seems determined to make his life harder."
    lan "Forget it. I'll come back when you get Horza or GA in."
    "Store Employee" "Okay. Have a nice day."
    "As we walk out of the store, I can see the relief in the employee's face."
    tb "Do you think you were a little harsh with him?"
    lan "How long have we known each other?{w} A few hours?{w} You shouldn't be judging me like that."
    tb "It just seems like you were trying to make things harder for him."
    lan "If you aren't forceful with people, they'll either ignore you or run over you."
    lan "You've gotta be the biggest, toughest bitch if you want anyone to care."
    tb "I get what you're saying, but I just don't feel like it's right."
    lan "You'll learn someday. Or you'll get run over."
    "I hope she means that metaphorically."
    lan "I'm hungry. Wanna get some grub?"
    tb "Sure."
    jump day_2_mall_event



    #Mall Night

    label day_2_mall_event:



    scene foodcourt with dissolve

    if with_mia:
        show mia
    elif with_sil:
        show silvia
    elif with_lan:
        show lanna
    elif with_she:
        show mustang
    elif solo:
        jump staci_intro

    "We found a small noodle shop in the food court and sat down to a nice meal."
    "For once, she was asking more about me than I was asking about her."

    if with_mia:
        mia "So have you really spent your whole life working on cars?"
        tb "Yeah. I started helping my dad restore an old car when I was six."
        tb "Honestly, I didn't do much but pass him tools, but it started my passion for cars."
        tb "When he had to sell it before it was done, I felt bad about it. It felt like we could have finished it if I could have done more."
        mia "As a car, I think that's really sweet of you. I bet she would have been an awesome Kuruma Musume if you finished her."
        tb "You think we'd have made one of you?"
        mia "Definitely!{w} If you felt bad about not finishing her, you were absolutely putting enough heart and soul into her."
        tb "So you believe that heart and soul theory?"
        mia "Of course I do. I've never met anyone who didn't, honestly. We're all born with a very deep connection to the humans who built us."
        mia "That connection is special. I can't imagine how anyone can try to say something different."
        tb "You must have been very fond of the human who made you."
        #show mia_sad
        mia "I was."
        tb "Is it too much to ask about what happened to him?"
        #show mia_mad
        mia "I'm only going to warn you once.{w} Never ask about him ever again."
        #show mia_sad
        mia "Humans have ways of hurting us that they'll never understand."
        tb "I'm sorry. I won't bring it up."
        mia "Thanks."
    elif with_sil:
        sil "Did I scare you when I fused for the first time?"
        tb "I didn't know what to think. I thought it was some crazy magic trick and there was going to be a team of cameramen jumping out suddenly to film my reaction."
        sil "That sounds like an idea [Mia] would have for a show."
        tb "I'm sure it'd be just as shocking for everyone watching on TV as whoever was with the car."
        sil "Don't suggest that to [Mia], you'd only encourage her. She already likes to go around telling humans what she is."
        tb "I don't imagine any of them believe her. I've been working on cars my whole life and would have never believed that this could happen if I didn't see it."
        sil "You've really been a mechanic your whole life?"
        tb "Kind of. I used to help my dad with a car he was restoring when I was a kid. Sadly, we never finished it."
        sil "You should totally try to finish her!"
        tb "I can't. Dad had to sell it to afford rent once."
        sil "That's too bad. You might have managed to make a Kuruma Musume if you finished her."
        tb "I wonder what she'd be like?"
        sil "If she was born from you, she probably would be pretty cool."
        tb "Cool?"
        sil "Um...{w} I mean...{w} I just think it's kind of cool that you can take all of this Kuruma Musume stuff so well."
        tb "I guess most people would have a hard time accepting it."
        #show relieved silvie
        sil "Exactly. You're really level-headed and quick to accept new things. That kind of person would make a pretty great Kuruma Musume."
    elif with_lan:
        lan "So why did you decide to be a mechanic?"
        tb "I've been really into cars since I was a kid working on an old car with my dad."
        lan "You tell your dad about your car girlfriends yet?"
        tb "Girlfriends?"
        lan "Okay, mister \"I'm totally not interested in car girls,\" did you tell your dad about Kuruma Musumes?"
        tb "It's not that I'm not interested, I just haven't tried to make a move yet."
        lan "So you do want in Silvie's pants?"
        "Oh crap. I spoke without thinking."
        tb "I didn't say that. And no, I haven't told my dad. We don't really talk much anymore."
        lan "Well, if you're not trying to get in Silvie's pants, how about mine? If I like it, maybe we can both go talk to your dad sometime."
        tb "I don't know how to react to that."
    elif with_she:
        she "How long have you been working on cars?"
        tb "Techinically since I was just about 10. I was helping my dad restore a car. I barely did anything but pass tools, but I still learned a bit, and more importantly, learned what I wanted to do for the rest of my life."
        she "Wow, you really love cars, huh?"
        tb "Yep, I live for cars. I only really feel myself covered in grease and elbows deep into an engine bay."
        "[Shelby] suddenly turned a deep red, and avoided eye contact with me."
        #Embarrased shelby
        tb "That's- that's a strange thing to say to a car, isn't it?"
        she "I could sue you for sexual harrassment, you know."
        she "Anyways, how did the car turn out? Do you still have it?"
        tb "No actually, my dad ended up having to sell it before we finshed."
        she "Oh... I'm sorry. Well at least you've got a bunch of Karuma Musume to, what did you say? Get covered in their grease and violate their engine bays?"
        "It was my turn to turn red."
        tb "That's not what I said!"



    #Introducing Staci
    label staci_intro:
    stop music fadeout 2.5
    "Busty Woman" "[PC]?"
    "I know that voice."
    "Busty Woman" "[PC]! It's you! I haven't seen you in years!"
    play music forget fadein 2
    if solo:
        show staci with dissolve
    else:
        show staci at left with dissolve
    tb "[Staci]! I haven't seen you since high school."
    sta "I know. It's crazy."

    if with_mia:
        sta "Is this your daughter?"
        mia "I most certainly am not.{w} [PC], who is this woman?"
        tb "[Mia], this is [Staci]. [Staci], [Mia]."
        tb "[Staci] was my girlfriend for a couple years in high school, and [Mia] is a friend I made recently."
        "[Staci] looked [Mia] up and down."
        sta "Isn't she, umm...{w} A little young?"
        mia "I'm twenty-six. Can't help the body I'm born with."
        sta "Oh. Well then. I was getting worried there."
        sta "I'm actually still a little worried."
        "She ignored [Mia] and didn't even try to lower her voice."
        "Just like in high school, [Staci] speaks her mind without a single thought for the people around her."

    elif with_sil:
        sta "Oh, is she your girlfriend?"
        sil "I... {w=0.5} I'm... {w=0.5} It's not like..."
        tb "She's my friend. We met a few days ago at work."
        sta "I see."
        tb "[Silvie], this is [Staci]. She was my girlfriend for a few years in high school."
        sta "It's nice to meet you. I figured [PC] would never find another girl who could put up with all his car talk. Does he still talk about cars?"
        sil "Of course-"
        sta "He was such a nerd back in high school, but he was cute, so what the heck?"
        "Not even a moment for anyone else to talk. Doesn't seem like [Staci]'s changed much since those days."

    elif with_lan:
        sta "Is this your girlfriend?"
        "I see [Lanna] open her mouth, but I don't give her the chance to speak."
        tb "{cps=*2}Nah, I just met her.{/cps}"
        "[Lanna] closes her mouth and gives me an unenthused look."
        sta "Oh, I see."
        tb "[Lanna], this is [Staci]. She was my girlfriend back in high school."
        sta "It's nice to meet you. [PC] always sucked with the girls. Guess that's still true if he's not making a move on you."
        sta "Seems there's not many people who can crack open that heart of his. Always \"cars this\" and \"cars that.\""
        sta "I was the only girl who could ever get his attention."
        lan "Is that so?"
        lan "I hear he actually does have his eye on a girl. Beautiful young thing, too. He even tells me that she's really into her car."
        "The smug look vanishes from Staci's face."
        sta "Well. Good for him."
        "She turns away from [Lanna] and back to me."
    elif with_she:
       sta "Am I interrupting a date?"
       tb "No actually, this is new friend, we bonded over... working on cars."
       sta "Oh. Well that explains why she's so... dirty."
       she "Excuse me?"
       "I shoot [Shelby] an appologetic glance."
       tb "[Shelby], this is [Staci]. She was my girlfriend for a few years in high school."

    sta "So what have you been doing these past few years?"
    tb "I run my own car shop now."
    sta "Oh, like a dealership?"
    tb "No, I work on cars."
    sta "Oh. So you're still really into cars then? I thought you might have grown out of that by now."

    if with_mia:
        "If looks could kill, [Mia] would be a murderer."

    elif with_sil:
        #show angry silvie
        "I've never seen [Silvie]'s angry face before, but she definitely didn't take that comment well."

    elif with_lan:
        "[Lanna] smirked."
        lan "Boys and their toys, am I right?"

    elif with_she:
        "[Shelby] had fire in her eyes at that remark."
        "I heard her mutter under her breath, 'Can bench more than you, Tittymonster.'"

    tb "Cars have always been my life. I doubt that's going to change any time soon."
    sta "That's a shame. There's so much more to life than wheels and engines."
    sta "Anyways, I'm really sorry, but I can't stay and chat right now. Here's my number. You should call sometime and we can catch up. It's been way too long."
    play sound cell
    "{color=FFF700}Acquired [Staci]'s number.{/color}"
    $   staci_number = True
    sta "See ya!"
    hide staci with moveoutleft
    stop music fadeout 2.5

    play music mall fadein 2

    "What a blast from the past."

    if with_mia:
        "[Mia] stuck her tongue out at [Staci] once her back was turned."
        mia "What the heck is her problem?"
        tb "She never really cared about cars back in high school. She always made fun of me for wanting to be a mechanic."
        tb "When I finally got a job at a repair shop, she dumped me, saying how she needed someone who makes real money at a real job."
        mia "Who the F does she take her car to when it breaks down?"
        tb "Whoever it is, he probably still makes more than her."
        mia "I bet she doesn't even change her oil regularly. Why would you date someone like that?"
        tb "She had her positive qualities."
        "[Mia] looked down at her chest."
        #show mia_mad_yelling
        mia "Oh, I get it now. So that's how it is with you."
        mia "A girl's only worth her weight in boobs?"
        tb "That's not what I meant!{w} [Staci] was nice to me when it wasn't about cars."
        tb "She wasn't the best, but she did care for me. She was the first girl who actually took an interest in me."
        tb "She might not have liked my passion for cars, but she liked me."
        mia "Your passion for cars is a part of you. If she couldn't accept that, then she didn't really like you."
        tb "You wouldn't understand."
        mia "Whatever. Let's just go. I'll take you back to your car."
    elif with_sil:
        "[Silvie] tried to hide the face she had been making, but it was obvious she wasn't happy."
        tb "Sorry about that. Staci never was very fond of cars."
        sil "Yeah. I gathered that much."
        tb "I guess it sounds a little worse to someone who's actually a car."
        sil "You don't say."
        tb "Look, she was really good to me back in high school. I was kind of a loser for a while, but she liked me anyway."
        sil "Didn't you say cars were your life? Didn't you have a passion for cars since you were a kid? How did you end up with someone like that?"
        tb "She might not have liked my interest in cars, but she was still good to me. In a way, she helped me through high school."
        sil "You deserve someone who supports what you care about."
        tb "It was a long time ago anyway. I don't need a lecture."
        sil "Sorry. Let's just go."

    elif with_lan:
        lan "Ah ha ha ha ha ha!"
        lan "I can't believe you used to date that bimbo."
        lan "I guess I had you figured all wrong.{w} I thought you were just some desperate virgin too busy with his car to see a pretty girl in front of him."
        lan "But apparently you were into those big tiddied air heads."
        tb "I don't really want to talk about [Staci]."
        lan "How does the man who loves cars end up with someone like her?"
        tb "High school was a rough time for me. Somehow Staci ended up actually caring about me."
        tb "She dumped me when I started working as a mechanic, but she was good for me while we were together."
        lan "Well, I guess I'll have to tell [Silvie] that she's gonna have to get some implants if she wants to stand a chance with you."
        tb "It's not like that!"
        lan "Whoa! Chill. Seriously, I know we just met, but I can tell Monster Tits back there isn't your type."
        tb "How's that?"
        lan "The kind of guy who can get a car to open up to him just by making a few repairs isn't the kind of guy who'll end up with some chick who hates cars."
        "[Lanna] isn't exactly wrong, but [Staci] still made me happy back then."
        tb "We should probably go."
        lan "Alright, but on one condition."
        tb "What condi-"
        show lanna:
            linear 0.75 zoom 1.5 yalign 0.5
        "Without warning, she wrapped her arms around my neck and pulled me in for a kiss."
        show lanna:
            linear 1.0 zoom 1.0 yalign 1.0
        lan "I prefer to kiss on the first date."
        "My heart was racing in my chest as fast as it had back in her car."
        tb "But I..."
        lan "Shh. You don't need to say anything. Time to go."
        "[Lanna] might be too fast for me."

    elif with_she:
        she "What was that?"
        tb "I'm really sorry, she's never been big on cars."
        she "Huh, I'm surprised you had a trophy girlfriend."
        tb "It's not like that! She was kind to me back when no one else was. Not liking cars isn't the only thing she's about."
        she "I thought you dedicated your life to cars? Seems like a stressful relationship."
        tb "Well, that is why she dumped me. Anyways, let's get out of here, I don't really want to talk about [Staci] anymore."

    stop music fadeout 2


    #Back at Day2 Start
    if with_mia:
        scene bg miain
        show mia at right
        play music mia fadein 2

        "[Mia] kept quiet as we drove away from the mall."
        "I can't blame her for not liking [Staci], but she's totally over-reacting. [Staci]'s not all bad, she just doesn't value cars."
        "I guess maybe that is \"all bad\" for someone who's actually a car."
        mia "Hey.{w} I'm sorry I tried to say you only care about girls for their boobs."
        mia "I just don't get why someone who cares about cars so much would let someone like that into his life."
        tb "She helped me through a lot during school, and having someone who cared made me happy."
        "We pulled into the cafe parking lot next to my car."
        mia "Well, don't go letting her try to make you \"grow out\" of cars."
        mia "And here, take my number as well. If you ever want to hang out, or if you'd like to race, give me a call."
        play sound cell
        "{color=FFF700}Acquired [Mia]'s number.{/color}"
        $   mia_number = True
        tb "Thanks. Have a good night."
        mia "You too."
        $   with_mia = False
        stop music fadeout 2
        $   renpy.jump("dend_" + str(day))

    elif with_sil:
        scene bg silin
        show silvia with dissolve
        play music fallapart fadein 2
        "[Silvie]'s mood didn't improve as we drove. She was quite for most of the way, and I didn't know what I could say to fix things."
        "Obviously [Staci] was not going to go over well with any Kuruma Musume, but this felt a little ridiculous."
        "It had been years since I last saw [Staci] and I hadn't even thought of her since high school. I know [Silvie] won't ever like someone who hates cars, but it's not like [Staci] matters."
        sil "I'm sorry I got so upset back there. This was supposed to be a happy day."
        tb "It's alright. I just don't see why [Staci] matters enough for you to get so upset."
        sil "She wants you to give up your love for cars. What am I going to do if my mechanic decides he wants to swap to a desk job?"
        tb "That's not going to happen. Besides, why would she try to change me? We haven't seen each other in years."
        sil "It's fine. Let's just drop it. Happy day. Today was a happy day. It can't end as an angry day."
        tb "I'm sorry. Today was very nice. I had a lot of fun, and it was even nice getting to go shopping with you."
        sil "It was. I even got to take you for a fun drive. I've never done that for anyone before."
        tb "It was really nice. I haven't ever been in a car with someone who drove like that."
        sil "Well, we're here now. I'll let you head home. Good night, [PC]."
        tb "Good night, [Silvie]."
        $   with_sil = False


    elif with_lan:
        scene bg lanin
        show lanna at right with dissolve
        play music kisstokiss fadein 1.5
        lan "You know, [PC], you're alright."
        tb "Thanks, I guess."
        lan "I told you I'm not really big on that whole \"friends\" thing, but you're not too bad. I'm glad I gave you a chance."
        "I don't know what to say. My mind is still replaying the kiss over and over again."
        "We didn't speak much on the drive back to my car. The only sound was the sound of her engine."
        "When we finally arrived back at my car, [Lanna] nudged my arm."
        lan "Must have been a long time since you've been kissed by a pretty girl if you're still this speechless."
        lan "I'll have to give [Silvie] some tips so she doesn't let you down when it's her turn."
        tb "You're probably the craziest person I've ever met."
        #Show lanna wink
        lan "If you think the first date is wild, just wait until the second."
        tb "I'm not sure I can handle that, but I'll be sure to give you a call sometime soon."
        lan "Don't worry. I already know you'll call me back."
        "She gave me one last seductive smile, and drove away."
        "What a day."
        $   with_lan = False

    elif with_she:
        scene bg stang
        play music she fadein 1.5
        show shelby at left with dissolve
        "We drove back to the parts store where I was parked."
        she "I'm glad we ran into each other today, even if it did mean meeting your racist ex."
        tb "I'm glad too, and I'm sorry about [Staci], though she's really not that bad."
        tb "Thanks for driving me around, it's not too often I get to ride in a classic."
        she "You calling me old?"
        "[Shelby] smiled with a wink."
        she "Oh! Before I forget, here's my number. give me a call sometime. I'll give you a rematch at that pullup contest."
        play sound cell
        "{color=FFF700}Acquired [Shelby]'s number.{/color}"
        $   shelby_number = True
        tb "I don't know about the pullups, but I'll give you a call for sure. Goodnight [Shelby]."
        she "'Night [PC]"
        "I watched her peel out and blast away before getting in my car and doing the same."
        "Everyone needs to cut loose every now and then."
        $ with_she = False


    $   renpy.jump("dend_" + str(day))







    label dend_2:

    #Whichever girl you date, you will spend the day with and do an activity at the end of the day.
    #This activity will end with meeting UNNAMED HUMAN WHO HATES CARS GIRL


    stop music fadeout 1.5
    scene bg bed with dissolve
    play music bed fadein 1.5
    "I can't believe I ran into [Staci]. She really did a lot to help get me through high school."
    "Until she dumped me of course."
    "I wonder if she's changed much since then?"
    "Somehow I get the feeling she's not going to go over well with the Kuruma Musumes, but maybe she'll learn to accept my passion for cars now that she's older."
    "It's been an eventful day, but it was a good day."


    #Day 3
    label dstart_3:
    $   call_silvie = False
    $   day += 1
    show bg bed with fade
    "DEBUG: Day 3 Start | Actually Day [day]"


    menu:
        "Call Someone":
            label d3_call:
            "Who should I call?"
            menu:
                "Call [Silvie]":
                    $   call_silvie = True
                    $   sil_rel += 3
                    $   renpy.jump("sil_dc" + str(sil_date +1))
                    #if sil_date == 1:
                    #    tb "Hey, Silvie. Are you busy today?"
                    #    sil "Not at all! Would you like to meet up?"
                    #    tb "Sure. Where should we meet?"
                    #    sil "I'd like to go to that little park downtown, if you don't mind."
                    #    $   sil_rel += 3
                    #    jump sil_park_date1
                    #elif sil_date == 1:
                    #    jump sil_park_date1
                    #else:
                    #    return
                "Call [Mia]" if mia_number:
                    $   call_mia = True
                    $   mia_rel += 3
                    $   renpy.jump("mia_dc" + str(mia_date+1))


                "Call [Staci]" if staci_number:
                    $   call_sta = True
                    $   sta_rel += 3
                    $   renpy.jump("sta_dc" + str(sta_date+1))

                "Call [Lanna]" if lanna_number:
                    return

                "Call [Shelby]" if shelby_number:
                    return

                "Go somewhere":
                    jump d3_go


        "Go somewhere":
            label d3_go:
            "Where should I go?"
            menu:
                "Coffee shop":
                    if sil_date < 1:
                        "I should try that coffee shop near work."
                        #On day 3, you will meet Silvie working at the coffee shop. You can have the coffee date on her break.
                        jump sil_coffee_date1
                    elif mia_date == 1:
                        return
                "Park":
                    #Hachi Roku is at the park on day 3
                    return
                "Parts 4 U":
                    "I could probably use a few extra tools. I guess I'll go check Parts 4 U."
                    if mia_date < 1:
                        jump mia_p4uintro

                "Call someone":
                    jump d3_call

    label dend_3:

    "I should really get some rest."


    #Day 4
    label dstart_4:
    $   call_silvie = False
    $   call_mia = False
    $   call_staci = False
    $   call_lanna = False
    $   call_shelby = False
    $   day += 1
    show bg bed with fade
    "DEBUG: Day 4 Start | Actually Day [day]"

    menu:
        "Call Someone":
            label d4_call:
            "Who should I call?"
            menu:
                "Call [Silvie]":
                    $   call_silvie = True
                    $   sil_rel += 3
                    $   renpy.jump("sil_dc" + str(sil_date +1))

                "Call [Mia]" if mia_number:
                    $   call_mia = True
                    $   mia_rel += 3
                    $   renpy.jump("mia_dc" + str(mia_date+1))

                "Call [Staci]" if staci_number:
                    $   call_sta = True
                    $   sta_rel += 3
                    $   renpy.jump("sta_dc" + str(sta_date+1))
                "Call [Lanna]" if lanna_number:
                    return
                "Call [Shelby]" if shelby_number:
                    return
                "Go somewhere":
                    jump d4_go


        "Go somewhere":
            label d4_go:
            "Where should I go?"
            menu:
                "Coffee shop":
                    if sil_date < 1:
                        "I should try that coffee shop near work."
                        jump sil_coffee_date1
                    elif mia_date == 1:
                        return
                "Park":
                    return
                "Parts 4 U":
                    return

                "Call someone":
                    jump d4_call

    label dend_4:
    stop music fadeout 1.5
    scene bg bed with dissolve
    play music bed fadein 1.5

    "I should really get some rest."


    return

#Calls
    #Silvie
    #Date 1
    label sil_dc1:
    "I guess I should call Silvie."
    sil "Hello?"
    "DEBUG: sil_date=[sil_date]"
    tb "Hey, [Silvie]. I was wondering if you'd like to go have that coffee today."
    sil "I'd love to! Let's go to that little coffee shop over near your work. Want to meet there?"
    tb "That'll be fine. See you soon."
    "I hung up, grabbed my keys, and was over to the coffee shop as fast as I could."
    jump sil_coffee_date1


    #Date 2
    label sil_dc2:
    tb "Hey, Silvie. Are you busy today?"
    sil "Not at all! Would you like to meet up?"
    tb "Sure. Where should we meet?"
    sil "I'd like to go to that little park downtown, if you don't mind."
    $   sil_rel += 3
    jump sil_park_date1


    #Mia
    #Date 1
    label mia_dc1:
    "The phone rang only twice before [Mia] answered."
    mia "Hello? Who is this?"
    tb "Hi, it's [PC]. [Silvie] gave me your number."
    mia "Of course she did. What do you want?"
    tb "I was wondering if you'd like to meet up somewhere."
    mia "Fine, I guess. How about coffee?"
    tb "Great. I'll meet you there."
    $   mia_rel += 3
    jump mia_coffee_date1

    #Date 2
    label mia_dc2:
    "The phone rang twice before [Mia] answered."
    mia "Hey, [PC]."
    tb "Hi. I was wondering if you could hang out today."
    mia "Well, I'm actually working right now, but I could go out with you later. How does 6:00 sound?"
    tb "That'd be great."
    mia "Anywhere in particular we're going?"
    tb "If it's going to be that late, how about dinner?"
    mia "Oh, dinner? Are you sure [Silvie] won't mind?"
    tb "It's fine. I think she'll be okay with it."
    mia "Alright. Mind if I pick you up? Seeing as how it won't really work well the other way around."
    tb "Sure."
    "I gave [Mia] my address and hung up."
    "I really do hope [Silvie] won't be jealous of me spending time with another car."
    $   mia_rel += 3
    jump mia_dinner1


    #Staci
    #Date 1
    label sta_dc1:
    "The phone rang."
    "It kept ringing."
    "I decided to hang up if there was no answer by the next ring."
    sta "Hello?"
    "Thank goodness."
    tb "[Staci]! How are you?"
    sta "Oh, hey [PC]. I was wondering when you'd call."
    if day == 3:
        tb "It's only been a day."
        sta "Has it? Oh. I guess it has."
    tb "So I was wondering if you might want to go out for coffee."
    sta "Of course I would! Would you mind picking a girl up?"
    "[Staci] gave me her home address."
    tb "Great. I'll see you soon."
    jump staci_coffee1



#Dates

    #Silvie Dates


    #Silvie Coffee Date 1

    label sil_coffee_date1:

    stop music fadeout 1.5

    scene bg coffee with dissolve

    play music burning fadein 1.5

    "Hostess" "Welcome to Cafe Le Auto. Please have a seat."

    if sil_date < 1:
        if day > 1:
            jump no_first_day_date


    "Somehow I never knew that this place was here."
    "Even though it's within walking distance from work, we drove here because [Silvie] can't travel far from her car form."
    jump sil_date1_2

    label no_first_day_date:
    show silvia
    if call_silvie == False:
        sil "Hey, [PC]! What are you doing here?"
        "Looks like [Silvie]'s here today too."
        tb "I just thought I'd check this place out since I've never been here before."
    elif call_silvie == True:
        tb "Hey, [Silvie]. It's good to see you again."
        sil "You too. Have a seat."
        "I pull up a chair across from [Silvie]."
        tb "So, do you come here often?"
    sil "It's my favorite."
    "I look around and notice why.{w} The whole place is car themed for some reason."
    tb "The car theme's a little odd for a coffee shop, don't you think?"
    sil "Maybe it is, but I like it."

    if call_silvie == False:
        sil "Since we're here, do you want to sit together and talk?"

        menu:
            "Sure.":
                "We place our orders and take a seat."
                $   sil_rel += 2
                jump sil_date1_2
            "Not today.":
                $   sil_rejection += 1
                $   sil_rel -= 1
                tb "Sorry to put it off again. I can't stay here long."
                #show sil_dejected
                sil "Oh.{w} Okay then. Maybe next time."
                tb "Next time for sure."
                hide silvia with dissolve
                jump sil_coffee_denial


    label sil_date1_2:

    $   first_date = True
    $   sil_coffee_date1 = True

    show silvia
    tb "So do most cars like coffee?"
    sil "Not necessarily."
    sil "We all have our own tastes, just like people, but most of us do like to come to cars and coffee meets just to socialize, so we all know the local coffee shops."
    tb "Do you even need to eat, or can you just pull up to a gas station to drink?"
    sil "Hehe~"
    sil "Yeah, we do need food and water and all of that on top of needing gas, oil, brake fluid, and everything for our car."
    #show sil.wink
    sil "I guess you could say we're pretty high maintenance girls. {b}USE WINKING SILVIE IMAGE{/b}"
    tb "Haha. I guess so."
    tb "How do you even afford all of that?"
    sil "Well, there's plenty of people who will pay you for a ride somewhere."
    sil "And some kuruma musumes will even pick up jobs at cafes and restaurants."
    sil "We don't really need a house, even if we're independent, so that's one thing that doesn't cost much, though it is nice to have a warm garage to rest in."
    tb "Are most of you homeless then?"
    sil "Well, home is where you make it."
    sil "Besides, don't you know the saying \"you can live in a car but can't race a house?\""
    tb "Wait. You girls actually race? Seems especially dangerous for someone who's whole existence is tied to her car."
    sil "It's not like it's that much more dangerous than it is for humans."
    sil "Besides, there's nothing that makes a car feel more alive than going full throttle to test herself against another car."
    tb "So you're thrill seekers then?"
    sil "I guess you could say that."
    sil "Though maybe it's because of the souls who created us. My owner was a street racer when I was born, so maybe that's why."
    tb "You better be careful out there if you're racing. I think I'd prefer it if I didn't have to fix you."
    sil "It's fine. I'm a pretty good driver."

    if mia_met:
        mia "Hey, [Silvie]! I didn't expect to see you here today."
    else:
        "Small Child" "Hey, [Silvie]! I didn't expect to see you here today."

    $   with_mia = True


    show silvia at slideleft
    show mia behind silvia:
        xalign 1.75 yalign 1.0
        linear 0.5 right


    sil "Oh, hi [Mia]. How are you?"
    if mia_met:
        mia "Doin' pretty good. Hi, [PC]. Nice to see you again."
        tb "Hi, [Mia]."
        sil "Oh, have you two met?"
        mia "Yeah, we met the other day. Honestly, he's kind of hopeless, but I can see why you like him."
        #show silvie blush
        sil "I don't know what you mean."
        mia "Poor guy has no clue how to talk to cars. And the lewd things he said to me? Well, you might be more open to them."
        #show silvie mad
        sil "What did you say to her!?"
        mia "He asked to look up my skirt!"
        tb "I asked to look at your engine! I didn't know that was taboo for you girls!"
        #show silvie laugh
        sil "Hahahahahaha!{w} Is that all? Come on, [Mia]. You know the poor guy's new to all of this."
        mia "It was still really awkward."
        sil "You better get used to it. He might be working on you some day."
        mia "Well I'm sure you just loved having him under you."
        #show silvie embarrassed
        sil "It's not like that!"
        "These cars and their innuendos..."
        mia "Relax. You know I'm teasing. Anyway, sorry to interrupt your date."
        sil "It's not really a date."
        mia "Sure it's not."
        #show mia serious
        mia "You better be nice to [Silvie]. I don't like people hurting my best friend."
        mia "Anyway...{w} See ya!"
        hide mia
        with moveoutright

        $   with_mia = False

        show silvia:
            left
            linear 0.5 center

        "[Silvie] burried her face in her hands as [Mia] strolled out of the coffee shop."
        sil "I'm so sorry. [Mia] lives to embarrass me."
        tb "Don't sweat it. I could tell she was just trying to press your buttons."
        "..."
        tb "Wait, that's not a car innuendo too, is it?"
        #show silvie giggle
        sil "Haha. No, that's okay."
        tb "She's right though. I really am kind of clueless on all of this."
        sil "Don't feel bad about that. Humans have trouble adjusting to something that completely breaks their understanding of the world."
        #show silvie smile
        sil "You're doing just fine."
        tb "Thanks. I'm trying my best to learn my way around it all."
        sil "I'm glad you and [Mia] can be friends now. Knowing more Kuruma Musume should help you learn faster."

    else:
        mia "Doin' pretty good. Say, who's this guy you're with? Is he-"
        "[Silvie] blushes."
        sil "He's my mechanic. He did a really great job the other day so I thought I'd say thanks by buying him a cup of coffee."
        tb "Hi, I'm [PC]."
        mia "[Mia]. Pleased to meet ya."
        "Mia reached out her hand and shook mine viggorously."
        mia "Poor [Silvie] here sucks at talking to guys. Glad she found someone she's comfortable with."

        show mia:
            right
            linear 0.5 center

        "[Mia] whispered something to [Silvie] and her blush brightened."

        show mia:
            center
            linear 0.5 right

        mia "Well, it was nice to meet you. I've got places to be, so I'll stop interrupting your date. You two have a nice evening."

        hide mia
        with moveoutright

        $   with_mia = False

        show silvia:
            left
            linear 0.5 center

        "[Silvie] burried her face in her hands as [Mia] strolled out of the coffee shop."
        sil "I'm so sorry. [Mia] lives to embarrass me. Please just ignore everything she said."
        tb "Don't worry about it. That's just how kids are. So do you know her mom or something?"
        sil "Kid? You mean you couldn't tell?"
        sil "[Mia] is another kuruma musume."
        "I looked out of the window and sure enough, there went that little girl peeling out of the parking lot in the driver's seat of her own car."
        "Insert CG of [Mia] driving away"
        tb "Seriously!? But she looks so young!"
        sil "Well, she is a pretty small car. Most older roadsters are about her size."
        tb "I can only imagine how the police react to seeing a kid driving around like that."
        sil "She's good at playing up the cute and innocent act, so I think they're usually pretty lenient once they see her ID."
        tb "Do you girls get fake driver's licenses?"
        sil "Some of us manage to get real ones. I'm sure she has a real license. It's just a nightmare trying to sort out the paperwork when the only document you have is a title."
        tb "I see."
        $   mia_met = True



    tb "Well, it's been a lot of fun today, but I should be heading home."
    if day == 1:
        tb "I'm taking the next week off from work, so maybe I'll give you a call."
    elif day > 1:
        tb "I have the rest of the week off, so maybe I'll give you a call soon."
    sil "If you want to. Please don't feel like you have to or anything. I'm just happy I got to spend this time with you."
    tb "Take care of yourself, [Silvie]."
    sil "You too."
    $   coffee_date = True
    $   sil_date += 1
    $   with_sil = False

    if day == 1:
        jump dnight_1
    elif day == 2:
        jump solo_mall1
    else:
        $   renpy.jump("dend_" + str(day))



    label nosildate1:
    $ first_date = False
    tb "Besides, it's getting late. I should probably get home."
    "[Silvie] looks a bit dejected."
    sil "Alright. Well, if you want to go some other time, just give me a call."
    $   with_sil = False
    jump dnight_1

    #Sil Coffee Loop Break
    label sil_coffee_denial:
    if day == 2:
        jump solo_mall1
    if day == 3:
        return


    #Sil Park Date 1

    label sil_park_date1:
    play music park fadein 1.5
    if call_silvie:
        show bg park
        show silvia with dissolve
        $   with_sil = True
        $   solo = False
        sil "Hey! It's good to see you again!"
        tb "You too."
        sil "It's such a nice day out, isn't it?"
        sil "I just want to relax and soak up some sun."
        tb "Me too."
        jump sil_park_date1_2

    else:
        show bg park
        "I always enjoy this park. It has such a relaxing atmosphere."
        sil "[PC]? Is that you?"
        show silvia with dissolve
        $   with_sil = True
        $   solo = False
        "[Silvie] walks over to me, grinning from ear to ear."
        sil "It's good to see you again! This is such a nice park, especially on a day like today."
        tb "Kuruma Musumes like pretty days too?"
        sil "Of course we do. I mean, don't get me wrong, rain is fun in its own right, but it feels great to relax out in the sun."


    label sil_park_date1_2:
    tb "I never would have guessed a car could be so human-like."
    sil "What do you mean?"
    tb "Just the fact that you enjoy nice days like this and like to relax the same as us."
    sil "Constant strain on our parts gets pretty tiring for us too. As much as we like driving, we need time off."
    sil "And like I said, our \"human\" bodies need all of the same things as actual humans."
    tb "It must be weird having two bodies."
    sil "Maybe to you, but to us, it seems weird that humans only have one body."
    tb "I guess it would."
    sil "It's like having two selves, each with different desires. The car part of me wants to drive and burn rubber and make some noise."
    sil "But at the same time, my human side enjoys relaxing, eating, and has every single desire that a normal human would have."
    tb "Do you remember anything about being just a car?"
    sil "Not really. It's kind of like, one day you just exist. You don't know where you came from or anything. It's kind of scary, actually."
    tb "Did your owner know?"
    sil "I was never brave enough to let him see me."
    sil "The one thing you do know early on is that you're unique. At first, I thought I was the only car in the world before I met Mia."
    tb "How did you meet?"
    sil "I went to a cars and coffee meet and she noticed me right away. I was terrified when she called me out, but it was such a relief to know I wasn't alone."
    tb "It must be terrifying to not have anyone like yourself to talk to."
    sil "Yeah. There were so many questions I had to ask Mia. She knows a lot of other Kuruma Musumes in town, so she introduced me to some of them."







    menu:
        "What was your owner like?":
            jump about_sil_owner
            $   sil_rel += 2
        "Tell me about [Mia].":
            jump sil_about_mia
            $   mia_rel += 1

    label about_sil_owner:
    "Sorrow instantly filled [Silvie]'s eyes and she looked away."
    tb "Sorry, I didn't mean to pry. If it's a sad story, you don't have to tell it."
    "[Silvie] wiped her eyes."
    sil "It's fine. I'll tell you someday, but not like this. Today's a happy day."
    tb "You're right. Today's just too dang pretty to be sad."
    sil "Hey, you wanna go feed the ducks?"
    menu:
        "Sure.":
            $   sil_rel += 2
            jump sil_park_date1_ducks
        "Nah. I really can't stay any longer.":
            $   sil_rejection += 1
            sil "That's too bad. It was great to see you again."
            tb "It was great seeing you too."
            sil "Give me a call next time you want to hang out."
            tb "I will."
            if day == 2:
                $   with_sil = False
                $   solo = True
                jump solo_mall1
            else:
                return

    label sil_park_date1_ducks:
    "Silvie suddenly took me by the hand and pulled me along to the pond in the middle of the park."
    #scene bg pond
    #show silvia
    "We bought some duck food from a machine and split it between ourselves."
    #cg of Silvie leaning over a handrail, throwing food to the ducks, her hair blowing freely
    #scene bg pond
    #show silvia
    sil "I love ducks. They're just so cute."
    jump sil_park_date1_3



    label sil_about_mia:
    sil "She's wild. I don't know anyone quite as crazy as she is on the road."
    tb "I better not ride with her!"
    sil "No, it's okay. She's actually a {i}really{/i} good driver. Definitely one of the best I know."
    tb "That little girl?"
    sil "Absolutely. Trust me, you don't want to underestimate her. She does not take it well."
    tb "Noted."
    sil "Also, don't insult her popups. She loves them."
    sil "She knows how young she looks and makes a point of proving that she's just as capable as anyone else. It's actually really inspiring."
    tb "She seems to act kind of childish though."
    sil "That's just [Mia]'s personality. When she's not racing, she's pretty carefree and thoroughly enjoys being able to act like a kid and get away with it."
    tb "I guess she could get away with a lot if people think she's just a kid. I'm sure there's a lot of downsides to looking so young as well."
    sil "Yeah, she's been kicked out of bars a few times."
    tb "I hope they didn't try to keep her I.D. thinking it was fake."
    sil "Sadly, she's gone through several drivers' licenses because of that."
    tb "It must suck to not get the respect you deserve because people think you're just a kid."
    sil "It does, but she makes the most of it."
    sil "You know what? I should give you her number. Maybe she can start embarassing you instead of me."
    $   mia_number = True
    "I added Mia's number to my phone as Silvie read it out."
    sil "She's michievous, though. Be careful."
    tb "Trust me, I will."
    jump sil_park_date1_3

    label sil_park_date1_3:
    tb "Say, when Kuruma Musumes are born, are you like, babies, or are you just born as adults?"
    sil "Mentally, we're usually similar to our owners. We know how to speak and all that. We're adults in a way, but because we're still inexperienced, we're also like kids."
    tb "Do you mature faster than people?"
    sil "Generally, yeah. A lot of it has to do with what kind of car we're born from, but overall we learn and grow very quickly."
    tb "What do you mean? Like, different cars have different capabilities?"
    sil "I thought a mechanic would know that."
    #show silvie wink
    tb "Come on now, you know what I mean."
    sil "Hehe~"
    sil "Yeah, while a lot of our personality is based on the people who create us, there's plenty of aspects that are based on the capabilities of our car-self."
    tb "So, a slow car's gonna be slow in other ways as well?"
    #show silvie wink
    sil "Now that's just mean."
    #show silvie smile
    extend " But yeah, that's kinda how it is."

    sil "Well, this park has been wonderful, but I think I can hear my tires calling."
    tb "Do you feel things in your car even when you're walking around as a person?"
    sil "Yeah! I experience everything as a car and a human at the same time."
    sil "You know how sometimes it's like part of you feels one way about something, but then you also feel a different way?"
    sil "It's like that all the time for us. Sometimes it's hard to find a balance because we want to be cars and drive until we break, but we also just want to be normal people doing normal things."
    tb "Sounds like it would drive you crazy."
    sil "Maybe it does for some cars?"
    sil "Anyway, I'm just itching to go for a drive right now."
    menu:
        "Would it be alright if I rode with you?":
            $   sil_date += 1
            $   sil_rel += 2
            sil "Sure! That'd be awesome!"
            jump sil_drive1
        "Alright. I guess I'll see you later.":
            if day == 2:
                $   with_sil = False
                $   solo = True
                jump solo_mall1
            else:
                return

    label sil_drive1:
    #CG of Silvie walking through the park, hand outstretched behind her holding player's hand
    "[Silvie] once again took me by the hand and lead me off to her car."
    #CG sequence
    stop music fadeout 1.5
    play music fallapart fadein 1.5
    scene bg silin
    show silvia
    sil "Buckle up, please."
    "I planned to anyway."
    "[Silvie] took off at a slow pace, navigating her way through the city."
    "It felt strange letting someone drive me around. Since getting my license, I almost always drove everywhere on my own."
    "In fact, I was usually pretty nervous letting someone else drive me."
    "Yet with Silvie behind the wheel, it just felt natural. Like I had no reason to worry."
    sil "We're almost out of the city now. Mind if I cut loose a little?"
    tb "Go ahead. Just be careful with me in here."
    sil "Of course I will."
    "[Silvie] hit the throttle hard and we took off like a rocket."
    "I consider myself to be a good driver, but I doubt I could ever compare to [Silvie]."
    "These Kuruma Musumes really were something else."
    "The sheer joy on her face each time the rear end slid out reassured me that she knew exactly what she was doing."
    tb "You're a really good driver."
    "She didn't respond, but I noticed her smile grow and her cheeks redden."
    "For a car, this must be the best way to live. No restrictions, no cares, just yourself and the road beneath your tires."
    "After at least an hour of [Silvie] racing down every road she could find, she finally slowed to a normal speed."
    sil "Did you have fun?"
    tb "Yeah. That was incredible. I guess it's only natural that a car would be good at driving."
    sil "Yeah. No one knows a car better than herself."
    #end cg sequence
    if day == 2:
        sil "Hey, I've got some shopping to do tonight. Would you like to come with me?"
        menu:
            "Sure.":
                sil "Awesome! I'll drive."
                stop music fadeout 1.5
                $   sil_rel += 2
                jump sil_mall1
            "No thanks.":
                tb "It's getting a little late."
                sil "Aw, that's too bad. I had a lot of fun today."
                tb "Yeah, me too. We'll have to get together again soon."
                sil "Bye, [PC]."
                $   with_sil = False
                $   solo = True
                jump solo_mall1

        jump sil_mall1
    else:
        $   renpy.jump("dend_" + str(day))





    #Mia Dates

    #Mia Alternate Intros

    #P4U Intro
    label mia_p4uintro:
    stop music fadeout 1.5
    scene bg p4u
    play music p4u fadein 1.5
    "I love coming to this store, even when I don't need anything. Sales actually feel like sales and the prices are never too high."
    "Owner" "Good to see you again. Need any help this time?"
    tb "No thanks. Just grabbing a few extra tools. One of the socket wrenches at work went missing the other day."
    "Owner" "That's not good. Think it was stolen?"
    tb "I'm afraid one of my employees might have taken it, but it's hard to say for sure who it was."
    "Owner" "That bastard. Hope you catch him."
    tb "It's just a socket wrench, so I'm not really out much if I never find out who it was."
    "Owner" "You just better hope he doesn't get any ideas about stealing more important things. Or worse, stealing valuables out of a customer's car."
    tb "That is the fear, isn't it?"
    tb "I'll just keep a close eye on the boys for a while."
    show mia with dissolve
    if mia_met:
        "Mia stepped out of one of the aisles. She's so short that I never even noticed her in here."
        mia "You could always just bring it up at work. Tell 'em all that if they give themselves up now they can keep their job, but if you catch them, you'll make sure they never work again."
    else:
        "A young girl stepped out of one of the aisles. I thought I was alone in here, but I guess this child was hiding between the racks."
        "Small Child" "You could always just bring it up at work. Tell 'em all that if they give themselves up now they can keep their job, but if you catch them, you'll make sure they never work again."


    if mia_met:
        "Mia's cunning is surprising. I know she's not actually a child, but it's so hard not to see her that way sometimes."
    else:
        "This girl's pretty smart for her age. I wonder who's kid she is?"
    "Owner" "Hey, [Mia]. Sorry, I didn't see you come in. Lookin' for anything specific?"
    mia "Nah. I was just looking for ideas."
    "Owner" "Did [Silvie] ever get her car checked out? I know it was in pretty bad shape the other day."
    if mia_met == False:
        "Wait a second..."
        mia "Yeah, she took it to a shop pretty close to this place. Apparently the mechanic did a good job 'cause she won't shut up about it. It's always \"[PC]\" this and \"[PC]\" that. I think she has a crush."
        "I have to ask."
        tb "You know [Silvie]?"
        mia "I guess. Who are you?"
        tb "I'm [PC]."
        mia "Oh. Well then, this is awkward."
        mia "For what it's worth, I'm glad she found such a good mechanic."
        tb "Thanks. Are [Silvie] and your mom friends or something?"
        #Angry Mia
        "[Mia] stares me down with fire in her eyes."
        "Owner" "Easy now, [Mia]. He didn't mean any harm."
        "Owner" "[Mia] might look young, but trust me, buddy, she's no child."
        #Smug Mia
        mia "That's right."
        "Owner" "And she certainly won't take kindly to you acting like she is."
        mia "Since [Silvie] is over the moon about you, I'll give you a break this once for her sake."
        "[Mia] sticks out her hand, and I shake it."
        mia "Pleased to meet ya."
        tb "So you're friends with [Silvie] then?"
        mia "Of course. Why don't you come check out my car if you're wondering why we're friends."
        tb "Well, I never pass up an opportunity to check out a nice car."
        #Mia Blush
        mia "Uh, yeah. Well, come on. I parked over around the side of the building."
        scene bg miap with dissolve
        show mia at right with dissolve
        mia "Well, this is me."
        tb "That's a beautiful car."
        #show mia blush
        tb "Seems a little plain on the outside, though."
        mia "Appearances aren't everything."
        tb "Oh really? Can I see under the hood then?"
        #show mia blushangry
        mia "Pervert! Asking to look under a girl's hood? That's as bad as looking up a girl's skirt!"
        #show mia blushshy
        mia "I mean..."
        mia "Uh..."
        mia "Damnit, I didn't want to do it like this."
        tb "So, that really is you, isn't it?"
        #show mia cuteangry
        mia "I wanted to be really cool when I revealed it, and you had to go throw everything off saying pervy things. That's not cool."
        tb "Heh. Sorry. As a mechanic, looking under a car's hood is just normal stuff. And the cars that come through my shop don't usually complain about it."
        mia "Well yeah, it's the same as people going to the doctor. I doubt you'd be okay with your doctor asking to check out your parts in the middle of a parking lot for no reason."
        tb "That's a fair point."

    else:
        mia "She sure did. In fact, it was this guy right here who fixed her up."
        mia "Just between you and me-"
        "[Mia] moved closer to the shop owner, but didn't lower her voice at all."
        mia "I think [Silvie] likes him."
        tb "Come on, [Mia]. I'm sure [Silvie]'s told you that we're just friends."
        mia "We'll see."
        mia "Hey, [PC], I don't think you've had a chance to see my car yet, have you?"
        tb "Nope. Do you mind if I take a look?"
        mia "Not at all. Always glad to show off my hard work to someone who can appreciate quality."
        mia "At least [Silvie] tells me you have good taste. We'll see."
        "I paid for the tools and followed [Mia] around the side of the shop where she had parked."
        scene bg miap with dissolve
        show mia at right with dissolve
        mia "Before you embarrass yourself, I know [Silvie] already told you what I am, so it's fine to just come out and talk about it. Don't act like you're clueless."
        tb "I thought Kuruma Musumes liked to keep themselves secret."
        mia "Not really. We don't go telling everybody, but we don't really hide ourselves either. Not like anyone ever believes us when we say something."
        mia "Anyway, this is me. What do you think?"
        tb "It looks very clean. A bit plain, but I think it's very nice."
        #Disgruntled mia
        mia "Plain? Haven't you ever been told not to judge a book by its cover?"
        mia "Sure, my wheels aren't crooked and I don't have some wild bodykit or anything, but a race car's about what's under the hood and that's what I am."
        tb "I'm sorry. Can I look under your hood then?"
        #show mia blushangry
        mia "That's way too forward, you pervert!"
        tb "Sorry, is that a car faux pas?"
        #show mia disgruntled
        mia "I should say so. That's like peeking up a girl's dress. Sure, we'll let a mechanic look to fix us, but this is like a doctor asking you to take off your pants in a parking lot."
        tb "I didn't mean to offend you. I'm not used to cars that can tell me what they like and don't like. Most cars don't complain."

    mia "For someone who works with cars for a living, you sure don't know much about cars."
    tb "I guess I must have slept through the part of class where they explained proper etiquette for when a car starts talking to you."
    mia "I can't believe you'd sleep through the best part of class!"
    tb "Hahaha. Trust me, if they actually did teach anything about this, I'd have been paying full attention. Give a guy a break, okay?"
    mia "Fine. I'd better tell [Silvie] that you're hopeless and she should give up on you though."
    tb "So, since I clearly don't know enough about Kuruma Musume, would you be interested in grabbing a cup of coffee and having a chat with me? I'd love to learn more."
    mia "Eh, sure. Maybe I can teach you how to not embarrass yourself in front of [Silvie] at the very least."
    mia "Does Cafe le Auto sound good?"
    if coffee_date:
        tb "That sounds perfect."
    else:
        tb "Where is that?"
        mia "It's actually just down the street from your shop. You can follow me over to it."

    #CG of Mia driving down the road ahead of Tofuboy from TB's perspective.
    "CG - See note in code"
    "I got in my car and followed [Mia]. She was hard to keep up with, yet I got the strangest feeling that she was trying to make it easier for me."
    "Show Cafe le Auto exterior"
    if coffee_date:
        mia "Wasn't too hard to follow, was I?"
        tb "Nah, I could keep up just fine. You're pretty good though."
        "That's a lie. I was worried I'd lose her several times."
        mia "Well, in that case, I'll just have to make it harder next time."
        "I should have been honest."
    else:
        mia "Sorry if I was hard to keep up with."
        tb "It's alright. I managed just fine."
        mia "I can't wait for you to see inside. I think you'll love it, and we cars always feel right at home here."
    stop music fadeout 1.5

    show bg coffee with dissolve
    play music burning fadein 1.5

    if coffee_date == False:
        "Mia was right. I love the car aesthetic in here."
        $   mia_met = True

    "We placed our orders and took a seat at one of the empty tables around the cafe."
    mia "So [Silvie] hasn't been very clear with me and I'm curious. Why did you actually believe her when she told you what she was?"

    jump m_alt_intro_link









    #Mia Coffee Date 1

    label mia_coffee_date1:

    stop music fadeout 1.5

    show bg coffee with dissolve

    play music burning fadein 1.5



    if day == 2:
        $   day2_date = True


    if call_mia == True:
        "I don't see [Mia] anywhere. I guess she's not here yet."

    "I'm still surprised I never came here before. It's so close to work and the coffee is great."
    tb "[Silvie] really does have good taste."
    mia "Is that so?"
    $   with_mia = True
    show mia with dissolve
    tb "Oh, did I say that out loud?"
    if call_mia == True:
        "She can be really quiet when she wants to. I never noticed her come in."

    mia "Ha-haha! Not quite as red as she was, but I still got you."
    "The nerve of this girl."
    tb "I bet I can get you."
    mia "Oh yeah?"
    tb "You're a car, aren't you?"
    mia "{cps=10}...{/cps}"
    mia "{cps=10}...{/cps}"
    mia "Is that all?"
    tb "Aren't you surprised that I knew? Embarrassed that your secret was found out?"
    mia "Of course you knew. You were here with [Silvie], weren't you? If she's talking to you, you probably already know who every Kuruma Musume in the city is."
    tb "Actually, I don't. [Silvie] said you girls were usually pretty shy."
    mia "Hah. That's just [Silvie]. Yeah, we don't advertise ourselves, but we don't exactly hide from the world either."
    mia "If we like you, we tell you. Heck, I tell people I just met for a laugh when they think I'm pulling their leg. I'm surprised you even believed [Silvie]."
    label m_alt_intro_link:
    tb "Well, the only other option was that I was crazy after the way she revealed herself, so I like the option that means I'm not insane."
    mia "She fused in front of you, didn't she?"
    tb "If you mean got in her car and vanished into thin air, then started talking to me through the speakers, then yeah. She fused."
    mia "I hope she at least gave you some warning."
    tb "None at all."
    mia "Ha-haha. That's [Silvie] for you. She's got a good heart, but she's pretty careless sometimes. {w}Even on the road."
    tb "I'll have to keep that in mind if I ride with her any distance."
    mia "I'm sure she'll be safer with you in the car."

    menu:
        "Tell me about yourself.":
            $   mia_rel += 2
            jump about_mia

        "Tell me about [Silvie].":
            $   sil_rel += 1
            jump mia_about_silvie

        "I should go.":
            $   mia_rejection += 1
            $   day2_date = False
            mia "Oh, alright then. Let me give you my number at least."
            $   mia_number = True
            $   with_mia = False
            jump solo_mall1


    label about_mia:

    mia "What do you want to know about me?"
    tb "Well, what do you do to make money? [Silvie] said some cars sell rides and others get waiting jobs."
    mia "I sell drugs."
    "..."
    tb "Seriously?!"
    mia "Ha-haha! Wow, you're so easy. Nah, I actually get paid to watch over this woman's elderly parents."
    mia "I mean, I guess I do sometimes give them drugs. {w}But obviously that's just the stuff their doctor gives them."
    tb "That's actually really kind of you."
    mia "Yeah. They have someone else who takes them to see doctors and that kinda thing. The downsides of being a two-seater."
    tb "Do they know what you are?"
    mia "Oh hell no! I wouldn't do that to some poor elderly couple. They've got it hard enough without completely breaking their view of the world."
    tb "I guess you're right."
    tb "So what about racing? Do you do that too?"
    mia "Every{w} single{w} night."
    mia "Sometimes I race for money, but I usually just race for fun."
    tb "Is the money good at least?"
    mia "It's acceptable. Considering my actual job, any extra is good."
    tb "But what if you lose?"
    "[Mia] bored holes through me with her stare."
    mia "I never lose."
    tb "Never?"
    mia "Never."
    tb "Somehow I doubt that."
    mia "You."
    mia "My car."
    mia "Now."
    "[Mia] pulled out a few bills and placed them on the table we were sitting at, then motioned for me to follow her."

    stop music fadeout 1.5
    scene bg miain with dissolve
    show mia at right
    #CG mia-in_car_1
    play music mia fadein 1.5

    "This will be a CG sequence"
    $   mia_first_drive = True
    mia "I'll give you a break this time. Obviously you don't know who you're talking to."
    mia "But it's time for you to know what I'm capable of."

    #play sound mia_ig
    "[Mia] started her engine."
    #CG mia-in_car_2(Playfully open mouth speaking)
    mia "Buckle up. If I get pulled over 'cause of you, I don't want you getting me another ticket."
    "[Mia] is seriously fired up right now. She must take racing way too seriously."
    #CG mia-in_car_3 (red light)
    "We pulled out of the parking lot naturally and casually drove down the road to a nearby red light."
    mia "Don't go grabbing my {i}\"oh crap\"{/i} handle now. It's rude to grab a girl you just met."
    #CG mia-in_car_4 (green light)
    #play sound mia_acceleration.mp3
    "The light changed green and I was pinned to my seat."
    "It was instantly obvious that she was anything but stock. While she looked normal on the outside, there was no telling how much work was done under the hood."
    #CG mia-in_car_5 (just a road)
    "I could see a corner up ahead, but we weren't even beginning to slow down."
    "Against [Mia]'s insistence, I grabbed her handle and braced myself, preparing for a collision."
    #CG mia-in_car_6 (serious face)
    "At the last possible moment, [Mia] braked, downshifted, and threw the car into a drift, sliding perfectly around the corner more expertly than I'd seen outside of movies."
    #CG mia-in_car_5
    mia "Still doubt me?"
    "I couldn't answer with my heart in my throat."
    "She took me in a loop around some small back roads that she was obviously very familiar with, then back to the coffee shop."

    scene bg miain with dissolve
    show mia at right

    mia "Well?"
    "I took a moment to find my ability to speak again."
    tb "So, you never lose, huh?"
    mia "Ha-haha! {w}That's right. You're talkin' to the only roadster in town who's never lost a race."
    tb "With driving like that, I can see why."
    mia "Aw, did I scare you?"
    mia "You don't have to answer. It's written all over your face.{w} Your {i}very{/i} pale face."
    tb "I've loved cars my whole life, so much so that I wanted to work on them for my carreer, but that's way more than I'd be willing to try behind the wheel."
    mia "It probably helps that I know myself better than any human knows their car."
    mia "For me, driving is as simple as walking. I can feel everything. I know exactly how much grip I have, exactly how fast I'm moving, everything."
    mia "If even one little thing changes, I can feel it instantly. I guess it's kind of cheating that I only race against humans, but you guys can still be a challenge."
    tb "So you've never raced another kuruma musume?"
    mia "Never."
    tb "Any reason you haven't?"
    #show mia_dejected
    "[Mia] looked away and the enthusiasm faded from her face."
    mia "I'd really rather not talk about it right now."
    tb "Sorry. If you're not comfortable with talking about it, that's okay."
    mia "Thanks."
    jump mia_coffee_date1_end


    label mia_about_silvie:
    mia "She's pretty cool, I guess."
    mia "Like I said, she's kinda careless, but she's always fun to be around and really does care about others."
    tb "How did you meet her?"
    mia "We met right here, actually.{w} There's a cars and coffee thing they do here. I think I was actually the first Kuruma Musume that she ever talked to."
    tb "Are you girls normally that nervous to talk to others?"
    mia "Only at first. It's kind of weird when you're born and don't know who you are or what you are, just that clearly no one else is like you."
    mia "I knew right away what she was and went to say hi. I think I scared her."
    mia "Poor [Silvie] still thought she was alone in the world, but now that she knows that she's not, she'll go talk to just about any car."
    tb "She's lucky to have met you for her first friend."
    #show mia_blush
    mia "Yeah.{w} I guess so."
    mia "Anyway, she's so enthusiastic about meeting new Kuruma Musumes, I've actually caught her trying to talk to a normal car a few times."
    mia "Don't tell her I told you that, though!"
    tb "My lips are sealed."
    mia "As for racing, though."
    mia "Let's just say no one puts their heart into it more than her while still losing."
    tb "So she's not good?"
    mia "No, she's still pretty good, but she tends to bite off more than she can chew.{w} Doesn't know her limitations at all."
    tb "And you do?"
    mia "Of course. I was racing since before I was born and I've only improved."
    tb "Have you tried to teach [Silvie] at all?"
    mia "Oh, trust me. I've tried. She's a hard student to teach, but she's probably learned some things."
    tb "So how did you know that [Silvie] was one of you?"
    mia "I could tell she recently lost her owner by the look on her face."
    tb "Oh, that's sad. What happened?"
    mia "Sorry, I shouldn't have brought that up. If [Silvie] wants you to know, she'll tell you when she's ready."
    mia "A lot of us have sad stories."
    tb "You're right. I just don't really know how to talk to cars, I guess."
    mia "It's fine. You're new to this."

    label mia_coffee_date1_end:
    $   mia_date += 1
    if day == 2:
        mia "Looks like it's starting to get late. {w}Hey, I've been meaning to do some clothes shopping. Would you like to come with me?."

        menu:
            "Yeah, sure.":
                $   mia_rel += 2
                jump mia_mall1
            "Sorry, not this time.":
                mia "Did I scare you that bad?"
                tb "No, that's not it. I'd just rather be on my own for the rest of the day."
                mia "Fine. I guess I'll see you around.{w} Here, you can have my number. Give me a call if you ever want to hang out."
                $   mia_number = True
                $   with_mia = False
                jump solo_mall1


    else:
        mia "It was nice hanging out with you, [PC]. I know you're busy with work and [Silvie], but if you ever want to hang out again, just give me a call."

        play sound cell
        "{color=FFF700}Acquired [Mia]'s number.{/color}"
        $   mia_number = True

        "Scene Cafe Exterior"
        "I returned to my car and said my farewells to [Mia]. She may be small, but she really does have the heart of a racer in her."
        "We drove off in our separate directions and I returned home."
        stop music fadeout 1.5
        scene bg bed
        play music bed fadein 1.5

        $   renpy.jump("dend_" + str(day))


    #Mia Dinner Date 1
    label mia_dinner1:
    "The day couldn't pass any faster. I spent most of it browsing the internet and watching the clock like I was some love-struck school kid."
    "What was I thinking? I wasn't in love."
    "Besides, she kind of looked like a school kid. I shouldn't get involved with that."
    "Just a normal dinner out with a new friend."
    "That's all it was going to be."
    "Insert horn honk sound effect here"
    pause
    "That's probably her."
    "I walk outside to find [Mia] leaning against the side of her car waiting me."
    #Show CG of Mia as described
    $   with_mia = True
    mia "Not gonna make me wait forever, are you?"
    tb "Sorry, my zero to sixty time is a bit slower than yours."
    mia "Ha-haha!"
    mia "Well come on. Get your butt in gear and let's go. If you haven't picked out a restaurant yet, I know just the one."
    tb "If you have a place you like, then that's fine with me."
    mia "Great. I think you'll love it."
    tb "What restaurant is it?"
    mia "It's a surprise!"
    "I hope there's no dancing animatronics there."
    stop music fadeout 1.5
    scene bg miain with dissolve
    play music mia fadein 1.5
    show mia at right with dissolve
    "Since she won't tell me where we're going, I decide to make conversation to pass the time."
    tb "So does looking so young cause you problems?"
    mia "Yeah. It's actually pretty difficult being a roadster."
    tb "At least you're a girl so you can drive in peace. I'm sure people would laugh at me if they saw me driving you."
    #show mia blush
    mia "Hey, people call it a hairdresser's car all the time. Or they talk about how cute I am with it."
    mia "I mean, I try to make both of my bodies cute, but they say it like it's a bad thing.{w} Like I'm not capable because I'm just some tiny little car."
    tb "I guess that would suck."
    mia "And 'cause I look like a kid, people treat me like a kid. Even when they know my age."
    if mall_date == mia:
        tb "Well, you do buy your clothes from Not-Justice."
        mia "And what of it? They're cute arne't they? So what if they were made for kids. Clothes don't make me who I am."
    tb "Sometimes you act a little childish."
    mia "Are humans one-dimensional? Do you not have multiple sides? I didn't think that was a trait only reserved for cars."
    tb "Sorry, I didn't mean it like that."
    tb "It's just that people often let their first impressions be the only judge of who someone is."
    mia "Yeah, but even still. Even a kid deserves some respect every now and then, but I get none even despite my age."
    tb "I guess you're right."
    mia "I didn't choose to be a roadster, but I am. And you know what? I love it. I just hate being looked down on."
    mia "And don't you dare crack a short joke."
    "I guess even I've been too quick to judge her by her looks."
    tb "Well, from now on, you can count on me to show you respect."
    tb "For what it's worth, I think you're an excellent driver, and a wonderful car."
    #show mia blush
    mia "C- Come on. Don't make this weird."
    tb "Alright."
    "We continued to have lighter conversations until we pulled up on what appeared to be a very nice Italian restaurant."
    mia "They have a vallet here, so I'm going to disappear for a minute to make sure he's not an idiot when he parks me."
    tb "I'll wait for you inside."
    mia "Just tell them you're waiting for someone. It's not crowded today, so it should be fine that we don't have a reservation."
    "I steped out of the car and entered while Mia sliped into the shadows out of sight to fuse as the vallet drove off."
    "I don't think I'll ever get used to seeing people disappear in front of me."
    scene bg itally with dissolve
    stop music fadeout 1.5
    play music restaurant fadein 1.5
    "Hostess" "Benvenuto! How many will be dining with us this evening?"
    tb "Two. She should be here in just a minute."
    show mia with dissolve
    mia "Hi, Christy."
    "Christy" "Oh, hey Mia. I haven't seen you in here in a while."
    mia "Yeah, well, it's a special day."
    "Christy" "I imagine so."
    "Christy looks me up and down."
    "Christy" "Right this way then."
    "We're lead to a small table set for two and left with the menu."
    mia "This place is kind of pricey. I probably should have warned you about that first. If you need me to, I'll pay for you."
    "Despite appearances, she really isn't a child."
    tb "No, no, that's fine. If anything I feel like I should pay for your food."
    mia "Please don't. I have a feeling [Silvie] will be jealous enough already. Don't want her thinking we're actually dating or anything."
    tb "I guess not."
    "[Mia] keeps implying that [Silvie] is interested in me. I thought she was just excited to have a human friend, but is there something more?"
    "I've basically been on two dates with [Mia] now.{w} I keep insisting they're just friendly, but is it? Am I being insensitive to [Silvie]?"
    menu:
        "Does [Silvie] really like me?":
            $   sil_rel += 1
            $   ms_help = True
            mia "You really haven't noticed?"
            mia "It was obvious the first time I saw her with you. She's absolutely in love with you."
            tb "I thought she was just interested in me because I'm a human who knows what she is."
            mia "Well, of course she's interested in that, but you ought to know it's more than that."
            tb "Do you think we've been hanging out too much? I don't want her to feel bad because I spend too much time with you."
            mia "Look, when I first saw you two together, I said to myself that I'd do my best for [Silvie]. She's the best friend I have and I want her to be happy."
            tb "That's really kind of you."
            mia "Do you like her?"
            tb "Maybe. I'm not really sure, to be honest. I've never been really good with girls."
            if mall_date == mia:
                tb "You saw what my last girlfriend was like."
                mia "You haven't had a girlfriend since high school? Yikes."
            mia "Tell you what. Whenever we hang out, I'll give you some advice on [Silvie]."
        "Do you feel bad about hanging out with me so much?":
            $   mia_rel += 2
            mia "Maybe a little. [Silvie] gets jealous pretty easily, but we're good friends. She knows I've got her back."
            tb "I don't want to cause any trouble in your friendship."
            mia "You're really sweet. It's a good thing [Silvie] opened up to you. She's pretty shy with humans."
            tb "Just let me know if I'm causing you girls any problems."
            mia "Don't worry so much. You're fine."
    "The waitress comes after a few minutes to take our orders. Half of the menu was in Italian, so I went the easy route and ordered spaghetti."
    tb "I bet a lot of fancy sports cars come here."
    mia "Ha-haha! When was the last time you saw some Italian trash being worked on with love?"
    mia "I mean, worked on, sure, but not the kind of work that's gonna birth a Kuruma Musume."
    mia "Best case is some cheap economy Italian car showing up here if she hasn't spent all her money on repairs."
    tb "Haha. I guess you have a point."
    tb "Do you think I could have ever created a Kuruma Musume at work?"
    mia "Doubtful. Though I pity anyone who was born like that. Poor girl would be even more confused than the rest of us."
    mia "Even if you had to replace a bunch of parts and loved the heck out of the car you were working on, it probably wouldn't be enough."
    mia "I believe that it requires a very close connection to the car, and I can't see that happening without you being the owner."
    "The server brought out our food, interrupting the conversation."
    "I couldn't pronounce the dish [Mia] ordered, but it looked quite delicious."
    mia "The food here's so good!"
    tb "Yeah, even this spaghetti is better than I think I've ever had."
    #show mia wink
    mia "Don't let anyone ever try to tell you that [Mia] has bad taste."
    tb "Sure. At least when it comes to food."
    mia "What's that supposed to mean?"
    "I gave her a teasing grin."
    mia "Oh, you're right. Since I'm hanging out with you, I must have terrible taste in people."
    mia "But hey, at least you have good taste in cars."
    #show mia wink
    "The dinner was excellent. We ate and talked well into the evening, sharing stories of our pasts."
    "It was mostly [Mia] sharing the stories, and mostly about the races she's won. The excitement she expressed over each victory gave me equal amounts of joy."
    "The server came by and placed the check in front of me."
    mia "Oh, could we get separate checks?"
    "She picked the check back up, but not before I saw the price at the bottom."
    "My stomach tightened.{w} Even with the price split between us, the only noodles I'll be eating any time soon will be out of a styrofoam cup."
    mia "I suggested this place, so I'll pay for yours if you want."
    "I don't know how much her job pays her, but I'm sure she'd be set back a lot more than me."
    tb "No, it's fine. I can pay for my own."
    tb "Thank you, though."
    mia "Good. That's a relief. Heh heh heh."
    tb "Maybe next time we should go somewhere a little cheaper."
    mia "Definitely."
    "We paid for our meals as I felt a slight burning sensation emanating from my wallet, then we left."
    stop music fadeout 1.5
    scene bg miain with dissolve
    show mia at right with dissolve
    play music mia fadein 1.5
    mia "Hey, I know we both said that [Silvie] shouldn't mind this, but she does get jealous, so could we maybe not mention it?"
    tb "Alright. I mean, this isn't really a date or anything anyway. We're just friends going out for dinner."
    mia "Yeah.{w} You're right."
    mia "Just don't go breaking [Silvie]'s heart, alright?"
    tb "I'll be careful."
    "[Mia] droped me off back at my apartment and sped off."
    $   with_mia = False
    stop music fadeout 1.5
    scene bg bed with dissolve
    play music bed fadein 1.5
    "This is all so confusing. [Silvie] is a nice girl, and I might like her as well, but have I just been leading her on?"
    "Somehow I didn't realize her feelings for me, but it all seems so clear now. I've been a fool."
    if ms_help:
        "[Mia] offered to help, so maybe I should take her up on that, or maybe I should go it on my own."
    "I'm going to have to be more conscious of how I handle things with [Silvie] from now on. Even if I don't end up with her, I don't want to hurt her."

    $   renpy.jump("dend_" + str(3))





    return
    #Evo Dates

    #Evo Park Date 1

    label evo_park_date1:
    scene bg park with dissolve
    play music park fadein 1.5
    "I wouldn't really consider myself an outdoorsy person, but I always love coming to this park."
    "The trees, the air, the sound of the ducks over by the pond all add together into an almost magical feeling."
    if  lan_met == True:
        jump evo_park_date1_2
    label evo_meet:
    "Noisy Woman" "Leave me alone you creep."
    "Noisy Man" "Baby, please. Don't make such a scene."
    "Well, it {i}was{/i} an almost magical feeling."
    "Noisy Woman" "It was one night, and a night I'll always regret. Now get lost."
    "Noisy Man" "But-"

    #I'm not sure what the following were in here for. I think they were for testing different sounds. May delete.

    #Kick Hard Impact 4/7
    #Kick Heavy Impact 6
    #Punch Low Deep Impact 2
    #Punch Grit Wet Impact 5 8
    #Heavy Huge Distorted

    #CG of Lanna kicking some pussyboi in the junk
    play sound kick
    "Insert CG of Lanna kicking some pussyboi in the junk"
    scene bg park

    show lanna
    "Noisy Woman" "Take a hint and get out of here!"
    "Now she's looking at me."
    "Noisy Woman" "What? You want some too?"
    tb "No. No thanks. I was just wondering what all the commotion was about."
    "Noisy Woman" "The commotion was about some some whiny little turd who just can't seem to understand how a woman wouldn't want him."
    tb "I'm sorry."
    "Noisy Woman" "The hell are you appologizing for? Was he your friend?"
    tb "Nope. Never met the guy and don't really care to."
    "Noisy Woman" "Can't believe I even gave him a chance after he insulted my car."
    tb "Insulting a woman's car? Truly the reddest of flags."
    "Noisy Woman" "Are you mocking me?"
    #show lanna angry
    tb "No! No! Sorry, I didn't mean it like that. Some of my best friends are cars."
    #show lanna confused
    "Noisy Woman" "Wait, what did you say?{w} Are you crazy or something?"
    tb "How am I supposed to answer that convincingly?"
    "Noisy Woman" "Does the name [Silvie] mean anything to you?"
    tb "Yeah, she's my-"
    tb "Wait a minute. Are you a-"
    "Noisy Woman" "For pete's sake, not right here."
    "I looked around and saw half a dozen faces watching us. I probably should shut up."
    "Noisy Woman" "Look, let's just get out of here and find somewhere a bit quieter, okay?"
    "She lead me to a quiet part of the park where the magic of nature once again eveloped me in its magesty."
    "Noisy Woman" "So before you go blabbing your mouth again without thinking, I'll answer the questions you're about to ask."
    "Noisy Woman" "Yes, I'm a car.{w} Yes, I know [Silvie]. Who doesn't?{w} No, I will not date you. You already saw how my last almost-relationship ended up."
    tb "What about your name?"
    "Noisy Woman" "What difference does it make? I'm not big on this whole \"friends\" thing, I just didn't want you going around talking to me like a maniac in front of everyone."
    tb "Sorry, I just really want to meet more Kuruma Musumes. I've loved cars all my life and want to meet more of you, but [Silvie] isn't too keen on introducing me to others."
    "Noisy Woman" "Is that so?"
    lan "Fine. My name's [Lanna].{w} {color=AFAFAF}Lanna Evolina{/color}."
    tb "It's nice to meet you, [Lanna]. I'm [PC]."
    lan "I'm sorry I was kind of rude to you. It's just been a bad day."
    tb "It's not a problem. We all have days like that."
    lan "Why don't you take my number and if you'd like to give me a call sometime, we could hang out. I'm sure you have a lot of questions."
    play sound cell
    "{color=FFF700}Acquired [Lanna]'s number.{/color}"
    $   lanna_number = True
    lan "So would you like to hang out for a while?"
    menu:
        "That sounds fun.":
            lan "Great!"
            $   lan_rel += 2
            $   with_lan = True
            jump evo_park_date1_2
        "Nah, I should really get going.":
            tb "Maybe some other time."
            lan "That's fine. Just give me a call if you want to meet up!"
            $   lan_met = True
            jump solo_mall1

    label evo_park_date1_2:
    $   with_lan = True
    if lan_met == False:
        $   lan_met = True
        "[Lanna] smiled at me and motioned for me to walk with her around the winding path through the park."
        lan "So how did you figure out we exist?"
        tb "[Silvie] came into the shop I run for some repairs and accidentally spilled the beans."
        lan "How so?"
        tb "Well, she was rambling. At first I thought she was crazy."
        #show lanna_wink
        lan "A fair assumption for [Silvie]."
        tb "I then thought I was crazy when she disappeared inside her car."
        lan "She didn't..."
        lan "Right in front of you?"
        tb "Haha, I thought a camera crew was about to jump out from behind the cars saying it's some kind of prank."
        lan "[Silvie]'s careless, but she's not usually that reckless."
    tb "How do you know [Silvie]?"
    lan "She's got a habbit of trying to befriend any Kuruma Musume she can find. Kind of annoying, really."
    lan "I showed up at a cofee shop one day and that girl somehow instantly recognized me as my car."
    lan "At first I thought she was just trying to compliment my car, which of course I enjoy, but then she got really talkative about Kuruma Musume souls and stuff."
    tb "Do you believe that whole \"heart and soul\" theory?"
    lan "I don't really care. I'm here and that's all there is to it. I don't care if there was some spiritual connection or not."
    tb "You're not at all curious where you came from?"
    lan "Nope. Doesn't really matter, does it?"
    tb "I guess it doesn't."
    "[Lanna] is really different from Silvie."
    if  mia_met == True:
        "Even Mia isn't this different from Silvie."
    "I guess cars are just as different from each other as humans are."
    lan "So, are you and [Silvie], you know..."
    lan "..."
    lan "...a couple?"
    "I try to hide the surprise on my face at such an abrupt question."
    tb "Uh...{w} Not really, I don't think."
    lan "What do you mean? You either are or you aren't."
    tb "I'm just not sure. We've not really known each other for very long. I don't know what we are to be honest."
    lan "You're such a pussy."
    tb "Whoa! I think that's uncalled for."
    lan "Some guy who's apparently devoted his life to cars and isn't even brave enough to take a chance with the girl who actually {i}is{/i} a car?"
    lan "Yeah, kind of a pussy."
    lan "But knowing [Silvie], she doesn't care either way. Aren't you lucky?"
    "This car's not just different from other cars, she's different from any other girls I've known."
    tb "Does it have to be about dating?"
    lan "Come on. You like cars, don't you? You've never wanted to date a car before?"
    lan "You can't convince me that you haven't thought about going steady with [Silvie]."
    tb "Well, I guess I have."
    lan "That's the spirit."
    lan "You're going to have to get more assertive if you ever want to take a car to bed with you."
    "Would it be rude to ask if her car was missing as many filters as her mouth is?"
    "[Lanna] abruptly stops walking as we pass by an open field in the middle of the park."
    lan "This is as far as I can go. I'm parked back that way."
    "She gestured towards the parking lot where my car was also parked."
    lan "I like to come to this field a lot, though."
    "[Lanna] kicked off her shoes, took a few steps forward, and then fell back on the grass."
    #CG Lanna laying on the grass
    "CG of Lanna Laying on the Grass"
    lan "I love the way the grass tickles my skin."
    lan "It's like a million tiny fingers caressing my body."
    "I took a seat on the grass next to her."
    tb "I've never really thought about how it feels. It's just grass to me."
    lan "You've really gotta open up your mind a bit more. Learn to let go."
    tb "If I'm not mistaking, your car's all-wheel-drive, isn't it? I figured you AWD girls were about holding on."
    play sound spunch
    "She punched my leg."
    lan "I can lose grip if I wanna."
    tb "I guess I'm just not much of an outdoors person. I enjoy places like this park, but I don't find the same comfort in nature that I find under the hood of a car."
    lan "Oh, so now you want to look under my hood, huh? Naughty, naughty!"
    tb "What? Do cars consider that a euphamism?"
    lan "What do you think? We might as well be showing you our tits."
    tb "In that case, you should probably cover up your exhaust."
    lan "Don't even go there, you perv."
    lan "You might be a little more assertive than I thought."
    tb "Maybe I am."
    lan "Ah. It's been nice here, but I should probably get going."
    $   lan_date += 1
    scene bg park with dissolve
    show lanna
    if day == 2:
        lan "You want to go for a ride with me? Maybe hit the mall afterwards?"
        menu:
            "Yeah.":
                $   lan_rel += 2
                jump evo_first_drive
            "Nah.":
                $   with_lan = False
                tb "I should probably get going myself, but I'll give you a call sometime."
                lan "Alright. We'll definitely have to hang out more."
                jump solo_mall1
    else:
        lan "You want to go for a ride with me?"
        menu:
            "Yeah.":
                jump evo_first_drive
            "Nah.":
                $   with_lan = False
                tb "I should probably get going myself, but I'll give you a call sometime."
                lan "Alright. We'll definitely have to hang out more."
                lan "I'll be doing some shopping, but you can feel free to give me a call if you change your mind."
                jump solo_mall1


    label evo_first_drive:
    lan "Excellent. You better not get scared on me. I'm not slowing down just 'cause some pussy's in my car."
    tb "I wouldn't tell you to slow down."
    "Probably."
    lan "Good."
    "She lead me back to her car. I apparently parked next to it without even realizing it."
    stop music fadeout 1.5
    scene bg lanin with dissolve
    show lanna at right
    play music kisstokiss fadein 1.5
    "I buckled my seatbelt."
    lan "Pussy."
    "She said it with a playful smile."
    "We slowly pulled out of the parking area and onto the road."
    "[Lanna] took every chance she could get to rev her engine. It did sound nice, though I was certain the people around us were annoyed at how loud it was."
    lan "Just wait 'til we get out of this traffic. I'm going to take you for a ride you'll never forget."
    #CG sequence
    "Begin CG sequence"
    "We finally made our way out of town and the traffic began to thin."
    "Without warning, [Lanna] floored it, pinning me to my seat.{w} It was exhilarating."
    "She whipped in and out of the light traffic until we left the highway for some more exciting roads."
    #Change from City to country scenery in windows
    "She certainly could grip the road remarkably well, but as if to prove to me, she managed to get the tires to slip and we began to slide."
    "I couldn't help but grab her handle, clinging to it in fear."
    lan "Can't keep your hands to yourself, huh?"
    "I couldn't answer."
    "Kuruma Musumes really were incredible drivers. It stands to reason that they would know themselves and their limits better than any human driver."
    lan "You better not be wetting yourself over there."
    "She would probably know if I was."
    "She slowed as we came back towards the city, her breathing heavy."
    #Change from country scenery to city in windows
    lan "Damn, it feels good to show off to someone who doesn't start crying when they see a corner."
    lan "You did pretty good."
    "And here I thought I was coming across as a total chicken with how hard I was gripping the handle of her door."
    tb "You think so?"
    lan "Yeah, but you can let go of me now."
    "I look down and realize I still hadn't loosened the death grip I held her handle with."
    tb "Sorry."
    lan "Pants still dry?"
    tb "..."
    lan "You wouldn't be the first guy that's had to clean up after himself in here."
    tb "I did not!"
    lan "Haha. You're such a dork."
    "Does she treat everyone like this, or is it just me?"
    if day == 2:
        lan "So how 'bout that trip to the mall? You down?"
        menu:
            "Yeah.":
                $   lan_rel += 2
                lan "Need to go take a leak before we drive more or are you good?"
                tb "I'm fine! Stop with that. You didn't scare the piss out of me."
                lan "Hey, I'm just asking. I meant it when I said you wouldn't be the first."
                "I actually do feel the urge now."
                tb "Let's go. I'm fine."
                jump lan_mall1

            "Maybe another day.":
                $   with_lan = False
                lan "I really did scare the piss out of you, didn't I?"
                tb "No, I've just had enough excitement for one day."
                lan "Fine. I'll let you out back at your car."
                "[Lanna] took me back to the park and we said our goodbyes."
                scene bg park with dissolve
                "Come to think of it, I actually do need to take a trip to the mall. I guess I'll make a quick stop there myself and hope I don't accidentally bump into her."
                jump solo_mall1



    lan "Well, it was pretty fun, but I've got some other stuff to do."
    tb "Yeah. I enjoyed it."
    lan "Now that's something I haven't heard in a while."
    lan "About my driving at least."
    "No filter."
    "[Lanna] drove me back to my car and we said our goodbyes."
    lan "You better give me a call. Don't keep a nice car waiting."
    lan "Or a naughty one."
    tb "I'll call you when I can. See ya."
    "Somehow I feel like I've just gotten in over my head."
    $   renpy.jump("dend_" + str(day))
    return



    #Staci Dates

    #Staci Coffee Date
    label staci_coffee1:
    stop music fadeout 1.5
    scene bg coffee with dissolve
    play music burning fadein 1.5
    "I picked Staci up and took her to the little coffee place near the shop."
    show staci with dissolve
    sta "This is a very strange coffee shop. What's with all of the car decorations?"
    if coffee_date == True:
        tb "That's what I thought when I first came here. You get used to it though. It's actually a pretty nice place."
    else:
        tb "I'm not sure. It is a little odd for a coffee shop. Maybe the owners are really into cars?"
    sta "I guess you love it, but I can't say I'm a fan."
    tb "We can go somewhere else if you'd like."
    sta "No, this is fine."
    sil "Hi, welcome to Cafe le Auto."
    "Am I hearing things?"
    show staci:
        linear 0.5 left
    show silvia at right with dissolve
    sil "Hey, [PC]."
    tb "Wait, do you work here?"
    sil "That's right!"
    if mall_date == 1:
        sta "Oh, it's you again."
        "[Silvie] glares at [Staci]."
        sil "I didn't think someone who doesn't like cars would come here."
        tb "That's on me. I decided it would be nice to come here."
        "[Silvie]'s expression almost looked hurt."
        sil "Well, let me take your orders."
    else:
        sta "Do you know [PC]?"
        tb "This is [Silvie]. She's a good friend of mine."
        tb "[Silvie], this is [Staci]. We used to date back in high school. Since I ran into her again, I thought it'd be nice to catch up."
        sil "Well.{w} That's great.{w} What can I get you two?"
    "We place our orders with [Silvie] and choose a table."
    hide silvia with dissolve
    show staci:
        linear 0.5 center
    sta "It figures that you'd come to this cafe. I never could get you away from cars, could I?"
    tb "Even when I was a little kid, I thought cars were amazing. I love understanding how they work, and that turned into my dream job."
    sta "But don't you want a job that pays better?"
    tb "I own my own business, a business that's in high demand with how many people own cars. I make pretty good money after only a short time, and it keeps increasing."
    tb "When I pay off my loans, I'll be making quite a bit."
    "[Staci] looked at me contemplatively."
    sta "Well, I guess if you're actually making money, it's not so bad."
    tb "So what do you do now? You must be doing pretty well for yourself by the clothes you're wearing."
    sta "I'm a manager at an accounting firm downtown."
    tb "Really? I never would have guessed that you'd end up in accounting."
    sta "Well, I might not have been the best in school, but if it has to do with money, I'm great at that."
    tb "I suppose you were always pretty fond of money, considering that's why you broke up with me."
    sta "I might have been too hard on you back then. I just didn't see a point if I was going to end up supporting the both of us."
    tb "You know we could have talked about it."
    sta "I don't recall you trying to talk it over with me. You just hopped in your car and left after school that day."
    tb "I had to work. Fixing cars was all that got me through that day. It distracted me from the pain."
    "I can't even put into words how much it hurt me when [Staci] broke up with me. And over something as trivial as my first job?"
    tb "It's probably for the best. If I'd have tried to change anything for you, I'd be working in some office with no joy in my life."
    #Show Staci Shocked
    sta "What's that about? You think cars can give you more happiness than me?"
    show staci:
        linear 0.5 left
    show silvia at right with dissolve
    "[Silvie] brought our orders to us and placed them on the table. The look on her face indicated she had definitely overheard what was just said."
    sil "And what if he asked you to give up all of those fancy clothes you're wearing?"
    sta "Everyone needs clohtes, sweetheart. A car's just an appliance. No need to get all sentimental over it."
    #Show Silvia platinum mad
    "I definitely need to talk to [Silvie] after this. I've never seen someone look so angry."
    tb "Cars can be as much of a satus symbol as your clothes, you know."
    "[Silvie]'s expression didn't change, but somehow It seemed like she was directing it towards me instead."
    sta "Sure, I guess, but it's still just a car. If it breaks, you get someone to fix it like you'd call a plumber if your toilet's backed up."
    sta "No reason to get all obsessed with working on cars yourself. You can do so much more with your life if you want to."
    tb "I remember you liking art back in high school. You've got some paintings at home probably, right?"
    sta "Yeah. So what?"
    tb "To me, cars are a form of art."
    #show silvia slight smile
    tb "The way you tune them to perform just right is art. The way you design them to make them fit your stylistic tastes is art. And driving is its own art form."
    #show silvia frown
    sta "Oh come on, you can't really compare cars to the art I like any more than you can compare street graffiti to the art I like."
    "Some would argue with her on that point as well."
    tb "Look at us. We just met each other again and we're already arguing like we're the same old high school couple."
    sta "Haha. You're the one who keeps trying to make me like cars."
    "I think it's the other way around."
    tb "Let's just drop it."
    show staci:
        linear 0.3 xalign -0.2
    show silvia:
        linear 0.5 center
    "I turn to [Silvie]."
    tb "Sorry to get you caught up in this silly squabble."
    sil "No. I guess I'm sorry I interrupted.{w} But, well..."
    sil "You understand."
    show silvia:
        linear 0.5 right
    show staci:
        linear 0.5 left
    sta "I should have known that you'd get all ridiculous if I started giving my oppinions on cars."
    sta "Waitress, you can go now. Thanks for bringing the coffee."
    sil "..."
    "[Silvie] paused for a moment like she wanted to respond, then turned and left."
    hide silvia with dissolve
    show staci:
        linear 0.5 center
    tb "We had some good times back then, didn't we?"
    sta "Yeah. If you were only about cars, I wouldn't have stuck with you for so long. You had your charms."
    sta "I think you still do under all that engine grease."
    tb "Thanks."
    #show staci sincere
    sta "Even if you'll never stop loving cars, you shouldn't make your whole life about them. Try something new every now and then. It'll be good for you."
    tb "Like what?"
    sta "I don't know.{w} Go to the gym?{w} Hang glide?{w} Take me on another date."
    tb "That last one sounded more like an order than a suggestion."
    sta "Maybe it was."
    tb "You don't have a boyfriend who'll get mad right now, do you?"
    sta "Hah. Hardly. It's been a while since my last boyfriend."
    tb "Well, maybe I'll call you again soon."
    sta "I can't wait."
    tb "Are you ready to go?"
    sta "Yeah. This was fun."
    tb "Then let's go."
    "I waved to [Silvie] as we left, but she turned away from us. I was definitely going to have to talk to her."
    stop music fadeout 0.5
    scene bg tbin
    play music tbcar fadein 0.5
    show staci at left with dissolve
    sta "It feels weird sitting on this side of the car."
    tb "I didn't think you drove."
    sta "This is supposed to be the driver's seat, isn't it?"
    tb "What do you mean? Almost every car I've seen around here is right hand drive."
    sta "Only your cars. It was the same back in high school. You had the weird car with the steering wheel on the wrong side."
    tb "I'm pretty sure this is the...{w} {i}right{/i} side of the car."
    sta "God, you're such a dork. I don't know what I ever saw in you."
    tb "A cute guy who cared about you?"
    sta "Hmm..."
    #show staci sly
    sta "Nope. That's definitely not it."
    tb "I always did enjoy talking with you like this."
    sta "Me too."
    "We pulled up to [Staci]'s house."
    tb "Well, here's you."
    sta "Hey, I have another suggestion for you to try."
    tb "Oh, what is it?"
    "She paused for a moment."
    sta "Kiss me."
    menu:
        "Kiss [Staci].":
            $ sta_rel += 3
            $ sil_rel -= 1
            "I wraped my arm around [Staci] and pulled her closer as I leaned across to the passenger seat."
            show staci:
                linear 0.75 zoom 1.5 yalign 0.5
            "I lightly kissed her lips, savoring the taste for just a moment."
            show staci:
                linear 1.0 zoom 1.0 yalign 1.0
            tb "I thought you said to try new things."
            #show staci lovely smile
            sta "You can also try old things you've forgotten."
            #show staci neutral smile
            sta "Well, I'll let you get going now. Thanks for the date. Can't wait for the next one."
            hide staci with dissolve
            "[Staci] left, giving me a dainty wave before entering her house."
            "I think it's safe to say I'm dating my ex now. I hope this time turns out better than the last."
            "I drove home, wondering how [Silvie] would take the news."
            stop music fadeout 1.5
            scene bg bed
            play music bed fadein 1.5
            $   renpy.jump("dend_" + str(day))

        "Don't kiss [Staci].":
            tb "Sorry, I'm not sure I'm comfortable going back down that road right now."
            sta "That's a shame. Well, if you change your mind, you have my number. Thanks for the date anyway. It was really fun."
            tb "We'll have to meet up again soon."
            sta "Definitely. Well, see ya."
            "I watched as [Staci] returned to her house without looking back. Part of me regretted saying no, but I'm not convinced that it will end up better this time."
            "Thinking back, I remembered how hurt [Silvie] was and thought it might be good to call her."
            menu:
                "Call [Silvie].":
                    "*Ring*"
                    $   sil_rel += 1
                    sil "Hi, [PC]."
                    tb "Hey, [Silvie]. Are you still at work? I'd like to talk to you."
                    sil "Yeah, I'm still here."
                    tb "I'll see you in a few."
                    "I hang up and drive over to Cafe le Auto as quickly as I can."
                    scene bg coffee with dissolve
                    show silvia with dissolve
                    sil "Hey, good to see you're alone this time."
                    tb "I'm sorry about all the things [Staci] said earlier."
                    sil "You don't need to appologize for her; just promise me you're not going to get too involved with her. I'd hate to see her change you."
                    tb "That won't be a problem. You know I'm too into cars for her anyway."
                    sil "You're too sweet for your own good, [PC]."
                    #show silvie embarrassed
                    sil "Eh-{w} I mean-{w} It's just that you seem to be easily persuaded by cute girls and I don't want you to get hurt by that."
                    sil "I mean..."
                    tb "I get it. I don't think [Staci] and I would work out any better than last time. She's fun to be around, but I'm not certain she's for me."
                    #show silvie relieved
                    sil "Good. I'm glad you feel that way."
                    tb "Besides, why should I hang out with someone who hates cars when I could hang out with someone who {i}is{/i} a car?"
                    #Blushing Silvie
                    sil "You're right. I guess I just worry about stupid things sometimes."
                    tb "I'll call you soon."
                    sil "Thanks."
                    "We said our farewells and I drove back home."
                    $   renpy.jump("dend_" + str(day))
                "Don't call.":
                    $   sil_rel -= 1
                    "On second thought, she was probably still in a bad mood. I'd just have to talk to her another time."
                    $   renpy.jump("dend_" + str(day))






    return


#Shelby Dates

    #Shelby P4U and shop date
    label she_d2_date:
    stop music fadeout 1.5
    scene bg p4u
    play music p4u fadein 1.5
    "This is my favorite parts store in town. It's pretty small, but the owner always seems to have just what you need."
    "I don't actually need anything right now, I guess I'm just here to look around and pass some time."
    tb "I really don't need a new socket set, but the shiny chrome is oh so tempting..."
    "The owner's voice suddenly fills the small shop."
    "Owner""[Shelby]! I didn't expect to see you back in here so soon. Everything alright with that filter I sold you?"
    "I look over and see a girl making her way into the shop.{w} She's tall and athletic looking, with a stern look on her pretty face."
    show mustang with dissolve
    she "The filter is fine, I just lost my damn 10 millimeter socket! Just need to pick up a new one and get back at it."
    "She walked over to near where I was standing, and reached for a high grade 10mm socket."
    "I let out a low whistle."
    tb "Strap-on, huh? Good brand but pretty pricey."
    "She gives me a self assured grin and holds the socket out in front of her, flexing her bisceps with her other arm."
    she "Only the best of the best for {b}me!"
    "The girl gives another flex of her arm, as if to emphasize her point.{w} The definition of her muscles shows clearly, even through her short sleeved work shirt."
    tb "I see. What kind of car are you working on?"
    she "I'm a-"
    with hpunch
    "She starts coughing, very loudly and suddenly."
    she "Whoah, sorry about that! It's an old school muscle car."
    "What did she say? I couldn't have met another one... Could I?"
    "I was so lost in thought that I didn't hear what she said next."
    she "Hey, earth to... to you. What was your name again?"
    tb " Oh! Sorry, spaced out a bit. My name's [PC]."
    she "Well, nice to meet you [PC], I'm [Shelby]. I asked if you wanted to check out my car."

    menu:
        "Yeah, sure.":
            $ she_rel += 1
            tb "Yeah, I'd love to!"
            she"C'mon, let me pay real quick, and I'll show you!"
            "[Shelby] pays for her socket quickly as I waited near the exit"
            she "Alright, prepare to be amazed!"
            jump shelby_mall1



        "Sorry, not right now.":
            tb "Sorry, I've actually got to get going now."
            "Her beaming grin only falters for a second."
            she "Oh, that's alright, maybe another time!{w} Here, I'll give you my number. Give me a call if you change your mind."
            play sound cell
            "{color=FFF700}Acquired [Shelby]'s number.{/color}"
            $   shelby_number = True
            $   with_shelby = False
            jump solo_mall1


    label shelby_mall1:
    stop music fadeout 1.5
    scene bg stang with dissolve
    play music she fadein 1.5
    show mustang at right with dissolve
    $   with_she = True
    "[Shelby] led me over to a car parked toward the edge of the lot."
    "It was a dark green and low to the ground, looking mean and ready to go."
    tb "Oh wow, the '67! With the 7.0 liter?"
    "[Shelby] looks over at me with pride, and a hint of surprise."
    she "Yep, that's right! Glad to see you know your cars."
    tb "Only spent my whole life working on 'em. Even have my own shop!"
    "Her eyes light up after hearing that."
    she "Oh wow! That's amazing, can I see it? I just work in my garage."
    tb "Yeah no problem, give me a ride and I'll show you how to get there."
    she "Hop in!"
    "I walk over to the left hand side of the car and start to climb in, but I'm greeted by the steering column."
    she"So bold! We just met, and you're already trying to drive me around?"
    "I turn a bit red."
    tb "Just opening the door for you, your majesty!"
    she "Nice recovery, not used to American cars, huh?"
    tb "Yeah, I suppose it's been a while."
    scene bg shein with dissolve
    show shelby at left with dissolve
    "After we both climb in, I look around. {w} It feels so strange to be on the right side of the car and not be driving."
    she "So which way are we headed, [PC]?"
    "I give her a rundown of our route and we make our way at a brisk, but reasonable pace."
    tb "This is a pretty relaxing drive, it's a bit strange to be a passenger though."
    she "You drive yourself around mostly?"
    tb "That's right. You're a good driver though, so I don't mind."
    "A small smile shows on [Shelby]'s face."
    she "You're goddam right I'm a good driver!"
    tb "Oh! If you hang a right up ahead we can take a shortcut through the old tunnel."
    "Her small smile morphs into a huge grin."
    she "Got it."
    "The atmosphere in the car shifted. [Shelby] was was suddenly emenating an aura of intensity."
    "As we entered the tunnel, [Shelby] downshifted and her car let out an immense roar, echoing through the entire tunnel."
    "She shifted back up and started accelerating, spinning her tires a bit and careening through to the exit."
    "I grabbed the handle, in an attempt to steady myself in the cabin that was suddenly sent sideways through a turn onto a back road I knew well."
    "[Shelby] looked over at me with the huge grin still plastered on her face."
    she "Yeah, you better hold on, this road is twisty, and muscle cars cars can get sideways too!"
    "My voice felt like a seed stuck in my throat, but I managed to croak out a reply"
    tb "Yeah I take cars out here after suspension work to test them out."
    "The wild look in her eyes was scaring me a bit, but the impressive control she had over her car was a small comfort."
    #driving wild scene, shelby "cutting loose"
    tb "This is it here."
    "We pulled into the lot in front of my shop and hopped out of the car."
    she "WHOOOOOO! I love that road!"
    "[Shelby] was practically bouncing around her car, radiating energy and beaming"
    she "The wind in my vents, the asphalt on my tires, it all feels so good!"
    "Vents, huh? Well... Worth a shot."
    tb "Hey Shelby, are you by any chance, uh, well, are you a car?"
    "She stopped bouncing all at once and looked at me with a serious look on her face."
    she "I wish."
    "She broke back out into a goofy grin."
    she "C'mon, what kinda question is that? [PC] You're a bit weird."
    "I could feel the blush creeping over my face as I scratched the back of my neck."
    tb "Ehehe, yeah, sorry, it's a weird thing to just ask somebody."
    "I must be getting paranoid, just because I met one girl thats a car doesn't mean ALL girls are secretly cars."
    "I gotta keep it cool, or she'll think I'm a freak."
    scene bg mg with dissolve
    show mustang with dissolve
    "I open up the garage door and invite her inside."
    show mustang:
        linear 1 left
        linear 1 right
        repeat
    "She immediately started bouncing off the walls again looking at everything"
    show mustang:
        linear 0.5 center
    #cute scene with shelby fangirling about random garage equipment
    "Her eyes finally rest on an old rack bolted on the wall."
    she "I bet I can do more pull ups than you."
    tb "What."
    she "C'mon, scared you're gonna be beat by a giiiirrrlll?"
    "How did this come up? I look over at her car. [Shelby] left it idling in the entryway. The shop had good ventilation, so I decided not to mention it yet as we walked over to the rack."
    tb "Okay, but I warn you I lift a lot of heavy stuff, don't feel too bad when I beat you!"
    she "Ooh, now you're getting in the mood! Let's go!"
    "She hops on the bar suddenly and starts cranking out pullups at an alarming rate."
    tb "Wait, I wasn't ready!"
    "I hop on the bar and frantically start trying to keep up."
    "I'm not in bad shape by any means, but just trying to keep up with her is tiring me out quick."
    "Looking over at Shelby, she's only just started to break a sweat. She looks over at me, sticks her tongue out and switches to one handed pull ups."
    tb "Ack, show off!"
    she "Time for my ultra secret rapid fire pull up technique to finish you off!"
    "She grabs the bar with her other hand, and doubles her pace. A strange noise in the shop tears my eyes away from her blur and towards the entrance."
    tb "Huh?"
    "Shelby's car is idling really hard. Wait, no, it's revving!"
    "I look back over at [Shelby] and realize it's revving in time with her pullups. The shock cause my grip to slip off the bar."
    she "Wiped out already, [PC]?"
    tb "You are a car! I knew it!"
    "I call out at her while sitting flat on my ass under the bar."
    "[Shelby] lets herself drop down from the bar and looks at me with a shocked face."
    she "I don't- Why do you-"
    "She stutters around a million questions, turning a deep red."
    she "HOW DO YOU KNOW ABOUT THAT?"
    "She finally decides on one and almost screams it at me, red faced."
    "Oh shit, I may have pushed it too far, she seems pretty upset."
    tb "I uh- sorry I didn't mean to push it so hard. I've just met more cars than I'm used to lately."
    she "You know other cars?"
    "I tell her the story of how Silvie came into my shop and revealed herself as a Karuma Musume, and filler her in on what my life has been like since then."
    she "Oh wow, no wonder you're so paranoid of girls being cars, that's-"
    "She puts a hand over her mouth poorly stifling a laugh."
    she "That's actually pretty funny!"
    "She finally gives up and starts giggling uncontrolably."
    "I can't help but laugh along, honestly. My life has been crazy lately."
    "We talk for a bit more, getting to know each other on a bit more open terms."
    tb "Honestly, what really made me suspicious was how well you could keep control, even when driving so wildly."
    "[Shelby] giggles, and brushes some hair from her face, seeming a little self conscious."
    she "Well, obviously I have perfect control over myself... to an extent."
    she "I get a little worked up, and every now and then I get a little crazy. I just feel like I need to let out energy, break the tires loose, or I'll just die."
    tb "I noticed. It looks like it's that way with your other body too..."
    "I glance up at the improptu pull up bars, where she destroyed me."
    she "Hehe, yeah... But actually [PC], I'm glad you know. This is a BITCHING shop. I definitely want to do some work here."
    "We chatter on like this until [Shelby] glances at the clock."
    she "Oh shit! It's already this late? My gym closes in half an hour!"
    tb "Do you need a ride?"
    "[Shelby] looks at me with a blank look on her face."
    tb "Oh.. right, dumb question."
    "I try to hide my blush as [Shelby] sticks her tongue out at me."
    tb "Why do you need to get to the gym before it closes today anyways?"
    she "I need to renew my membership, and today's the deadline. If I miss it, I'll get hella fines!"
    "Hella?"
    she "I need to get to the mall, do you mind coming along?"
    tb "Not at all, I actually need to pick some stuff up too."
    she "Great! Let's roll."
    "We hop in the car and head off to the mall at brisk speed."
    "We were definitely going fast but it wasn't like it was before. [Shelby] seemed more relaxed, and wasn't going sideways at every available chance."
    "We arrived with little time to spare, we parted ways, with a plan to meet back at the food court afterwards."
    stop music fadeout 1.5
    play music mall fadein 1.5
    jump day_2_mall_event




    $   renpy.jump("dend_" + str(day))






    # This ends the game.

    return
