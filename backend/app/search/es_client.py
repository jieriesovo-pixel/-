from elasticsearch import AsyncElasticsearch
from app.core.config import settings

class ESClient:
    def __init__(self):
        self.client = AsyncElasticsearch(settings.ES_URL)
        self.index = settings.ES_INDEX_FILES
    async def init_indices(self):
        try:
            if not await self.client.indices.exists(index=self.index):
                await self.client.indices.create(index=self.index)
        except: pass
    async def index_file(self, doc):
        await self.client.index(index=self.index, id=doc['file_id'], document=doc)
    async def search(self, tenant_id, query, page=1, size=20):
        body = {'query': {'bool': {'must': [{'term': {'tenant_id': tenant_id}}, {'multi_match': {'query': query, 'fields': ['name^3', 'description']}}]}}, 'from': (page-1)*size, 'size': size}
        r = await self.client.search(index=self.index, body=body)
        return {'total': r['hits']['total']['value'], 'items': [{'file_id': h['_id'], **h['_source']} for h in r['hits']['hits']]}
    async def close(self): await self.client.close()

es_client = ESClient()
