# Line

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#line)*

## 1. Purpose
The **Line** represents a public transport service line within a ServiceFrame. It is a core organizational entity that groups together related routes and journeys providing the same public transport service (e.g., "Bus Line 5" or "Train Line 101"). A Line identifies the operator, provides visual presentation properties (colors), and serves as the container for route patterns and scheduled journeys.

## 2. Structure Overview
```text
Line
 ├─ 📄 @id (1..1)
 ├─ 📄 @version (1..1)
 ├─ 📄 Name (1..1)
 ├─ 📄 TransportMode (1..1)
 ├─ 📁 TransportSubmode (0..1)
 │  ├─ 📄 BusSubmode (0..1)
 │  ├─ 📄 RailSubmode (0..1)
 │  ├─ 📄 WaterSubmode (0..1)
 │  ├─ 📄 TramSubmode (0..1)
 │  ├─ 📄 MetroSubmode (0..1)
 │  ├─ 📄 AirSubmode (0..1)
 │  ├─ 📄 CoachSubmode (0..1)
 │  └─ 📄 TelecabinSubmode (0..1)
 ├─ 🔗 OperatorRef/@ref (1..1)
 ├─ 📄 PublicCode (0..1)
 ├─ 📄 PrivateCode (0..1)
 ├─ 🔗 RepresentedByGroupRef/@ref (0..1)
 ├─ 📄 Monitored (0..1)
 ├─ 🔗 TypeOfLineRef/@ref (0..1)
 ├─ 📁 AccessibilityAssessment (0..1)
 │  ├─ 📄 MobilityImpairedAccess (1..1)
 │  └─ 📁 limitations (0..1)
 │     └─ 📄 AccessibilityLimitation (0..n)
 ├─ 📁 allowedDirections (0..1)
 │  └─ 📄 AllowedLineDirection (0..n)
 │     └─ 🔗 DirectionRef/@ref (1..1)
 ├─ 📁 documentLinks (0..1)
 │  └─ 📄 InfoLink (0..n)
 └─ 📁 Presentation (0..1)
    ├─ 📄 Colour (0..1)
    └─ 📄 TextColour (0..1)
```

## 3. Key Elements
- **Name**: Internal line identifier used in planning tools and administrative systems; describes the service rather than being shown to passengers.
- **TransportMode**: Primary public transport mode for the line (e.g., `bus`, `rail`, `water`, `tram`, `metro`). Mandatory in this profile.
- **TransportSubmode**: Optional refinement of the transport mode (e.g., `regionalBus`, `localRail`). Only one submode element should be present, matching the TransportMode.
- **OperatorRef**: Mandatory reference to the Operator responsible for running this Line; must resolve to an Operator defined in ResourceFrame.
- **Monitored**: Boolean indicating whether the line is tracked by a real-time monitoring system (AVL/APC). Used by journey planners to show real-time data availability.
- **TypeOfLineRef**: Reference to a TypeOfLine classification (e.g., commercial line, school line, replacement service).
- **AccessibilityAssessment**: Declares line-level accessibility. MobilityImpairedAccess is mandatory within it; limitations can list specific AccessibilityLimitation entries.
- **allowedDirections**: Defines which directions (inbound, outbound, etc.) are valid for this line.
- **documentLinks / InfoLink**: Collection of external information links about the line (timetable PDFs, passenger information URLs).
- **Presentation**: Optional container for visual presentation properties; defines line color and text color for passenger-facing displays.
- **Colour**: Hexadecimal color code (6 uppercase digits without `#`) for the line's visual representation; e.g., `005EB8` for blue.
- **TextColour**: Hexadecimal color code for text displayed on the line; typically contrasts with Colour for readability; e.g., `FFFFFF` for white.

## 4. References
- [Operator](../Operator/Table_Operator.md) – Organization responsible for operating this Line
- [Route](../Route/Table_Route.md) – Geographic path definition for journeys on this Line
- [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md) – Stop sequence patterns served by this Line

## 5. Usage Notes

### 5a. Consistency Rules
- A Line should have a unique Name within the scope of its Operator to avoid confusion in system references.
- The OperatorRef must be defined in ResourceFrame/organisations before the Line is referenced by Routes, JourneyPatterns, or ServiceJourneys.
- The Line @id is used as a trigger mechanism for fare products — sales systems use it to determine which products are valid for a given journey. Producers must ensure Line IDs are stable and consistent across deliveries.
- Presentation colors (Colour and TextColour) should be consistent across all visual touchpoints (websites, signage, information systems) to reinforce brand identity.
<!-- PROPOSAL: Document TransportSubmode as a product filtering mechanism. Non-departure-specific products (e.g. monthly tickets) may be filtered to the line with the highest frequency when multiple lines of different submodes serve the same stretch (local, longDistance, regional). Edge case relevant to producers, not passengers. -->

### 5b. Validation Requirements
- **Name is mandatory** – Every Line must have a Name element for public identification.
- **OperatorRef is mandatory** – Every Line must reference exactly one Operator with @ref attribute; cardinality is 1..1.
- **@id and @version are mandatory** – Must follow codespace conventions (e.g., `NP:Line:1`); version typically "1" or incremental.
- **Colour format is strict** – If Presentation is used, Colour must be exactly 6 uppercase hexadecimal digits (0–9, A–F) without a leading # character.
- **TextColour format is strict** – Same format requirements as Colour; recommended to ensure text-to-background contrast for accessibility.

### 5c. Common Pitfalls

> [!WARNING]
> - **Missing TransportMode**: TransportMode is mandatory in this profile (1..1). It must be one of the standard NeTEx modes: `bus`, `rail`, `water`, `tram`, `metro`, `air`, `coach`, `telecabin`.
> - **Presentation element mistakes**: Do NOT add `@id` or `@version` attributes to the Presentation element; it is a simple container with only child text elements.

> [!TIP]
> **Colour format**: Must be exactly 6 uppercase hexadecimal digits (0–9, A–F) without a leading `#`. Example: `005EB8` not `#005eb8`.

## 6. Additional Information
See [Table_Line.md](Table_Line.md) for detailed attribute specifications, cardinality rules, and XSD constraints.

```xml
<Line id="NP:Line:100" version="1">
  <Name>Arendal-Kristiansand</Name>
  <TransportMode>bus</TransportMode>
  <TransportSubmode>
    <BusSubmode>regionalBus</BusSubmode>
  </TransportSubmode>
  <PublicCode>100</PublicCode>
  <PrivateCode>100</PrivateCode>
  <OperatorRef ref="NP:Operator:923"/>
  <RepresentedByGroupRef ref="NP:Network:AKTNett"/>
  <Presentation>
    <Colour>000000</Colour>
    <TextColour>FFFF00</TextColour>
  </Presentation>
</Line>
```

→ [Full file](Example_Line_NP.xml)
