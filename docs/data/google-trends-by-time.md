# Google Trends By Time API

Query and analyze Google Trends real-time hot topics and trending searches for a specified time range and country/region. Triggered by: Google Trends, hot topics, real-time trending, popular trends, current hot searches, recent trending, viral topics, trending searches, trend discovery, market trends, what's popular, trending now, breakout topics.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/google-trends-by-time?view=api&co-from=github-ecommerce-api)

Category: Search & Trend Intelligence · Data API

Query and analyze Google Trends real-time hot topics and trending searches for a specified time range and country/region. Triggered by: Google Trends, hot topics, real-time trending, popular trends, current hot searches, recent trending, viral topics, trending searches, trend discovery, market trends, what's popular, trending now, breakout topics.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/google-trends-by-time/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `days` | integer | No | Time range, query trend data for the last N days, default 7. Common values: 1, 2, 7 | {} |
| `region` | string | No | Country/region code, default US. Options: US, GB, JP, CA, MX, DE, FR, IT, ES, NL, AU, SG, AE, BR, IN, TR, PL, SE | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/google-trends-by-time.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh google-trends-by-time request.json
# Or: node examples/javascript/run.mjs google-trends-by-time request.json
# Or: python3 examples/python/run.py google-trends-by-time request.json
```

### Published request example

```json
{
  "region": "US",
  "days": 1
}
```

## Response

The run endpoint returns its API-specific payload directly. Do not assume a `data` or `result` wrapper. For asynchronous APIs, the run response is a task receipt, not the final generated asset.

### Published response example

```json
{
  "costToken": 1,
  "chartOption": {
    "data": [],
    "fieldY": []
  },
  "trendValues": [
    {
      "query": "phone case",
      "searchVolume": 1,
      "increasePercentage": 1
    }
  ]
}
```

## Full definitions

- [Request definition](../../schemas/google-trends-by-time.request.json) — field-descriptors
- [Response definition](../../schemas/google-trends-by-time.response.json) — field-descriptors
- [Editable request sample](../../payloads/google-trends-by-time.json)
- [Response fixture](../../examples/responses/google-trends-by-time.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_google_trends_by_time`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
