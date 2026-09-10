# Amazon Product Detail API

Retrieve detailed Amazon product information by ASIN, including title, images, bullet points, specifications, A+ content, pricing, ratings & reviews, variants, and more.

[All APIs](../../README.md#complete-api-catalog) · [Official documentation](https://www.nexscope.ai/api-docs/amazon-product-detail?view=api&co-from=github-ecommerce-api)

Category: Amazon Marketplace Intelligence · Data API

Retrieve detailed Amazon product information by ASIN, including title, images, bullet points, specifications, A+ content, pricing, ratings & reviews, variants, and more.

## Endpoint

`POST https://api.nexscope.ai/api/skill-api/v1/skills/amazon-product-detail/run`

Headers: `Authorization: Bearer YOUR_API_KEY` and `Content-Type: application/json`.

Execution: synchronous; inspect the direct API-specific response body.

## Request parameters

| Name | Type | Required | Description | Constraints |
|---|---|---|---|---|
| `asins` | string | Yes | ASIN list, supports batch query, up to 40 ASINs. Format: ^[A-Z0-9]+(,[A-Z0-9]+){0,39}$. Example: B072MQ5BRX,B08N5WRWNW | {} |
| `amazonDomain` | string | No | Amazon country site, default amazon.com. Options: amazon.com, amazon.co.uk, amazon.de, amazon.fr, amazon.it, amazon.es, amazon.co.jp, amazon.ca, amazon.com.au, amazon.com.br, amazon.in, amazon.nl, amazon.se, amazon.pl, amazon.sg, amazon.sa, amazon.ae, amazon.com.tr, amazon.com.mx, amazon.eg, amazon.cn, amazon.com.be | {} |
| `language` | string | No | Language. Examples: en_US, de_DE, fr_FR, ja_JP, it_IT, es_ES, pt_BR, en_GB, zh_CN | {} |
| `deliveryZip` | string | No | Delivery zip code, used to get delivery-related pricing. Examples: 10001 (New York, US), 10115 (Berlin, Germany), EC1A 1BB (London, UK) | {} |
| `device` | string | No | Device type: desktop (default), mobile, tablet | {} |
| `returnBoughtTogether` | boolean | No | Whether to return frequently bought together items (boughtTogether), default false | {} |
| `returnRelatedProducts` | boolean | No | Whether to return related product list (relatedProducts), default false | {} |
| `returnAuthorsReviews` | boolean | No | Whether to return author review list (authorsReviews), default false | {} |

The table summarizes the published fields. Consult the full request definition for nested objects, alternatives, and conditional requirements.

## Call this API

Run these commands from the repository root after [setting your API key](../../README.md#1-get-and-configure-your-api-key). Copy the sample to a separate file and replace illustrative URLs, IDs, search terms, and required values before submitting. Sample responses are documentation fixtures, not live results.

```bash
cp payloads/amazon-product-detail.json request.json
# Edit request.json for your inputs.
bash examples/curl/run.sh amazon-product-detail request.json
# Or: node examples/javascript/run.mjs amazon-product-detail request.json
# Or: python3 examples/python/run.py amazon-product-detail request.json
```

### Published request example

```json
{
  "returnRelatedProducts": false,
  "returnAuthorsReviews": false,
  "asins": "B072MQ5BRX",
  "returnBoughtTogether": false
}
```

## Response

The run endpoint returns its API-specific payload directly. Do not assume a `data` or `result` wrapper. For asynchronous APIs, the run response is a task receipt, not the final generated asset.

### Published response example

```json
{
  "total": 1,
  "columns": [],
  "costToken": 1,
  "products": [
    {
      "asin": "B072MQ5BRX",
      "price": 1,
      "extractedPrice": 1,
      "oldPrice": 1,
      "extractedOldPrice": 1,
      "rating": 1,
      "ratings": 1,
      "prime": false,
      "asinUrl": "B072MQ5BRX",
      "imageUrl": "https://example.com/image.jpg",
      "productImageUrls": [],
      "aboutItem": [],
      "climatePledgeFriendly": false,
      "snapEbtEligible": false,
      "boughtLastMonthCount": 1,
      "reviewsImages": [],
      "pageFileUrl": "https://example.com/image.jpg",
      "review": 1,
      "fiveStar": 1,
      "fourStar": 1,
      "threeStar": 1,
      "twoStar": 1,
      "oneStar": 1,
      "items": [],
      "position": 1,
      "image": "https://example.com/image.jpg",
      "carouselImages": []
    }
  ],
  "asin": "B072MQ5BRX",
  "extractedPrice": 1,
  "extractedPriceUnit": 1,
  "delivery": [],
  "position": 1,
  "extractedOldPrice": 1,
  "rating": 1,
  "reviews": 1,
  "prime": false,
  "sponsored": false,
  "climatePledgeFriendly": false,
  "badges": [],
  "authorImage": "https://example.com/image.jpg",
  "date": "2026-01-01",
  "verifiedPurchase": false
}
```

## Full definitions

- [Request definition](../../schemas/amazon-product-detail.request.json) — field-descriptors
- [Response definition](../../schemas/amazon-product-detail.response.json) — field-descriptors
- [Editable request sample](../../payloads/amazon-product-detail.json)
- [Response fixture](../../examples/responses/amazon-product-detail.json)

Some source definitions use field descriptors rather than JSON Schema; these are preserved and labeled rather than presented as strict validation schemas.

## MCP

Tool name: `nexscope_amazon_product_detail`. See [MCP integration](../calling-apis.md#mcp).

Source retrieved: 2026-09-10. See [source and validation notes](../source-notes.md).
