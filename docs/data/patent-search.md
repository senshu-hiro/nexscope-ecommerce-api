# Patent Search API

Search patent publications with an Analytics query expression.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-search?view=api&co-from=github-ecommerce-api)

Category: Patent Intelligence · Data API

Searches the Zhihuiya patent database and returns matching patent identifiers and publication numbers.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `queryText` | string | No | Optional patent Analytics query expression forwarded as documented by the provider. | {} |
| `pageNum` | integer | No | Page number. | {} |
| `pageSize` | integer | No | Results per page. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-search request.json
# Or: node examples/javascript/run.mjs patent-search request.json
# Or: python3 examples/python/run.py patent-search request.json
```

### Published request example

```json
{
  "pageSize": 20,
  "queryText": "TI=(wireless speaker)",
  "pageNum": 1
}
```

## Response

The run endpoint returns its API-specific payload directly. Do not assume a `data` or `result` wrapper. For asynchronous APIs, the run response is a task receipt, not the final generated asset.

### Published response example

```json
{
  "data": [
    {
      "patentId": "CN123456789",
      "publicationNumber": "CN123456789A"
    }
  ],
  "total": 1
}
```

## Full definitions

- [Request definition](../../schemas/patent-search.request.json) — field-descriptors
- [Response definition](../../schemas/patent-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-search.json)
- [Response fixture](../../examples/responses/patent-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
