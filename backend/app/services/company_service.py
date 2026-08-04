from app.db.database import db


class CompanyService:

    @staticmethod
    def get_all():

        query = """
        MATCH (c:Company)
        RETURN c
        ORDER BY c.name
        """

        return db.execute_query(query)