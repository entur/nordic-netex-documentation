## Structure Overview

```text
Vehicle
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ RegistrationNumber (0..1)
 ├─ OperatorRef/@ref (0..1)
 └─ VehicleTypeRef/@ref (1..1)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the Vehicle | Vehicle/@id |
| @version | String | Version label | Vehicle/@version |
| RegistrationNumber | String | Vehicle registration or license plate number | Vehicle/RegistrationNumber |
| [Operator](../Operator/Table_Operator.md)@ref | Reference | Reference to the operating organisation | Vehicle/OperatorRef/@ref |
| [VehicleType](../VehicleType/Table_VehicleType.md)@ref | Reference | Reference to the vehicle type definition | Vehicle/VehicleTypeRef/@ref |
