# Patent Cited By API

Retrieve patents that cite one or more PatSnap patents.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-cited-by?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Returns cited-by counts and citing patent records for up to 100 patents.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-cited-by/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `patentId` | string | No | One or up to 100 comma-separated PatSnap patent IDs. Takes precedence when both identifiers are provided. | {} |
| `patentNumber` | string | No | One or up to 100 comma-separated publication or grant numbers. | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

### Alternative required fields

- Provide patentId or patentNumber. Fields: `patentId`, `patentNumber`.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-cited-by.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-cited-by request.json
# Or: node examples/javascript/run.mjs patent-cited-by request.json
# Or: python3 examples/python/run.py patent-cited-by request.json
```

### Published request example

```json
{
  "patentNumber": "US10123456B2"
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
      "patentId": "patent-id",
      "pn": "US10123456B2",
      "citedBy3y": 1,
      "citedBy5y": 1,
      "citedByPatents": []
    }
  ],
  "columns": [],
  "costToken": 6000
}
```

## Full definitions

- [Request definition](../../schemas/patent-cited-by.request.json) — field-descriptors
- [Response definition](../../schemas/patent-cited-by.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-cited-by.json)
- [Response fixture](../../examples/responses/patent-cited-by.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_cited_by`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
