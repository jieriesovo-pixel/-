<template>
<el-container style="height:100vh">
  <el-aside width="200px" style="background:#fff;border-right:1px solid #e6e6e6">
    <div style="padding:20px;font-weight:700;font-size:18px;border-bottom:1px solid #f0f0f0">☁️ 企業雲盤</div>
    <el-menu router :default-active="$route.path">
      <el-menu-item index="/files">📁 我的文件</el-menu-item>
      <el-menu-item index="/search">🔍 全文搜索</el-menu-item>
      <el-menu-item index="/shares">🔗 分享管理</el-menu-item>
      <el-menu-item v-if="auth.isAdmin" index="/admin">⚙️ 管理控制台</el-menu-item>
      <el-menu-item v-if="auth.isAdmin" index="/audit">📋 審計日誌</el-menu-item>
    </el-menu>
    <div style="position:absolute;bottom:0;padding:16px;width:100%;border-top:1px solid #f0f0f0">
      <span style="font-size:13px;color:#909399">{{ auth.user?.username }}</span>
      <el-button link @click="auth.logout" style="margin-left:8px">退出</el-button>
    </div>
  </el-aside>
  <el-main style="background:#f5f7fa;padding:24px"><router-view /></el-main>
</el-container>
</template>
<script setup>
import { useAuthStore } from "@/stores/auth"
const auth = useAuthStore()
</script>
