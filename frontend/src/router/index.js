import { createRouter, createWebHistory } from "vue-router"
const routes = [
  { path: "/login", component: () => import("@/views/LoginView.vue") },
  { path: "/", component: () => import("@/views/MainLayout.vue"),
    children: [
      { path: "", redirect: "/files" },
      { path: "files", component: () => import("@/views/FilesView.vue") },
      { path: "search", component: () => import("@/views/SearchView.vue") },
      { path: "shares", component: () => import("@/views/SharesView.vue") },
      { path: "admin", component: () => import("@/views/AdminView.vue") },
      { path: "audit", component: () => import("@/views/AuditView.vue") },
    ]
  },
  { path: "/s/:token", component: () => import("@/views/ShareView.vue") }
]
const router = createRouter({ history: createWebHistory(), routes })
export default router
