# Amazon Sales Estimates API

Jungle Scout ASIN sales estimates query, returning daily estimated sales and latest known price for a specified ASIN over a given time period, covering 10 marketplaces including US, UK, Germany, and Japan.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-sales-estimates?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Jungle Scout ASIN sales estimates query, returning daily estimated sales and latest known price for a specified ASIN over a given time period, covering 10 marketplaces including US, UK, Germany, and Japan.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-sales-estimates/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `marketplace` | string | Yes | Target marketplace code. Options: us, uk, de, in, ca, fr, it, es, mx, jp | {} |
| `asin` | string | Yes | Amazon ASIN to query | {} |
| `startDate` | string | Yes | Start date (format: YYYY-MM-DD) | {} |
| `endDate` | string | Yes | End date (format: YYYY-MM-DD); must be earlier than the current date | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-sales-estimates.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-sales-estimates request.json
# Or: node examples/javascript/run.mjs amazon-sales-estimates request.json
# Or: python3 examples/python/run.py amazon-sales-estimates request.json
```

### Published request example

```json
{
  "asin": "B072MQ5BRX",
  "startDate": "2026-01-01",
  "endDate": "2026-01-01",
  "marketplace": "us"
}
```

## Response

The run endpoint returns its API-specific payload directly. Do not assume a `data` or `result` wrapper. For asynchronous APIs, the run response is a task receipt, not the final generated asset.

### Published response example

```json
{
  "costToken": 1,
  "salesEstimateList": [
    {
      "asin": "B072MQ5BRX",
      "id": "example-id",
      "parentAsin": "B072MQ5BRX",
      "isParent": false,
      "isVariant": false,
      "isStandalone": false,
      "variants": [],
      "dailyEstimates": [],
      "date": "2026-01-01",
      "estimatedUnitsSold": 1,
      "lastKnownPrice": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/amazon-sales-estimates.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-sales-estimates.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-sales-estimates.json)
- [Response fixture](../../examples/responses/amazon-sales-estimates.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_sales_estimates`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
