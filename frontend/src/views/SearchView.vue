<template>
<div>
  <h2 style="margin-bottom:16px">🔍 全文搜索</h2>
  <el-input v-model="q" size="large" placeholder="搜索文件..." @keyup.enter="doSearch" clearable>
    <template #append><el-button @click="doSearch">搜索</el-button></template>
  </el-input>
  <div style="margin-top:16px">
    <el-empty v-if="searched && !results.length" description="未找到相關文件" />
    <el-card v-for="r in results" :key="r.file_id" style="margin-bottom:8px">{{r.name}}</el-card>
  </div>
</div>
</template>
<script setup>
import { ref } from "vue"
import { searchApi } from "@/api/search"
const q=ref(""), results=ref([]), searched=ref(false)
async function doSearch() {
  if(!q.value) return
  const d = await searchApi.search(q.value)
  results.value=d.items; searched.value=true
}
</script>
