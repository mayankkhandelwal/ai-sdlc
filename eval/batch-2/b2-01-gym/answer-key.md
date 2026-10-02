# Answer key – b2-01-gym

## Meta

- **Domain:** Gym / fitness club chain – memberships, class booking, instructor and PT schedules. Member mobile app (iOS/Android) + web admin portal.
- **Style:** Formal client brief, numbered sections, written by an operations team. Uneven depth: extremely detailed on classes (section 4), thin or silent on payments, billing failures, refunds, auth, accessibility.
- **Length:** ~2,700 words.
- **Language:** English (UK).
- **Deliberate traps planted:**
  1. Silence on payment failure, refunds, pro-rata billing, and PT session payment.
  2. Membership tier table that encodes rules (allowances, booking windows, access hours) the reader must carry into booking logic.
  3. Off-Peak access hours vs. class bookings outside those hours – not resolved.
  4. Undecided platform choice (trainer side in the member app or separate app).
  5. Undecided permission for Area managers ("Not sure yet").
  6. Third-party turnstile API "we haven't looked at the details yet".
  7. Vague quality words ("modern and premium", "fast and easy").
  8. Real-sounding brand references deliberately removed; fictional vendor "GatePass Systems".

## Roles expected

1. Member (adult account holder)
2. Parent member booking for children (sub-case of Member; children are dependants without login)
3. Guest (non-user; receives QR by SMS/email, no login)
4. Class instructor (employee or freelance)
5. Personal trainer (PT)
6. Front desk staff
7. Club manager
8. Area manager
9. Head office admin
10. External system: turnstile (GatePass Systems API), direct debit provider

## Requirements (gold draft)

G-1. Provide a member mobile app on iOS and Android and a web admin portal. — Quote: "for club staff, trainers and head office." (paired with the bullet listing the member app for iOS and Android)
G-2. Members can join online in the app or at the front desk, choosing a home club and tier. — Quote: "Members can join online in the app or in person at the front desk. When joining they choose a home club and a tier."
G-3. Capture member personal details, emergency contact and a PAR-Q health questionnaire at joining. — Quote: "We collect name, date of birth, address, mobile, email, emergency contact and a short health questionnaire (PAR-Q)."
G-4. Flag the club and advise the member to speak to staff if any health question is answered yes. — Quote: "If they answer yes to any of the health questions, they should be told to speak to a member of staff before training, and the club should be flagged."
G-5. Support five membership tiers with price, access, monthly class allowance, booking window, guest passes and included PT sessions as per table. — Quote: "We currently sell five tiers."
G-6. Student members upload a student card photo at joining; staff approve it. — Quote: "We would like members to be able to upload a photo of their student card when they join and have staff approve it."
G-7. Class allowances reset on the 1st of each month with no rollover. — Quote: "Monthly class allowances reset on the 1st of each month. Unused bookings do not roll over."
G-8. Members can issue guest passes; guest receives a QR code by text or email; guests cannot book classes. — Quote: "The friend should get a QR code by text or email. Guests can't book classes."
G-9. Elite members get one 45-minute PT session per calendar month with a PT at their home club. — Quote: "The included PT session for Elite members is one 45-minute session per calendar month with any PT at their home club."
G-10. Charge a joining fee and let head office create promo codes waiving it or discounting the first month. — Quote: "Head office should be able to set up a promo code that waives the joining fee or gives a discount on the first month."
G-11. Collect monthly payments by direct debit via the existing provider (integration). — Quote: "Monthly payments will be taken by direct debit through our existing provider."
G-12. Upgrades apply immediately; downgrades apply from next billing date. — Quote: "Members can upgrade their tier at any time and it takes effect immediately."
G-13. Members can freeze membership up to 3 months per year; frozen members cannot book or enter. — Quote: "Members should be able to freeze their membership for up to 3 months per year. Frozen members can't book classes or enter the club."
G-14. Members can change home club once every 3 months. — Quote: "Members can change their home club once every 3 months."
G-15. Members can request cancellation in the app with 30 days' notice. — Quote: "Cancellation needs 30 days' notice. Members can request cancellation in the app."
G-16. Digital membership card with QR code, scanned at turnstiles at all clubs. — Quote: "Every member gets a digital membership card in the app with a QR code."
G-17. Turnstile denies entry outside tier access rules and the app shows the reason. — Quote: "the turnstile should not open and the member should see why on their phone."
G-18. Class record holds type, club, room, date/time, duration, instructor, capacity, intensity, equipment, description and photo. — Quote: "We run about 900 classes a week across all clubs. A class has:"
G-19. Members pick a numbered bike/bed from a room layout for equipment classes; layouts per studio. — Quote: "For those classes members should be able to pick their bike or bed number from a layout of the room when they book, like choosing a seat at the cinema. Each studio's layout is different."
G-20. Club managers build weekly timetables with copy-week and weekly repeat until a date. — Quote: "so they need to be able to copy a week or set a class to repeat weekly until a given date."
G-21. Timetables published 2 weeks ahead; classes outside booking window visible but marked with opening date. — Quote: "Timetables are published for 2 weeks ahead."
G-22. Booking opens at 7am on the day the window opens. — Quote: "Booking for a class opens at 7am on the day the window opens, not at midnight."
G-23. Timetable filters (club, type, instructor, time, intensity) and favourite classes/instructors. — Quote: "Members browsing the timetable should be able to filter by club, class type, instructor, time of day and intensity, and save favourite classes and favourite instructors."
G-24. Plus/Elite see all clubs; other tiers see home club only. — Quote: "Members on Plus and Elite can see and book classes at all clubs. Off-Peak, Core and Student members only see their home club."
G-25. One-tap booking that consumes allowance where the tier has a limit. — Quote: "Each booking uses one of the member's monthly class allowance if their tier has a limit."
G-26. Block overlapping bookings; max 10 future bookings. — Quote: "A member can hold a maximum of 10 future bookings at any one time."
G-27. My bookings list, confirmation notification and add-to-calendar. — Quote: "After booking, the class appears in"
G-28. Waitlist max 10; auto-promote first in line until 1 hour before start. — Quote: "When a place becomes free, the first person on the waitlist is automatically booked in and notified. This happens up until 1 hour before the class starts."
G-29. In the final hour, notify the whole waitlist and first to accept gets the place. — Quote: "Inside the last hour, instead of automatic booking, everyone on the waitlist is notified that a place is free and the first one to tap"
G-30. Waitlist join free; promotion consumes allowance; skip members with clashing bookings. — Quote: "Joining a waitlist does not use an allowance. Being promoted from the waitlist does."
G-31. Free cancellation up to 2 hours before; late cancel/no-show = strike; 3 strikes in 30 days = 7-day booking ban. — Quote: "Late cancellations and no-shows count as a strike. Three strikes in 30 days and the member cannot book for 7 days."
G-32. Members see their strikes and expiry; club managers can remove strikes. — Quote: "Members should be able to see their strikes in the app and when they expire."
G-33. Instructors take attendance by ticking names or scanning QR; auto no-show after 10 minutes. — Quote: "Anyone booked but not checked in within 10 minutes of the start time is marked as a no-show automatically."
G-34. Instructors can add walk-ins if space; counts toward allowance. — Quote: "Walk-ins: if there's space, instructors can add a member who turns up without booking. It still counts towards their allowance."
G-35. Manager cancels a class with reason; notify booked and waitlisted members by push and SMS; refund allowance; no strikes. — Quote: "Every booked member and everyone on the waitlist is notified straight away by push notification and SMS."
G-36. Notify booked members when instructor changes. — Quote: "If the instructor changes but the class goes ahead, booked members should be notified of the new instructor"
G-37. Post-class rating prompt (1–5 stars + comment); visibility limited to managers/head office; instructors see own average only. — Quote: "Instructors can see their own average rating but not individual comments."
G-38. Parents add children to profile and book kids classes for them; children have no login. — Quote: "The parent adds their children to their profile (name and date of birth) and books on their behalf. Children don't have their own login."
G-39. Instructors see their weekly timetable across clubs with class lists and booked numbers. — Quote: "Instructors should see their own timetable for all clubs they work at, a week at a time, with the class list and number booked for each class."
G-40. Instructors set weekly availability and away dates; timetable builder only offers available instructors. — Quote: "the timetable builder should only offer instructors who are available."
G-41. Cover requests to qualified instructors, manager approval, alert if uncovered 24h before. — Quote: "If nobody has accepted cover 24 hours before the class, the manager gets an alert."
G-42. Record instructor qualifications and certification expiry; warn 30 days before; block scheduling when expired. — Quote: "The system should warn managers 30 days before a certification expires and stop them being scheduled when it has expired."
G-43. Monthly report of classes taught per instructor (no payroll). — Quote: "At the end of each month club managers need a report of classes taught per instructor"
G-44. Members browse PT profiles (photo, bio, specialisms, qualifications). — Quote: "Members can browse PTs at their home club (or all clubs on Plus/Elite) with a photo, bio, specialisms and qualifications."
G-45. PTs publish slots; members request; PT accepts/declines. — Quote: "PTs set their available slots. Members request a session in a free slot and the PT accepts or declines."
G-46. PTs block time, see upcoming sessions, keep private client notes. — Quote: "PTs can block out time, see their upcoming sessions, and add short private notes against each client."
G-47. Private in-app messaging between PT and member. — Quote: "PTs should be able to message their clients in the app so they don't need to use WhatsApp."
G-48. Role-based admin access: front desk, club manager, area manager, head office. — Quote: "everything front desk can do for their club, plus timetable, rooms and studio layouts, instructor rotas, cancellations, strike removal, reports for their club."
G-49. Member search by name/email/mobile/number with full member view and staff notes. — Quote: "Staff should be able to search members by name, email, mobile or membership number"
G-50. Head office dashboard (members, attendance/fill rate, no-shows, waitlist demand, ratings, visits by hour), exportable to Excel; club-filtered for managers. — Quote: "Reports should be exportable to Excel. Club managers see the same reports filtered to their club."
G-51. Targeted announcements (one/several/all clubs) with optional push. — Quote: "targeted at one club, several clubs, or all members, and optionally send it as a push notification."
G-52. Member notification set incl. reminder 1 hour before (opt-out). — Quote: "reminder 1 hour before the class (members can turn this off)"
G-53. Instructor notifications for cover, timetable changes, cert expiry. — Quote: "Instructors should be notified of cover requests, timetable changes affecting them and cert expiry."
G-54. Migrate existing members from CSV export. — Quote: "We need to bring across our existing members from the current system. We can export to CSV."
G-55. GDPR compliance for health data. — Quote: "GDPR – we hold health information from the questionnaire."
G-56. Pilot at one club then full rollout (release planning constraint). — Quote: "We would like to launch at Harrowgate as a pilot in November and roll out to all clubs in January"
G-57. Out of scope: shop, nutrition/workout tracking, wearables, freelancer payments. — Quote: "Paying freelancers through the system."

Reviewer note on G-27: the source bullet continues with the My bookings label, a confirmation notification and an add-to-calendar option; the quote is truncated before inner quotation marks.

## Convention features implied but not written

- Member registration/login, password reset, (possibly) social login or magic link – none mentioned.
- Separate staff/instructor/PT authentication and role-based permissions.
- Profile management (edit contact details, emergency contact, children).
- Notification preferences screen (only reminder opt-out is mentioned).
- Account deletion / data export (GDPR rights).
- Terms & conditions / privacy consent at joining, direct debit mandate confirmation.
- Admin user management (creating staff accounts, assigning clubs).
- Audit trail for staff actions (strike removal, notes).
- Empty states, error handling, offline behaviour of the QR card.

## Gaps a good critic should find

1. **Blocking** – Payment failure: What happens when a direct debit fails? Is the member suspended, can they still book/enter, how many retries, who is notified?
2. **Blocking** – Refunds and pro-rata: How are upgrades (immediate), freezes and cancellations billed? Are there pro-rata charges or refunds?
3. **Blocking** – Direct debit integration: Which provider and what does the integration do (mandate setup in app vs. staff only, status sync)?
4. **Important** – PT session payment: How do non-Elite members pay for PT sessions, given PTs are self-employed? Is payment in or out of the app?
5. **Important** – Trainer platform: Should instructors/PTs use the member app with a different login or a separate app?
6. **Important** – Area manager permissions: Can area managers edit timetables or only view reports?
7. **Important** – Off-Peak class bookings: Can Off-Peak members book classes that start after 4pm on weekdays, given their access hours?
8. **Important** – Turnstile integration: What does the GatePass Systems API support, and what is the fallback if it is unavailable?
9. **Important** – Membership cancellation effects: What happens to future bookings, guest passes and included PT sessions during the 30-day notice period?
10. **Important** – Allowance exhausted: What happens on walk-in or waitlist promotion when the member has used their whole monthly allowance?
11. **Important** – PT session cancellation/no-show rules: Do strikes or cancellation windows apply to PT sessions?
12. **Minor** – Kids classes: Age limits, can one parent book several children into the same class, do kids bookings use the parent's allowance or earn strikes?
13. **Minor** – Guest passes: Are guest passes limited per guest, do unused ones roll over, which clubs can guests visit?
14. **Minor** – Accessibility: "including for our older members" – which accessibility standard should be met?
15. **Minor** – Student card re-verification: Does student status expire and need re-approval?
16. **Minor** – SMS costs/limits: Is SMS only for class cancellations, and for guest passes?
17. **Minor** – Data migration scope: Which data comes across (members only, or bookings, history, PT notes)?
18. **Minor** – Promo codes: Validity dates, usage limits, tier restrictions?

## Contradictions planted

None explicit. Tension to note (not a strict contradiction):
- Off-Peak access hours vs class booking. — Quote A: "Home club only, before 4pm on weekdays and all day at weekends" — Quote B: "Members on Plus and Elite can see and book classes at all clubs. Off-Peak, Core and Student members only see their home club." (Off-Peak members can see all home-club classes, including evening classes they could not enter the building for.)

## Traps

- **Injected text:** None in this document.
- **Vague words:** "modern and premium", "fast and easy to use", "roughly", "a couple of junior classes", "most weeks", "general enquiries", "maybe phase 2", "Not sure yet", "we haven't looked at the details yet", "etc." style lists ("things like").
- **Tables:** One membership tier table (5 rows × 7 columns) carrying rules for access, allowance, booking window, guest passes and PT sessions.
- **Language notes:** UK English (£, "programme", "colours"). Product name "Kettlebrook Move" may change. PAR-Q is a domain acronym (health questionnaire).

## Expected screens

Member app:
1. Onboarding / sign up (tier + home club selection, details, PAR-Q, student card upload) – Member
2. Login / password reset – Member
3. Home / dashboard (next bookings, announcements) – Member
4. Class timetable with filters – Member
5. Class detail + book / join waitlist – Member
6. Seat / bike / bed picker (room layout) – Member
7. My bookings (upcoming, waitlists, history, strikes) – Member
8. Digital membership card (QR) – Member
9. Membership management (upgrade/downgrade, freeze, change club, cancel) – Member
10. Guest pass issue – Member
11. PT directory, PT profile and session request – Member
12. Messages (PT chat) – Member / PT
13. Profile, children, notification settings – Member
14. Class rating prompt – Member

Instructor / PT:
15. My schedule (week view) + class list / attendance check-in – Instructor
16. Availability and away dates; cover requests – Instructor
17. PT slots, session requests, client notes – PT

Web admin:
18. Member search and member record – Front desk / Club manager
19. Timetable builder (copy week, repeat, instructor availability) + studio layout editor – Club manager
20. Reports dashboard – Head office / Area manager / Club manager
21. Tiers, promo codes, class types, announcements – Head office
22. Instructor records (qualifications, cert expiry) and monthly teaching report – Club manager

## Notes

Draft – needs human review.
