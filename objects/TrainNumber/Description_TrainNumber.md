> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#trainnumber)*

# TrainNumber

## 1. Purpose

A **TrainNumber** represents a railway-specific service number advertised to passengers (e.g. train 41 Oslo–Bergen). In the Nordic Profile, train numbers are typically referenced via JourneyPart rather than directly on ServiceJourney, where PrivateCode/PublicCode is preferred for the journey-level identifier.

## 2. Structure Overview

```text
📄 @id (1..1)
📄 @version (1..1)
📄 ForAdvertisement (0..1)
```

## 3. Key Elements

- **@id, @version** – Unique identifier and version label
- **ForAdvertisement** – The train number string shown to passengers (e.g. "41", "601")

## 4. References

TrainNumber does not reference other objects. It is referenced by:
- JourneyPart – Via TrainNumberRef (links a segment of a ServiceJourney to its advertised number)

## 5. Usage Notes

### 5d. Profile-Specific Notes

- **NP (railway):** Train numbers are used for long-distance and regional rail. A ServiceJourney may have multiple JourneyParts, each with its own TrainNumber (e.g. when a train splits/joins).
- For bus, tram, metro: Use `Line/PublicCode` or `ServiceJourney/PrivateCode` instead.

## 6. Additional Information

For the full element specification, see [Table — TrainNumber](Table_TrainNumber.md).
Example XML: [Example_TrainNumber_NP.xml](Example_TrainNumber_NP.xml)
