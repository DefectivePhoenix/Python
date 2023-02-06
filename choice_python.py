import random

location = ["Grand Canyon",
            "Las Vegas",
            "Devil's Tower",
            "Alamo",
            "Gettysburg"]

month = ["March",
         "April",
         "May",
         "June",
         "July"]

random_location = random.choice(location)
random_month = random.choice(month)

print(f"Our next Trip is to {random_location} in {random_month}")
