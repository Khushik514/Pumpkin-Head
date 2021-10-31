import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(
    command_prefix = commands.when_mentioned_or('!'),
    help_command = help_command
)
client = discord.Client()

def random_movie():
  movie_list = [
    {
      "title" : "Halloween Kills",
      "link" : "https://www.imdb.com/title/tt10665338/?ref_=kw_li_tt",
      "desc" : "The saga of Michael Myers and Laurie Strode continues in the next thrilling chapter of the Halloween series.",
      "image" : "https://m.media-amazon.com/images/M/MV5BM2RmMGY2Y2UtNjA1NS00NGE4LThiNzItMmE1NTk5NzI5NmE0XkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_UX140_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Halloween",
      "link" : "https://www.imdb.com/title/tt0077651/?ref_=kw_li_tt",
      "desc" : "Fifteen years after murdering his sister on Halloween night 1963, Michael Myers escapes from a mental hospital and returns to the small town of Haddonfield, Illinois to kill again.",
      "image" : "https://m.media-amazon.com/images/M/MV5BNzk1OGU2NmMtNTdhZC00NjdlLWE5YTMtZTQ0MGExZTQzOGQyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX140_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Hocus Pocus",
      "link" : "https://www.imdb.com/title/tt0107120/?ref_=kw_li_tt",
      "desc" : "A curious youngster moves to Salem, where he struggles to fit in before awakening a trio of diabolical witches that were executed in the 17th century.",
      "image" : "https://m.media-amazon.com/images/M/MV5BMWUxNWI0YTYtY2RiZS00ZjNmLTg4ZGUtNDI0Mzk4NmQ5NWE5XkEyXkFqcGdeQXVyNjk1Njg5NTA@._V1_UY209_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Muppets Haunted Mansion",
      "link" : "https://www.imdb.com/title/tt14602326/?ref_=kw_li_tt",
      "desc" : "On Halloween night, Gonzo is challenged to spend one night in The Haunted Mansion.",
      "image" : "https://m.media-amazon.com/images/M/MV5BNDYwMGI4ZTctZTgwNC00YmRmLThjODQtYjNjMzNkMTdhYTQzXkEyXkFqcGdeQXVyMTEzMTI1Mjk3._V1_UY209_CR13,0,140,209_AL_.jpg"
    },
    {
      "title" : "Harry Potter and the Philosopher's Stone",
      "link" : "https://www.imdb.com/title/tt0241527/?ref_=kw_li_tt",
      "desc" : "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.",
      "image" : "https://m.media-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UY209_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "The Addams Family",
      "link" : "https://www.imdb.com/title/tt0101272/?ref_=kw_li_tt",
      "desc" : "Con artists plan to fleece an eccentric family using an accomplice who claims to be their long-lost uncle.",
      "image" : "https://m.media-amazon.com/images/M/MV5BODc1NmY0MDUtNjUzNS00ODdhLWJlN2ItMTgwZjczZjI0MDkyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY209_CR9,0,140,209_AL_.jpg"
    },
    {
      "title" : "The Nightmare Before Christmas",
      "link" : "https://www.imdb.com/title/tt0107688/?ref_=kw_li_tt",
      "desc" : "Jack Skellington, king of Halloween Town, discovers Christmas Town, but his attempts to bring Christmas to his home causes confusion.",
      "image" : "https://m.media-amazon.com/images/M/MV5BNWE4OTNiM2ItMjY4Ni00ZTViLWFiZmEtZGEyNGY2ZmNlMzIyXkEyXkFqcGdeQXVyMDU5NDcxNw@@._V1_UX140_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "The Crow",
      "link" : "https://www.imdb.com/title/tt0109506/?ref_=kw_li_tt",
      "desc" : "A man brutally murdered comes back to life as an undead avenger of his and his fiancée's murder.",
      "image" : "https://m.media-amazon.com/images/M/MV5BM2Y4ZGVhZjItNjU0OC00MDk1LWI4ZTktYTgwMWJkNDE5OTcxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY209_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Hocus Pocus 2",
      "link" : "https://www.imdb.com/title/tt11909878/?ref_=kw_li_tt",
      "desc" : "Three young women accidentally bring back the Sanderson Sisters to modern day Salem and must figure out how to stop the child-hungry witches from wreaking havoc on the world.",
      "image" : "https://m.media-amazon.com/images/M/MV5BMzAzNzY5ZDUtOGUzYS00ZjdmLWE4ZDUtNjI4NDYyZmNhODU0XkEyXkFqcGdeQXVyNzEzNjU1NDg@._V1_UX140_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Halloween H20: 20 Years Later",
      "link" : "https://www.imdb.com/title/tt0120694/?ref_=kw_li_tt",
      "desc" : "Laurie Strode, now the dean of a Northern California private school with an assumed name, must battle the Shape one last time, as the life of her own son hangs in the balance.",
      "image" : "https://m.media-amazon.com/images/M/MV5BNzA3ZjMzZWItNWUyNy00ZmNiLWIwYmYtN2UxNWUwMGY5Yzc2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY209_CR1,0,140,209_AL_.jpg"
    },
    {
      "title" : "Scary Movie",
      "link" : "https://www.imdb.com/title/tt0175142/?ref_=kw_li_tt",
      "desc" : "A year after disposing of the body of a man they accidentally killed, a group of dumb teenagers are stalked by a bumbling serial killer.",
      "image" : "https://m.media-amazon.com/images/M/MV5BMGEzZjdjMGQtZmYzZC00N2I4LThiY2QtNWY5ZmQ3M2ExZmM4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY209_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Halloween III: Season of the Witch",
      "link" : "https://www.imdb.com/title/tt0085636/?ref_=kw_li_tt",
      "desc" : "Kids all over America want Silver Shamrock masks for Halloween. Doctor Daniel Challis seeks to uncover a plot by Silver Shamrock owner Conal Cochran.",
      "image" : "https://m.media-amazon.com/images/M/MV5BN2YzYjI0MWYtYWUyZS00ZDQ4LWEzN2EtMDU4NDJmNjA2ZWFiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX140_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Addams Family Values",
      "link" : "https://www.imdb.com/title/tt0106220/?ref_=kw_li_tt",
      "desc" : "The Addams Family try to rescue their beloved Uncle Fester from his gold-digging new love, a black widow named Debbie.",
      "image" : "https://m.media-amazon.com/images/M/MV5BZWFhNjY0YjItNjM5NC00NzAwLWI3ZWUtMTlkNTA0ZWVkNjBkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX140_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Halloween II",
      "link" : "https://www.imdb.com/title/tt1311067/?ref_=kw_li_tt",
      "desc" : "Laurie Strode struggles to come to terms with her brother Michael's deadly return to Haddonfield, Illinois; meanwhile, Michael prepares for another reunion with his sister.",
      "image" : "https://m.media-amazon.com/images/M/MV5BMjE2OTEzODI0NF5BMl5BanBnXkFtZTcwMTE4MTY2Mg@@._V1_UY209_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Trick 'r Treat",
      "link" : "https://www.imdb.com/title/tt0862856/?ref_=kw_li_tt",
      "desc" : "Five interwoven stories that occur on Halloween: An everyday high school principal has a secret life as a serial killer; a college virgin might have just met the guy for her; a group of teenagers pull a mean prank; a woman who loathes the night has to contend with her holiday-obsessed husband; and a mean old man meets his match with a demonic, supernatural trick-or-treater.",
      "image" : "https://m.media-amazon.com/images/M/MV5BYmIyY2E5YjMtZDA3NC00MmIzLWFkZmItNzVlODllZWNlZmRkXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX140_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Halloween: Resurrection",
      "link" : "https://www.imdb.com/title/tt0220506/?ref_=kw_li_tt",
      "desc" : "Three years after he last terrorized his sister, Michael Myers confronts her again, before traveling to Haddonfield to deal with the cast and crew of a reality show which is being broadcast from his old home.",
      "image" : "https://m.media-amazon.com/images/M/MV5BODczZDMxNTMtZDIxOC00YWEzLWJkMmEtZjczNGUwZDA2NTNhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY209_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Halloween 4: The Return of Michael Myers",
      "link" : "https://www.imdb.com/title/tt0095271/?ref_=kw_li_tt",
      "desc" : "Ten years after his original massacre, the invalid Michael Myers awakens on Halloween Eve and returns to Haddonfield to kill his seven-year-old niece. Can Dr. Loomis stop him?",
      "image" : "https://m.media-amazon.com/images/M/MV5BYWNiNjBhZjAtMzVkNi00MTJiLWI0NGQtODE2NmIyNmU2OTQwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX140_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Hubie Halloween",
      "link" : "https://www.imdb.com/title/tt10682266/?ref_=kw_li_tt",
      "desc" : "Despite his devotion to his hometown of Salem (and its Halloween celebration), Hubie Dubois is a figure of mockery for kids and adults alike. But this year, something is going bump in the night, and it's up to Hubie to save Halloween.",
      "image" : "https://m.media-amazon.com/images/M/MV5BMTE0N2EyMzgtMWJhZS00ZWNmLThjZmQtMjcxYTk1NTJiMGVkXkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_UY209_CR13,0,140,209_AL_.jpg"
    },
    {
      "title" : "The Exorcist",
      "link" : "https://www.imdb.com/title/tt0070047/?ref_=kw_li_tt",
      "desc" : "When a 12-year-old girl is possessed by a mysterious entity, her mother seeks the help of two priests to save her.",
      "image" : "https://m.media-amazon.com/images/M/MV5BYjhmMGMxZDYtMTkyNy00YWVmLTgyYmUtYTU3ZjcwNTBjN2I1XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX140_CR0,0,140,209_AL_.jpg"
    },
    {
      "title" : "Zodiac",
      "link" : "https://www.imdb.com/title/tt0443706/?ref_=kw_li_tt",
      "desc" : "Between 1968 and 1983, a San Francisco cartoonist becomes an amateur detective obsessed with tracking down the Zodiac Killer, an unidentified individual who terrorizes Northern California with a killing spree.",
      "image" : "https://m.media-amazon.com/images/M/MV5BN2UwNDc5NmEtNjVjZS00OTI5LWE5YjctMWM3ZjBiZGYwMGI2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY209_CR1,0,140,209_AL_.jpg"
    },
    {
      "title" : "Insidious",
      "link" : "https://www.imdb.com/title/tt1591095/?ref_=kw_li_tt",
      "desc" : "Insidious: Directed by James Wan. With Patrick Wilson, Rose Byrne, Ty Simpkins, Lin Shaye. A family looks to prevent evil spirits from trapping their comatose child in a realm called The Further.",
      "image" : "https://m.media-amazon.com/images/M/MV5BMTYyOTAxMDA0OF5BMl5BanBnXkFtZTcwNzgwNTc1NA%40%40._V1_FMjpg_UX1000_.jpg"
    },
    {
      "title" : "The Grudge",
      "link" : "https://www.imdb.com/title/tt0391198/?ref_=kw_li_tt",
      "desc" : "The Grudge: Directed by Takashi Shimizu. With Sarah Michelle Gellar, Jason Behr, William Mapother, Clea DuVall. An American nurse living and working in Tokyo is exposed to a mysterious supernatural curse, one that locks a person in a powerful rage before claiming their life and spreading to another victim.",
      "image" : "https://m.media-amazon.com/images/M/MV5BMjIxODg1Nzc3NF5BMl5BanBnXkFtZTcwMjM0MjEzMw%40%40._V1_FMjpg_UX1000_.jpg"
    }
  ]
  return random.choice(movie_list)

@bot.command(name='spook_n_chill', help='Suggests you creepy movies for u to spook n chill.')
async def movie_embed(ctx):
    movie = random_movie()
    embed=discord.Embed(title=movie["title"], url=movie["link"], description=movie["desc"], color=discord.Color.orange())
    embed.set_image(url=movie["image"])
    await ctx.send(embed=embed)

def random_meme():
  meme_list = ["https://i.imgflip.com/4keurh.jpg", "https://i.imgflip.com/5s4tcx.jpg", "https://i.imgflip.com/3e7svp.jpg","https://i.imgflip.com/4jwjip.jpg", "https://i.imgflip.com/5rmcln.jpg","https://i.imgflip.com/2o6s2e.jpg", "https://i.imgflip.com/5sf0zq.jpg","https://i.imgflip.com/5sf15w.jpg", "https://i.imgflip.com/59xkry.jpg","https://i.imgflip.com/5sf1sh.jpg", "https://i.imgflip.com/1ygzcs.jpg",
  "https://i.imgflip.com/1yg2m5.jpg", "https://i.imgflip.com/2kz3tk.jpg",
  "https://i.imgflip.com/5ro26t.jpg", "https://i.imgflip.com/5mt5pj.jpg",
  "https://i.imgflip.com/4cli2w.jpg", "https://i.imgflip.com/5sf2iy.jpg",
  "https://i.imgflip.com/5sf2s5.jpg", "https://i.imgflip.com/1ykpdd.jpg",
  "https://i.imgflip.com/5sf2ys.jpg", "https://i.imgflip.com/2ijyr1.jpg"
  ]
  return random.choice(meme_list)

@bot.command(name='make_me_laugh', help='Makes you laugh with creepy memes.')
async def meme_embed(ctx):
    meme = random_meme()
    embed=discord.Embed(title="Here's a creepy meme for your ugly laughter", color=discord.Color.green())
    embed.set_image(url=meme)
    await ctx.send(embed=embed)
  
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

@bot.command(name='creep_me_up', help='Sends some creepy pasta for you to creep up.')
async def creepypasta_embed(ctx):
    pasta = random_creepypasta()
    embed=discord.Embed(title=pasta["title"], description=pasta["story"], color=discord.Color.red())
    embed.set_image(url=pasta["link"])
    await ctx.send(embed=embed)

def random_costume():
  costume_list = [
    {
      "title" : "Bob Ross and a Happy Little Tree Halloween",
      "image" : "https://images-ext-1.discordapp.net/external/OIY3X5XqrkZQ0f0rTQbWhnkHC-eBXgFEwp8JfZjH8nI/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/bobrossandhappytrees-1535564537.jpg?width=400&height=600"
    },
    {
      "title" : "Joker Halloween Costume",
      "image" : "https://images-ext-1.discordapp.net/external/vfBfHFiDmaHu_lcwmeA-l5OXcbcJNUlcWvSuMD39F2A/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/constance-jablonsk-attends-heidi-klums-20th-annual-news-photo-1593017591.jpg?width=399&height=600"
    },
    {
      "title" : "Bread Winner Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/XGUjIrSqKRC_m1tzg3cKumK9KY5lgSm3bppfbV7FT-k/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/breadwinner-1535482242-1-1536607547.jpg?width=400&height=600"
    },
    {
      "title" : "Cloud and Rainbow Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/nkhcJKmaIjsGQGlB14v8vC6SzSg_JupxHpXDN-ZMccY/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/diy-costumes-cloud-rainbow-1540916842.png?width=400&height=600"
    },
    {
      "title" : "Pennywise halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/mJhbiQsgpLdnLMLegCqaVH7ZYNk9VUcVIlH9mtnYfE8/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/76f397239e98d5d6be60a7c007036e47-1593021029.jpg"
    },
    {
      "title" : "Men in Black Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/uP33zjkHbSLLMfur_JSGN8kzDdk-5NKpPhHXxJXLzUA/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/diy-halloween-costumes-men-in-black-1591884312.jpg?width=398&height=600"
    },
    {
      "title" : "Ashitaka and San from 'Princess Mononoke' Halloween Costume",
      "image" : "https://images-ext-1.discordapp.net/external/KbRZamM4FRzHbNHV3N_bP9DQ0Tgqrgd9LuFfFrRrl0Q/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/barbara-palvin-and-dylan-sprouse-attend-heidi-klums-20th-news-photo-1593017760.jpg?width=400&height=600"
    },
    {
      "title" : "Farmers Market Family Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/JRvYUiCFhDDJ3y4wb4nJadSuJlYUgNiqhUdxSTv32AA/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/couples-halloween-costumes-farmers-market-1592923972.jpg?width=401&height=600"
    },
    {
      "title" : "Temptation of Eve Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/hYnCrLzqAY_COGILa5oeMYFZiL32unB5ugnWFbGRS40/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/adam-eve-best-costumes-1539031186.jpg?width=400&height=600"
    },
    {
      "title" : "Dolores and Teddy Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/yeSY8iM0WEaaeU3rq8BJefOdPUy9dQMfY2FPpHrXHk8/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/westworld-best-costumes-1539031201.jpg?width=400&height=600"
    },
    {
      "title" : "Patrick Bateman Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/D9wXg6wfaEwp60WoP-Piat0ZcmR74hSJLUBJ7QkA3AM/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/american-psycho-best-costumes-1539031184.jpg?width=400&height=600"
    },
    {
      "title" : "Xenomorph Halloween Costume",
      "image" : "https://images-ext-1.discordapp.net/external/c6U4NJ2sD83q5AaRE6BTqzG2TQkRRsve9IpmDmw16eU/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/alien-xenomorph-best-costumes-1539031185.jpg?width=400&height=600"
    },
    {
      "title" : "Adam and Barbara Maitland Halloween Costume",
      "image" : "https://images-ext-1.discordapp.net/external/IRZcgfh56LGLu2bTO0UA95uxsLtISVSpNk-TVI94Evk/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/beetle-juice-best-costumes-1539031186.jpg?width=400&height=600"
    },
    {
      "title" : "Tiana, Prince Naveen and Dr. Facilier Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/lwsFT7kFtOVKCrrNPMJLR6GZXytoQx5S3ckWLflmTQk/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/frog-princess-best-costumes-1539031187.jpg?width=400&height=600"
    },
    {
      "title" : "Edward Scissorhands Halloween Costume",
      "image" : "https://images-ext-1.discordapp.net/external/TIvWaCtiWhSmPV_9ddZocDIFY0vXL7DiDlxDUNLV78U/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/edward-scissorhands-1539031193.jpg?width=400&height=600"
    },
    {
      "title" : "Zoltar Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/OfasUAfEOEB7oExVW7xPQrefbvfweoIyeogUtP8C_Bc/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/zoltar-dog-best-costumes-1539031193.jpg?width=400&height=600"
    },
    {
      "title" : "Diva Plavalaguna Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/PFkVEhFn81eOBErYwafYvtkUE5qdBhR30_62AzNiAv8/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/fifth-element-best-costumes-1539031186.jpg?width=400&height=600"
    },
    {
      "title" : "Thriller Werewolf Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/XSz2I83dPlbC78XnLxrNPw-j8IvYU1YgeLn4NH10-_U/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/thriller-werewolf-best-costumes-1539031191.jpg?width=400&height=600"
    },
    {
      "title" : "She-Ra Halloween Costume",
      "image" : "https://images-ext-2.discordapp.net/external/bmEGgiO68Crm2eHNkea38VT7qVBYSrzC18JPpF_O0BA/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/shera-best-costumes-1539031189.jpg?width=400&height=600"
    },
    {
      "title" : "Rorschach Halloween Costume",
      "image" : "https://images-ext-1.discordapp.net/external/B-z7wuc1qvvjii445m1aKHkFfNgFr6q-hpyTg9j236A/https/hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/watchmen-best-costumes-1539031193.jpg?width=400&height=600"
    }
  ]
  return random.choice(costume_list)

@bot.command(name='dress_me_up', help='Sends some great halloween costume ideas')
async def costume_embed(ctx):
    costume = random_costume()
    embed=discord.Embed(title=costume["title"], color=discord.Color.blue())
    embed.set_image(url=costume["image"])
    await ctx.send(embed=embed)

def random_candy():
  candy_list = ["https://www.maxpixel.net/static/photo/1x/Sweetie-Food-Sweet-Sweets-Candy-Sugar-Goody-146690.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdf7IwduZtUnM0fVy2h-f36bnMCSfGqFI62g&usqp=CAU", "https://lh3.googleusercontent.com/proxy/A3OFrDpF1hyxETOkgU7OHX28m01ctOP_KhHIK5uLgTFVltSpOipTIGx3LMh8Ev1OitxuSY2d4SPusl2ULxZ7baPvFi9AtYg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNe81pIaQdUsVNsb8VoNO42-BpZGalVQaNKg&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnzVL7zq9wwqOzx4kmM1iaACofPDLfWgwdDw&usqp=CAU", "https://lh3.googleusercontent.com/proxy/3Q-gAH4BFYRZ6HoPpDF9bch5Ibn-d_kdhzw8daqJ9w8aI3uZwpE9UtNWx9LKgj8uJw_CmZlUwTnh5CkLW40siqV8BA_sMgg", "https://lh3.googleusercontent.com/proxy/LapvjybLihG_5AqAGFNRhwbX-aoAGMXB3URwMTsLgIvo962MXtFvT5uzCNBjvK0CCvEDQS6WbFf55O2g5HNpkNSLCQ3Y9MLYSki8S8OWxzgalObOsH0-SimaXArA0FtgdHttYGden74FCroCOJg_zsPpOPn9tVnfm6pB", "https://thumbs.dreamstime.com/b/lollipop-clip-art-cartoon-illustration-sweet-32871223.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQRulOgisX1e9JxBMjqAUFQdRgLkyCyG4tgQ&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ36lQKDUv_2L0oq5EhnbHu-ayqfAFnMTaqKg&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoo1OiyXu4IqEmLtpcofPERQ0sD7a_G7lA0g&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQsPOy-cJah_2jzOkhP2fkGi4APCScCtgW5Q&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXwHMksrM67S33Dlbg9Z528xjUFTSaJwWdk57R-PrtXncEKiSLZ1j3VeCXbjmgDQWrcqQ&usqp=CAU", "https://www.nicepng.com/png/detail/7-70728_dessert-clipart-gelato-sweet-food-clip-art.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9BfZwsFDE8Weqx_lsd4Hvnvdm9cPnbLNGmQ&usqp=CAU", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu5YIEMnaxKsXxYzqhlwklhyWg9bl3TDlOZA&usqp=CAU", "https://livelighter.com.au/content/menu-app/static/mexican.jpg", "https://thumbs.dreamstime.com/b/cake-dessert-plate-spoon-illustration-clipart-cake-dessert-plate-spoon-vector-illustration-clipart-isolated-white-167808314.jpg", "https://www.pngitem.com/pimgs/m/154-1543329_transparent-pastries-clipart-pastry-clip-art-hd-png.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDgOyNlHuWIYYTsTK8QgGBkYhoCJRA-1ta-A&usqp=CAU"]
  return random.choice(candy_list)

def random_trick():
  trick_list = ["You froze gummy eyeballs in ice cubes, then added them to pumpkin head's drink.", "You bought cheap hair extensions the same color as pumpkin head’s hair and scattered them around its pillow at night."]
  return random.choice(trick_list)

@bot.command(name='trick_or_treat', help='Play trick or treat with Pumpkin Head')
async def trick_or_treat_embed(ctx):
    choice = random.choice(["trick","treat", "treat", "treat"])
    if choice == "treat":
      candy = random_candy()
      embed=discord.Embed(title="Here's a treat for you!", color=discord.Color.purple())
      embed.set_image(url=candy)
    else:
      trick = random_trick()
      embed=discord.Embed(title="You tricked ME!", description=trick, color=discord.Color.purple())
    await ctx.send(embed=embed)

bot.run(TOKEN)