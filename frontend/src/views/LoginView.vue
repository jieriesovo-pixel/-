<template>
<div class="wrap">
  <div class="card">
    <h1>☁️ 企業級雲盤系統</h1>
    <el-form size="large" @keyup.enter="doLogin">
      <el-form-item><el-input v-model="email" placeholder="郵箱" clearable /></el-form-item>
      <el-form-item><el-input v-model="password" type="password" placeholder="密碼" show-password clearable /></el-form-item>
      <el-button type="primary" style="width:100%" :loading="loading" @click="doLogin">登錄</el-button>
    </el-form>
  </div>
</div>
</template>
<script setup>
import { ref } from "vue"
import { useAuthStore } from "@/stores/auth"
const auth = useAuthStore()
const email = ref(""), password = ref(""), loading = ref(false)
async function doLogin() {
  loading.value=true
  try { await auth.login(email.value, password.value) } finally { loading.value=false }
}
</script>
<style scoped>
.wrap{display:flex;justify-content:center;align-items:center;height:100vh;background:linear-gradient(135deg,#667eea,#764ba2)}
.card{background:#fff;padding:40px;border-radius:16px;width:400px;box-shadow:0 20px 60px rgba(0,0,0,.2)}
h1{text-align:center;margin-bottom:24px;font-size:22py}
</style>
