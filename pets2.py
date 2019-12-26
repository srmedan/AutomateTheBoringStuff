def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

#adding keyword arguments
describe_pet(pet_name='Rex', animal_type='dog')
describe_pet(pet_name='Willie')
