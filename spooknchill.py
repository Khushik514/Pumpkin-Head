import random

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