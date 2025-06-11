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

> ⚠️ **Version Warning**
>
> This application is currently developed in **two major versions** in parallel:
>
> - **v6.x (>=6.0.0)** — Stable and production-ready. Maintains support for Pydantic v1 and v2 through a compatibility layer.
> - **v7.x (>=7.0.0)** — Public beta. Fully functional, with native support for Pydantic v2. Still experimental and may introduce breaking changes in **internal and integration interfaces**.
>
> ⚠️ No breaking changes are expected in the **public standard or data model**, only in internal APIs and integration points.
> 
> Both versions currently offer the same set of features.  
> We recommend using **v6** for most production use cases as the more mature and stable option.  
> **v7** is suitable for production environments that can tolerate some level of interface instability and want to adopt the latest internals.
>
> 💡 Only the **latest version of v7** is guaranteed to contain all the features and updates from v6. Earlier v7 releases may lack some recent improvements.
>
> Once **v7 is promoted to stable**, all earlier **pre-stable (beta) v7 releases** will be **marked as yanked** to prevent accidental usage in production.
>

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

[Read More about OpenEPD format here](https://www.open-epd-forum.org).

## Usage

### Models

The library provides the Pydantic models for all the OpenEPD entities. The models are available in the `openepd.models`
module. For mode details on the usage please refer to Pydantic documentation.

### API Client

The library provides the API client to work with the OpenEPD API. The client is available in the `openepd.client`
module.
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

### Model attribute access

OpenEPD extends its pydantic models with extra functionality: field descriptors can be accessed via dot notation from
class name:

* Usual pydantic way: TheModel().__field__["the_field"]
* In openEPD: TheModel.the_field

Instances hold data as usual.

This behaviour is enabled by default. To disable, run the code with `OPENEPD_DISABLE_PYDANTIC_PATCH` set to `true`.

See src/openepd/patch_pydantic.py for details.

### Generated enums

The geography and country enums are generated from several sources, including pycountry list of 2-character country
codes, UN m49 codification, and special regions. To update the enums, first update any of these sources, then use
`make codegen`. See 'tools/openepd/codegen' for details.

## Development

Windows is not supported for development. You can use WSL2 with Ubuntu 20.04 or higher.
Instructions are the same as for regular GNU/Linux installation.

### Commit messages

Commit messages should follow [Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/#specification) 
specification as we use automatic version with [commitizen](https://commitizen-tools.github.io/commitizen/).

# Credits

This library has been written and maintained by [C-Change Labs](https://c-change-labs.com/).

# License

This library is licensed under [Apache 2](/LICENSE). This means you are free to use it in commercial projects.
