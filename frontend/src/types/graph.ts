export interface GraphNode {
    data: {
        id: string;
        label: string;
        type: string;
    };
}

export interface GraphEdge {
    data: {
        source: string;
        target: string;
        label: string;
    };
}

export interface GraphData {
    nodes: GraphNode[];
    edges: GraphEdge[];
}