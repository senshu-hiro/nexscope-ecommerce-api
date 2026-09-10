# Patent References API

Retrieve patent and non-patent references cited by one or more patents.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-references?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Returns forward citation details for up to 100 patents.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-references/run`

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
cp payloads/patent-references.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-references request.json
# Or: node examples/javascript/run.mjs patent-references request.json
# Or: python3 examples/python/run.py patent-references request.json
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
      "citedPatents": [],
      "citedOthers": []
    }
  ],
  "columns": [],
  "costToken": 6000
}
```

## Full definitions

- [Request definition](../../schemas/patent-references.request.json) — field-descriptors
- [Response definition](../../schemas/patent-references.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-references.json)
- [Response fixture](../../examples/responses/patent-references.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_references`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
