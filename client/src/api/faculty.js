import api from "./axios";

export const getFacultyDashboard = async () => {
  const response = await api.get("academics/faculty/dashboard/");
  return response.data;
};
