import random

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