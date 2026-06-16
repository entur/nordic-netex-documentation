# FlexibleServiceProperties

## Structure Overview

```text
FlexibleServiceProperties
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ BookingMethods (0..1)
  ├─ BookingAccess (0..1)
  ├─ BookWhen (0..1)
  └─ LatestBookingTime (0..1)
```

## Table

| Element | Type | MIN | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the flexible service properties | FlexibleServiceProperties/@id |
| @version | String | 1..1 | Version number for change tracking | FlexibleServiceProperties/@version |
| BookingMethods | String |  | Accepted booking methods (e.g., online, callOffice) | FlexibleServiceProperties/BookingMethods |
| BookingAccess | Enum |  | Who may book (e.g., public) | FlexibleServiceProperties/BookingAccess |
| BookWhen | Enum |  | When booking must be made (e.g., untilPreviousDay) | FlexibleServiceProperties/BookWhen |
| LatestBookingTime | Time |  | Latest allowed booking time | FlexibleServiceProperties/LatestBookingTime |
