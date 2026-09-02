import http from "./http"
export const authApi = { login: (e,p) => http.post("/auth/login",{email:e,password:p}), logout: () => http.post("/auth/logout") }
