import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samuel L. Jackson",
          "Joakino",
          "Maxwell"]

random_bar = random.choice(bars)
random_person_A = random.choice(people)
random_person_B = random.choice(people)

print(f"How about you go to {random_bar} with {random_person_A} and {random_person_B}?")
