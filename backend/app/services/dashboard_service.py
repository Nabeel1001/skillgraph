from app.db.database import db


class DashboardService:

    @staticmethod
    def get_stats():

        query = """
        MATCH (p:Person)
        WITH count(p) AS people

        MATCH (c:Company)
        WITH people,count(c) AS companies

        MATCH (s:Skill)
        WITH people,companies,count(s) AS skills

        MATCH ()-[r]->()
        RETURN
            people,
            companies,
            skills,
            count(r) AS relationships
        """

        return db.execute_query(query)[0]