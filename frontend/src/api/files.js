import http from "./http"
export const filesApi = {
  listFolder: (id) => http.get("/folders",{params:{parent_id:id}}),
  createFolder: (name,pid) => http.post("/folders",{name,parent_id:pid}),
  deleteFile: (id) => http.delete(`/files/${id}`),
  downloadUrl: (id) => `/api/v1/files/${id}/download`,
  getVersions: (id) => http.get(`/files/${id}/versions`),
}
