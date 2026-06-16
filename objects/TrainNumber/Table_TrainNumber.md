## Structure Overview

```text
TrainNumber
 ├─ @id (1..1)
 ├─ @version (1..1)
 └─ ForAdvertisement (0..1)
```

## Table

| Element | Type | NP | Description | Path |
|---------|------|----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the TrainNumber | TrainNumber/@id |
| @version | String | 1..1 | Version label | TrainNumber/@version |
| ForAdvertisement | String | 0..1 | The train number as advertised to passengers (e.g. "41") | TrainNumber/ForAdvertisement |
