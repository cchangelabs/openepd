# Material Extensions

This package contains openEPD material extensions. They are used to represent the material properties of the openEPD
materials, and are a more dynamic, frequently changing part of the standard.

## Versioning

Extensions are versioned separately from the openEPD standard or openEPD API.

Each material extension is named after the corresponding EC3 product class, and is located in the relevant place
in the specs tree. For example, `RebarSteel` is nested under `Steel`.

Extensions are versioned as Major.Minor, for example "2.4".

Rules:

1. Minor versions for the same major version should be backwards compatible.
2. Major versions are not compatible between themselves.
3. Pydantic models representing versions are named in a pattern SpecNameV1, where 1 is major version and SpecName is
   the name of the material extension.

## Range specs

Normal EPDs get singular specs (e.g. `SteelV1`). Single specs can express performance parameters of one concrete
material/EPD. However, the IndustryEDPs and Generic Estimates often cover a specific segment of the market, and
include a range of products under the hood, thus demanding for ranges. For example, a single EPD has one `strength_28d`
of `4000 psi`, but an industry EPD can be applicable to certain concretes in the range of `4000 psi` to `5000 psi`.

Range specs are used to express that. Range specs are located in `specs.range` package, and are auto-generated from the
single specs, please see `make codegen` command and `tools/openepd/codegen/generate_range_spec_models.py`

Range specs are created by following general rules:

1. A QuantityStr (such as `QuantityMassKg`) becomes an `AmountRange` of certain type - `AmountRangeMass`
2. Float -> RangeFloat, Ratio -> RatioRange, int -> IntRange
3. Enums become lists of enums, for example: `cable_trays_material: enums.CableTrayMaterial` in normal spec becomes a
   `cable_trays_material: list[enums.CabeTrayMaterial]` in the range spec.
4. Complex objects, strings remain unchanged.

This is, however, not always desired. For example, `recarbonation: float` and `recarbonation_z: float` property of CMU
should not be converted to ranges as these do not make sense.

The default rule-base behaviour can be overridden with the
`CodeGenSpec` class annotation like this: `recarbonation: Annotated[float, CodeGenSpec(override_type=float)]` in single
spec to make RangeSpec have normal `float` type.
