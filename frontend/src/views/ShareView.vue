<template>
<div style="display:flex;justify-content:center;align-items:center;height:100vh;background:linear-gradient(135deg,#667eea,#764ba2)">
  <el-card style="width:400px;text-align:center;padding:24px">
    <div style="font-size:48px;margin-bottom:16px">📁</div>
    <h2>外鏈文件下載</h2>
    <p style="color:#909399;margin:12px 0">{{ info?.file?.name }}</p>
    <el-button type="primary" size="large" @click="download">⬇️ 下載文件</el-button>
  </el-card>
</div>
</template>
<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import { shareApi } from "@/api/share"
const route=useRoute(), info=ref(null)
onMounted(async()=>{ try { info.value=await shareApi.accessShare(route.params.token) } catch{} })
function download() { window.open(shareApi.downloadUrl(route.params.token)) }
</script>
