from app.db.database import db
from app.seed.utils import insert_nodes

from app.data.companies import companies
from app.data.locations import locations
from app.data.skills import skills
from app.data.people import people
from app.data.relationships import works_at, has_skill, knows
# --------------------------------------------------
# Cypher Queries
# --------------------------------------------------

company_query = """
MERGE (c:Company {id: $id})
SET
    c.name = $name,
    c.industry = $industry
"""

location_query = """
MERGE (l:Location {id: $id})
SET
    l.city = $city,
    l.country = $country
"""

skill_query = """
MERGE (s:Skill {id: $id})
SET
    s.name = $name,
    s.category = $category
"""
person_query = """
MERGE (p:Person {id: $id})
SET
    p.name = $name,
    p.email = $email,
    p.title = $title,
    p.experience = $experience,
    p.bio = $bio
"""
works_at_query = """
MATCH (p:Person {id:$person_id})
MATCH (c:Company {id:$company_id})

MERGE (p)-[:WORKS_AT]->(c)
"""

has_skill_query = """
MATCH (p:Person {id:$person_id})
MATCH (s:Skill {id:$skill_id})

MERGE (p)-[:HAS_SKILL]->(s)
"""
knows_query = """
MATCH (p1:Person {id:$person_id})
MATCH (p2:Person {id:$friend_id})

MERGE (p1)-[:KNOWS]->(p2)
"""

company_location_query = """
MATCH (c:Company {id: $company_id})
MATCH (l:Location {id: $location_id})

MERGE (c)-[:LOCATED_IN]->(l)
"""


# --------------------------------------------------
# Relationships
# --------------------------------------------------

company_locations = [
    {"company_id": 1, "location_id": 2},   # Google -> Bangalore
    {"company_id": 2, "location_id": 1},   # Microsoft -> Hyderabad
    {"company_id": 3, "location_id": 3},   # Amazon -> Pune
    {"company_id": 4, "location_id": 1},   # OpenAI -> Hyderabad
    {"company_id": 5, "location_id": 2},   # Meta -> Bangalore
    {"company_id": 6, "location_id": 5},   # Netflix -> Mumbai
    {"company_id": 7, "location_id": 4},   # Tesla -> Chennai
    {"company_id": 8, "location_id": 1},   # Infosys -> Hyderabad
    {"company_id": 9, "location_id": 3},   # TCS -> Pune
    {"company_id": 10, "location_id": 2},  # Accenture -> Bangalore
]


# --------------------------------------------------
# Seed Function
# --------------------------------------------------

def seed():

    print("\nSeeding database...\n")

    # Insert Nodes
    insert_nodes(companies, company_query, "Companies")
    insert_nodes(locations, location_query, "Locations")
    insert_nodes(skills, skill_query, "Skills")
    insert_nodes(people, person_query, "People")

    # Create Relationships
    insert_nodes(
        company_locations,
        company_location_query,
        "Company Locations"
    )
    insert_nodes(
    works_at,
    works_at_query,
    "Works At Relationships"
    )
    insert_nodes(
    has_skill,
    has_skill_query,
    "Person Skills"
    )
    insert_nodes(
    knows,
    knows_query,
    "Knows Relationships"
    )
    
    print("\nDatabase seeded successfully!\n")

    db.close()


if __name__ == "__main__":
    seed()