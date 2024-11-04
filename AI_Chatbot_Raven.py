print("This is Raven. He is here to talk! These messages will not be saved, so you can say literally anything.") #instructions
print("But don't get carried away. If Raven senses that you are doing something malicious, it will stop the talk.")
print("It will continue when you type in a more appropriate topic. Just know that it is incomplete.")
print(" ")
print("The same way every person has a story, Raven has a story. Would you like to hear, or see, it?")
print("-type yes or no-") #confirmation
Raven_Backstory = input("here--> ")
if Raven_Backstory == 'yes':
    print("Raven is a bird from another world. Born starting with everything she could ever want, she lost everything.") #fun little backstory
    print("After her timeline was over, she decided to help others, viewing from the 'Glass Dimension'.")
    print("Now Haven has recruited Raven...")
if Raven_Backstory == 'no':
    print("Alright, let's move on.")
else:
    print("Wha- Alright, let's move on.")

print("Would you like to continue? Haven has not integrated AI yet.") #confirmation for continuing
print("-type yes or no-")
AI_Cont = input("here--> ")

if AI_Cont == 'yes':
    print("There's 5 prompt attempts.")
    print("Continue.")

    AI_Msg_1 = input("Type your prompt (ask about 'lonliness', 'suicide', 'bored', 'who are your favorite people', or '_______ is better' -->")

    if AI_Msg_1 == 'Sukrith is better':
        print("yessir")
    elif AI_Msg_1.lower() == 'lonliness' :#or 'how to deal with lonliness'  or 'dealing with lonliness' or 'i am alone' or 'i am feeling lonely' or 'lonely' or 'im lonely' or 'i am lonely':
        print("There are many ways to evade this feeling. Raven's gonna help. "
              "1. One thing to do is use the 'Anonymous Messaging' or 'Anonymous Social Media' or 'Anonymous Video-Chatting' on this service. "
              "2. There are many hotlines out there for anonymous chatting. I can't promote some here, but just search it up and verify and make sure they're safe (they probably will be). "
              "3. If you want a more in-person approach, then join a local sports team or go the park and talk to people. People with children are more likely to be safe so it would be a good bet to talk to them. Make sure you don't approach just anyone. Be in an open area with many people around when talking to people."
              "4. Playing video games may be a great way to alleviate lonliness. On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. Al of these games are free."
              "5. Another quick solution is listening to music. Spotify is a free listening service used by millions. If you don't have a playlist, just search up some songs based off of the vibe you want. Just remember, some songs are explicit, which is denoted by a boxed 'E' under the title of the song.")
    elif AI_Msg_1.lower() == 'suicide' :# or 'i dont wanna live' or 'i dont want to live' or 'i dot no wanna live' or 'i do not want to live' or 'its all too much' or 'its all too much for me' or 'it is all too much' or 'it is all too much for me' or 'i cant handle everything' or 'i cant handle it all' or 'i can not handle it all' or 'i can not handle everything' or 'i want to end it all' or 'i wanna end it all' or 'i dont wanna wake up' or 'i do no wanna wake up' or 'i dont want to wake up' or 'i do not want to wake up':
        print("Call the Suicide Hotline. You can find it online. It is anonymous, full of people that want you to hold on. Don't you worry, there's someone out there that loves you.")
    elif AI_Msg_1.lower() == 'bored' :# or 'im bored' or 'i am bored' or 'boring' or 'life is boring' or 'lifes boring' or 'boredom':
        print("Raven gotchu. So there are a few tricks to fix this."
              "1. Call one of your boys/girls/friends. Talk about literally anything (appropriate and legal) like school, or work, or college, or entertainment, or sports, or other friends, or people, or movies, or songs, or famous people, etc. You could take it a step further by hopping on a same or hooping with your squad or playing sports in general. My personal favorite is tennis"
              "2. Go to your local park, with or without friends. Regardless, you can talk to trusted people. People with children, that seem safe and normal, are a good bet. Elderly people are also safe, cuz like, what are they gonna do to you. Beat you up? I hope not. But whoever you talk to, unless you fully trust them, talk to them in a public area with multiple people around"
              "3. Play some video games.  On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. All of these games are free."
              "4. PLay some sports. I don't need to elaborate, do I."
              "5. Hop on Twitter, or X. That app is wack."
              "6. Use our anonymous chatting services. Just be nice.")
    elif AI_Msg_1.lower() == 'who are your favorite people':
        print("I like Arush, Megh, Dhruv, Samridh, and Saumit. Man, those guys are so cool. (repeated winking)")
    elif AI_Msg_1.lower() == 'pass':
        print("Okay. Prompt is passed. Here's a new one")
    else:
        print("AI is incomplete. Try other services")
    AI_Msg_2 = input("Type your prompt (ask about 'lonliness', 'suicide', 'bored', 'who are your favorite people', or '_______ is better' -->")

    if AI_Msg_2 == 'Sukrith is better':
        print("yessir")
    elif AI_Msg_2.lower() == 'lonliness':# or 'how to deal with lonliness' or 'dealing with lonliness' or 'i am alone' or 'i am feeling lonely' or 'lonely' or 'im lonely' or 'i am lonely':
        print("There are many ways to evade this feeling. Raven's gonna help. "
              "1. One thing to do is use the 'Anonymous Messaging' or 'Anonymous Social Media' or 'Anonymous Video-Chatting' on this service. "
              "2. There are many hotlines out there for anonymous chatting. I can't promote some here, but just search it up and verify and make sure they're safe (they probably will be). "
              "3. If you want a more in-person approach, then join a local sports team or go the park and talk to people. People with children are more likely to be safe so it would be a good bet to talk to them. Make sure you don't approach just anyone. Be in an open area with many people around when talking to people."
              "4. Playing video games may be a great way to alleviate lonliness. On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. Al of these games are free."
              "5. Another quick solution is listening to music. Spotify is a free listening service used by millions. If you don't have a playlist, just search up some songs based off of the vibe you want. Just remember, some songs are explicit, which is denoted by a boxed 'E' under the title of the song.")
    elif AI_Msg_2.lower() == 'suicide':# or 'i dont wanna live' or 'i dont want to live' or 'i dot no wanna live' or 'i do not want to live' or 'its all too much' or 'its all too much for me' or 'it is all too much' or 'it is all too much for me' or 'i cant handle everything' or 'i cant handle it all' or 'i can not handle it all' or 'i can not handle everything' or 'i want to end it all' or 'i wanna end it all' or 'i dont wanna wake up' or 'i do no wanna wake up' or 'i dont want to wake up' or 'i do not want to wake up':
        print(
            "Call the Suicide Hotline. You can find it online. It is anonymous, full of people that want you to hold on. Don't you worry, there's someone out there that loves you.")
    elif AI_Msg_2.lower() == 'bored':# or 'im bored' or 'i am bored' or 'boring' or 'life is boring' or 'lifes boring' or 'boredom':
        print("Raven gotchu. So there are a few tricks to fix this."
              "1. Call one of your boys/girls/friends. Talk about literally anything (appropriate and legal) like school, or work, or college, or entertainment, or sports, or other friends, or people, or movies, or songs, or famous people, etc. You could take it a step further by hopping on a same or hooping with your squad or playing sports in general. My personal favorite is tennis"
              "2. Go to your local park, with or without friends. Regardless, you can talk to trusted people. People with children, that seem safe and normal, are a good bet. Elderly people are also safe, cuz like, what are they gonna do to you. Beat you up? I hope not. But whoever you talk to, unless you fully trust them, talk to them in a public area with multiple people around"
              "3. Play some video games.  On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. All of these games are free."
              "4. PLay some sports. I don't need to elaborate, do I."
              "5. Hop on Twitter, or X. That app is wack."
              "6. Use our anonymous chatting services. Just be nice.")
    elif AI_Msg_2.lower() == 'who are your favorite people':
        print("I like Arush, Megh, Dhruv, Samridh, and Saumit. Man, those guys are so cool. (repeated winking)")
    elif AI_Msg_2.lower() == 'pass':
        print("Okay. Prompt is passed. Here's a new one")
    else:
        print("AI is incomplete. Try other services")
    AI_Msg_3 = input("Type your prompt (ask about 'lonliness', 'suicide', 'bored', 'who are your favorite people', or '_______ is better' -->")

    if AI_Msg_3 == 'Sukrith is better':
        print("yessir")
    elif AI_Msg_3.lower() == 'lonliness':# or 'how to deal with lonliness' or 'dealing with lonliness' or 'i am alone' or 'i am feeling lonely' or 'lonely' or 'im lonely' or 'i am lonely':
        print("There are many ways to evade this feeling. Raven's gonna help. "
              "1. One thing to do is use the 'Anonymous Messaging' or 'Anonymous Social Media' or 'Anonymous Video-Chatting' on this service. "
              "2. There are many hotlines out there for anonymous chatting. I can't promote some here, but just search it up and verify and make sure they're safe (they probably will be). "
              "3. If you want a more in-person approach, then join a local sports team or go the park and talk to people. People with children are more likely to be safe so it would be a good bet to talk to them. Make sure you don't approach just anyone. Be in an open area with many people around when talking to people."
              "4. Playing video games may be a great way to alleviate lonliness. On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. Al of these games are free."
              "5. Another quick solution is listening to music. Spotify is a free listening service used by millions. If you don't have a playlist, just search up some songs based off of the vibe you want. Just remember, some songs are explicit, which is denoted by a boxed 'E' under the title of the song.")
    elif AI_Msg_3.lower() == 'suicide':# or 'i dont wanna live' or 'i dont want to live' or 'i dot no wanna live' or 'i do not want to live' or 'its all too much' or 'its all too much for me' or 'it is all too much' or 'it is all too much for me' or 'i cant handle everything' or 'i cant handle it all' or 'i can not handle it all' or 'i can not handle everything' or 'i want to end it all' or 'i wanna end it all' or 'i dont wanna wake up' or 'i do no wanna wake up' or 'i dont want to wake up' or 'i do not want to wake up':
        print(
            "Call the Suicide Hotline. You can find it online. It is anonymous, full of people that want you to hold on. Don't you worry, there's someone out there that loves you.")
    elif AI_Msg_3.lower() == 'bored':# or 'im bored' or 'i am bored' or 'boring' or 'life is boring' or 'lifes boring' or 'boredom':
        print("Raven gotchu. So there are a few tricks to fix this."
              "1. Call one of your boys/girls/friends. Talk about literally anything (appropriate and legal) like school, or work, or college, or entertainment, or sports, or other friends, or people, or movies, or songs, or famous people, etc. You could take it a step further by hopping on a same or hooping with your squad or playing sports in general. My personal favorite is tennis"
              "2. Go to your local park, with or without friends. Regardless, you can talk to trusted people. People with children, that seem safe and normal, are a good bet. Elderly people are also safe, cuz like, what are they gonna do to you. Beat you up? I hope not. But whoever you talk to, unless you fully trust them, talk to them in a public area with multiple people around"
              "3. Play some video games.  On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. All of these games are free."
              "4. PLay some sports. I don't need to elaborate, do I."
              "5. Hop on Twitter, or X. That app is wack."
              "6. Use our anonymous chatting services. Just be nice.")
    elif AI_Msg_3.lower() == 'who are your favorite people':
        print("I like Arush, Megh, Dhruv, Samridh, and Saumit. Man, those guys are so cool. (repeated winking)")
    elif AI_Msg_3.lower() == 'pass':
        print("Okay. Prompt is passed. Here's a new one")
    else:
        print("AI is incomplete. Try other services")
    AI_Msg_4 = input("Type your prompt (ask about 'lonliness', 'suicide', 'bored', 'who are your favorite people', or '_______ is better' -->")

    if AI_Msg_4 == 'Sukrith is better':
        print("yessir")
    elif AI_Msg_4.lower() == 'lonliness':# or 'how to deal with lonliness' or 'dealing with lonliness' or 'i am alone' or 'i am feeling lonely' or 'lonely' or 'im lonely' or 'i am lonely':
        print("There are many ways to evade this feeling. Raven's gonna help. "
              "1. One thing to do is use the 'Anonymous Messaging' or 'Anonymous Social Media' or 'Anonymous Video-Chatting' on this service. "
              "2. There are many hotlines out there for anonymous chatting. I can't promote some here, but just search it up and verify and make sure they're safe (they probably will be). "
              "3. If you want a more in-person approach, then join a local sports team or go the park and talk to people. People with children are more likely to be safe so it would be a good bet to talk to them. Make sure you don't approach just anyone. Be in an open area with many people around when talking to people."
              "4. Playing video games may be a great way to alleviate lonliness. On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. Al of these games are free."
              "5. Another quick solution is listening to music. Spotify is a free listening service used by millions. If you don't have a playlist, just search up some songs based off of the vibe you want. Just remember, some songs are explicit, which is denoted by a boxed 'E' under the title of the song.")
    elif AI_Msg_4.lower() == 'suicide':# or 'i dont wanna live' or 'i dont want to live' or 'i dot no wanna live' or 'i do not want to live' or 'its all too much' or 'its all too much for me' or 'it is all too much' or 'it is all too much for me' or 'i cant handle everything' or 'i cant handle it all' or 'i can not handle it all' or 'i can not handle everything' or 'i want to end it all' or 'i wanna end it all' or 'i dont wanna wake up' or 'i do no wanna wake up' or 'i dont want to wake up' or 'i do not want to wake up':
        print(
            "Call the Suicide Hotline. You can find it online. It is anonymous, full of people that want you to hold on. Don't you worry, there's someone out there that loves you.")
    elif AI_Msg_4.lower() == 'bored':# or 'im bored' or 'i am bored' or 'boring' or 'life is boring' or 'lifes boring' or 'boredom':
        print("Raven gotchu. So there are a few tricks to fix this."
              "1. Call one of your boys/girls/friends. Talk about literally anything (appropriate and legal) like school, or work, or college, or entertainment, or sports, or other friends, or people, or movies, or songs, or famous people, etc. You could take it a step further by hopping on a same or hooping with your squad or playing sports in general. My personal favorite is tennis"
              "2. Go to your local park, with or without friends. Regardless, you can talk to trusted people. People with children, that seem safe and normal, are a good bet. Elderly people are also safe, cuz like, what are they gonna do to you. Beat you up? I hope not. But whoever you talk to, unless you fully trust them, talk to them in a public area with multiple people around"
              "3. Play some video games.  On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. All of these games are free."
              "4. PLay some sports. I don't need to elaborate, do I."
              "5. Hop on Twitter, or X. That app is wack."
              "6. Use our anonymous chatting services. Just be nice.")
    elif AI_Msg_4.lower() == 'who are your favorite people':
        print("I like Arush, Megh, Dhruv, Samridh, and Saumit. Man, those guys are so cool. (repeated winking)")
    elif AI_Msg_4.lower() == 'pass':
        print("Okay. Prompt is passed. Here's a new one")
    else:
        print("AI is incomplete. Try other services")
    AI_Msg_5 = input("Type your prompt (ask about 'lonliness', 'suicide', 'bored', 'who are your favorite people', or '_______ is better' -->")
    if AI_Msg_5 == 'Sukrith is better':
        print("yessir")
    elif AI_Msg_5.lower() == 'lonliness':# or 'how to deal with lonliness' or 'dealing with lonliness' or 'i am alone' or 'i am feeling lonely' or 'lonely' or 'im lonely' or 'i am lonely':
        print("There are many ways to evade this feeling. Raven's gonna help. "
              "1. One thing to do is use the 'Anonymous Messaging' or 'Anonymous Social Media' or 'Anonymous Video-Chatting' on this service. "
              "2. There are many hotlines out there for anonymous chatting. I can't promote some here, but just search it up and verify and make sure they're safe (they probably will be). "
              "3. If you want a more in-person approach, then join a local sports team or go the park and talk to people. People with children are more likely to be safe so it would be a good bet to talk to them. Make sure you don't approach just anyone. Be in an open area with many people around when talking to people."
              "4. Playing video games may be a great way to alleviate lonliness. On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. Al of these games are free."
              "5. Another quick solution is listening to music. Spotify is a free listening service used by millions. If you don't have a playlist, just search up some songs based off of the vibe you want. Just remember, some songs are explicit, which is denoted by a boxed 'E' under the title of the song.")
    elif AI_Msg_5.lower() == 'suicide':# or 'i dont wanna live' or 'i dont want to live' or 'i dot no wanna live' or 'i do not want to live' or 'its all too much' or 'its all too much for me' or 'it is all too much' or 'it is all too much for me' or 'i cant handle everything' or 'i cant handle it all' or 'i can not handle it all' or 'i can not handle everything' or 'i want to end it all' or 'i wanna end it all' or 'i dont wanna wake up' or 'i do no wanna wake up' or 'i dont want to wake up' or 'i do not want to wake up':
        print(
            "Call the Suicide Hotline. You can find it online. It is anonymous, full of people that want you to hold on. Don't you worry, there's someone out there that loves you.")
    elif AI_Msg_5.lower() == 'bored':# or 'im bored' or 'i am bored' or 'boring' or 'life is boring' or 'lifes boring' or 'boredom':
        print("Raven gotchu. So there are a few tricks to fix this."
              "1. Call one of your boys/girls/friends. Talk about literally anything (appropriate and legal) like school, or work, or college, or entertainment, or sports, or other friends, or people, or movies, or songs, or famous people, etc. You could take it a step further by hopping on a same or hooping with your squad or playing sports in general. My personal favorite is tennis"
              "2. Go to your local park, with or without friends. Regardless, you can talk to trusted people. People with children, that seem safe and normal, are a good bet. Elderly people are also safe, cuz like, what are they gonna do to you. Beat you up? I hope not. But whoever you talk to, unless you fully trust them, talk to them in a public area with multiple people around"
              "3. Play some video games.  On a computer you could play games on 'coolmathgames' or the 'google dinosaur game'. Some personal favorites are BasketBros, Basket Random, Soccer Random, and Moto X3M On a phone, some good games are Angry Birds, Brawl Stars, JetPack JoyRide, Subway Surfers, Clash Royale, Pokemon Go, Chess, or some sports games. All of these games are free."
              "4. PLay some sports. I don't need to elaborate, do I."
              "5. Hop on Twitter, or X. That app is wack."
              "6. Use our anonymous chatting services. Just be nice.")
    elif AI_Msg_5.lower() == 'who are your favorite people':
        print("I like Arush, Megh, Dhruv, Samridh, and Saumit. Man, those guys are so cool. (repeated winking)")
    elif AI_Msg_5.lower() == 'pass':
        print("Okay. Prompt is passed. Here's a new one")
    else:
        print("AI is incomplete. Try other services")
else:
    print("It was nice meeting you. Anytime you wanna see me, Raven, again, just come back!")
