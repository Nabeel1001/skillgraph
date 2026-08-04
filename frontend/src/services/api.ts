import axios from "axios";

export const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
});

export const getPeople = async () => {
    const { data } = await api.get("/people");
    return data;
};

export const getDashboardStats = async () => {
    const { data } = await api.get("/dashboard/stats");
    return data;
};

export const getGraph = async (id: number) => {
    const { data } = await api.get(`/graph/person/${id}`);
    return data;
};

