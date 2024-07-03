# Python Library to work with OpenEPD format

<p align="center">
<a href="https://pypi.org/project/openepd/"><img src="https://img.shields.io/pypi/l/openepd?style=for-the-badge" title="License: Apache-2"/></a> 
<a href="https://pypi.org/project/openepd/"><img src="https://img.shields.io/pypi/pyversions/openepd?style=for-the-badge" title="Python Versions"/></a> 
<a href="https://github.com/psf/black/"><img src="https://img.shields.io/badge/Code%20Style-black-black?style=for-the-badge" title="Code style: black"/></a> 
<a href="https://pypi.org/project/openepd/"><img src="https://img.shields.io/pypi/v/openepd?style=for-the-badge" title="PyPy Version"/></a> 
<a href="https://pypi.org/project/openepd/"><img src="https://img.shields.io/pypi/dm/openepd?style=for-the-badge" title="PyPy Downloads"/></a> 
<br>
<a href="https://github.com/cchangelabs/openepd/actions/workflows/sanity-check.yml"><img src="https://img.shields.io/github/actions/workflow/status/cchangelabs/openepd/sanity-check.yml?style=for-the-badge" title="Build Status"/></a> 
<a href="https://github.com/cchangelabs/openepd/"><img src="https://img.shields.io/github/last-commit/cchangelabs/openepd?style=for-the-badge" title="Last Commit"/></a> 
<a href="https://github.com/cchangelabs/openepd/releases/"><img src="https://img.shields.io/github/release-date/cchangelabs/openepd?style=for-the-badge" title="Last Release"/></a> 
<a href="https://github.com/cchangelabs/openepd/releases/"><img src="https://img.shields.io/github/v/release/cchangelabs/openepd?style=for-the-badge" title="Recent Version"></a> 
</p>

This library is a Python library to work with OpenEPD format.

## About OpenEPD

[openEPD](https://www.buildingtransparency.org/programs/openepd/) is an open data format for passing digital
third-party verified Environmental Product Declarations (EPDs) among Program Operators, EPD Databases,
Life Cycle Analysis tools, design tools, reporting, and procurement.

Unlike print or PDF EPDs, openEPD provides a shared and precise format to express and refer to EPDs in ways that
modern databases can use. openEPD can be used alongside a printable document, or can generate printable EPDs.

Unlike existing formats such as ILCD+EPD, it enforces a key set of guarantees for interoperable data processing,  
including uniqueness of organizations/plants, precise PCR references, and dated version control.

The openEPD format is **extensible**. Standard extensions exist for concrete products, and for
documenting supply-chain specific data.

[Read More about OpenEPD format here](https://www.buildingtransparency.org/programs/openepd/).

## Usage

## Usage

**❗ ATTENTION**: Pick the right version. The cornerstone of this library models package representing openEPD models. 
Models are defined with Pydantic library which is a dependency for openepd package. If you use Pydantic in your project
carefully pick the version:

* Use version **below** `2.0.0` if your project uses Pydantic version below `2.0.0`
* Use version `2.x.x` or higher if your project uses Pydantic version `2.0.0` or above

### Models

The library provides the Pydantic models for all the OpenEPD entities. The models are available in the `openepd.models`
module. For mode details on the usage please refer to Pydantic documentation.

### API Client

The library provides the API client to work with the OpenEPD API. The client is available in the `openepd.client` module.
Currently, the only available implementation is based on synchronous [requests]() library. Client provides the following
features:
* Error handling - depending on HTTP status code the client raises different exceptions allowing to handle errors
  in a more granular way.
* Throttling - the client is able to throttle the requests to the API to avoid hitting the rate limits.
* Retry - the client is able to retry the requests in case of the network errors.

#### API Client Usage

The following example illustrates the usage of the API client:

```python
from openepd.api.sync_client import OpenEpdApiClientSync

# Setup the client
api_client = OpenEpdApiClientSync(
    "https://openepd.buildingtransparency.org/api",
    "<Your API Token>",
)

# Use API, e.g. get EPD by ID
epd = api_client.epds.get_by_openxpd_uuid("ec3b9j5t")
```

### Bundle

Bundle is a format which allows to bundle multiple openEPD objects together (it might be EPDs, PCRs, Orgs + any
other files which might be related to mentioned objects like pdf version of EPD, logo of the PCR company, etc).

Bundle consists of root-level and dependent objects. Dependents are objects which are referenced by root-level objects
or related to the root-level objects. For example, EPD is a root-level object, PDF version of this EPD is a dependent,
translated version of the same EPD is dependent as well.

The following example illustrates reading of the bundle file containing PCR and some of the related objects:

```python
from openepd.bundle.reader import DefaultBundleReader
from openepd.bundle.model import AssetType, RelType

with DefaultBundleReader("test-bundle.epb") as reader:  # You could either file path or file-like object
    pcr = reader.get_first_root_asset(AssetType.Pcr)  # Get FIRST available root level PCR object. We consider that
    # there is only one PCR in the bundle
    # Read relative PDF file of the found PCR. `related_pdf` is a reference to the PDF file containing metadata only
    related_pdf = reader.get_first_relative_asset(pcr, RelType.Pdf)
    # We have to read the file content separately
    with reader.read_blob_asset(related_pdf) as f:
        pass  # Do something with the file content here
```

The next example illustrates the writing of the bundle file:

```python
from openepd.bundle.writer import DefaultBundleWriter
from openepd.bundle.model import RelType
from openepd.model.pcr import Pcr

pcr_obj = Pcr(...)  # Let's assume we already have PCR object

with DefaultBundleWriter("my-bundle.epb") as writer, open("test-pcr.pdf", "rb") as pcr_pdf_file:
    # Add our PCR to the bundle. We do not specify any extra information, however you might what to add language
    # and a file name to make it look nicer in the bundle. If omitted the name will be generated automatically.
    pcr_asset = writer.write_object_asset(pcr_obj)
    # Now add related PDF document. We have to specify the content type, related (parent) object and the 
    # type of relation. Again, optionally you might want to specify the language and file name.
    writer.write_blob_asset(pcr_pdf_file, "application/pdf", pcr_asset, RelType.Pdf)
```

### Mypy

OpenEPD uses a small modification to standard pydantic models (see PydanticClassAttributeExposeModelMetaclass). Mypy,
in order to work correctly, requires a modified pydantic plugin. To enable it, add an 
`openepd.mypy.custom_pydantic_plugin` to list of mypy plugins in your `pyproject.toml` or other mypy-related config
file. See [Mypy configuration](https://mypy.readthedocs.io/en/stable/extending_mypy.html)

# Credits

This library has been written and maintained by [C-Change Labs](https://c-change-labs.com/).

# License

This library is licensed under [Apache 2](/LICENSE). This means you are free to use it in commercial projects.
