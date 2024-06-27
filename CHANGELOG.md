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

## 3.4.0 (2024-06-03)

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
