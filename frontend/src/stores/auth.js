import { defineStore } from "pinia"
import { ref, computed } from "vue"
import { authApi } from "@/api/auth"
import router from "@/router"
export const useAuthStore = defineStore("auth", () => {
  const token = ref(localStorage.getItem("token")||"")
  const user = ref(JSON.parse(localStorage.getItem("user")||"null"))
  const isAdmin = computed(() => ["super_admin","tenant_admin"].includes(user.value?.role))
  async function login(email, password) {
    const d = await authApi.login(email, password)
    token.value = d.access_token
    user.value = {id:d.user_id, username:d.username, role:d.role, tenant_id:d.tenant_id}
    localStorage.setItem("token", d.access_token)
    localStorage.setItem("user", JSON.stringify(user.value))
    router.push("/files")
  }
  async function logout() {
    token.value=""; user.value=null
    localStorage.removeItem("token"); localStorage.removeItem("user")
    router.push("/login")
  }
  return { token, user, isAdmin, login, logout }
})
