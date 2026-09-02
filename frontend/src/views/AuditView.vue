<template>
<div>
  <h2 style="margin-bottom:16px">📋 審計日誌</h2>
  <el-table :data="logs">
    <el-table-column prop="action" label="操作類型" />
    <el-table-column prop="created_at" label="時間" />
  </el-table>
</div>
</template>
<script setup>
import { ref, onMounted } from "vue"
import { adminApi } from "@/api/admin"
const logs=ref([])
onMounted(async()=>{ logs.value=await adminApi.getAuditLogs({}) || [] })
</script>
