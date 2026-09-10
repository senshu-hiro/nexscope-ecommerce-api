# Patent Fulltext Images API

Retrieve fulltext images (drawings, diagrams, charts) from patent documents by patent ID or publication number.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-fulltext-images?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Retrieve fulltext images (drawings, diagrams, charts) from patent documents by patent ID or publication number.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-fulltext-images/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `patentId` | string | No | Patent ID | {} |
| `patentNumber` | string | No | Publication (grant) number | {} |
| `limit` | string | No | Total number of images to return, max 100, default "100" | {} |
| `offset` | string | No | Offset | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-fulltext-images.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-fulltext-images request.json
# Or: node examples/javascript/run.mjs patent-fulltext-images request.json
# Or: python3 examples/python/run.py patent-fulltext-images request.json
```

### Published request example

```json
{
  "patentNumber": "US11299876B2",
  "offset": "0",
  "limit": "10"
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
      "patentId": "example-id",
      "fulltextImagePath": "https://example.com/image.jpg",
      "imageType": "https://example.com/image.jpg"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/patent-fulltext-images.request.json) — field-descriptors
- [Response definition](../../schemas/patent-fulltext-images.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-fulltext-images.json)
- [Response fixture](../../examples/responses/patent-fulltext-images.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_fulltext_images`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
