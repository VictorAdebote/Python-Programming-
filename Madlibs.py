'''
It was_(Food)_ day at school, and_(Name)_was super _(Adjective)_ for Lunch.
But when he was about to go into the cafeteria to eat a _(Animal)_ came and stole his_(Food)_._(Name)_was_(Adjective)_.
But he had great friends and the gave some other food to him.
'''

Name = input('Input your name: \n')
print()
Food = input('Input the name of the food: \n')
print()
Animal = input('Input the name of the animal: \n')
Adjective = input('Input one of these adjectives: happy, sad , exited, amazed: \n')

print(f'''
It was {Food} day at school, and {Name} was super {Adjective} for Lunch.
But when he was about to go into the cafeteria to eat, a {Animal} came and stole his {Food}. {Name} was {Adjective}.
But he had great friends and they gave some of their food to him.
''')