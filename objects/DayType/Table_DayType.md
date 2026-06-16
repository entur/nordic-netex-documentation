## Structure Overview

```text
DayType
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ Description (0..1)
 └─ properties (0..1)
    └─ PropertyOfDay (0..n)
       ├─ DaysOfWeek (0..1)
       ├─ Seasons (0..1)
       ├─ HolidayTypes (0..1)
       └─ Tides (0..1)
```

## Table

| Element | Type | MIN | NP | FR | SLO | Description | Path |
|---------|------|-----|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | 1..1 | Unique identifier for the DayType | DayType/@id |
| @version | String | 1..1 | 1..1 | 1..1 | 1..1 | Version label | DayType/@version |
| Name | String | 1..1 |  | 1..1 | 1..1 | Human-readable name of the day classification | DayType/Name |
| Description | String |  |  | 0..1 |  | Additional description of the DayType | DayType/Description |
| PropertyOfDay | Element |  | 0..n | 0..n | 1..n | Operational characteristic of the day type | DayType/properties/PropertyOfDay |
| DaysOfWeek | String |  | 0..1 | 0..1 | 1..1 | Space-separated list of day names (Monday Tuesday Wednesday Thursday Friday Saturday Sunday) | DayType/properties/PropertyOfDay/DaysOfWeek |
| Seasons | SeasonEnum |  |  | 0..1 |  | Seasonal classification: `Spring`, `Summer`, `Autumn`, `Winter`, `Perennial` | DayType/properties/PropertyOfDay/Seasons |
| HolidayTypes | HolidayTypeEnum |  |  | 0..1 | 0..1 | Holiday classification: `AnyDay`, `WorkingDay`, `SchoolDay`, `NotHoliday`, `AnyHoliday`, `NationalHoliday`, `RegionalHoliday`, `EveOfHoliday`, `HolidayDisplacementDay` | DayType/properties/PropertyOfDay/HolidayTypes |
| Tides | TideEnum |  |  | 0..1 |  | Tide classification: `HighTide`, `LowTide`, `NeapTide` (for ferry/water transport) | DayType/properties/PropertyOfDay/Tides |
