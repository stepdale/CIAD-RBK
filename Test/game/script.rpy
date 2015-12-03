# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image bg uni = "uni.jpg"
image bg dark_clouds = "dark_clouds.jpg"
image bg town = "town.jpg"
image bg fire = "fire_smoke.jpg"

#mc prologue images
image mc_prologue default = "mc_prologue_default.png"
image mc_prologue annoyed = "mc_prologue_annoyed.png"
image mc_prologue uncomfortable = "mc_prologue_uncomfortable.png"

# Declare characters used by this game.

define mage = Character('Mage', color="#c8ffc8")
define narrator = Character(None, window_top_padding=30)
define player = Character("[playerName]", color="#c8ffc8")
define nvl_narrator = Character(None, kind=nvl, window_top_padding=30)
define marcy = Character('Marcy', color="#c8ffc8")
define man = Character('Man', color="#c8ffc8" )



# The game starts here.
label start:
    scene bg dark_clouds
    with fade

    nvl_narrator "It could be said that everyone has a certain fate. That everyone, or rather everything, happens because there is a set limit to how things will turn out."  

    nvl_narrator "Heh. I was never really a believer in fate. But in recording all of these events, I have come to wonder if I should start to..."

    nvl_narrator "Looking back, I suppose everything started years before I was even born and yet...it affected me greatly. It should be said that the life of a merchant is not as glorious as one is lead to believe."

    nvl clear 

    nvl_narrator "My father and mother were lower class merchants, but with hard work, they climbed up the ladder, landing somewhere in the middle."

    nvl_narrator "My brother and I were inconviences thrust upon them, until they realized that they could bank on the emotions of other parents, by playing up the 'I would not sell it to you if I didn't use it on my own child' ploy."

    nvl_narrator "Well, the fact that my mother died trying to bring in my younger brother, was and is, of little consequence. After all, we were only truly a family if it got us another business deal." 

    nvl_narrator "But still...My father and brother was all I really had left in the world. And the world is a dark and cruel place, no matter what the minstrals say."

    nvl clear
    nvl_narrator "Ahh, right. This is not my story. What you came for was the recording of the events now known as the Knights of Calien Rebellion right?" 

    nvl_narrator "Well...Let's start with my perspective shall we?"

    scene bg uni
    with fade

    "It was the summer of my one and twentieth year."

    "My brother and father had not yet come back from Kaln. I was more than a little peeved that they might have smelt a good trade and left me behind in Rulin while chasing after it."

    "I began to read the letter Father had sent."

    "'{i}To my dearest daughter...{/i}'"

    "Hah! Oh, this is going to be great."

    "'{i}I am happy to inform you that your precious brother and I have discovered a new trade in Kaln. We shall contact you with news when we arrive. All the love in the world - Father.{/i}'"

    "All the love in the world. Why that sneaky old bandit!"

    "He stole my trade route! Precious brother indeed."

    "When I get my hands on that little traitor...I'll, well I don't know, but I'll do something."

    python:
      playerName = renpy.input("I heard someone call my name...")
      playerName = playerName.strip()
      while playerName == "":
        playerName = renpy.input("That's not right...My name...")
        playerName = playerName.strip()  


    "Good morning [playerName]! My, you're making quite a scary face dear. Is everything alright?"

    show mc_prologue annoyed
    player "Ahh? Oh. Morning Marcy!"
    player " No...EVERYTHING is NOT ALRIGHT. That father of mine has gone and stolen my trade route..."
    player "Listen Marcy, never trust a youner sibling...you hear me? NEVER."
    player "They are treacherous little things. They try to pull upon your maternal instincts, with wide eyes and easy smiles. And--"


    marcy "*giggle* Your family is getting along well as usual I see. But...didn't you say that your new trade route led to Kaln?"

    player "YES! Those little..."
    player "There is so much money to be made there, since some kind of rebel force has been active in the area. Prices for all goods can be raised! Oooh, those sneaks took my--"

    marcy "But [playerName]...I've heard that the rebel group is in the underground market. Its not safe! They capture young people and poof! They are never seen again!"
    marcy "That kind of place...the money you make wont even be close to buying your pinky free."

    show mc_prologue uncomfortable
    player "Marcy, have you been reading those tabloids again? Honestly you know that they exaggerate! The Cosmos guild is full of narcissistic--"


    marcy "[playerName]. Enough."
    marcy "The point is that all rumors have some form of truth to them."
    marcy "I think you should go and stop your family from reaching Kaln. It wont be good especially for MCB if those rumors are true."

    show mc_prologue annoyed
    player "Marcy, were you also planning on piggy backing on my trade route?"
    

    marcy "*sigh* [playerName]...I say this, with all the love I have for you. Stop being so obsessed with your trade route and go get your family! I have a bad feeling about this."
    

    player "I knew it! You are after my route!"
    player "I'm going after them, of course. But not to stop them. Its fine, I know you're in a bit of a bind since your wedding is coming up soon."

    show mc_prologue default
    player "You know what? I'll sell your goods there free of charge. Think of it as my wedding present to you!"
    

    marcy "Sometimes I wonder..."
    
    player "What? "
    

    marcy "How one of the best barter merchants in Ruiln can be so incredibly dense at times!"

    hide mc_prologue

    #Kaln
    scene bg town
    with fade

    show mc_prologue default
    player "Welcome to the city of Kaln, [playerName]."    
    player "..."
    
    show mc_prologue annoyed
    player "Its about damn time!"
    player "That lousy father and brother of mine had better not of picked this place clean yet. It took me forever to gather anything worth trading and bartering for on the journey here." 

    show mc_prologue default
    player "Ahh! Excuse me, sir? Can you direct me to the merchant square?"
    
    man "Ehh? Ahhh. A merchant are ya?"
    man "Well this is a surprise."
    man "Don't see to many women merchants in these parts."
    
    player "Really? Well..."
    
    man "Nope. Not to many women in general." 
    man "Not since that accursed rebel group set up shop around here. Picked the whole town clean." 
    man "You wouldnt be for sale would you?"
    
    player "No, I am most certainly am not. But I do have many different kinds of wares and--"
    
    man "Not interested. You can try down the main street."
    
    show mc_prologue annoyed
    player "Thanks, jerk. Am I for sale? Pfft. In his dreams...and not even then!"
    
    "ITS THE REBELS!"
    
    player "What?"

    #attack    
    scene bg fire
    with fade

    nvl clear

    nvl_narrator "Fire. That is all I can say with certainty about that skirmish that just broke out between the Rihnowan knights and the rebel forces."

    nvl_narrator "The flames roared and created utter chaos." 

    nvl_narrator "I watched in horror as my cart was engulfed by the flames. My garron bolted away, with its mane ablaze. A crowsbow bolt flew past me, nearly making its mark, were it not for a loud scream that came from my right. A child had been engulfed in flames screamed as he ran towards the well. "

    nvl_narrator "How I came upon the village square, I don't really know." 

    nvl clear
    
    nvl_narrator "I just ran and ran and ran."

    nvl clear
    nvl_narrator "The sight in the square made me stop in my tracks."
    nvl_narrator "The scene looked like the preacher's vision of the apocalypse. The scattered helmets in the square looked like deformed, horned heads, reflecting the flames from the destroyed buildings. It almost seemed like the flames were dancing and reveling in the chaos and destruction."

    nvl_narrator "The flash of light from their weapons, seemed like claws moving too and fro, like a conductor before his concert. Though this was one concert I never wanted to see or be apart of."

    nvl_narrator "How long I stood their staring, I cannot say. But a rough hand gripped my wrist and suddenly I was staring into pale ice blue eyes."



    return
