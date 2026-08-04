export default function Navbar() {
    return (
        <header className="border-b border-zinc-800 bg-zinc-950">
            <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
                <div>
                    <h1 className="text-2xl font-bold text-white">
                        SkillGraph
                    </h1>

                    <p className="text-sm text-zinc-400">
                        Discover Professional Connections
                    </p>
                </div>

                <div className="rounded-lg bg-blue-600 px-3 py-1 text-sm font-medium text-white">
                    CognoDB
                </div>
            </div>
        </header>
    );
}