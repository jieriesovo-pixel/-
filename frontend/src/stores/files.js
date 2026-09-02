import { defineStore } from "pinia"
import { ref } from "vue"
import { filesApi } from "@/api/files"
export const useFilesStore = defineStore("files", () => {
  const folders = ref([])
  const files = ref([])
  const loading = ref(false)
  const currentFolderId = ref(null)
  async function loadFolder(id=null) {
    loading.value=true; currentFolderId.value=id
    try { const d=await filesApi.listFolder(id); folders.value=d.folders||[]; files.value=d.files||[] }
    finally { loading.value=false }
  }
  async function deleteFile(id) {
    await filesApi.deleteFile(id)
    files.value=files.value.filter(f=>f.id!==id)
  }
  return { folders, files, loading, currentFolderId, loadFolder, deleteFile }
})
