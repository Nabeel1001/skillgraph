from faker import Faker
import random
from pprint import pformat

fake = Faker("en_IN")

JOB_TITLES = [
    "Software Engineer",
    "Senior Software Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Developer",
    "AI Engineer",
    "Machine Learning Engineer",
    "DevOps Engineer",
    "Cloud Engineer",
    "Data Engineer",
]

people = []

for i in range(1, 21):
    people.append({
        "id": i,
        "name": fake.name(),
        "email": fake.unique.email(),
        "title": random.choice(JOB_TITLES),
        "experience": random.randint(1, 12),
        "bio": fake.sentence(nb_words=12)
    })

# Save to people.py
with open("app/data/people.py", "w", encoding="utf-8") as f:
    f.write("people = ")
    f.write(pformat(people, indent=4))

print("✅ Generated 50 people and saved to app/data/people.py")