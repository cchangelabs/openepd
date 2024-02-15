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
