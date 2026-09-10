# Web Search API

Web search, online retrieval, real-time information query, search engine search, Reddit and other community platform discussions, external site posts and trending topics.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/web-search?view=api&co-from=github-ecommerce-api)

Category: Search & Trend Intelligence · Data API

Web search, online retrieval, real-time information query, search engine search, Reddit and other community platform discussions, external site posts and trending topics.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/web-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `keyword` | string | Yes | Search keyword, max length 1000 characters | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/web-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh web-search request.json
# Or: node examples/javascript/run.mjs web-search request.json
# Or: python3 examples/python/run.py web-search request.json
```

### Published request example

```json
{
  "keyword": "phone case"
}
```

## Response

The run endpoint returns its API-specific payload directly. Do not assume a `data` or `result` wrapper. For asynchronous APIs, the run response is a task receipt, not the final generated asset.

### Published response example

```json
{
  "searchList": [
    {
      "score": 1,
      "url": "https://example.com/image.jpg"
    }
  ],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/web-search.request.json) — field-descriptors
- [Response definition](../../schemas/web-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/web-search.json)
- [Response fixture](../../examples/responses/web-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_web_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
