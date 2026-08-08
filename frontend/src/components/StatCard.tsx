type Props = {
    title: string;
    value: number;
    isLoading: boolean;
};

export default function StatCard({ title, value, isLoading }: Props) {
    return (
        <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-6 shadow-lg">
            <p className="text-sm text-zinc-400">
                {title}
            </p>

            <h2 className="mt-2">
                {isLoading ? (
                    <div className="h-8 w-20 animate-pulse rounded bg-zinc-700/70" />
                ) : (
                    <span className="text-3xl font-bold text-white">{value}</span>
                )}
            </h2>
        </div>
    );
}