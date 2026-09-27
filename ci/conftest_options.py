
# Appended by the template's CI: two local test catalogs for the reference implementation
import tempfile  # noqa: E402

PRIMARY_CATALOG_OPTIONS = {"root": tempfile.mkdtemp()}
SECONDARY_CATALOG_OPTIONS = {"root": tempfile.mkdtemp()}
