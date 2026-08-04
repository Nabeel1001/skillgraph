import type { GraphData } from "../../types/graph";
import GraphViewer from "./GraphViewer";

type Props = {
    open: boolean;
    onClose: () => void;
    graph: GraphData | null;
};

export default function GraphModal({
    open,
    onClose,
    graph,
}: Props) {

    if (!open || !graph) return null;

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70">

            <div className="w-[90vw] max-w-6xl rounded-xl bg-zinc-950 p-6">

                <div className="mb-5 flex items-center justify-between">

                    <h2 className="text-2xl font-bold text-white">
                        Professional Graph
                    </h2>

                    <button
                        onClick={onClose}
                        className="rounded bg-red-500 px-3 py-1 text-white"
                    >
                        Close
                    </button>

                </div>

                <GraphViewer graph={graph} />

            </div>

        </div>
    );
}