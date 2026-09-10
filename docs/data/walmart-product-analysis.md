# Walmart Product Analysis API

Walmart Product Analysis public data API.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/walmart-product-analysis?view=api&co-from=github-ecommerce-api)

Category: Walmart Marketplace Intelligence · Data API

Returns normalized public ecommerce research data with a fixed read-only provider path.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/walmart-product-analysis/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `operation` | string | Yes | Operation: searchByName, detail, trend, or salesVolume | {} |
| `name` | string | No | Product name required by searchByName | {} |
| `productId` | string | No | Walmart product ID required by detail, trend, and salesVolume | {} |
| `queryDate` | string | No | Sales-volume start date in YYYY-MM-DD format | {} |
| `queryEndDate` | string | No | Sales-volume end date in YYYY-MM-DD format | {} |
| `pageIndex` | integer | No | Page number, starting at 1 | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/walmart-product-analysis.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh walmart-product-analysis request.json
# Or: node examples/javascript/run.mjs walmart-product-analysis request.json
# Or: python3 examples/python/run.py walmart-product-analysis request.json
```

### Published request example

```json
{
  "productId": "5169493923",
  "operation": "detail"
}
```

## Response

The run endpoint returns its API-specific payload directly. Do not assume a `data` or `result` wrapper. For asynchronous APIs, the run response is a task receipt, not the final generated asset.

### Published response example

```json
{
  "requestConsumed": 1,
  "value": {
    "Price": 1,
    "ProductId": "5169493923",
    "Title": "Example Walmart product"
  },
  "operation": "detail"
}
```

## Full definitions

- [Request definition](../../schemas/walmart-product-analysis.request.json) — json-schema
- [Response definition](../../schemas/walmart-product-analysis.response.json) — json-schema
- [Editable request sample](../../payloads/walmart-product-analysis.json)
- [Response fixture](../../examples/responses/walmart-product-analysis.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_walmart_product_analysis`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
