# dbt-polars catalog template

[dbt-polars](https://github.com/datamindedbe/incubator-dbt-polars) integrates the flexibility and performance of Polars with the data governance and lineage capabilities of dbt.

Since polars doesn't have a default warehouse, catalogs determine how and where data is stored. Catalogs are configured via the `catalog_type` key in the dbt `profile.yml` and are distributed as separate packages `dbt-polars-catalog-<catalog_type>`.

See the [list of available catalogs](https://github.com/datamindedbe/incubator-dbt-polars/blob/main/docs/catalog-overview.md#catalog-reference). If none of these meet  your requirements, this repository provides a template for creating a new catalog extension.

## Creating a new catalog

This repository is a [Copier](https://copier.readthedocs.io) template that sets up such a package, ready to implement, test and publish:

```bash
uvx copier copy gh:datamindedbe/incubator-dbt-polars-catalog-template dbt-polars-catalog-<name>
```

Copier asks for:

- `catalog_name`: the `catalog_type` in the profile. The package is named `dbt-polars-catalog-<catalog_name>`.
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
