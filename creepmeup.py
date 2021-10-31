import random

def random_creepypasta():
  creepypasta_list = [
    {
      "title" : "Slender Man",
      "story" : """Before this pale, faceless ghoul had his own movie and video game series, he haunted the forums of the internet with his finely pressed suit and unnaturally long limbs. The Slender Man's story is not a narrative one, but a pseudo-historical look at this monster's history with humanity that is tied into several other creepypastas.

      Typically, the Slender Man preys on children and those who become obsessed with his existence, though no one knows exactly what happens to the bodies since no one has ever escaped from an encounter with him. Suggested stories featuring the Slender Man include The Tall Man and the Marble Hornets videos.

      In the real world, this creepypasta figure became a key figure during an assault and subsequent criminal case in 2014 involving three 12-year-old girls. Wisconsin teens Anissa Weier and Morgan Geyser, lured their friend, Payton Leutner, into the woods during a game of hide-and-seek. In an reported attempt to appease Slender Man, the duo stabbed Leutner 19 times and left her at the scene. Leutner managed to drag herself to a nearby road where a cyclist found her, and she was immediately taken to a hospital where she recovered from her injuries.

      Soon after the attack, Weier and Geyser were arrested and tried for attempted second-degree murder. In 2017, Weier was sentenced to 25 years in a mental institution, while her accomplice Geyser was sentenced to 40 years in a mental hospital in 2018.""",
      "link" : "https://images-ext-1.discordapp.net/external/5CeLXfsfKdp60ZPCAW0V-ek2mkJ_H1jt6j3fZiyaczk/https/cdn.vox-cdn.com/thumbor/kSu6ardo8vx7aur4lGRfD6PV3Nw%3D/0x0%3A1920x1080/1400x933/filters%3Afocal%28807x387%3A1113x693%29%3Ano_upscale%28%29/cdn.vox-cdn.com/uploads/chorus_image/image/61078135/slender_man.0.jpeg?width=800&height=533"
    },
    {
      "title" : "Candle Cove",
      "story" : """Everyone has a television show from their childhood that they fondly remember. Like those who nostalgically recall the adventures of Dora the Explorer, Mister Rogers, and Sesame Street, some adults rediscovered their favorite show from the 1970s, Candle Cove, on a television forum in this creepypasta. Slowly, their memories of the show grow darker and more disturbing until one of the adults asks his mother about the true nature of the show.

      The forum format of the story adds a spooky realism to the tale, also making it easy to recreate and share on other boards. If you find this story particularly compelling, watch the first season of the Syfy original series Channel Zero, which is based off this creepypasta.""",
      "link" : "https://i.ytimg.com/vi/2vyOeZxBYTc/maxresdefault.jpg?width=800&height=450"
    },
    {
      "title" : "Robert the Doll",
      "story" : """Not for the faint of heart, Robert the Doll really exists. The myths surrounding him vary, especially since it became so popular on the internet. The doll was given to artist Robert Eugene Otto in the late 1800s or early 1900s by a servant working in his family home. The doll, which he named after himself, then took on a life of its own and began to terrorize the family.
      
      Otto is said to have kept his doll into adulthood and it subsequently tormented his late wife to insanity. When the doll was found by another family, the girl to whom it was given was terrified of it and refused to have it in her room.

      The doll is currently residing in the Fort East Martello Museum in Key West, Florida. Visitors must ask Robert politely if they want to take his photo. If they mock him or take his photo without permission, Robert is said to lay a curse on them.""",
      "link" : "https://www.ghostsandgravestones.com/wp-content/uploads/2017/12/key-west-haunted-robert-the-doll-768x432.jpg?width=800&height=450"
    },
    {
      "title" : "Anasi's Goatman Story",
      "story" : """Based on a Native American legend, this creepypasta was originally found on 4Chan's paranormal board /x/, where some of the best creepypastas can be found.

      The story follows a teenager who goes down to Alabama to be with his extended family. While he, his cousins, and their friends are camping out in the woods, they see a strange figure — the Goatman — jerking and spouting gibberish as it follows them. They spend the rest of the night in fear as the Goatman slowly infiltrates the group, terrorizing the teens into a frenzied state of paranoia.

      This mix of pre-existing lore and new narrative is not rare for creepypastas, but it's the strength of the writing that really makes this particular story worth sharing. There are variations of this story, but most follow a similar formula where a group is stalked by the titular monster with different outcomes.""",
      "link" : "https://i.ytimg.com/vi/irYuUF7l9Ys/maxresdefault.jpg?width=800&height=450"
    },
    {
      "title" : "The Russian Sleep Experiment",
      "story" : """A staple of best creepypasta lists everywhere, the title of this story itself carries with it a sense of dread and horror. Shortly after World War II, five political prisoners are subjected to an experiment in which they have to remain awake for 30 days in a tank filled with an experimental gas. As with most science-gone-wrong stories, the test subjects begin to lose their minds among a number of other gruesome symptoms. The horror does not end when the experimenters try to save their subjects — far from it.

      Just know that this story may not be appropriate if you are squeamish or dislike gore, as the narrative goes into graphic detail about the physical state of the patients. Thankfully there are no pictures, or this would be the ultimate nightmare fuel.""",
      "link" : "https://mysteriesrunsolved.com/wp-content/uploads/2020/05/PhotoCollage_20200518_073906760_compress12.jpg?width=800&height=450"
    },
    {
      "title" : "Jeff the Killer",
      "story" : """If you've never laid eyes on the infamous image of Jeff the Killer before, consider yourself lucky. The basic story concerns Jeff, a serial killer who hides in the closet and whispers "go to sleep" to its victim before slaughtering everyone in the household. Even more disturbing than his M.O. is his appearance — his face is smooth and stark white, a huge grin and small lid-less eyes. He is one of the most easily recognizable creepypastas, with his eerie stare posted across forums.

      His origin story involves a fight that resulted in a chemical burn on his face and caused him to suffer a mental break. Soon after, he murdered his family and disappeared into the night to make guest appearances in your nightmares.""",
      "link" : "https://images-ext-1.discordapp.net/external/93sEpFzpkDChp5KX9bQNbhYyn0IUO3FMA94_jn5VWEo/https/i.ytimg.com/vi/waedDlIsYvI/maxresdefault.jpg?width=800&height=450"
    },
    {
      "title" : "BEN Drowned",
      "story" : """Hacked video games are often found in creepypastas, but none is more infamous than BEN Drowned, the story of Matt, a college-age boy who picks up a hacked cartridge of The Legend of Zelda: Majora's Mask at a garage sale.

      As the boy plays, he captures the strange occurrences in the game and real life until it ultimately culminates into a full haunting. The narrator and BEN's fates are left up to the reader's imagination, but the tale implies that a happy ending is not in the realm of possibility.

      This creepypasta is one of the few that integrate multiple types of media into the story. There is the text of the story itself — both a formal post version that went up on 4Chan's /x/ forums in real time and a diary included on the final post — and videos of the disturbing gameplay under the YouTube channel Alex Hall (originally Jadusable). The footage includes a warped soundtrack, terrifying glitches, and a creepy statue that is supposed to be BEN following the player around.

      While the story is clearly fictional, the level of dedication to creating this eerie story makes it worth the read.""",
      "link" : "https://static.wikia.nocookie.net/youtubepoop/images/a/a4/BenDrowned.jpg?width=800&height=450"
    },
    {
      "title" : "Persuaded",
      "story" : """Zombies definitely have a place in creepypastas, especially after having taken over the majority of pop culture. However, in the spirit of keeping readers on their toes, these zombies don't need frenzied biting to increase their numbers, which elevates this tale above and beyond other zombie-inspired creepypastas.

      After a massive oil spill, all those touched by the substance begin to viciously attack other creatures, causing mass panic across the country. The nameless protagonist holes himself up in his apartment, waiting for the screaming, violent horde to come crashing through his door and tear him limb from limb. If only that had actually happened, instead of the two day-long nightmare that really unfolds.""",
      "link" : "https://previews.123rf.com/images/icetray/icetray1602/icetray160205075/51602780-persuaded-word-on-concrette-wall.jpg?width=800&height=450"
    },
    {
      "title" : "Smile Dog",
      "story" : """If there's any story on this list that best captures the message "be careful what you wish for," Smile Dog is it. The creepypasta deals with an image posted on an old bulletin board system back in 1992 called smile.jpg. Those who saw the image either disappeared or died, save for one Mary E., who the narrator goes to interview. What he eventually learns is that some things, even simple pictures, are better left as mysteries than dealing with the horrifying truth.

      In case you were wondering, the story does come with an accompanying image, but you may not want to see it after reading the full story. Though, in the end, you may not have a choice.""",
      "link" : "https://upload.wikimedia.org/wikipedia/commons/e/e8/The_Smile_Dog.jpg?width=800&height=450"
    },
    {
      "title" : "Annora Petrova",
      "story" : """This tale reminds us that it's best not to Google yourself, no matter how tempting it may be. Annora Petrova was one of the most promising figure skaters in the United States, until she discovered a sentient Wikipedia page about her. After trying to selfishly alter her fate by editing the page, her life spirals out of control in the most unexpected ways, until she is a friendless orphan (which isn't even the worst part).

      While the Wikipedia page does not actually exist, it's a harrowing tale about messing with the unknown forces of the internet. If you do check this story out, make sure you click on the image at the bottom of the email for an extra layer of spookiness.""",
      "link" : "https://www.zeezo.com/wp-content/uploads/2019/07/d9i6xft7w0e21.jpg?width=800&height=450"
    },
    {
      "title" : "NoEnd House",
      "story" : """Haunted houses are at the center of many famous scary narratives, and surviving the night in one earned teenagers instant respect. Still, is the potential trauma and death worth the admiration of people who you'll likely never see again after graduation? This creepypasta answers with a firm and decisive "no."

      NoEnd House promises $500 to whomever can survive a trip through its nine rooms of torture, a challenge that our narrator David readily accepts. The rooms begin to grow increasingly sinister and evil, pushing the limits of David's psyche and humanity. Are nine rooms really worth such a small monetary compensation that won't even pay for one therapy session?

      The Syfy series Channel Zero also covers this creepypasta in its second season if you want to add some visuals to this spooky story.""",
      "link" : "https://static3.srcdn.com/wordpress/wp-content/uploads/2020/02/channel-zero-no-end-house-poster.jpg?width=800&height=450"
    },
    {
      "title" : "Psychosis",
      "story" : """Can you really trust what you see and feel? Is your life all a computer simulation? Do we live in the Matrix? Are we all just people in someone's else dream that is bound to end? Is this the real life, or is this just fantasy?

      Existentialism may not be the scariest of philosophies, but Psychosis shows that proving human existence beyond innate fears and paranoia is an inner battle that can never be won.

      John soon finds out that he's been cut off from the rest of the world — his only communication with other people is through electronic devices. He quickly becomes paranoid and becomes convinced that everyone around him is lying, trying to get him to come outside his door so an unknown entity can get him. His logic tries to defy his gut feeling, but he falls further into the belief that something has gone horribly wrong outside, and it's coming for him next.""",
      "link" : "https://i.ytimg.com/vi/eDIJVI72jcw/maxresdefault.jpg?width=800&height=450"
    },
    {
      "title" : "Doors",
      "story" : """This creepypasta is popular for its Shyamalan-esque nature. The tale follows a family with a young male narrator who talks about their daily lives together.

      One night, the household is attacked by a mysterious figure that our intrepid protagonist tries to chase out. Giving any more of the plot away would ruin the surprise, but this story proves that brevity can be an effective tool when used to properly horrifying and amaze.""",
      "link" : "https://i.ytimg.com/vi/pufsWQVDxGE/maxresdefault.jpg?width=800&height=450"
    },
    {
      "title" : "Gateway of the Mind",
      "story" : """Ever wonder what would happen if you couldn't see, hear, smell, taste, or touch? Well, this creepypasta is here to put that theory to the test in what is honestly the most terrifying science experiment.

      The story centers around a group of scientists who wish to make contact with God, and they believe that this could be possible by removing the body of all five senses. After performing a complex sensory surgery on a test subject, the poor person is completely disoriented and begins to hallucinate and "hear" people who have passed away.

      What happens at the end is extremely meta, but the grueling details involving the pure mental torture the subject goes through is enough to absolutely creep anyone out.""",
      "link" : "https://i.ytimg.com/vi/pySDIX_rIIg/maxresdefault.jpg?width=800&height=450"
    },
    {
      "title" : "The Rake",
      "story" : """This monster may not be as famous as his cousin, Slender Man, but he sure is just as creepy. The Rake is a humanoid creature that is completely pale, hairless, and has a thirst for human flesh.

      According to Know Your Meme, this creature was originally created in 4chan's board where someone opened a "make your own monster" thread. The description that eventually became a part of The Rake was, "no apparent mouth, pale skin, six feet tall when standing, but usually crouches and walks on all fours, no nose, no mouth," and many other disturbing physical features.""",
      "link" : "https://static.wikia.nocookie.net/creepypasta/images/0/04/The_Rake.jpg?width=800&height=450"
    },
    {
      "title" : "Lavender Town Syndrome",
      "story" : """A classic video game creepypasta that hits a little too close to home for those of us who grew up playing the original Pokémon Red and Blue during the late '90s. This creepypasta centers around the game Pokémon Green, which was only released in Japan in 1996.

      According to the legend, rates of illness and suicide in children in Japan between the ages of 7-12 have reached a fever pitch. The common connection between all of them? They all played Pokémon Green and had reached an area known as Lavender Town whose theme music had extremely high pitches.

      After conducting studies on this phenomenon that became known as "Lavender Town Syndrome," scientists realized that there was a certain tone in the town's music that only the ears of young children and teens could hear. This had essentially drove this demographic who played the game to insanity, causing them to have headaches, ear issues, and die from suicide.

      While this sparked many theories and creepypastas surrounding Lavender Town and the original Pokémon games, this creepypasta is actually loosely based off a real-life incident involving a Pokémon episode that only aired in Japan in 1997.

      During the airing of the 38th episode of the original Pokémon television series titled Electric Soldier Porygon, a scene that made use of extreme flashing images gave hundreds of children epileptic seizures.""",
      "link" : "https://gamingbolt.com/wp-content/uploads/2017/10/Pokemon-Lavender-Town.jpg?width=800&height=450"
    },
    {
      "title" : "The Expressionless",
      "story" : """In this creepypasta classic, a woman wearing a white gown that was covered in blood stumbled into a hospital in 1972. According to the nurse who is recounting this event, she said that this woman had the appearance of a mannequin, but was very much human-like in her movement and mannerisms.

      After throwing a kitten she had clamped in her jaws on the ground, doctors and nurses rushed the woman into a hospital room for evaluation. Little does the hospital staff know that they have no idea who, or rather what, they're dealing with.""",
      "link" : "https://mysteriesrunsolved.com/wp-content/uploads/2020/06/20200603_110320_compress31.jpg?width=800&height=451"
    }
  ]
  return random.choice(creepypasta_list)