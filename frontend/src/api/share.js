import http from "./http"
export const shareApi = {
  createShare: (d) => http.post("/shares",d),
  accessShare: (t,p) => http.post(`/shares/${t}/access`,{password:p}),
  revokeShare: (t) => http.delete(`/shares/${t}`),
  myShares: () => http.get("/shares/my"),
  downloadUrl: (t) => `/api/v1/shares/${t}/download`,
}
