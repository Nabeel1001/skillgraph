export interface Person {
    id: number;
    name: string;
    title: string;
    email: string;
}

export interface DashboardStats {
    people: number;
    companies: number;
    skills: number;
    relationships: number;
}