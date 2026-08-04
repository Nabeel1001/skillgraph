# 🚀 SkillGraph

A full-stack graph-based professional network explorer built using **React**, **FastAPI**, and **CognoDB**. SkillGraph demonstrates how graph databases efficiently model and visualize relationships between professionals, companies, skills, and locations.

---

## 📌 Overview

Traditional relational databases struggle with highly connected data. SkillGraph leverages a **graph database** to efficiently model relationships and perform graph traversals such as exploring professional networks.

The application allows users to:

- Browse professionals
- Search professionals
- View professional profiles
- Visualize connections using an interactive graph
- Explore relationships between people, companies, and skills

---

## ✨ Features

### Dashboard
- Display total People
- Display total Companies
- Display total Skills
- Display total Relationships

### Professional Directory
- Browse all professionals
- Search professionals by name

### Interactive Graph Visualization
- Explore professional connections
- View companies
- View technical skills
- View professional network

### Graph Database
- Person → Company
- Person → Skill
- Person → Person
- Company → Location

---

# 🏗 Architecture

```
                    React + TypeScript
                            │
                      Axios REST API
                            │
                    FastAPI Backend
                            │
                  Graph Service Layer
                            │
                        CognoDB
```

---

# 🗂 Project Structure

```
skillgraph/

├── backend/
│
│   ├── app/
│   │
│   ├── routes/
│   │     ├── people.py
│   │     ├── dashboard.py
│   │     ├── companies.py
│   │     └── graph.py
│   │
│   ├── services/
│   │     ├── person_service.py
│   │     ├── dashboard_service.py
│   │     ├── company_service.py
│   │     ├── graph_service.py
│   │     ├── recommendation_service.py
│   │     └── path_service.py
│   │
│   ├── db/
│   ├── seed/
│   └── main.py
│
└── frontend/
    ├── src/
    │
    ├── components/
    ├── pages/
    ├── services/
    ├── types/
    └── App.tsx
```

---

# 📊 Graph Schema

```
(Person)-[:WORKS_AT]->(Company)

(Person)-[:HAS_SKILL]->(Skill)

(Person)-[:KNOWS]->(Person)

(Company)-[:LOCATED_IN]->(Location)
```

---

# 🧠 Why Graph Database?

The application models highly connected data.

Examples:

- Which company does a person work at?
- What skills does a person have?
- Who does this person know?
- Which company is located in which city?

These relationships are naturally represented as a graph.

---

# 🛠 Tech Stack

## Frontend

- React
- TypeScript
- Tailwind CSS
- Axios
- Cytoscape.js
- TanStack React Query
- Vite

---

## Backend

- FastAPI
- Python
- CognoDB
- Pydantic
- Faker

---

# 📡 API Endpoints

## Dashboard

```
GET /dashboard/stats
```

Returns dashboard statistics.

---

## People

```
GET /people
```

Returns all professionals.

---

```
GET /people/{id}
```

Returns a professional profile.

---

## Companies

```
GET /companies
```

Returns all companies.

---

## Graph

```
GET /graph/person/{id}
```

Returns graph nodes and edges for Cytoscape visualization.

---

# 🌐 Graph Response Example

```json
{
  "nodes": [
    {
      "data": {
        "id": "person_1",
        "label": "John Doe",
        "type": "Person"
      }
    }
  ],
  "edges": [
    {
      "data": {
        "source": "person_1",
        "target": "company_1",
        "label": "WORKS_AT"
      }
    }
  ]
}
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/skillgraph.git

cd skillgraph
```

---

## Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate
```

Windows

```cmd
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
COGNODB_URI=YOUR_DATABASE_URI
COGNODB_USERNAME=YOUR_USERNAME
COGNODB_PASSWORD=YOUR_PASSWORD
```

Run backend

```bash
uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🧪 Seed Database

Generate sample graph data.

```bash
python -m app.seed.seed_data
```

This creates:

- Companies
- Locations
- Skills
- People
- Relationships

---

# 📸 Screenshots

## Dashboard

> Add screenshot here

---

## Graph Visualization

> Add screenshot here

---

# Future Improvements

- Shortest path between professionals
- Professional recommendations
- Skill-based filtering
- Expandable graph nodes
- Multi-hop graph traversal
- Graph analytics
- Responsive mobile interface

---

# Key Learnings

This project demonstrates:

- Graph database modeling
- FastAPI REST API development
- React with TypeScript
- Cytoscape.js graph visualization
- Full-stack application architecture
- Graph-based relationship traversal

---

# Author

**Nabeel Abdul Aziz Khan**

GitHub:
https://github.com/Nabeel1001

LinkedIn:
https://www.linkedin.com/in/nabeel-abdul-aziz-khan/

---

# License

This project was developed as part of a technical assignment and is intended for educational and evaluation purposes.