from app.db.database import db


class PersonService:

    @staticmethod
    def get_all():

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
    def get_profile(person_id):

        query = """
        MATCH (p:Person {id:$id})

        OPTIONAL MATCH (p)-[:WORKS_AT]->(c)

        OPTIONAL MATCH (p)-[:HAS_SKILL]->(s)

        OPTIONAL MATCH (p)-[:KNOWS]->(k)

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