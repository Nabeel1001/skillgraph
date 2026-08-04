import CytoscapeComponent from "react-cytoscapejs";
import type { GraphData } from "../../types/graph";

type Props = {
    graph: GraphData;
};

export default function GraphViewer({ graph }: Props) {
    return (
        <div className="h-[600px] w-full rounded-lg bg-zinc-900">

            <CytoscapeComponent
                elements={[...graph.nodes, ...graph.edges]}
                style={{
                    width: "100%",
                    height: "600px",
                }}
                layout={{
                    name: "cose",
                    animate: true,
                }}
                stylesheet={[
                    {
                        selector: "node",
                        style: {
                            label: "data(label)",
                            color: "#fff",
                            "text-valign": "center",
                            "text-halign": "center",
                            "font-size": "12px",
                        },
                    },

                    {
                        selector: 'node[type="Person"]',
                        style: {
                            "background-color": "#3B82F6",
                            width: 45,
                            height: 45,
                        },
                    },

                    {
                        selector: 'node[type="Company"]',
                        style: {
                            "background-color": "#10B981",
                            shape: "round-rectangle",
                            width: 60,
                            height: 40,
                        },
                    },

                    {
                        selector: 'node[type="Skill"]',
                        style: {
                            "background-color": "#F59E0B",
                            shape: "diamond",
                            width: 35,
                            height: 35,
                        },
                    },

                    {
                        selector: "edge",
                        style: {
                            width: 2,
                            "line-color": "#52525b",
                            "target-arrow-color": "#52525b",
                            "target-arrow-shape": "triangle",
                            "curve-style": "bezier",
                            label: "data(label)",
                            color: "#a1a1aa",
                            "font-size": "10px",
                        },
                    },
                ]}
            />

        </div>
    );
}