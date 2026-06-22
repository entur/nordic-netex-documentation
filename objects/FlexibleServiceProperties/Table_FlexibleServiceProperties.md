# FlexibleServiceProperties

## Structure Overview

```text
FlexibleServiceProperties
  â”œâ”€ @id (1..1)
  â”œâ”€ @version (1..1)
  â”œâ”€ BookingMethods (0..1)
  â”œâ”€ BookingAccess (0..1)
  â”œâ”€ BookWhen (0..1)
  â””â”€ LatestBookingTime (0..1)
```

## Table

| Element | Type | Description | Path |
|---------|------|-------------|------|
| @id | ID | Unique identifier for the flexible service properties | FlexibleServiceProperties/@id |
| @version | String | Version number for change tracking | FlexibleServiceProperties/@version |
| BookingMethods | String | Accepted booking methods (e.g., online, callOffice) | FlexibleServiceProperties/BookingMethods |
| BookingAccess | Enum | Who may book (e.g., public) | FlexibleServiceProperties/BookingAccess |
| BookWhen | Enum | When booking must be made (e.g., untilPreviousDay) | FlexibleServiceProperties/BookWhen |
| LatestBookingTime | Time | Latest allowed booking time | FlexibleServiceProperties/LatestBookingTime |
