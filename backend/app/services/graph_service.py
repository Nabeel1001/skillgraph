from app.db.database import db


class GraphService:

    @staticmethod
    def get_all_people():

        query = """
        MATCH (p:Person)
        RETURN
            p.id AS id,
            p.name AS name,
            p.title AS title,
            p.email AS email
        ORDER BY p.name
        """

        return db.execute_query(query)
    
    @staticmethod
    def get_person_profile(person_id: int):

        query = """
        MATCH (p:Person {id:$id})

        OPTIONAL MATCH (p)-[:WORKS_AT]->(c:Company)

        OPTIONAL MATCH (p)-[:HAS_SKILL]->(s:Skill)

        OPTIONAL MATCH (p)-[:KNOWS]->(k:Person)

        RETURN
            p.id AS id,
            p.name AS name,
            p.title AS title,
            c.name AS company,
            collect(DISTINCT s.name) AS skills,
            collect(DISTINCT k.name) AS connections
        """

        result = db.execute_query(query, {"id": person_id})

        return result[0] if result else {}