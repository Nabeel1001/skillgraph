import axios from "axios";

export const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
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

