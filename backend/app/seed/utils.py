from app.db.database import db


def insert_nodes(data, query, label):
    for item in data:
        db.execute_query(query, item)

    print(f"✅ {label} inserted successfully!")