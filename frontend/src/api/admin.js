import http from "./http"
export const adminApi = {
  getDashboard: () => http.get("/admin/dashboard"),
  listUsers: () => http.get("/users"),
  getAuditLogs: (p) => http.get("/audit",{params:p}),
}
