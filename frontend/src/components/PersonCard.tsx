import type { Person } from "../types/person";

type Props = {
    person: Person;
    onExplore: (id: number) => void;
};

export default function PersonCard({ person, onExplore }: Props) {
    return (
        <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-5 transition hover:border-blue-500">
            <h3 className="text-xl font-semibold text-white">
                {person.name}
            </h3>

            <p className="mt-1 text-zinc-400">
                {person.title}
            </p>

            <p className="mt-2 text-sm text-zinc-500">
                {person.email}
            </p>

            <button
                onClick={() => onExplore(person.id)}
                className="mt-5 rounded-lg bg-blue-600 px-4 py-2 text-white transition hover:bg-blue-500"
            >
                Explore Graph
            </button>
        </div>
    );
}