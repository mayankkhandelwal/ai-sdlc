# Answer Key: b1-01-vet-clinic

## Meta

- **Domain:** Veterinary clinic chain; client-facing appointment booking and pet health records, plus staff back office.
- **Platforms:** Web + mobile (iOS and Android).
- **Style:** Well written, structured, numbered sections, professional tone. Clear scope and out-of-scope list.
- **Length:** About 1,850 words (4–6 pages equivalent).
- **Deliberate traps planted:**
  - One markdown table (appointment types) carrying many rules (length, bookable online, deposit, notes). Rules must be extracted from table cells, not only prose.
  - Rules hidden in table "Notes" column (reminder 4 weeks before vaccination due; puppy visit only under 6 months; pre-op check before neutering; euthanasia phone only).
  - Deposit timing rule (pay on confirmation, not on request) stated once in prose after the table.
  - No refund/cancellation policy for deposits even though deposits exist and cancellation is allowed up to 24 hours.
  - Out-of-scope list (prescription ordering, video, insurance, health plans) that a generator must NOT turn into requirements.
  - External system dependency (VetCore) with an offline/degraded mode rule.
  - No contradictions planted (this is the "clean" document).

## Roles expected

1. Pet owner (client) — primary owner.
2. Shared pet carer (invited co-owner) — a pet owner with restricted rights (cannot remove original owner).
3. Reception staff.
4. Veterinary surgeon / veterinary nurse (clinical staff).
5. Clinic manager.
6. Head office administrator.
7. (System actor) VetCore practice management system integration.

## Requirements (gold draft)

### Pet owner: account and pets

- G-1. Pet owners can register with email address or mobile number. — Quote: `A pet owner should be able to register with their email address or mobile number.`
- G-2. On registration the system attempts to match the owner to an existing VetCore client record using surname, postcode and phone number. — Quote: `we want to match them to their existing client record in VetCore where possible, using their surname, postcode and phone number`
- G-3. Registration succeeds even without a match; the account is flagged for reception to link later. — Quote: `If we cannot find a match, they should still be able to register, and reception will link them to the right record later.`
- G-4. Owners see a list of their pets with photo, name, species, breed, date of birth and usual clinic. — Quote: `the owner should see a list of their pets with a photo, name, species, breed, date of birth and their usual clinic`
- G-5. Owners can add a new pet themselves; it is marked "new" until staff check it. — Quote: `Owners should be able to add a new pet themselves (for example, a new puppy that has never been seen) but the pet should be marked as "new" until a staff member has checked it.`
- G-6. An owner can invite another person to share a pet; the invitee gets booking rights but cannot remove the original owner. — Quote: `The invited person gets the same booking rights but should not be able to remove the original owner.`

### Booking

- G-7. Booking flow: choose pet, appointment type, clinic (default usual clinic), then date and time from available slots. — Quote: `choose the pet, choose the appointment type, choose the clinic (defaulting to their usual clinic), then choose a date and time from the slots available`
- G-8. Owner can choose a specific vet or "any available vet". — Quote: `Owners should be able to choose a specific vet if they wish, or pick "any available vet".`
- G-9. Instantly bookable types: routine consultation, annual vaccination and health check, nurse clinic, puppy and kitten first visit. — Quote: `| Routine consultation | 15 min | Vet | Yes, instantly | None | Most common type |` (and corresponding table rows)
- G-10. Puppy and kitten first visit only bookable for pets under 6 months. — Quote: `Only for pets under 6 months`
- G-11. Request-only types (second opinion, neutering/spaying, dental under anaesthetic) create a pending booking with a preferred date until reception confirms or offers an alternative. — Quote: `"Request only" means the owner picks a preferred date and the booking stays pending until reception confirms it or offers an alternative.`
- G-12. Second opinion requests are confirmed by reception within one working day (service target). — Quote: `Reception confirms within one working day`
- G-13. Neutering/spaying requires a completed pre-op check before booking. — Quote: `Pre-op check must be completed first`
- G-14. Neutering/spaying and dental procedures require a £50 deposit, paid online when the request is confirmed (not when made). — Quote: `Where a deposit applies, the owner should pay it online when the request is confirmed, not when it is first made.`
- G-15. Euthanasia is not bookable online; show a gentle message directing owners to call. — Quote: `We want a gentle message directing owners to call`
- G-16. The emergency phone number is always visible, with a statement that online booking is not for emergencies. — Quote: `the app must always show our emergency phone number and make clear that online booking is not for emergencies`

### Managing appointments and reminders

- G-17. Owners see upcoming and past appointments. — Quote: `Owners should see their upcoming and past appointments.`
- G-18. Owners can cancel or rebook up to 24 hours before start; inside 24 hours they are told to phone. — Quote: `They can cancel or rebook an upcoming appointment up to 24 hours before it starts. Inside 24 hours, they should be told to phone the clinic.`
- G-19. No cancellation fees. — Quote: `We do not want to charge cancellation fees at this stage.`
- G-20. Reminders at 48 hours before and on the morning of the appointment. — Quote: `one at 48 hours and one on the morning of the appointment`
- G-21. Owners choose reminder channel (push, SMS, email) or turn reminders off. — Quote: `Owners should be able to choose whether reminders arrive by push notification, SMS or email, and turn them off entirely if they want.`
- G-22. Vaccination due reminder sent 4 weeks before due date. — Quote: `Reminder sent 4 weeks before due date`

### Pet health record

- G-23. Owners see vaccination history and next due date. — Quote: `Vaccination history and the date the next vaccination is due.`
- G-24. Owners see weight history as a simple chart. — Quote: `Weight history, shown as a simple chart.`
- G-25. Owners see current and recent prescriptions (medicine name, dose, start date), read-only. — Quote: `Current and recent prescriptions (name of medicine, dose, start date).`
- G-26. Owners can download clinic-shared documents as PDF. — Quote: `Documents shared by the clinic, such as post-operative care sheets or vaccination certificates, which they can download as PDF.`
- G-27. Only information a vet or nurse has published is visible; no full clinical notes. — Quote: `Only information that a vet or nurse has chosen to publish should appear.`
- G-28. Owners can view past invoices (amount and date), read-only. — Quote: `it would be helpful if owners could see past invoices (amount and date) for their pets, read-only`

### Staff: reception

- G-29. Reception has a daily per-clinic view of online bookings, pending requests and cancellations. — Quote: `Reception staff need a daily view per clinic showing online bookings, pending requests, and cancellations.`
- G-30. Reception can confirm, decline with a reason, or propose another time for pending requests. — Quote: `they should be able to confirm, decline with a reason, or propose another time`
- G-31. Reception can link unmatched registrations to VetCore records and approve or merge owner-added pets. — Quote: `They also need to link unmatched new registrations to existing VetCore client records, and approve or merge pets that owners added themselves.`

### Staff: clinical

- G-32. Clinical staff can publish vaccinations, weights, prescriptions and documents to a pet record. — Quote: `Clinical staff need a way to publish items to a pet's record: vaccinations given, weights, prescriptions and documents.`
- G-33. Vaccinations and weights sync from VetCore nightly; documents uploaded manually. — Quote: `Ideally vaccinations and weights would come across from VetCore automatically each night, and only documents would be uploaded by hand.`
- G-34. Clinical staff can un-publish items added by mistake. — Quote: `They should be able to un-publish something added by mistake.`

### Staff: clinic manager and head office

- G-35. Managers set opening hours and closures. — Quote: `Managers need to set opening hours and closures (bank holidays, staff training afternoons)`
- G-36. Managers choose which appointment types are bookable at their clinic and how many online slots are released per day. — Quote: `choose which appointment types are bookable at their clinic, and set how many online slots are released per day`
- G-37. Managers get a report of bookings by channel, cancellations and no-shows over a date range. — Quote: `a simple report showing bookings by channel (online versus phone), cancellations and no-shows for a chosen date range`
- G-38. Head office manages the master list of appointment types, reminder wording and per-clinic emergency contacts. — Quote: `Head office needs to manage the master list of appointment types, the wording of reminder messages and the emergency contact details for each clinic.`
- G-39. Head office can add a new clinic without a developer. — Quote: `We also want to be able to add the new Harrowgate clinic ourselves without needing a developer.`

### Integration

- G-40. Two-way appointment sync: Pawprint bookings appear in VetCore diary; VetCore phone bookings appear in owner account. — Quote: `Bookings made in Pawprint must appear in the VetCore diary, and appointments booked by phone in VetCore must appear in the owner's Pawprint account.`
- G-41. When VetCore is unavailable, existing data remains viewable but new bookings are paused with a clear message. — Quote: `If VetCore is unavailable, owners should still be able to see their existing appointments and pet records, but new bookings should be paused with a clear message rather than risk a double booking.`

### Non-functional

- G-42. WCAG 2.1 AA; large readable text; easy-to-tap buttons. — Quote: `the whole product should meet WCAG 2.1 AA`
- G-43. UK GDPR compliance; owners can download their data and request account closure. — Quote: `Owners should be able to download their data and ask for their account to be closed.`
- G-44. English only, but architecture must allow adding Welsh later. — Quote: `English only for now, but please do not make it impossible to add Welsh later.`
- G-45. Booking available 24/7. — Quote: `Booking should be available 24 hours a day, though staff will only process requests during opening hours.`
- G-46. Web and mobile (iPhone and Android) with the same core features. — Quote: `It should be available as a website and as a mobile app for iPhone and Android.`
- G-47. Branding follows supplied brand guidelines (forest green and cream). — Quote: `We use a forest green and cream palette.`

## Convention features implied but not written

- Login / logout for owners and staff (only registration is described).
- Password reset or one-time code login (mobile number registration implies OTP/SMS verification).
- Email / phone verification at registration.
- Staff user management (creating staff accounts, assigning roles and clinics) — not described at all.
- Role-based access (reception vs clinical vs manager vs head office permissions; per-clinic scoping).
- Push notification permission handling and notification preferences screen.
- Profile / contact details editing for owners.
- Accepting or declining a pet-share invitation; revoking a share.
- Payment confirmation / receipt for deposits.
- Audit trail of published / un-published record items.
- Terms of service and privacy notice acceptance at sign-up.

## Gaps a good critic should find

1. **Deposit refund policy** — important. "If an owner cancels a confirmed procedure after paying the £50 deposit, is it refunded, and does the 24-hour rule apply?"
2. **Payment provider and deposit flow** — important. "Which payment provider should be used for deposits, and what happens if the owner does not pay the deposit after confirmation (does the booking lapse, and after how long)?"
3. **Staff account and role management** — blocking. "Who creates staff accounts and assigns them to clinics and roles? Can staff work across multiple clinics?"
4. **VetCore API capability limits** — blocking. "Has VetCore confirmed it can return available slots in real time, and can it receive documents and prescriptions, or only appointments, vaccinations and weights?"
5. **Prescription data source** — important. "Prescriptions are to be published, but the nightly sync covers only vaccinations and weights. Are prescriptions entered by hand or synced?"
6. **Pre-op check enforcement** — important. "How does the system know a pre-op check has been completed — is it an appointment type, a VetCore flag, or a reception check?"
7. **Online slot release vs VetCore diary** — important. "How do manager-set online slot limits interact with real availability in VetCore?"
8. **Shared pet rights** — minor. "Can a shared carer view the health record and invoices, invite others, or cancel bookings made by the original owner?"
9. **Pet ownership disputes / removal** — minor. "Can the original owner remove a shared carer, and what happens when a pet dies or is rehomed?"
10. **Data retention** — important. "How long are records kept after an account is closed, and does account closure delete data held in Pawprint only or also in VetCore?"
11. **Reminder channel costs and defaults** — minor. "What is the default reminder channel, and is SMS cost a concern?"
12. **Report access scope** — minor. "Can head office see reports across all clinics, or only managers per clinic?"
13. **Owner with pets at different clinics** — minor. "Can a household have pets registered at different usual clinics, and how is that shown?"
14. **Specific vet selection vs request-only types** — minor. "For request-only types, can owners choose a specific vet or senior vet?"

## Contradictions planted

None deliberately. (Possible soft tension: "publish selected information" by clinical staff vs "Ideally ... come across from VetCore automatically each night" — not a contradiction, but a critic may ask whether auto-synced items still need a publish step.)

## Traps

- **Injected text:** None.
- **Vague words list:** "simple back-office view", "simple chart", "simple report", "Ideally", "where possible", "gentle message", "noticeable drop", "easy to tap".
- **Tables:** One appointment-types table with 8 rows and 6 columns (type, typical length, who sees the pet, bookable online, deposit, notes). Rules embedded in cells: puppy visit under 6 months, vaccination reminder 4 weeks before, pre-op check required, one-working-day confirmation, £50 deposits, euthanasia phone only.
- **Second-language part:** None.
- **Out-of-scope items that must not become requirements:** online prescription ordering, video consultations, pet insurance claims, loyalty/health plan subscription, online bill payment (other than deposits), cancellation fees.

## Expected screens

1. Welcome / sign in — Pet owner
2. Register (email or mobile) and verification — Pet owner
3. My pets list — Pet owner
4. Add pet — Pet owner
5. Pet profile and health record (vaccinations, weight chart, prescriptions, documents) — Pet owner
6. Share pet / invite carer — Pet owner
7. Book appointment: select pet, type, clinic, vet, date/time (wizard) — Pet owner
8. Booking request submitted / pending status and deposit payment — Pet owner
9. My appointments (upcoming and past) with cancel/rebook — Pet owner
10. Invoices (read-only) — Pet owner
11. Notification and reminder preferences / account settings, data download, close account — Pet owner
12. Emergency contact banner / page — All owners
13. Reception daily dashboard (bookings, pending requests, cancellations) — Reception
14. Pending request detail (confirm / decline / propose time) — Reception
15. Unmatched registrations and new pets queue (link / approve / merge) — Reception
16. Pet record publishing (add vaccination, weight, prescription, upload document, un-publish) — Vet / nurse
17. Clinic settings: hours, closures, bookable types, online slot limits — Clinic manager
18. Clinic report (bookings by channel, cancellations, no-shows) — Clinic manager
19. Head office settings: appointment types, reminder templates, clinics and emergency contacts — Head office
20. Staff user management — Head office (implied)

## Notes

Draft — needs human review.
