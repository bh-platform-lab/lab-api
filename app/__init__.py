from importlib.metadata import PackageNotFoundError, version

# Use your real distribution name from pyproject.toml: [project].name
_DIST_NAME = "lab-api"

try:
    __version__ = version(_DIST_NAME)
except PackageNotFoundError:
    # When running from source (tests/dev) without installing the package
    __version__ = "0.0.0"
