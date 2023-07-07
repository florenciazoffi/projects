# Madlibs generator by Florencia Zoffi
# All texts were written by Beatriz Aseff

import random

noun1 = input('Please provide a noun: ')
noun2 = input('Please provide a second noun: ')
noun3 = input('Please provide a third noun: ')
noun4 = input('Please provide a fourth and last noun: ')

verb1 = input('Please provide a verb: ')
verb2 = input('Please provide a second verb: ')
verb3 = input('Please provide a third verb: ')
verb4 = input('Please provide a fourth and last verb: ')

adjective1 = input('Please provide an adjective: ')
adjective2 = input('Please provide a second adjective: ')
adjective3 = input('Please provide a third adjective: ')


madlibs = {
    1: f'\tMy friend’s name is {noun1}. She’s a {adjective1}, hard-working waitress at the small coffee shop around the corner called {noun2}. Today, she woke up agitated because her alarm didn’t go off. She was late for {verb1} before work! Upset, she went up to her mirror to look at herself and surprised, she said: “I am {adjective2}!”\nShe called her best friend to tell her what she saw and her friend, who misunderstood her, asked: “You’re {adjective3} today?”.\nStressed out, she explained and then hung up.\n“Okay,” she said to herself, “right now I have to {verb2} my {noun3}."\nShe combed her hair and rushed to work, as {noun1} was already late for {verb1}.\nShe passed her mom while rushing through the living room.\n“Sweetie,” her mom said, “will you {verb3} your grandmother before you go?”\n“I can’t {verb3} Grandma, mom. I’m already late!”\n“Okay then. Take {noun4}’s car if you want to.”\n“Yes, thanks! I’ll see you later and we’ll {verb4} the usual!"',
    2: f'\tOnce upon a time, inside a {noun1} far, far away, lived a very {adjective1} {noun2} who loved two things: to {verb1} and {verb2}. Every day, without an exception, this silly {noun2} would {verb2} around, making everyone laugh with their {adjective2} talent.\nOne day, the silly {noun2} decided to {verb3} themselves to go visit a {noun3} for a very {adjective3} adventure. Together with {noun3}, they planned to {verb1} through the forest, making sure to {verb4} as they skipped and danced before reaching their destination.\n As they reached their destination, {noun2} and {noun3} couldn´t contain their excitement. They decided to {verb4} up and down in the {noun4}, shouting with joy, before they had to return home. They had a lot of fun, creating a very {adjective3} adventure and an unforgettable memory.',
    3: f'\tRecently, I went to a {noun1} convention, and, to be honest, it was incredible! When I got there, people somehow only wanted to {verb1} and {verb2} all over the place. It was strange, but the atmosphere was buzzing with excitement and a very fascinating {adjective1} anticipation.\nDuring one of the conferences, they told us the instructions for a game called "Pass the {noun2}." It sounded easy enough, but once there, I had some difficulty. The goal was to {verb3} the {noun2} as quickly as possible without dropping it before you passed it. Many misunderstood that they had to {verb1}, so you can imagine the {adjective2} fun it brought!\nThe highlight of the {adjective3} event was the {noun3}-off competition. Participants had to {verb4} their way to the finish line while carrying a giant inflatable {noun3}. I was a contestant for that 5 times! People made sure to {verb1} and {verb2} with all their might, while also trying to stay balanced and not get tangled in the {noun4} mess that the earlier convention had left.\nThe grand finale was a talent show where participants showcased their unique skills. The laughter was contagious, and even the judges couldn´t help but {verb4}.\nAll in all, it was an unforgettable experience. I left the convention with sore cheeks from all the {verb2} and {verb1}. Who knew that a simple gathering of {noun1} could be so fun!'
}

num = random.randint(1, 3) # chooses one of the madlibs
print(madlibs[num])
