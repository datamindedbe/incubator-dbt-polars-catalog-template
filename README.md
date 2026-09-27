# dbt-polars catalog template

[Copier](https://copier.readthedocs.io) template for a custom [dbt-polars](https://github.com/datamindedbe/incubator-dbt-polars) catalog, published as its own package.

```bash
uvx copier copy gh:datamindedbe/incubator-dbt-polars-catalog-template dbt-polars-catalog-<name>
```

Copier asks for:

- `catalog_name`: the catalog `type` in profiles.yml. The package is named `dbt-polars-catalog-<catalog_name>`.
- `base_class`: the class your catalog extends.
- `author_name`, `author_email`: package metadata.

## Catalog classes

| Class | Use it when | You implement |
|---|---|---|
| `StorageCatalog` (recommended) | Your backend stores Delta tables or Parquet/CSV/NDJSON files at a URI | URIs, storage options and schema management; reading, writing, merging, snapshots and comments are inherited |
| `BaseCatalog` | Any other backend | Every catalog operation |

See [Custom catalogs](https://github.com/datamindedbe/incubator-dbt-polars/blob/main/docs/catalogs/custom.md) in dbt-polars for the catalog API and testing.

## Generated project

- `dbt_polars_catalog_<name>/catalog.py`: the catalog and its config, with every method to implement.
- `tests/`: the dbt-polars catalog tests and dbt tests, and a schema cleanup.
- `.github/workflows/`: CI and a PyPI publish workflow.

Run `uvx copier update` in a generated project to pull in template changes.
