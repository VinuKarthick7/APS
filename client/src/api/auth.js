import api from "./axios";

export const login = async (uid, password) => {
  const response = await api.post("accounts/login/", {
    uid,
    password,
  });

  localStorage.setItem("token", response.data.token);
  localStorage.setItem("user", JSON.stringify(response.data.user));

  return response.data.user;
};
