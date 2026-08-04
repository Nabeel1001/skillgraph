import { useMemo, useState } from "react";
import { useQuery } from "@tanstack/react-query";

import Navbar from "../components/Navbar";
import SearchBar from "../components/SearchBar";
import StatCard from "../components/StatCard";
import PersonCard from "../components/PersonCard";
import GraphModal from "../components/graph/GraphModal";

import {
    getDashboardStats,
    getPeople,
    getGraph,
} from "../services/api";

import type { Person, DashboardStats } from "../types/person";
import type { GraphData } from "../types/graph";

export default function Dashboard() {
    const [search, setSearch] = useState("");

    const [graph, setGraph] = useState<GraphData | null>(null);
    const [graphOpen, setGraphOpen] = useState(false);

    const { data: stats } = useQuery<DashboardStats>({
        queryKey: ["stats"],
        queryFn: getDashboardStats,
    });

    const { data: people = [] } = useQuery<Person[]>({
        queryKey: ["people"],
        queryFn: getPeople,
    });

    const filteredPeople = useMemo(() => {
        return people.filter((person) =>
            person.name.toLowerCase().includes(search.toLowerCase())
        );
    }, [people, search]);

    const handleExplore = async (id: number) => {
        try {
            const data = await getGraph(id);
            setGraph(data);
            setGraphOpen(true);
        } catch (error) {
            console.error("Failed to load graph:", error);
        }
    };

    return (
        <div className="min-h-screen bg-zinc-950 text-white">
            <Navbar />

            <main className="mx-auto max-w-7xl px-6 py-8">

                {/* Stats */}

                <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
                    <StatCard
                        title="People"
                        value={stats?.people ?? 0}
                    />

                    <StatCard
                        title="Companies"
                        value={stats?.companies ?? 0}
                    />

                    <StatCard
                        title="Skills"
                        value={stats?.skills ?? 0}
                    />

                    <StatCard
                        title="Relationships"
                        value={stats?.relationships ?? 0}
                    />
                </div>

                {/* Search */}

                <div className="sticky top-0 z-20 mt-8 bg-zinc-950/95 py-4 backdrop-blur-md">
                    <div className="mx-auto max-w-7xl px-6">
                        <SearchBar
                            value={search}
                            onChange={setSearch}
                        />
                    </div>
                </div>

                {/* People */}

                <div className="mt-8 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
                    {filteredPeople.length > 0 ? (
                        filteredPeople.map((person) => (
                            <PersonCard
                                key={person.id}
                                person={person}
                                onExplore={handleExplore}
                            />
                        ))
                    ) : (
                        <div className="col-span-full rounded-lg border border-zinc-800 p-8 text-center text-zinc-400">
                            No professionals found.
                        </div>
                    )}
                </div>
            </main>

            <GraphModal
                open={graphOpen}
                graph={graph}
                onClose={() => setGraphOpen(false)}
            />
        </div>
    );
}