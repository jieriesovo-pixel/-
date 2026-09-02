<template>
<div>
  <h2 style="margin-bottom:16px">⚙️ 管理控制台</h2>
  <el-row :gutter="16">
    <el-col :span="6" v-for="s in stats" :key="s.label">
      <el-card style="text-align:center">
        <div style="font-size:28px;font-weight:700;color:#409eff">{{s.value}}</div>
        <div style="color:#909399;margin-top:4px">{{s.label}}</div>
      </el-card>
    </el-col>
  </el-row>
</div>
</template>
<script setup>
import { ref, onMounted, computed } from "vue"
import { adminApi } from "@/api/admin"
const dash=ref({})
onMounted(async()=>{ dash.value=await adminApi.getDashboard() })
const stats=computed(()=>[
  {label:"用戶總數",value:dash.value.user_count||0},
  {label:"文件總數",value:dash.value.file_count||0},
])
</script>
