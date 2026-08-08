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
export  function PersonCardSkeleton() {
    return (
        <div className="animate-pulse rounded-xl border border-zinc-800 bg-zinc-900 p-6">
            {/* Avatar */}
            <div className="h-12 w-12 rounded-full bg-zinc-800" />

            {/* Name */}
            <div className="mt-4 h-6 w-40 rounded bg-zinc-800" />

            {/* Title */}
            <div className="mt-3 h-4 w-32 rounded bg-zinc-800" />

            {/* Email */}
            <div className="mt-2 h-4 w-52 rounded bg-zinc-800" />

            {/* Button */}
            <div className="mt-6 h-10 w-full rounded-lg bg-zinc-800" />
        </div>
    );
}