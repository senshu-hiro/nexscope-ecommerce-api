# GeekBI Temu Product Detail API

Product Detail using GeekBI Temu data.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/geekbi-temu-goods-detail?view=api&co-from=github-ecommerce-api)

Category: Temu Marketplace Intelligence · Data API

Execute the selected product detail operation and preserve provider business fields and extensions.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/geekbi-temu-goods-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `goodsId` | string | Yes | Product ID returned by product search. | {"minLength": 1, "type": "string", "maxLength": 100, "description": "Product ID returned by product search."} |
| `regionId` | integer | No | Temu region from sites[].regionId; never siteId. | {"default": 211, "type": "integer", "description": "Temu region from sites[].regionId; never siteId.", "minimum": 1} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/geekbi-temu-goods-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh geekbi-temu-goods-detail request.json
# Or: node examples/javascript/run.mjs geekbi-temu-goods-detail request.json
# Or: python3 examples/python/run.py geekbi-temu-goods-detail request.json
```

### Published request example

```json
{
  "goodsId": "601100240999226",
  "regionId": 211
}
```

## Response

The run endpoint returns its API-specific payload directly. Do not assume a `data` or `result` wrapper. For asynchronous APIs, the run response is a task receipt, not the final generated asset.

### Published response example

```json
{
  "errmsg": "ok",
  "columns": [],
  "errcode": 200,
  "goods": {},
  "history": [],
  "regionId": 211
}
```

## Full definitions

- [Request definition](../../schemas/geekbi-temu-goods-detail.request.json) — json-schema
- [Response definition](../../schemas/geekbi-temu-goods-detail.response.json) — json-schema
- [Editable request sample](../../payloads/geekbi-temu-goods-detail.json)
- [Response fixture](../../examples/responses/geekbi-temu-goods-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_geekbi_temu_goods_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
