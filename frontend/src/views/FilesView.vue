<template>
<div>
  <div style="display:flex;justify-content:space-between;margin-bottom:16px">
    <h2>我的文件</h2>
    <el-button type="primary" @click="$refs.fu.click()">⬆️ 上傳文件</el-button>
    <input ref="fu" type="file" multiple hidden @change="handleUpload" />
  </div>
  <el-card v-loading="store.loading">
    <el-empty v-if="!store.files.length" description="暫無文件，點擊上傳" />
    <div v-else style="display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px">
      <div v-for="f in store.files" :key="f.id" style="border:1px solid #e6e6e6;border-radius:8px;padding:12px;text-align:center">
        <div style="font-size:32px">📄</div>
        <div style="font-size:12px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;margin-bottom:8px">{{f.name}}</div>
        <el-button size="small" @click="download(f)">下載</el-button>
        <el-button size="small" type="danger" @click="store.deleteFile(f.id)">刪除</el-button>
      </div>
    </div>
  </el-card>
</div>
</template>
<script setup>
import { onMounted } from "vue"
import { useFilesStore } from "@/stores/files"
import { filesApi } from "@/api/files"
const store = useFilesStore()
onMounted(() => store.loadFolder())
function handleUpload(e) { console.log("上傳:", e.target.files) }
function download(f) { window.open(filesApi.downloadUrl(f.id)) }
</script>
