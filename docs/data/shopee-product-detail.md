# Shopee Product Detail API

Shopee Product Detail public data API.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/shopee-product-detail?view=api&co-from=github-ecommerce-api)

Category: Shopee Marketplace · Data API

Returns normalized public ecommerce research data with a fixed read-only provider path.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/shopee-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `productUrl` | string | Yes | HTTPS Shopee product URL ending in -i.<shopId>.<itemId> on a supported Shopee host | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/shopee-product-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh shopee-product-detail request.json
# Or: node examples/javascript/run.mjs shopee-product-detail request.json
# Or: python3 examples/python/run.py shopee-product-detail request.json
```

### Published request example

```json
{
  "productUrl": "https://shopee.sg/example-i.9641401.29691169956"
}
```

## Response

The run endpoint returns its API-specific payload directly. Do not assume a `data` or `result` wrapper. For asynchronous APIs, the run response is a task receipt, not the final generated asset.

### Published response example

```json
{
  "product": {
    "shopId": "9641401",
    "models": [],
    "images": [],
    "name": "Example Shopee product",
    "itemId": "29691169956"
  }
}
```

## Full definitions

- [Request definition](../../schemas/shopee-product-detail.request.json) — json-schema
- [Response definition](../../schemas/shopee-product-detail.response.json) — json-schema
- [Editable request sample](../../payloads/shopee-product-detail.json)
- [Response fixture](../../examples/responses/shopee-product-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_shopee_product_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
