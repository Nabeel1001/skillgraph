import random

works_at = []
has_skill = []
knows = []

for person_id in range(1, 51):
    skill_ids = random.sample(range(1, 21), random.randint(3, 6))

    for skill_id in skill_ids:
        has_skill.append({
            "person_id": person_id,
            "skill_id": skill_id
        })
        
    works_at.append({
        "person_id": person_id,
        "company_id": random.randint(1, 10)
    })
    
    connections = random.sample(
        [i for i in range(1, 51) if i != person_id],
        random.randint(2, 5)
    )
    
    for friend_id in connections:
        knows.append({
            "person_id": person_id,
            "friend_id": friend_id
        })
    