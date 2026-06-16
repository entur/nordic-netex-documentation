# Parking

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#parking)*

## 1. Purpose

The **Parking** represents a parking facility associated with public transport, such as a park-and-ride lot, a bike parking area, or a car park at a station. It is used within a SiteFrame to describe the type, location, and characteristics of parking infrastructure that supports multimodal transport.

## 2. Structure Overview

```text
Parking
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (1..1)
  ├─ 📁 Centroid (0..1)
  │  └─ 📁 Location (1..1)
  │     ├─ 📄 Longitude (1..1)
  │     └─ 📄 Latitude (1..1)
  ├─ 📄 Covered (0..1)
  ├─ 🔗 ParentSiteRef/@ref (0..1)
  ├─ 📄 ParkingType (0..1)
  ├─ 📄 ParkingVehicleTypes (0..1)
  ├─ 📄 ParkingLayout (0..1)
  ├─ 📄 TotalCapacity (0..1)
  ├─ 📄 RechargingAvailable (0..1)
  ├─ 📄 ParkingPaymentProcess (0..1)
  └─ 📁 parkingProperties (0..1)
     └─ 📁 ParkingProperties (0..*)
        └─ 📁 spaces (0..1)
           └─ 📁 ParkingCapacity (0..*)
              ├─ 📄 ParkingUserType (1..1)
              ├─ 📄 NumberOfSpaces (0..1)
              └─ 📄 NumberOfSpacesWithRechargePoint (0..1)
```

## 3. Key Elements

- **@id**: Unique identifier following the `{CODESPACE}:Parking:{LocalId}` pattern.
- **@version**: Version number for tracking changes.
- **Name**: Human-readable name of the parking facility (e.g., "Park and Ride Example").
- **ParkingType**: Categorizes the parking facility (e.g., `parkAndRide`, `liftShareParking`, `urbanParking`).

## 4. References

- [StopPlace](../StopPlace/Table_StopPlace.md) -- parking facilities are often co-located with or serve a StopPlace.
- [Quay](../Quay/Table_Quay.md) -- passengers may use parking before accessing a specific Quay.

## 5. Usage Notes

### 5a. Consistency Rules

- Each Parking must have a unique `@id` within the delivery.
- The ParkingType should accurately reflect the intended use of the facility.

### 5b. Validation Requirements

- **@id is mandatory** -- must follow the NeTEx identifier pattern.
- **@version is mandatory** -- must be provided for change tracking.
- **Name is mandatory** -- every Parking must have a human-readable name.

### 5c. Common Pitfalls

> [!WARNING]
> - **Wrong ParkingType**: Ensure the type matches the actual facility — `parkAndRide` is for transit-adjacent parking, not general urban parking.
> - **Missing link to StopPlace**: While not structurally required, parking facilities should be logically associated with the stop or station they serve.

## 6. Additional Information

See [Table_Parking.md](Table_Parking.md) for detailed attribute specifications.

Example XML: [Parking.xml](Parking.xml)
