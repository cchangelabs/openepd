# Release procedure

## Upload Release from local device (not recommended)

1. Configure auth tokens for PyPi:

```bash
# For test PyPi
poetry config pypi-token.test-pypi pypi-XXXXXXXXXXX
# For real PyPi index
poetry config pypi-token.pypi pypi-XXXXXXXXXXX
```

2. Run `make test-publish` to build and upload package to the test PyPi and `make publish` for prod.
