# Patent Description Data Translation API

Retrieve translated patent description (specification) text from Zhihuiya.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/patent-description-data-translation?view=api&co-from=github-ecommerce-api)

Category: Patent & IP Risk · Data API

Retrieve translated patent description (specification) text from Zhihuiya.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/patent-description-data-translation/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `patentId` | string | No | Patent ID. At least one of patentId and patentNumber must be provided; if both are present, patentId takes priority. Only a single value is supported; multiple values separated by commas are not allowed. Max length: 60000 characters | {} |
| `patentNumber` | string | No | Publication (grant) number. At least one of patentId and patentNumber must be provided; if both are present, patentId takes priority. Only a single value is supported; multiple values separated by commas are not allowed. Max length: 60000 characters | {} |
| `lang` | string | No | Translation language, supports en (English, default), cn (Chinese), jp (Japanese). Max length: 1000 characters | {} |
| `replaceByRelated` | integer | No | Whether to substitute with a family patent's description when the description is unavailable: 1 Yes, 0 No (default 0) | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/patent-description-data-translation.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh patent-description-data-translation request.json
# Or: node examples/javascript/run.mjs patent-description-data-translation request.json
# Or: python3 examples/python/run.py patent-description-data-translation request.json
```

### Published request example

```json
{
  "patentNumber": "CN115000000A",
  "replaceByRelated": 1,
  "lang": "en"
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
      "patentId": "example-id"
    }
  ],
  "columns": [],
  "costToken": 1
}
```

## Full definitions

- [Request definition](../../schemas/patent-description-data-translation.request.json) — field-descriptors
- [Response definition](../../schemas/patent-description-data-translation.response.json) — field-descriptors
- [Editable request sample](../../payloads/patent-description-data-translation.json)
- [Response fixture](../../examples/responses/patent-description-data-translation.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_patent_description_data_translation`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
