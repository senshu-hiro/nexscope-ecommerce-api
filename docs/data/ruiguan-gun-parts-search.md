# Ruiguan Gun Parts Search API

Check product images against a database of policy-violating items using visual similarity matching.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/ruiguan-gun-parts-search?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Check product images against a database of policy-violating items using visual similarity matching.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/ruiguan-gun-parts-search/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `imageUrl` | string | Yes | URL of the product image to inspect (maximum 1,000 characters) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/ruiguan-gun-parts-search.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh ruiguan-gun-parts-search request.json
# Or: node examples/javascript/run.mjs ruiguan-gun-parts-search request.json
# Or: python3 examples/python/run.py ruiguan-gun-parts-search request.json
```

### Published request example

```json
{
  "imageUrl": "https://m.media-amazon.com/images/I/719mRAn2VrL._AC_SL1500_.jpg"
}
```

## Response

The run endpoint returns its API-specific payload directly. Do not assume a `data` or `result` wrapper. For asynchronous APIs, the run response is a task receipt, not the final generated asset.

### Published response example

```json
{
  "total": 1,
  "data": [
    {
      "pdImgOssUrl": "https://example.com/image.jpg",
      "cosine": 1
    }
  ],
  "detectId": "example-id",
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/ruiguan-gun-parts-search.request.json) — field-descriptors
- [Response definition](../../schemas/ruiguan-gun-parts-search.response.json) — field-descriptors
- [Editable request sample](../../payloads/ruiguan-gun-parts-search.json)
- [Response fixture](../../examples/responses/ruiguan-gun-parts-search.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_ruiguan_gun_parts_search`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
