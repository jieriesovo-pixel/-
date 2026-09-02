import http from "./http"
export const searchApi = { search: (q,opts) => http.post("/search",{query:q,...opts}) }
