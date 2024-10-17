"""
Day 3: The Ultimate Wacky Recipe Maker
---------------------------------
We have learned enough skills for a simple, but cool, project!

Remember when you were a kid and thought the ideal dinner would just be all your favorite things mixed in a bowl? How did that Nutella Mac & Cheese taste? Well - let's come up with a recipe generator to build us an amazing dish for today's evening meal!

You will need to:

1. Create these as a variable:
A type of food
A type of plant
A method of cooking
A word to describe burned food
A household item


2. Output a nice looking Recipe page that *concatenates* a dish in this format:
cooking food with burned plant on a bed of item
    """
foodType=input("What type of food do you like? ")
plantType=input("Which plant do you like? ")
cookingMethod=input("How do you like to cook? ")
burnedFood=input("What word describes burned food? ")
householdItem=input("Name a household item: ")

print(cookingMethod, foodType, "with", burnedFood, plantType, householdItem,)