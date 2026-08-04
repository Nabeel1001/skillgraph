from app.db.database import db


class GraphService:

    @staticmethod
    def get_person_graph(person_id: int):

        query = """
        MATCH (p:Person {id:$id})

        OPTIONAL MATCH (p)-[:WORKS_AT]->(c:Company)
        OPTIONAL MATCH (p)-[:HAS_SKILL]->(s:Skill)
        OPTIONAL MATCH (p)-[:KNOWS]->(k:Person)

        RETURN
            p,
            c,
            collect(DISTINCT s) AS skills,
            collect(DISTINCT k) AS friends
        """

        result = db.execute_query(query, {"id": person_id})

        if not result:
            return {"nodes": [], "edges": []}

        row = result[0]

        person = row["p"]
        company = row["c"]
        skills = row["skills"]
        friends = row["friends"]

        nodes = []
        edges = []

        # Person
        nodes.append({
            "data": {
                "id": f"person_{person['id']}",
                "label": person["name"],
                "type": "Person"
            }
        })

        # Company
        if company:

            nodes.append({
                "data": {
                    "id": f"company_{company['id']}",
                    "label": company["name"],
                    "type": "Company"
                }
            })

            edges.append({
                "data": {
                    "source": f"person_{person['id']}",
                    "target": f"company_{company['id']}",
                    "label": "WORKS_AT"
                }
            })

        # Skills
        for skill in skills:

            nodes.append({
                "data": {
                    "id": f"skill_{skill['id']}",
                    "label": skill["name"],
                    "type": "Skill"
                }
            })

            edges.append({
                "data": {
                    "source": f"person_{person['id']}",
                    "target": f"skill_{skill['id']}",
                    "label": "HAS_SKILL"
                }
            })

        # Friends
        for friend in friends:

            nodes.append({
                "data": {
                    "id": f"person_{friend['id']}",
                    "label": friend["name"],
                    "type": "Person"
                }
            })

            edges.append({
                "data": {
                    "source": f"person_{person['id']}",
                    "target": f"person_{friend['id']}",
                    "label": "KNOWS"
                }
            })

        return {
            "nodes": nodes,
            "edges": edges
        }