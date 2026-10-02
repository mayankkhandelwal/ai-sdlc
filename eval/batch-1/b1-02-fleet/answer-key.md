# Answer Key: b1-02-fleet

## Meta

- **Domain:** Logistics / haulage; fleet maintenance and defect tracking for workshop staff and drivers.
- **Platform:** Web only (mobile browser for drivers, desktop PC and tablet for workshop). Explicitly no native app.
- **Style:** Short, informal email, bullet lists, vague language, half-decided points ("We can sort that later"), no structure beyond two bullet groups.
- **Length:** About 520 words.
- **Deliberate traps planted:**
  - Vague words throughout ("simple", "fast", "easy", "etc.", "that kind of thing", "whatever makes sense", "if it's not too much hassle").
  - Approval authority missing: who can sign a vehicle back on the road is explicitly undecided.
  - No definition of who classifies defect severity, or of the defect categories themselves.
  - Optional / maybe features ("maybe stock levels", "Maybe some reports", "pull in mileage somehow") that should be captured as tentative, not firm.
  - External dependency of unknown feasibility (telematics API).
  - Offline / poor-signal hint ("Signal ... is rubbish") which implies an offline requirement without stating one.
  - Data migration from a spreadsheet.
  - Hard deadline tied to an external regulator visit, with no date.

## Roles expected

1. Driver.
2. Workshop technician / mechanic ("workshop lads").
3. Workshop supervisor (approver for return to road; undecided).
4. Fleet & workshop manager (Gareth; likely admin).
5. Transport office / planner (read-only viewer, reports).
6. (Implied) System administrator.

## Requirements (gold draft)

- G-1. Drivers complete the daily walkaround check digitally (tyres, lights, mirrors, fluids, etc.), replacing the paper sheet. — Quote: `do their daily walkaround check on it (tyres, lights, mirrors, fluids, etc.) instead of the paper sheet`
- G-2. Drivers report a defect with a photo. — Quote: `report a defect with a photo`
- G-3. Drivers see whether their vehicle is OK to go out. — Quote: `see if their vehicle is OK to go out or not`
- G-4. Workshop sees all incoming defects, works them, and marks them fixed. — Quote: `see all the defects coming in, sort them out, mark them fixed`
- G-5. Workshop books vehicles in for services, MOTs, tacho calibration, LOLER inspections and similar. — Quote: `book vehicles in for services, MOTs, tacho calibration, LOLER on the tail lifts etc.`
- G-6. Per-vehicle maintenance history: work done, parts, technician. — Quote: `keep a history for each vehicle - what was done, parts, who did it`
- G-7. Advance warnings before inspections/services are due, MOT in particular (lead time undefined, "a few weeks"). — Quote: `get warned before stuff is due. MOT especially. Ideally a few weeks before but whatever makes sense`
- G-8. Track parts used per job; stock levels optional. — Quote: `track parts used, maybe stock levels if it's not too much hassle`
- G-9. Workshop classifies defects as immediate off-road vs can wait until next service. — Quote: `Workshop needs to be able to say which is which`
- G-10. A vehicle with an off-road defect shows as off road until signed off again. — Quote: `the vehicle should show as off road until it's signed off again`
- G-11. Sign-off back onto the road is restricted to an authorised role (role undecided). — Quote: `Not sure who should be allowed to sign it back on - probably the workshop supervisor, or Dave, or whoever's on.`
- G-12. Transport office sees vehicle availability each morning, read-only. — Quote: `would want to see which vehicles are available each morning so they can plan routes. They don't need to edit anything really, just look.`
- G-13. Reports for monthly meeting: cost per vehicle, defect counts (tentative). — Quote: `Maybe some reports for the monthly meeting, costs per vehicle, number of defects, that sort of thing.`
- G-14. Driver access via mobile browser; no app store install. — Quote: `We'd like it to work on the drivers' phones through the browser, no app store stuff.`
- G-15. Workshop uses office PCs and a shop-floor tablet (responsive layout). — Quote: `Workshop will mostly use the PCs in the office and a tablet on the shop floor.`
- G-16. Tolerate poor connectivity in the yard (offline capture / sync) — implied from: Quote: `Signal in the Kelling Road yard is rubbish so bear that in mind.`
- G-17. Import mileage from telematics if an API exists (tentative). — Quote: `it'd be good if it could pull in mileage somehow`
- G-18. One-off import of existing data from the spreadsheet. — Quote: `Existing data is all in the Excel so we'd need that loading in at the start.`
- G-19. Support two depots (vehicles assigned to a depot). — Quote: `we run about 140 vehicles out of two depots (Mossbridge and Kelling Road)`
- G-20. Support vehicle types (artic, rigid, van) with differing inspection needs. — Quote: `Mix of artics, rigids and a load of vans.`
- G-21. Fast, easy-to-use driver flow (usability NFR, unmeasured). — Quote: `Needs to be fast and easy, the drivers aren't going to faff about with anything complicated.`
- G-22. Records suitable for regulator inspection (audit trail of checks and repairs) — implied: the deadline is a regulator visit and paper sheets are being lost. — Quote: `We'd like something in place before the DVSA visit in the new year if possible.`

## Convention features implied but not written

- Login / logout for drivers, workshop and office staff; password reset.
- User and role management (who creates driver accounts, especially with driver turnover).
- Vehicle register management (add / edit / retire vehicles, registration, type, depot).
- Assigning a driver to a vehicle for the day (needed for "their vehicle").
- Notifications to workshop when a defect is reported; notifications to driver when vehicle is cleared.
- Search and filter on vehicles and defects.
- Photo upload handling and storage limits.
- Audit log (who signed what, when) — critical for compliance even though not stated.
- Data export (for reports / inspectors).

## Gaps a good critic should find

1. **Return-to-road approval authority** — blocking. "Which role(s) can sign a vehicle back on the road after an off-road defect, and does it need a second signature?"
2. **Who classifies defect severity** — blocking. "Does the driver, the workshop technician or the supervisor decide whether a defect takes the vehicle off the road, and what happens between report and classification — is the vehicle off road by default?"
3. **Walkaround checklist content** — important. "What exact items are on the walkaround check, and do they differ for artics, rigids and vans?"
4. **Failed walkaround check outcome** — important. "If a driver fails an item on the walkaround, does that automatically create a defect and block the vehicle?"
5. **Warning lead times and recipients** — important. "How far ahead should each inspection type warn (MOT, service, tacho, LOLER), and who receives the warning, by what channel?"
6. **Service intervals** — important. "Are services due by date, by mileage, or both, and where do the intervals come from?"
7. **Offline requirement** — important. "Must drivers be able to complete a walkaround with no signal and sync later?"
8. **Telematics integration** — minor (until vendor known). "Which telematics provider is used and does it expose an API; otherwise, should drivers enter mileage manually?"
9. **Parts and stock scope** — minor. "Is parts tracking just a free-text list per job, or a stock catalogue with quantities and reorder levels? Do you need part costs?"
10. **Cost data for reports** — important. "Costs per vehicle need labour and parts costs. Are labour rates and part prices entered in the system?"
11. **Transport office permissions** — minor. "Is the transport office strictly read-only, or can they mark a vehicle as allocated / report issues?"
12. **Data migration detail** — important. "What does the spreadsheet contain (columns, history depth), and how clean is it?"
13. **Deadline** — important. "What is the date of the regulator visit, and what is the minimum needed before then?"
14. **Record retention** — important. "How long must walkaround and repair records be kept for compliance?"
15. **External contractors** — minor. "Is any work (e.g. MOTs, tail lift inspections) done by outside contractors whose results must be recorded?"

## Contradictions planted

None deliberately. Soft tension: "keep it simple" / small budget vs a long feature list including stock, telematics and reports.

## Traps

- **Injected text:** None.
- **Vague words list:** "simple" (x2 incl. "keep it simple"), "fast", "easy", "etc." (x2), "that kind of thing", "that sort of thing", "whatever makes sense", "Ideally a few weeks", "maybe", "Maybe some reports", "if it's not too much hassle", "somehow", "really", "probably", "We can sort that later", "if possible", "a bit all over the place".
- **Missing approver:** sign-back-on authority explicitly undecided.
- **Tables:** None.
- **Second-language part:** None.
- **Domain jargon without definition:** walkaround, artics, rigids, MOT, tacho calibration, LOLER, DVSA, off road / VOR.

## Expected screens

1. Sign in — All users
2. Driver home: my vehicle today and road-worthy status — Driver
3. Daily walkaround check form — Driver
4. Report defect (with photo) — Driver
5. Workshop dashboard: incoming defects, off-road vehicles, upcoming due items — Workshop technician / supervisor
6. Defect detail: classify severity, assign, log work, mark fixed — Workshop technician
7. Return-to-road sign-off — Workshop supervisor
8. Vehicle list / fleet register — Workshop, Fleet manager
9. Vehicle detail and maintenance history — Workshop, Fleet manager
10. Workshop booking calendar (services, MOT, tacho, LOLER) — Workshop
11. Job card / work record (parts used, technician) — Workshop technician
12. Parts list / stock (optional) — Workshop
13. Daily availability board — Transport office
14. Reports (cost per vehicle, defects) — Fleet manager, Transport office
15. Users and roles admin — Fleet manager / admin (implied)
16. Data import (spreadsheet) — Admin (one-off)

## Notes

Draft — needs human review.
