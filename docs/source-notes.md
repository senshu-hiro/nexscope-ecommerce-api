# Source and validation notes

Retrieved: 2026-09-10.

The inventory follows the rendered [official API directory](https://www.nexscope.ai/api-docs?co-from=github-ecommerce-api), preserving its exact API display names, category names, and ordering. Public parameters and samples come from the same public API-definition service used by the documentation: `GET https://api.nexscope.ai/api/skill-api/v1/api-docs`.

Coverage: 225 unique API slugs, including 172 Data APIs across 17 categories and 53 Creative APIs across 3 categories (7 image generation, 12 video generation, 34 multimodal). Supporting task, authentication, and MCP routes are documented as integration mechanisms rather than counted as extra APIs.

Only developer-facing fields are included. Internal routing metadata and trigger instructions are omitted. Human-readable text is normalized using the public documentation's presentation rules. Request values, field constraints, and response examples are preserved. Catalog descriptions may lag presentation overrides on the website; the live API view is the final reference.

The directory inventory and public definition-service slug sets were reconciled. All 225 official API detail pages were fetched successfully (HTTP 200), and each displayed its expected run endpoint and request section. All 225 request fixtures and 225 response fixtures were compared with the public source. Every entry has its own documentation, request definition, response definition, request sample, and response fixture. Client syntax, local links, catalog counts, fixture equality, and representative request-building/error-handling behavior are checked offline.

No authenticated Data or Creative execution was performed for this publication. Documentation fixtures do not prove live success, price, availability, freshness, or complete backend behavior. No pricing or service-level guarantee is inferred from sample values.

Most Data definitions use field descriptors with `jsonSchema: null`. They are retained as that format rather than converted into an invented schema. Strict schema/example compatibility is not claimed across the catalog; consult the current API definition before sending a request. The offline validator checks preservation and coverage, not every server-side business rule.
