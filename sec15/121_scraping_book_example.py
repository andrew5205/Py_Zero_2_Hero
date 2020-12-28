
# basic steps
# 1. import requests, bs4 
# 2. make requests.get() - result = requests.get("URL")
# 3. make soup object - soup = bs4.BeautifulSoup(result.text, "lxml")
# 4. getText between tags - soup.select("TAG")[0].getText()


# wwww.toscrape.com
# https://books.toscrape.com/



# Goal: get all title of every book with a 2 star rating

import requests
import bs4


# base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
# # page_num = 12
# # print(base_url.format(page_num))


# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# soup.select('.product_pod')

# print(soup.select('.product_pod'))              
# print(len(soup.select('.product_pod')))         # 20

# product = soup.select('.product_pod')

# example = product[0]
# print(example)

# # approach 1
# # make it string 
# str(example)
# print('star-rating Three' in str(example))


# # approach 2
# # TIP: select call for class, the space in the class has to replace in "."
# example.select('.star-rating.Three')
# print(example.select('.star-rating.Three'))
                                            # [<p class="star-rating Three">
                                            # <i class="icon-star"></i>
                                            # <i class="icon-star"></i>
                                            # <i class="icon-star"></i>
                                            # <i class="icon-star"></i>
                                            # <i class="icon-star"></i>
                                            # </p>]

# example.select('a')
# print(example.select('a'))
                            # [<a href="a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>, 
                            #  <a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>]

# print(example.select('a')[1]['title'])          # A Light in the Attic
# ****************************************************************************************************************************************************************************************************************

# if __name__ == "__main__":


import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        # if 'star-rating Two' in str(book):
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

# print(two_star_titles)
# 'Starving Hearts (Triangular Trade Trilogy, #1)', 'Libertarianism for Beginners', "It's Only the Himalayas", 'How Music Works', 'Maude (1883-1993):She Grew Up with the country', "You can't bury them all: Poems", 'Reasons to Stay Alive', 'Without Borders (Wanderlove #1)', 'Soul Reader', 'Security', 'Saga, Volume 5 (Saga (Collected Editions) #5)', 'Reskilling America: Learning to Labor in the Twenty-First Century', 'Political Suicide: Missteps, Peccadilloes, Bad Calls, Backroom Hijinx, Sordid Pasts, Rotten Breaks, and Just Plain Dumb Mistakes in the Annals of American Politics', 'Obsidian (Lux #1)', 'My Paris Kitchen: Recipes and Stories', 'Masks and Shadows', 'Lumberjanes, Vol. 2: Friendship to the Max (Lumberjanes #5-8)', 'Lumberjanes Vol. 3: A Terrible Plan (Lumberjanes #9-12)', 'Judo: Seven Steps to Black Belt (an Introductory Guide for Beginners)', 'I Hate Fairyland, Vol. 1: Madly Ever After (I Hate Fairyland (Compilations) #1-5)', 'Giant Days, Vol. 2 (Giant Days #5-8)', 'Everydata: The Misinformation Hidden in the Little Data You Consume Every Day', "Don't Be a Jerk: And Other Practical Advice from Dogen, Japan's Greatest Zen Master", 'Bossypants', 'Bitch Planet, Vol. 1: Extraordinary Machine (Bitch Planet (Collected Editions))', 'Avatar: The Last Airbender: Smoke and Shadow, Part 3 (Smoke and Shadow #3)', 'Tuesday Nights in 1980', 'The Psychopath Test: A Journey Through the Madness Industry', 'The Power of Now: A Guide to Spiritual Enlightenment', "The Omnivore's Dilemma: A Natural History of Four Meals", 'The Love and Lemons Cookbook: An Apple-to-Zucchini Celebration of Impromptu Cooking', 'The Girl on the Train', 'The Emerald Mystery', 'The Argonauts', 'Suddenly in Love (Lake Haven #1)', 'Soft Apocalypse', "So You've Been Publicly Shamed", 'Shoe Dog: A Memoir by the Creator of NIKE', 'Louisa: The Extraordinary Life of Mrs. Adams', 'Large Print Heart of the Pride', 'Grumbles', 'Chasing Heaven: What Dying Taught Me About Living', 'Becoming Wise: An Inquiry into the Mystery and Art of Living', 'Beauty Restored (Riley Family Legacy Novellas #3)', 'Batman: The Long Halloween (Batman)', "Ayumi's Violin", 'Wild Swans', "What's It Like in Space?: Stories from Astronauts Who've Been There", 'Until Friday Night (The Field Party #1)', 'Unbroken: A World War II Story of Survival, Resilience, and Redemption', 'Twenty Yawns', 'Through the Woods', 'This Is Where It Ends', 'The Year of Magical Thinking', 'The Last Mile (Amos Decker #2)', 'The Immortal Life of Henrietta Lacks', 'The Hidden Oracle (The Trials of Apollo #1)', 'The Guilty (Will Robie #4)', 'Red Hood/Arsenal, Vol. 1: Open for Business (Red Hood/Arsenal #1)', 'Once Was a Time', 'No Dream Is Too High: Life Lessons From a Man Who Walked on the Moon', 'Naruto (3-in-1 Edition), Vol. 14: Includes Vols. 40, 41 & 42 (Naruto: Omnibus #14)', 'More Than Music (Chasing the Dream #1)', 'Lowriders to the Center of the Earth (Lowriders in Space #2)', 'Eat Fat, Get Thin', 'Doctor Sleep (The Shining #2)', 'Crazy Love: Overwhelmed by a Relentless God', 'Carrie', 'Batman: Europa', 'Angels Walking (Angels Walking #1)', 'Adulthood Is a Myth: A "Sarah\'s Scribbles" Collection', 'A Study in Scarlet (Sherlock Holmes #1)', 'A Series of Catastrophes and Miracles: A True Story of Love, Science, and Cancer', "A People's History of the United States", 'My Kitchen Year: 136 Recipes That Saved My Life', 'The Lonely City: Adventures in the Art of Being Alone', 'The Dinner Party', 'Stars Above (The Lunar Chronicles #4.5)', 'Love, Lies and Spies', 'Troublemaker: Surviving Hollywood and Scientology', 'The Widow', 'Setting the World on Fire: The Brief, Astonishing Life of St. Catherine of Siena', 'Mothering Sunday', 'Lilac Girls', '10% Happier: How I Tamed the Voice in My Head, Reduced Stress Without Losing My Edge, and Found Self-Help That Actually Works', 'Underlying Notes', 'The Flowers Lied', 'Modern Day Fables', "Chernobyl 01:23:40: The Incredible True Story of the World's Worst Nuclear Disaster", '23 Degrees South: A Tropical Tale of Changing Whether...', 'When Breath Becomes Air', 'Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel', 'The Martian (The Martian #1)', "Miller's Valley", "Love That Boy: What Two Presidents, Eight Road Trips, and My Son Taught Me About a Parent's Expectations", 'Left Behind (Left Behind #1)', 'Howl and Other Poems', "Heaven is for Real: A Little Boy's Astounding Story of His Trip to Heaven and Back", "Brazen: The Courage to Find the You That's Been Hiding", '32 Yolks', 'Wildlife of New York: A Five-Borough Coloring Book', 'Unreasonable Hope: Finding Faith in the God Who Brings Purpose to Your Pain', 'The Art Book', 'Steal Like an Artist: 10 Things Nobody Told You About Being Creative', 'Raymie Nightingale', 'Like Never Before (Walker Family #2)', 'How to Be a Domestic Goddess: Baking and the Art of Comfort Cooking', 'Finding God in the Ruins: How God Redeems Pain', 'Chronicles, Vol. 1', 'A Summer In Europe', 'The Rise and Fall of the Third Reich: A History of Nazi Germany', 'The Makings of a Fatherless Child', 'The Fellowship of the Ring (The Lord of the Rings #1)', "Tell the Wolves I'm Home", 'In the Woods (Dublin Murder Squad #1)', 'Give It Back', 'Why Save the Bankers?: And Other Essays on Our Economic and Political Crisis', 'The Raven King (The Raven Cycle #4)', 'The Expatriates', 'The 5th Wave (The 5th Wave #1)', 'Peak: Secrets from the New Science of Expertise', 'Logan Kade (Fallen Crest High #5.5)', "I Know Why the Caged Bird Sings (Maya Angelou's Autobiography #1)", 'Drama', "America's War for the Greater Middle East: A Military History", 'A Game of Thrones (A Song of Ice and Fire #1)', "The Pilgrim's Progress", 'The Hound of the Baskervilles (Sherlock Holmes #5)', "The Geography of Bliss: One Grump's Search for the Happiest Places in the World", 'The Demonists (Demonist #1)', 'The Demon Prince of Momochi House, Vol. 4 (The Demon Prince of Momochi House #4)', 'Misery', 'Far From True (Promise Falls Trilogy #2)', 'Confessions of a Shopaholic (Shopaholic #1)', 'Vegan Vegetarian Omnivore: Dinner for Everyone at the Table', 'Two Boys Kissing', 'Twilight (Twilight #1)', 'Twenties Girl', 'The Tipping Point: How Little Things Can Make a Big Difference', 'The Stand', 'The Picture of Dorian Gray', 'The Name of God is Mercy', "The Lover's Dictionary", 'The Last Painting of Sara de Vos', 'The Guns of August', 'The Girl Who Played with Fire (Millennium Trilogy #2)', 'The Da Vinci Code (Robert Langdon #2)', 'The Cat in the Hat (Beginner Books B-1)', 'The Book Thief', 'The Autobiography of Malcolm X', "Surely You're Joking, Mr. Feynman!: Adventures of a Curious Character", 'Soldier (Talon #3)', 'Shopaholic & Baby (Shopaholic #5)', 'Seven Days in the Art World', 'Rework', 'Packing for Mars: The Curious Science of Life in the Void', 'Orange Is the New Black', 'One for the Money (Stephanie Plum #1)', 'Midnight Riot (Peter Grant/ Rivers of London - books #1)', 'Me Talk Pretty One Day', 'Manuscript Found in Accra', 'Lust & Wonder', "Life, the Universe and Everything (Hitchhiker's Guide to the Galaxy #3)", 'Life After Life', 'I Am Malala: The Girl Who Stood Up for Education and Was Shot by the Taliban', 'House of Lost Worlds: Dinosaurs, Dynasties, and the Story of Life on Earth', 'Horrible Bear!', 'Holidays on Ice', 'Girl in the Blue Coat', 'Fruits Basket, Vol. 3 (Fruits Basket #3)', 'Cosmos', 'Civilization and Its Discontents', "Catastrophic Happiness: Finding Joy in Childhood's Messy Years", 'Career of Evil (Cormoran Strike #3)', 'Born to Run: A Hidden Tribe, Superathletes, and the Greatest Race the World Has Never Seen', "Best of My Love (Fool's Gold #20)", 'Beowulf', 'Awkward', 'And Then There Were None', 'A Storm of Swords (A Song of Ice and Fire #3)', 'The Suffragettes (Little Black Classics, #96)', 'Vampire Girl (Vampire Girl #1)', 'Three Wishes (River of Time: California #1)', 'The Wicked + The Divine, Vol. 1: The Faust Act (The Wicked + The Divine)', 'The Little Prince', 'The Last Girl (The Dominion Trilogy #1)', 'Taking Shots (Assassins #1)', 'Settling the Score (The Summer Games #1)', 'Rhythm, Chord & Malykhin', 'One Second (Seven #7)', "Old Records Never Die: One Man's Quest for His Vinyl and His Past", 'Of Mice and Men', 'My Perfect Mistake (Over the Top #1)', 'Meditations', 'Frankenstein', 'Emma']


for item in two_star_titles:
    print(item)
    

                                # Starving Hearts (Triangular Trade Trilogy, #1)
                                # Libertarianism for Beginners
                                # It's Only the Himalayas
                                # How Music Works
                                # Maude (1883-1993):She Grew Up with the country
                                # You can't bury them all: Poems
                                # Reasons to Stay Alive
                                # Without Borders (Wanderlove #1)
                                # Soul Reader
                                # Security
                                # Saga, Volume 5 (Saga (Collected Editions) #5)
                                # Reskilling America: Learning to Labor in the Twenty-First Century
                                # Political Suicide: Missteps, Peccadilloes, Bad Calls, Backroom Hijinx, Sordid Pasts, Rotten Breaks, and Just Plain Dumb Mistakes in the Annals of American Politics
                                # Obsidian (Lux #1)
                                # My Paris Kitchen: Recipes and Stories
                                # Masks and Shadows
                                # Lumberjanes, Vol. 2: Friendship to the Max (Lumberjanes #5-8)
                                # Lumberjanes Vol. 3: A Terrible Plan (Lumberjanes #9-12)
                                # Judo: Seven Steps to Black Belt (an Introductory Guide for Beginners)
                                # I Hate Fairyland, Vol. 1: Madly Ever After (I Hate Fairyland (Compilations) #1-5)
                                # Giant Days, Vol. 2 (Giant Days #5-8)
                                # Everydata: The Misinformation Hidden in the Little Data You Consume Every Day
                                # Don't Be a Jerk: And Other Practical Advice from Dogen, Japan's Greatest Zen Master
                                # Bossypants
                                # Bitch Planet, Vol. 1: Extraordinary Machine (Bitch Planet (Collected Editions))
                                # Avatar: The Last Airbender: Smoke and Shadow, Part 3 (Smoke and Shadow #3)
                                # Tuesday Nights in 1980
                                # The Psychopath Test: A Journey Through the Madness Industry
                                # The Power of Now: A Guide to Spiritual Enlightenment
                                # The Omnivore's Dilemma: A Natural History of Four Meals
                                # The Love and Lemons Cookbook: An Apple-to-Zucchini Celebration of Impromptu Cooking
                                # The Girl on the Train
                                # The Emerald Mystery
                                # The Argonauts
                                # Suddenly in Love (Lake Haven #1)
                                # Soft Apocalypse
                                # So You've Been Publicly Shamed
                                # Shoe Dog: A Memoir by the Creator of NIKE
                                # Louisa: The Extraordinary Life of Mrs. Adams
                                # Large Print Heart of the Pride
                                # Grumbles
                                # Chasing Heaven: What Dying Taught Me About Living
                                # Becoming Wise: An Inquiry into the Mystery and Art of Living
                                # Beauty Restored (Riley Family Legacy Novellas #3)
                                # Batman: The Long Halloween (Batman)
                                # Ayumi's Violin
                                # Wild Swans
                                # What's It Like in Space?: Stories from Astronauts Who've Been There
                                # Until Friday Night (The Field Party #1)
                                # Unbroken: A World War II Story of Survival, Resilience, and Redemption
                                # Twenty Yawns
                                # Through the Woods
                                # This Is Where It Ends
                                # The Year of Magical Thinking
                                # The Last Mile (Amos Decker #2)
                                # The Immortal Life of Henrietta Lacks
                                # The Hidden Oracle (The Trials of Apollo #1)
                                # The Guilty (Will Robie #4)
                                # Red Hood/Arsenal, Vol. 1: Open for Business (Red Hood/Arsenal #1)
                                # Once Was a Time
                                # No Dream Is Too High: Life Lessons From a Man Who Walked on the Moon
                                # Naruto (3-in-1 Edition), Vol. 14: Includes Vols. 40, 41 & 42 (Naruto: Omnibus #14)
                                # More Than Music (Chasing the Dream #1)
                                # Lowriders to the Center of the Earth (Lowriders in Space #2)
                                # Eat Fat, Get Thin
                                # Doctor Sleep (The Shining #2)
                                # Crazy Love: Overwhelmed by a Relentless God
                                # Carrie
                                # Batman: Europa
                                # Angels Walking (Angels Walking #1)
                                # Adulthood Is a Myth: A "Sarah's Scribbles" Collection
                                # A Study in Scarlet (Sherlock Holmes #1)
                                # A Series of Catastrophes and Miracles: A True Story of Love, Science, and Cancer
                                # A People's History of the United States
                                # My Kitchen Year: 136 Recipes That Saved My Life
                                # The Lonely City: Adventures in the Art of Being Alone
                                # The Dinner Party
                                # Stars Above (The Lunar Chronicles #4.5)
                                # Love, Lies and Spies
                                # Troublemaker: Surviving Hollywood and Scientology
                                # The Widow
                                # Setting the World on Fire: The Brief, Astonishing Life of St. Catherine of Siena
                                # Mothering Sunday
                                # Lilac Girls
                                # 10% Happier: How I Tamed the Voice in My Head, Reduced Stress Without Losing My Edge, and Found Self-Help That Actually Works
                                # Underlying Notes
                                # The Flowers Lied
                                # Modern Day Fables
                                # Chernobyl 01:23:40: The Incredible True Story of the World's Worst Nuclear Disaster
                                # 23 Degrees South: A Tropical Tale of Changing Whether...
                                # When Breath Becomes Air
                                # Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel
                                # The Martian (The Martian #1)
                                # Miller's Valley
                                # Love That Boy: What Two Presidents, Eight Road Trips, and My Son Taught Me About a Parent's Expectations
                                # Left Behind (Left Behind #1)
                                # Howl and Other Poems
                                # Heaven is for Real: A Little Boy's Astounding Story of His Trip to Heaven and Back
                                # Brazen: The Courage to Find the You That's Been Hiding
                                # 32 Yolks
                                # Wildlife of New York: A Five-Borough Coloring Book
                                # Unreasonable Hope: Finding Faith in the God Who Brings Purpose to Your Pain
                                # The Art Book
                                # Steal Like an Artist: 10 Things Nobody Told You About Being Creative
                                # Raymie Nightingale
                                # Like Never Before (Walker Family #2)
                                # How to Be a Domestic Goddess: Baking and the Art of Comfort Cooking
                                # Finding God in the Ruins: How God Redeems Pain
                                # Chronicles, Vol. 1
                                # A Summer In Europe
                                # The Rise and Fall of the Third Reich: A History of Nazi Germany
                                # The Makings of a Fatherless Child
                                # The Fellowship of the Ring (The Lord of the Rings #1)
                                # Tell the Wolves I'm Home
                                # In the Woods (Dublin Murder Squad #1)
                                # Give It Back
                                # Why Save the Bankers?: And Other Essays on Our Economic and Political Crisis
                                # The Raven King (The Raven Cycle #4)
                                # The Expatriates
                                # The 5th Wave (The 5th Wave #1)
                                # Peak: Secrets from the New Science of Expertise
                                # Logan Kade (Fallen Crest High #5.5)
                                # I Know Why the Caged Bird Sings (Maya Angelou's Autobiography #1)
                                # Drama
                                # America's War for the Greater Middle East: A Military History
                                # A Game of Thrones (A Song of Ice and Fire #1)
                                # The Pilgrim's Progress
                                # The Hound of the Baskervilles (Sherlock Holmes #5)
                                # The Geography of Bliss: One Grump's Search for the Happiest Places in the World
                                # The Demonists (Demonist #1)
                                # The Demon Prince of Momochi House, Vol. 4 (The Demon Prince of Momochi House #4)
                                # Misery
                                # Far From True (Promise Falls Trilogy #2)
                                # Confessions of a Shopaholic (Shopaholic #1)
                                # Vegan Vegetarian Omnivore: Dinner for Everyone at the Table
                                # Two Boys Kissing
                                # Twilight (Twilight #1)
                                # Twenties Girl
                                # The Tipping Point: How Little Things Can Make a Big Difference
                                # The Stand
                                # The Picture of Dorian Gray
                                # The Name of God is Mercy
                                # The Lover's Dictionary
                                # The Last Painting of Sara de Vos
                                # The Guns of August
                                # The Girl Who Played with Fire (Millennium Trilogy #2)
                                # The Da Vinci Code (Robert Langdon #2)
                                # The Cat in the Hat (Beginner Books B-1)
                                # The Book Thief
                                # The Autobiography of Malcolm X
                                # Surely You're Joking, Mr. Feynman!: Adventures of a Curious Character
                                # Soldier (Talon #3)
                                # Shopaholic & Baby (Shopaholic #5)
                                # Seven Days in the Art World
                                # Rework
                                # Packing for Mars: The Curious Science of Life in the Void
                                # Orange Is the New Black
                                # One for the Money (Stephanie Plum #1)
                                # Midnight Riot (Peter Grant/ Rivers of London - books #1)
                                # Me Talk Pretty One Day
                                # Manuscript Found in Accra
                                # Lust & Wonder
                                # Life, the Universe and Everything (Hitchhiker's Guide to the Galaxy #3)
                                # Life After Life
                                # I Am Malala: The Girl Who Stood Up for Education and Was Shot by the Taliban
                                # House of Lost Worlds: Dinosaurs, Dynasties, and the Story of Life on Earth
                                # Horrible Bear!
                                # Holidays on Ice
                                # Girl in the Blue Coat
                                # Fruits Basket, Vol. 3 (Fruits Basket #3)
                                # Cosmos
                                # Civilization and Its Discontents
                                # Catastrophic Happiness: Finding Joy in Childhood's Messy Years
                                # Career of Evil (Cormoran Strike #3)
                                # Born to Run: A Hidden Tribe, Superathletes, and the Greatest Race the World Has Never Seen
                                # Best of My Love (Fool's Gold #20)
                                # Beowulf
                                # Awkward
                                # And Then There Were None
                                # A Storm of Swords (A Song of Ice and Fire #3)
                                # The Suffragettes (Little Black Classics, #96)
                                # Vampire Girl (Vampire Girl #1)
                                # Three Wishes (River of Time: California #1)
                                # The Wicked + The Divine, Vol. 1: The Faust Act (The Wicked + The Divine)
                                # The Little Prince
                                # The Last Girl (The Dominion Trilogy #1)
                                # Taking Shots (Assassins #1)
                                # Settling the Score (The Summer Games #1)
                                # Rhythm, Chord & Malykhin
                                # One Second (Seven #7)
                                # Old Records Never Die: One Man's Quest for His Vinyl and His Past
                                # Of Mice and Men
                                # My Perfect Mistake (Over the Top #1)
                                # Meditations
                                # Frankenstein
                                # Emma
