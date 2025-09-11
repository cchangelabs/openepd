## 6.30.0 (2025-09-11)

### Feat

- add `FoodBeverage` category to specs
- deprecate `Unsupported.FoodBeverage` category
- add `OtherMineralMetal` category
- add `OtherPaperPlastic` category
- add `ConsumerGoods` category
- add `Services` category
- add `MachineryAndEquipment` category
- add `Vehicles` category
- add `ElectricityAndFuel` category
- add `Chemicals` category
- add `TextileProducts` category

## 6.29.0 (2025-09-05)

### Feat

- add dataUrl support for product image fields

## 6.28.0 (2025-09-01)

### Feat

- **api**: add optional fields parameter to get_by_openxpd_uuid method

### Fix

- add missing `EpdRef` mixin to `EpdPreviewV0`

## 6.27.0 (2025-08-28)

### Feat

- implement `Org.logo` field

## 6.26.0 (2025-08-01)

### Feat

- add third party verifier name field to declaration model
- add GWP-GHG LCIA method
- **openepd**: add constants module and classproperty decorator

## 6.25.0 (2025-06-27)

### Feat

- **utils**: introduce `openepd.utils` package as part of OpenEPD library

### Fix

- resolve explicit reference to pydantic v2 interfaces

## 6.24.0 (2025-06-27)

### Feat

- **specs**: add support for TRACI 2.2 and IPCC AR6

## 6.23.0 (2025-06-25)

### Feat

- add company description field to organization model

## 6.22.0 (2025-06-19)

### Feat

- **specs**: add `AsphaltInputs` specification
- **specs**: add `roof_window` property for `UnitSkylights`

## 6.21.0 (2025-06-18)

### Feat

- **asset**: support multiple assets
- **deps**: extend range of supported `open-xpd-uuid` lib versions

## 6.20.0 (2025-06-10)

### Feat

- **api**: add edit method for PcrApi with optional response
- **api**: add create and edit methods for Org, Plant, and Standard APIs

## 6.19.0 (2025-06-04)

### Feat

- **specs**: add `CellularConcrete` category
- **specs**: add `OtherConcrete` category
- **specs**: add `Polyurethane` for InsulatingMaterial choices

## 6.18.0 (2025-05-30)

### Feat

- **specs**: add `Access Floor Panels` category

## 6.17.1 (2025-05-29)

### Fix

- **specs**: resolve incorrect name of ExteriorImprovements range specifications

## 6.17.0 (2025-05-29) [YANKED]

### Feat

- **specs**: add Exterior Improvements category

## 6.16.0 (2025-05-16)

### Feat

- **specs**: allow additional CementBoard thicknesses

## 6.15.2 (2025-05-13)

### Fix

- **specs**: add missing Wood Fiber insulating material

## 6.15.1 (2025-05-12)

### Fix

- **specs**: resolve typo in CrudeSteelRangeV1 name

## 6.15.0 (2025-05-09)

### Feat

- **specs**: add CrudeSteel category
- **specs**: add safe navigation functionality for Specs object

## 6.14.0 (2025-03-21)

### Feat

- add ADP impacts

### Fix

- fix names of StorageFurniture subcategories.

  **IMPORTANT**: Some class names and property names have changed. Ensure you update any references to these 
  classes and properties in your code before upgrading to this version. Not updating your code will result in 
  references to non-existent classes and properties, causing compilation errors.

  Class names that were changed:
    - `OpenStorageV1` -> `OpenStorageFurnitureV1`
    - `ClosedStorageV1` -> `ClosedStorageFurnitureV1`
    - `RetractableStorageV1` -> `RetractableStorageFurnitureV1`
    - `MobileStorageV1` -> `MobileStorageFurnitureV1`
    - `WallMountedShelvingV1` -> `WallMountedStorageShelvingV1`
    - `OpenStorageRangeV1` -> `OpenStorageFurnitureRangeV1`
    - `ClosedStorageRangeV1` -> `ClosedStorageFurnitureRangeV1`
    - `RetractableStorageRangeV1` -> `RetractableStorageFurnitureRangeV1`
    - `MobileStorageRangeV1` -> `MobileStorageFurnitureRangeV1`
    - `WallMountedShelvingRangeV1` -> `WallMountedStorageShelvingRangeV1`
  
  Property names that were changed:
    - `StorageFurnitureV1.OpenStorage` -> `StorageFurnitureV1.OpenStorageFurniture`
    - `StorageFurnitureV1.ClosedStorage` -> `StorageFurnitureV1.ClosedStorageFurniture`
    - `StorageFurnitureV1.RetractableStorage` -> `StorageFurnitureV1.RetractableStorageFurniture`
    - `StorageFurnitureV1.MobileStorage` -> `StorageFurnitureV1.MobileStorageFurniture`
    - `StorageFurnitureV1.WallMountedShelving` -> `StorageFurnitureV1.WallMountedStorageShelving`
    - `StorageFurnitureRangeV1.OpenStorage` -> `StorageFurnitureRangeV1.OpenStorageFurniture`
    - `StorageFurnitureRangeV1.ClosedStorage` -> `StorageFurnitureRangeV1.ClosedStorageFurniture`
    - `StorageFurnitureRangeV1.RetractableStorage` -> `StorageFurnitureRangeV1.RetractableStorageFurniture`
    - `StorageFurnitureRangeV1.MobileStorage` -> `StorageFurnitureRangeV1.MobileStorageFurniture`
    - `StorageFurnitureRangeV1.WallMountedShelving` -> `StorageFurnitureRangeV1.WallMountedStorageShelving`

## 6.13.2 (2025-03-04)

### Fix

- **m49**: fix openepd to m49 conversion to support global regions
- **m49**: fix openepd to m49 area codes conversion

### Refactor

- **m49**: rename module, move utility method from const to utils

## 6.13.1 (2025-02-20)

### Fix

- fix compatibility with pydantic 1 in model definition

## 6.13.0 (2025-02-20)

### Feat

- **m49**: create m49 package for geography data manipulation

## 6.12.1 (2025-02-17)

### Fix

- fix default values for `Furnishings` properties

## 6.12.0 (2025-02-11)

### Feat

- **specs**: add `Furnishings` category properties

## 6.11.0 (2025-02-07)

### Feat

- **specs**: update `Furnishings` subcategories
- **specs**: add `OtherSteelRangeV1` specification

## 6.10.0 (2025-02-05)

### Feat

- **specs**: Add `OtherSteel` category

## 6.9.1 (2025-01-31)

### Fix

- correct parsing of extensions containing Pydantic models

## 6.9.0 (2024-12-03)

### Feat

- **specs**: update asphalt specification

## 6.8.0 (2024-11-21)

### Feat

- **ext**: make ec3 epd ext an openepd ext

## 6.7.1 (2024-11-19)

### Fix

- correct the schema for attachments object

## 6.7.0 (2024-11-19)

### Feat

- extract PlantRef from Plant model

## 6.6.0 (2024-11-15)

### Feat

- add sample_size to industry epd

## 6.5.1 (2024-11-15)

### Fix

- add explicit format_version for EpdPreview

## 6.5.0 (2024-11-14)

### Feat

- add compatibility layer to specs

## 6.4.2 (2024-11-13)

### Fix

- make known scopes validate for same-unit using dimensionality check

## 6.4.1 (2024-11-12)

### Fix

- implement unit validation for resource_uses, output_flows
- add includes/evidence or citation validator
- correct typo in ACI exposure classes for Concretes
- add validation to allow only positive Amounts
- correct plant validator

## 6.4.0 (2024-11-06)

### Feat

- add location-specific properties to Plant

## 6.3.1 (2024-11-04)

### Fix

- add advanced validation for Plant id and pluscode
- extract EpdRef model from Epd

## 6.3.0 (2024-10-28)

### Feat

- add ec3 extension to EPD object
- add OriginalDataFormat for EPD

### Fix

- add `pluscode` deprecated field to `plant`
- correct Use scenarios years upper limit to 100 years
- correct applicable_in from str to Geography
- correct the kg_C_per_declared unit to be Mass
- make declaration version allow 0

## 6.2.0 (2024-10-15)

### Feat

- extract StandardRef model from Standard

## 6.1.0 (2024-10-10)

### Feat

- **bundle**: add created_date into openEPDBundle manifest

## 6.0.1 (2024-09-20)

### Fix

- update the Spec typings for generation of RangeSpecs
- correct codegen to look at updated specs package

## 6.0.0 (2024-09-13) [YANKED]

### Fix

- **api**: remove exclude_defaults parameter from api client
- add support for 'indirect ingredient' schema

### Refactor

- **specs**: rename specs packages

## 5.3.0 (2024-09-13)

### Feat

- **api**: add exclude_defaults param for post with refs (#80)

## 5.2.0 (2024-09-11)

### Feat

- limit Distribution options of Measurement objects to a known set
- add exclusive group validator for exposure classes

## 5.1.1 (2024-09-05)

### Fix

- correct plant ID alias

## 5.1.0 (2024-09-03)

### Feat

- connect the GenericEstimate, IndustryEpd to generated SpecRange
- add tooling to generate RangeSpecs from normal Specs

### Fix

- allow for plain QuantityStr in modes
- improve apidocs generation for unit-specific RangeAmounts
- correct the examples for kg_c_per_declared_unit to work in apidocs

### Refactor

- rename and update validation factory methods for quantities

## 5.0.0 (2024-08-15)

### Feat

- implement strict validation for ScopeSets

## 4.13.1 (2024-08-01)

### Fix

- add correct kg_C_per_declared_unit to be AmountGWP
- fix dependencies by promoting `open-xpd-uuid` to runtime deps

## 4.13.0 (2024-08-01) [YANKED]

### Feat

- generalize certain EPD fields to other types of declarations

### Fix

- add validator for open_xpd_uuid id field

## 4.12.0 (2024-07-31)

### Feat

- add default timeout to API client

### Fix

- fix ValidationError to string representation
- add strict validation for Mass amounts in declaration objects
- fix parsing impacts with extensions
- enforce doctype matching in Epd, GE, IEPD

## 4.11.3 (2024-07-29)

### Fix

- fix root validator for Amount

## 4.11.2 (2024-07-25)

### Fix

- generalize `version` field from EPD

## 4.11.1 (2024-07-25)

### Fix

- make naming in GE, IEPD api consistent with the rest of the API

## 4.11.0 (2024-07-25) [YANKED]

### Feat

- **api**: add IndustryEPD openEPD API client
- **api**: add GenericEstimate openEPD API client

## 4.10.1 (2024-07-24)

### Fix

- correct descriptions in GenericEstimate
- correct models for openAPI compatibility

## 4.10.0 (2024-07-23)

### Feat

- add openIndustryEPD models
- extend Geography with North America continent (003)
- **specs**: add Conduit category properties

### Fix

- correct description for Steel.yield_tensile_str

## 4.9.0 (2024-07-19)

### Feat

- implement function to access ScopeSet by name in ImpactSet and related
- extract GenericEstimateRef superclass

## 4.8.0 (2024-07-17)

### Feat

- **specs**: add Painting subcategories
- **specs**: add Conduit categories

### Fix

- **specs**: resolve typo in Paint subcategories

## 4.7.0 (2024-07-16)

### Feat

- **specs**: add HvacDuctsV1 specification

## 4.6.1 (2024-07-12)

### Fix

- restore correct Org entities in EPD, GenericEstimate

## 4.6.0 (2024-07-12) [YANKED]

### Feat

- split EPD and GenericEstimate to an hierarchy

### Fix

- add stable ordering for Geography code generation
- update documentation for base declaration

## 4.5.1 (2024-07-10)

### Fix

- preserve pydantic 1 compatibility

## 4.5.0 (2024-07-09)

### Feat

- add GenericEstimate object to openEPD
- auto-generate geography definitions

### Fix

- correct the implementation of model type field attribute access

## 4.4.0 (2024-07-08)

### Feat

- add LIME2 LCIA method to supported methods

## 4.3.0 (2024-07-04)

### Feat

- add mypy plugin for modified Pydantic base model metaclass

## 4.2.0 (2024-07-02)

### Feat

- expose Pydantic fields via class dot access

### Refactor

- remove duplication in `forest_practices_certifiers` field

## 4.1.0 (2024-06-27)

### Feat

- **specs**: add PlasterV1 category specs

## 4.0.0 (2024-06-26)

### Feat

- add declared_units field for PCR

### Fix

- correct examples for Org.subsidiaries for openapi

### Refactor

- move PcrRef to models

## 3.5.1 (2024-06-13)

### Fix

- correct org/subsidiaries structure

## 3.5.0 (2024-06-10)

### Feat

- **api**: extend API client with EPD manipulation methods

## 3.4.1 (2024-06-05)

### Fix

- **specs**: resolve typo in `vertical_rize` -> `vertical_rise`

## 3.4.0 (2024-06-03) [YANKED]

### Feat

- **specs**: add `EscalatorsV1` properties
- **specs**: add `EscalatorsV1` category specs

## 3.3.0 (2024-05-30)

### Feat

- **specs**: add `element_type` property to PrecastConcrete specification
- **specs**: add `CivilPrecast` subtype to PrecastConcrete

## 3.2.0 (2024-05-27)

### Feat

- **specs**: add `Other` as a GypsumFireRating value

### Fix

- add descriptions to all specs

## 3.1.4 (2024-05-03)

### Fix

- correct json_schema modifiers for models

## 3.1.3 (2024-05-03)

### Fix

- add consolidated validators for quantity types

### Refactor

- clean up old material specs

## 3.1.2 (2024-04-23)

### Fix

- add validation for ratio type for Cementitious

### Refactor

- clean up Opening documentation
- clean up Concrete documentation
- clean up steel documentation

## 3.1.1 (2024-04-22)

### Fix

- add validation for ratio type for Cementitious

## 3.1.0 (2024-04-12)

### Feat

- support new Aggregate specs
- add semantic types for cementitious and some enums
- add initial scaffolded openepd pydantic models

### Fix

- correct initial apidocs for all openepd specs
- correct pydantic validation error propagation
- add fix and test for random read from real DB openepd specs
- clean up generated code, lint it

### Refactor

- clean up and rename the specs interfaces
- extract forest practices certifiers interface

## 3.0.0 (2024-04-06)

### Feat

- add pydantic 2.0 support

## 1.10.0 (2024-03-18)

### Feat

- extend quantity validator interface with less than and more than methods
- add more quantity types

## 1.9.0 (2024-03-12)

### Feat

- add type aliases for some quantity types

### Fix

- add default _EXT_VERSION to where it was missing

## 1.8.0 (2024-03-06)

### Feat

- add placeholder specs for Concrete children
- update `PrecastConcreteV1` to the new parameters

### Fix

- extend Concrete ACI exposure classes with missing values
- fix typing issues and allow nullability for some properties

## 1.7.2 (2024-03-06)

### Fix

- add commit to test versioning

## 1.7.1 (2024-03-05)

### Fix

- correct content and docs of Concrete exposure classes enums

## 1.7.0 (2024-03-04)

### Feat

- add more specs for materials
- add logic for replacing Impacts LCIA method

### Refactor

- extract semantic types for pydantic models

## 1.6.1 (2024-02-29)

### Fix

- correct conditional quantity validator

## 1.6.0 (2024-02-28)

### Feat

- support external quantity validators
- map models for Steel and Concrete

## 1.5.0 (2024-02-22)

### Feat

- implement factory function for EPD
- change spec structure to nested
- add `openepd_version` to EPD
- add material spec versions
- add initial specs named after categories
- add Readme on versioning specs

### Fix

- add test action
- fix broken tests

### Refactor

- generalize versions for other document types
- split validation to numbers and common

## 1.4.0 (2024-02-14)

### Feat

- add TypicalApplication spec for Concrete

## 1.3.3 (2024-02-09)

### Fix

- fix email-validator dependency

## 1.3.2 (2024-02-09)

### Fix

- enable serialization by alias when creating a bundle

## 1.3.1 (2024-01-03)

### Fix

- correct the retry logic for http client

### Refactor

- add retry count parameter for HTTP Client

## 1.3.0 (2023-10-12)

### Feat

- change type of PCR date fields to `datetime`

### Fix

- treat None as empty list for `epd.includes` field

## 1.2.0 (2023-09-26)

### Feat

- **epd**: update product image field

## 1.1.0 (2023-09-19)

### Feat

- add openEPD API client (just a few methods)

## 1.0.0 (2023-07-22)

### Feat

- preserve pydantic v1 support in separate branch

## 0.12.0 (2023-07-11)

### Feat

- **bundle**: add bundle writer
- **bundle**: add bundle models and bundle reader

## 0.11.2 (2023-07-04)

### Fix

- update dependencies

## 0.11.1 (2023-06-21)

### Fix

- change `Impacts` class definition to resolve deserialization issue

## 0.11.0 (2023-06-15)

### Feat

- add `hq_location` to Org, remove `contacts` from Org
- add `epd_developer_email` field
- add `third_party_verifier_email` field
- add location related objects
- add `epd_developer` field
- add `to_serializable` method to the base model
- relax validation

### Fix

- fix `get_typed_ext_field` behavior to handle missing data properly

## 0.10.0 (2023-06-10)

### Feat

- add base class for openEPD extensions

## 0.9.0 (2023-06-09)

### Feat

- add convenience method for reading typed objects from ext

### Fix

- fix impacts structure

## 0.8.1 (2023-06-08)

### Fix

- add missing base class for mixins

## 0.8.0 (2023-06-08)

### Feat

- extend base model with `set_ext_field_if_any` method
- add `alt_ids` field

### Fix

- add missing `gwp-fossil` impact

## 0.7.0 (2023-06-07)

### Feat

- add flows and indicators

## 0.6.0 (2023-06-02)

### Feat

- add missing fields to `Epd` model
- add convenience `to_quantity_str` method to `Amount`

## 0.5.0 (2023-06-01)

### Feat

- add utility methods to work with extensions

## 0.4.0 (2023-05-29)

### Feat

- add `address` field to the contact entity

## 0.3.0 (2023-05-29)

### Feat

- add `lca_discussion` field to EPD model
- add `CMU` spec

### Refactor

- move `Standard` into dedicated module

## 0.2.0 (2023-05-26)

### Feat

- add `compliance` field to EPD model
- remove `ExternalIdentification` model
- add `is_allowed_field` method to base model class

## 0.1.3 (2023-05-25)

### Fix

- add typing markers

## 0.1.2 (2023-05-25)

### Fix

- fix `pcr.product_classes` definition
- rename module orgs -> org

## 0.1.1 (2023-05-25)

### Fix

- fix package metadata

## 0.1.0 (2023-05-24)

### Feat

- add impacts, resources, output flows
- add Pcr model
- add Epd model (incomplete)
- add plant entity definition
- add Org model definition and a few base models
- add library skeleton
