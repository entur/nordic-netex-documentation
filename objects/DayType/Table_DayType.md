## Structure Overview

```text
DayType
 â”œâ”€ @id (1..1)
 â”œâ”€ @version (1..1)
 â”œâ”€ Name (1..1)
 â”œâ”€ Description (0..1)
 â””â”€ properties (0..1)
    â””â”€ PropertyOfDay (0..n)
       â”œâ”€ DaysOfWeek (0..1)
       â”œâ”€ Seasons (0..1)
       â”œâ”€ HolidayTypes (0..1)
       â””â”€ Tides (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the DayType | DayType/@id |
| @version | String | 1..1 | Version label | DayType/@version |
| Name | String |  | Human-readable name of the day classification | DayType/Name |
| Description | String |  | Additional description of the DayType | DayType/Description |
| PropertyOfDay | Element | 0..n | Operational characteristic of the day type | DayType/properties/PropertyOfDay |
| DaysOfWeek | String | 0..1 | Space-separated list of day names (Monday Tuesday Wednesday Thursday Friday Saturday Sunday) | DayType/properties/PropertyOfDay/DaysOfWeek |
| Seasons | SeasonEnum |  | Seasonal classification: `Spring`, `Summer`, `Autumn`, `Winter`, `Perennial` | DayType/properties/PropertyOfDay/Seasons |
| HolidayTypes | HolidayTypeEnum |  | Holiday classification: `AnyDay`, `WorkingDay`, `SchoolDay`, `NotHoliday`, `AnyHoliday`, `NationalHoliday`, `RegionalHoliday`, `EveOfHoliday`, `HolidayDisplacementDay` | DayType/properties/PropertyOfDay/HolidayTypes |
| Tides | TideEnum |  | Tide classification: `HighTide`, `LowTide`, `NeapTide` (for ferry/water transport) | DayType/properties/PropertyOfDay/Tides |
