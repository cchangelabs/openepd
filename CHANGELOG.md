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
