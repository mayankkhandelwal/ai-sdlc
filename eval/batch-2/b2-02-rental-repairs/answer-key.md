# Answer key – b2-02-rental-repairs

## Meta

- **Domain:** Residential property management – tenant repair reporting, contractor job management, landlord approvals, office oversight. Mobile app (tenants, contractors) + web (office; tenants optionally).
- **Style:** Informal meeting notes and email fragments by five people, pasted together. Bullet fragments, initials, repetition (photos mentioned three times, contractor updates twice), open questions, ambiguous pronouns ("they", "we", "them").
- **Length:** ~1,230 words.
- **Language:** English (UK, informal).
- **Deliberate traps planted:**
  1. Ambiguous "they": e.g. "they need to be able to say when they're in" (tenants), "they turn up" (contractors), "they should get it on their phone" (contractor), "they'd need a login too probably" (out-of-hours service).
  2. Unclear roles: property managers' visibility, whether landlords log in, out-of-hours provider, external freeholders, accounts.
  3. Inconsistent landlord approval threshold (£250 vs £300 vs per-landlord up to £500).
  4. Undecided who sets priority (office vs tenant suggests/office confirms).
  5. Repeated requirements across meetings (should be de-duplicated, not doubled).
  6. Phase 2 items mixed in (planned maintenance) and a rejected-then-maybe idea (auto-approve).
  7. Vague timing ("within a week or so, depends", "X days", "a set time").

## Roles expected

1. Tenant
2. Contractor (sole trader or firm user)
3. Office maintenance coordinator (Tom)
4. Property manager
5. Operations/admin (Priya; contractor compliance)
6. Accounts (Leanne)
7. Landlord (login undecided)
8. Out-of-hours service operator (undecided)
9. Director / management (reporting)
10. External: lettings system (tenancy sync), accounts package (CSV export), freeholder/managing agent (pass-on, no clear role)

## Requirements (gold draft)

G-1. Tenants report a repair from their phone; contractors update jobs; office sees everything in one place. — Quote: "want something tenants can use on their phone to report a repair, and contractors can update the job. and we can see everything in one place"
G-2. Repair report includes description, location in property and photos. — Quote: "report a repair: what's wrong, where in the property, photos"
G-3. Tenants can attach video as well as photos where possible. — Quote: "tenants must be able to upload photos and video if possible"
G-4. Repair categories list. — Quote: "plumbing, electrical, heating, roof, damp/mould, appliances, doors/locks/windows, pests, communal areas, other"
G-5. Tenants see repair status and appointment time. — Quote: "tenant should see the status of their repair and when someone is coming"
G-6. Tenants provide access availability. — Quote: "they need to be able to say when they're in"
G-7. In-app messaging about a job. — Quote: "also should be able to message about the job instead of ringing us"
G-8. Multi-language support (nice to have). — Quote: "can it do other languages? GH: nice to have"
G-9. Three priority levels with target attendance times (emergency 4h, urgent 24h, routine). — Quote: "attend within 4 hours"
G-10. Office decides or confirms priority (tenant may suggest – undecided). — Quote: "so we decide the priority not them. or they suggest and we confirm?"
G-11. Gas smell reports must first direct tenants to the gas emergency line. — Quote: "gas smell – app should tell them to ring the gas emergency line FIRST before anything else"
G-12. Coordinator assigns job to contractor; contractor accepts or rejects on phone. — Quote: "TM assigns the job to a contractor. they should get it on their phone, accept or reject"
G-13. Contractor status updates: on my way, on site, completed, needs parts/second visit, couldn't access. — Quote: "they update: on my way, on site, completed, needs parts / second visit, couldn't access"
G-14. Before and after photos from contractors. — Quote: "photos before and after"
G-15. Contractors upload invoices against jobs. — Quote: "they need to upload their invoice against the job"
G-16. Track contractor insurance and gas certificate; block assignment when expired. — Quote: "would be good if the system stops us assigning someone whose insurance has run out"
G-17. Landlord approval required above a threshold except emergencies; threshold configurable per landlord. — Quote: "so it's per landlord really"
G-18. Landlord portal to view jobs on their properties and approve quotes (undecided). — Quote: "GH thinks yes, at least to see jobs on their properties and approve quotes."
G-19. Mobile app for tenants and contractors; web for office; tenants may use web. — Quote: "SK: app for tenants and contractors, web for the office. tenants could also use web if they don't want to download"
G-20. Office user roles incl. property managers assigned to blocks (visibility undecided). — Quote: "property managers look after specific blocks. they should only see their blocks? or everything?"
G-21. Accounts matches invoices to jobs, approves, marks paid, exports CSV. — Quote: "approve invoice -> mark paid"
G-22. Flag recharge to tenant on a job when tenant caused damage. — Quote: "needs flagging on the job"
G-23. Link duplicate reports of communal issues to one job and notify all reporters. — Quote: "need to be able to link them to one job, and tell all of them when it's fixed"
G-24. Handle blocks managed by a third-party freeholder (pass on). — Quote: "then we just pass it on. not sure how that works in the system"
G-25. Tenant login method to be decided (email+password or SMS code). — Quote: "login for tenants – email + password? or text code?"
G-26. Tenant access ends on move-out; new tenants linked to the unit; possible sync with lettings system. — Quote: "tenants move out – their access should stop."
G-27. Contractor proposes time slot; tenant confirms. — Quote: "they should be able to propose a time slot to the tenant and the tenant confirms"
G-28. No-access outcome notifies tenant and returns job to coordinator. — Quote: "if they can't get in, they mark no access, tenant gets a message, and the job goes back to TM"
G-29. Contractor quote upload and landlord approval workflow for larger jobs. — Quote: "if job needs a quote first (bigger jobs) contractor uploads quote"
G-30. Overdue jobs vs priority deadline on map or list; red when overdue; open duration shown. — Quote: "we can see every open job and how long it's been open, red if it's past its deadline"
G-31. Monthly landlord statement report of work and cost per property. — Quote: "reports for the monthly landlord statements – what was done on their property and what it cost"
G-32. Full audit trail for ombudsman complaints. — Quote: "a record we can show the ombudsman if there's a complaint – who did what when"
G-33. Automatic tenant notifications on status change, via preferred channel. — Quote: "tenants should get an automatic update when status changes, text or push or email, whichever they prefer"
G-34. Post-completion satisfaction check; reopen if unhappy (undecided). — Quote: "after the job's done, ask them if they're happy with it. if not, job reopens?"
G-35. Damp and mould handled as a special workflow with inspection deadlines and records. — Quote: "they need inspecting within a set time and we need to keep a record"
G-36. Out-of-hours service access for night emergencies. — Quote: "they'd need a login too probably"
G-37. Office staff can raise jobs on behalf of tenants. — Quote: "we want to be able to add jobs ourselves when someone phones in, on behalf of the tenant"
G-38. Usability for non-technical tenants and speed for the coordinator (non-functional). — Quote: "needs to be easy for the tenants, a lot of them aren't techy. and quick for Tom."
G-39. Out of scope / phase 2: planned maintenance. — Quote: "GH: phase 2 maybe"
G-40. Property structure: blocks, flats, HMOs, houses, linked to landlords. — implied – the notes mention units, blocks, HMOs and landlords owning 1–20+ units; the system needs a property/unit/landlord data model.

## Convention features implied but not written

- Registration/invite flow for tenants and contractors, login, password reset / OTP resend.
- Admin management of users, contractors, properties, landlords.
- Notification preferences (explicitly hinted: "whichever they prefer").
- Push notifications for contractors on new job assignment.
- Search and filtering of jobs (by block, status, contractor, priority).
- Data import of properties, tenants, landlords, contractors.
- GDPR / privacy for tenant data and photos inside homes.
- Offline or poor-signal handling for contractors on site.

## Gaps a good critic should find

1. **Blocking** – Landlord approval threshold: Is it a global £250, £300, or configurable per landlord (with values like £500 or "approve everything")?
2. **Blocking** – Priority ownership: Does the tenant suggest a priority and the office confirm, or does the office alone set it? Who can change it later?
3. **Blocking** – Landlord access: Do landlords get a login, or are approvals handled by email/link? What can they see?
4. **Important** – Property manager visibility: Do property managers see only their blocks or all jobs?
5. **Important** – Out-of-hours service: What can the out-of-hours provider do in the system (create, assign, update jobs)?
6. **Important** – Lettings system sync: Is there an API, and which data (tenancies, move-in/move-out dates) syncs, how often?
7. **Important** – Third-party freeholder blocks: How should a job for a block managed by another company be recorded and handed off?
8. **Important** – Routine target time: What exactly is the routine deadline ("a week or so, depends")?
9. **Important** – Damp and mould rules: What inspection deadlines and records are required?
10. **Important** – Auto-approval: Should urgent jobs auto-approve if a landlord doesn't respond in X days? What is X?
11. **Important** – Contractor rejection and reassignment: What happens when a contractor rejects or doesn't respond? Is there a timeout?
12. **Minor** – Languages: Which languages, and is it UI translation or message translation?
13. **Minor** – Recharge workflow: How is a tenant notified and billed for a recharge? Can they dispute it?
14. **Minor** – Satisfaction / reopen: If the tenant is unhappy, does the job reopen automatically or go to review?
15. **Minor** – Map view: Is a map required or is a list sufficient?
16. **Minor** – Contractor firm users: Can a bigger contractor firm have several engineer logins under one company?

## Contradictions planted

- Landlord approval threshold. — Quote A: "GH: landlords have to approve anything over £250 unless it's an emergency" — Quote B: "we send to landlord for approval if over the limit (GH said £300 last time? check)" — and a third variant: "some say just do it up to £500. so it's per landlord really"
- Priority setter (internal inconsistency in one bullet). — Quote A: "so we decide the priority not them." — Quote B: "or they suggest and we confirm?"
- Auto-approve. — Quote A: "GH: no." — Quote B: "well, maybe for urgent. let's discuss."

## Traps

- **Injected text:** None.
- **Ambiguous pronouns:** "they need to be able to say when they're in. half the jobs fail because they turn up and nobody's home" (first "they" = tenants, second = contractors); "tenants will mark everything as emergency. so we decide the priority not them. or they suggest and we confirm?"; `PS: who are "we" in the system?`; "they'd need a login too probably" (= out-of-hours service).
- **Vague words:** "30-ish", "approx", "within a week or so, depends", "if possible", "nice to have", "maybe", "X days", "a set time", "keep it simple", "easy", "quick", "not techy", "new rules", "Tom has the details".
- **Repetition:** photos (Mtg 1 tenant side, Mtg 1 contractors, Mtg 2 recap); contractor updates (Mtg 1 and Mtg 2); open questions list restates earlier points.
- **Tables:** None.
- **Language notes:** UK property terms: HMO (house in multiple occupation), freeholder, block, recharge, property ombudsman. Initials used instead of names; roles inferred from context (TM = maintenance coordinator, LW = accounts/lettings, SK = IT).

## Expected screens

Tenant (mobile + web):
1. Login / sign-up (invite or OTP) – Tenant
2. Report a repair (category, location, description, photos/video, availability; gas emergency warning) – Tenant
3. My repairs list – Tenant
4. Repair detail (status timeline, appointment, messages, confirm time slot, satisfaction) – Tenant

Contractor (mobile):
5. Job inbox (accept/reject) – Contractor
6. Job detail (status updates, before/after photos, propose slot, no access) – Contractor
7. Quote and invoice upload – Contractor
8. Contractor profile / documents (insurance, gas certificate) – Contractor / Operations

Office (web):
9. Jobs dashboard (all open jobs, overdue in red, filters, map/list) – Coordinator / Property manager
10. Job detail and assignment (priority, contractor, link duplicates, recharge flag, audit log) – Coordinator
11. Create job on behalf of tenant – Office staff
12. Contractor management and compliance – Operations
13. Properties / units / tenants / landlords management – Office admin
14. Invoices (match, approve, mark paid, CSV export) – Accounts
15. Reports (landlord statements, overdue, ombudsman audit export) – Director / Office

Landlord (web, if confirmed):
16. Landlord portal – properties, jobs, approve/reject quotes – Landlord

Out-of-hours (if confirmed):
17. Emergency job intake / limited job view – Out-of-hours operator

## Notes

Draft – needs human review.
