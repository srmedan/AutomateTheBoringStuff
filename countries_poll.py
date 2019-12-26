responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("\nWhat country would you like to visit one day? ")

    responses[name] = response
    print(responses)