import { useEffect, useState } from "react";

type Props = {
    title: string;
    value: number;
    isLoading: boolean;
};

export default function StatCard({ title, value, isLoading }: Props) {
    const [count, setCount] = useState(0);

    useEffect(() => {
        if (isLoading) {
            setCount(0);
            return;
        }

        let start = 0;
        const duration = 800; // ms
        const increment = Math.max(1, Math.ceil(value / (duration / 16)));

        const timer = setInterval(() => {
            start += increment;

            if (start >= value) {
                setCount(value);
                clearInterval(timer);
            } else {
                setCount(start);
            }
        }, 16);

        return () => clearInterval(timer);
    }, [value, isLoading]);

    return (
        <div className="rounded-xl border border-zinc-800 bg-zinc-900 p-5">
            <p className="text-sm text-zinc-400">{title}</p>

            <h2 className="mt-2">
                {isLoading ? (
                    <div className="h-8 w-20 animate-pulse rounded bg-zinc-700/70" />
                ) : (
                    <span className="text-3xl font-bold text-white">
                        {count}
                    </span>
                )}
            </h2>
        </div>
    );
}