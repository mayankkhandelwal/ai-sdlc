# Answer Key: h-01-parking-permits

## Meta

- **Domain:** Local government on-street parking permits (application, payment, officer review, renewal, visitor permits).
- **Platforms:** Responsive web + native mobile (iOS/Android) for applicants; staff functions web only.
- **Style:** Formal procurement Statement of Requirements; numbered clauses; shall/should/may language; legal/regulatory and accessibility sections; one large fee table.
- **Length:** ~2,100 words.
- **Traps:** Large fee table with mixed units and dual durations; "should" auto-approval clause vs mandatory officer review; role used in one clause (contact centre staff) that is missing from the user list; per-zone permit limits referenced but never supplied; FOI clause actually describes a subject access export; out-of-scope list that a naive generator may ignore (enforcement, bay suspensions).

## Roles expected

1. Resident Applicant
2. Business Applicant (with multiple authorised users per business)
3. Carer Applicant
4. Parking Permit Officer
5. Senior Permit Officer
6. Service Administrator
7. Contact Centre Agent (assisted digital; implied by 10.5, not listed in 3.1)
8. (External, not a user of the UI) Civil Enforcement Officer — consumes data via enforcement system only.

## Requirements gold draft

| ID | Requirement | Support |
|----|-------------|---------|
| G-1 | Applicants can create an account with email/password or sign in via the council identity service. | "create an account using an email address and password, or sign in using the Council's existing resident identity service" |
| G-2 | Applicants can store multiple addresses and vehicles on their account. | "record one or more addresses and one or more vehicles against their account" |
| G-3 | Business accounts support multiple authorised users. | "support more than one authorised user acting for the same business" |
| G-4 | Postcode/address eligibility check shows the CPZ and available permit types before applying. | "enter a postcode and select an address to confirm whether the address falls within a CPZ, and which permit types are available at that address" |
| G-5 | Ineligible addresses get a plain-English explanation and cannot proceed. | "shall explain why in plain English and shall not allow an application to proceed" |
| G-6 | Support the ten permit types in Table 1 with configurable fees, durations and evidence requirements. | "The service shall support the permit types set out in Table 1" / "shall be configurable by the Service Administrator without supplier involvement" |
| G-7 | Application flow: choose permit type, choose/add vehicle by VRM, upload evidence, pay. | "select a permit type, select or add a vehicle by VRM, upload evidence and pay the applicable fee" |
| G-8 | Validate VRM format and look up make, colour and CO2 band. | "validate the VRM format and shall look up the vehicle make, colour and CO2 emissions band" |
| G-9 | Evidence upload: PDF/JPG/PNG, max 10 MB each; camera capture on mobile. | "accept PDF, JPG and PNG files up to 10 MB each" / "allow evidence to be captured using the device camera" |
| G-10 | Save draft application; drafts deleted after 30 days. | "save an incomplete application and return to it within 30 days, after which it shall be deleted" |
| G-11 | Payment taken at submission; full refund on refusal. | "Payment shall be taken at the time of submission. Where the application is subsequently refused, the fee shall be refunded in full." |
| G-12 | On submission, on-screen confirmation and email with reference number. | "receive an on-screen confirmation and an email with a reference number" |
| G-13 | Application statuses: Draft, Submitted, Under Review, Awaiting Information, Approved, Refused, Cancelled. | "Draft, Submitted, Under Review, Awaiting Information, Approved, Refused, Cancelled" |
| G-14 | Officer information requests notify by email and mobile push; applicant responds with documents or message. | "notified by email and, on mobile, by push notification, and shall be able to respond by uploading documents or by message" |
| G-15 | Vehicle change on active permit: two free per year, then £12 admin fee. | "no more than twice per permit year, free of charge. Further changes shall incur an administration fee of £12.00" |
| G-16 | Cancel active permit; refund for whole unused months less £12 admin fee. | "Refunds for cancelled 12-month permits shall be calculated for whole unused months, less an administration fee of £12.00" |
| G-17 | Renewal reminders 28 and 7 days before expiry. | "renewal reminders 28 days and 7 days before expiry" |
| G-18 | Residents book visitor sessions (VRM, date, start time) and view remaining allowance; virtual permits; 120 days/year default, configurable per CPZ. | "book visitor sessions by entering a visitor VRM, date and start time" / "limited to 120 visitor days per permit year" |
| G-19 | Downloadable payment receipts. | "download a receipt for any payment" |
| G-20 | Household permit limit enforced per CPZ; block further applications when reached. | "Where the limit is reached, the service shall prevent further applications for that address" |
| G-21 | Pro-rating of 12-month fees by whole remaining months; BUS-1 6-month not pro-rated. | "pro-rated by whole remaining months ... except for BUS-1 6-month permits" |
| G-22 | 50% concession on RES-1 for qualifying benefit recipients, with evidence. | "shall receive a 50% reduction on RES-1 only. Evidence of entitlement shall be required" |
| G-23 | Officer work queue ordered by submission date, filterable by CPZ, permit type, status. | "work queue showing submitted applications, ordered by submission date, filterable by CPZ, permit type and status" |
| G-24 | Officer decision: Approve / Refuse / Request Information, viewing evidence and vehicle lookup. | "record a decision of Approve, Refuse, or Request Information" |
| G-25 | Refusal requires a reason from a configurable list; optional note. | "select a refusal reason from a configurable list and may include a free-text note" |
| G-26 | Refer to Senior Permit Officer with note. | "refer an application to a Senior Permit Officer with a note" |
| G-27 | 5-working-day decision target with highlighting of at-risk/overdue items. | "highlight applications approaching or exceeding this target" |
| G-28 | (Should) Auto-approve resident renewals where address and vehicle verified within 12 months and unchanged. | "should be approved automatically without Officer review" |
| G-29 | Officer search by reference, VRM, address, applicant name. | "search for any permit by reference, VRM, address or applicant name" |
| G-30 | Full audit trail of decisions, changes, overrides with previous values. | "recorded in an audit trail showing the user, date and time and the previous value" |
| G-31 | Senior officer decides referrals; fee waiver/reduction with mandatory reason. | "apply a fee waiver or reduction with a mandatory reason" |
| G-32 | Appeal refusal within 28 days; decided by a different Senior Permit Officer. | "decided by a Senior Permit Officer who did not make the original decision" |
| G-33 | Admin maintains CPZs, permit types, fees, allowances, refusal reasons, notification templates. | "maintain CPZs (codes, names, hours, street and number ranges), permit types, fees, visitor allowances, refusal reasons and notification templates" |
| G-34 | Admin manages staff users and roles. | "manage staff user accounts and assign the Officer, Senior Permit Officer and Administrator roles" |
| G-35 | Reports (applications, decision times, permits by CPZ, income by type) exportable to CSV. | "exportable to CSV" |
| G-36 | Push active permits to enforcement system within 15 minutes. | "Updates shall be transmitted within 15 minutes of a change" |
| G-37 | Payments via council PSP; no card storage. | "The supplier shall not store card details" |
| G-38 | Address validation via the council gazetteer. | "Address validation shall use the Council's Local Land and Property Gazetteer" |
| G-39 | Data retention 6 years after last permit expiry, with legal hold exception. | "retained for 6 years after the expiry of the last permit held, then deleted" |
| G-40 | Privacy notice shown and acknowledgement recorded at account creation and application. | "shall record the applicant's acknowledgement" |
| G-41 | Evidence stored in UK, role-restricted access. | "stored securely within the United Kingdom and shall be accessible only to staff users with a role permitting access" |
| G-42 | Admin can export all data for an individual within 10 working days. | "export all data held for an individual within 10 working days of request" |
| G-43 | WCAG 2.2 AA, keyboard and screen reader operable, accessibility statement. | "conform to WCAG 2.2 Level AA" |
| G-44 | Session timeouts no shorter than 20 minutes without warning/extension. | "shall not use time limits on any page shorter than 20 minutes without warning the user and allowing extension" |
| G-45 | Contact centre staff can apply on behalf of a caller (assisted digital). | "Council contact centre staff shall be able to complete an application on behalf of a caller" |
| G-46 | Staff sign in via SSO with MFA. | "Staff users shall sign in using the Council's single sign-on with multi-factor authentication" |
| G-47 | NFRs: 99.5% availability, 2,000 concurrent users, <3 s on 4G. | "Availability of 99.5%" / "2,000 concurrent users" / "under 3 seconds on a 4G connection" |
| G-48 | Carer applications require resident consent and care-provider letter. | "applying with the resident's consent" / "resident's signed consent" |

## Convention features implied

- Password reset / account recovery (implied by email+password accounts).
- Profile and notification preferences.
- Payment history list (implied by receipts).
- Staff role-based access control (implied by 7.4, 9.4).
- Email/push notification templates (explicitly configurable).
- Accessibility statement page (explicit).
- Session timeout warning dialog (implied by 10.4).
- Empty states, error states, and plain-English validation messages.

## Gaps a good critic should find

| Importance | Gap | Question |
|------------|-----|----------|
| blocking | Household permit limits per CPZ are referenced (4.3) but no values given. | What is the maximum number of resident permits per household for each of the 14 CPZs, and does it vary by property type? |
| blocking | Assisted digital (10.5) introduces contact centre staff, but 1.3 says staff functions are web only and 3.1 lists no such role. | Is "Contact Centre Agent" a separate role, how do they take payment on behalf of callers, and how is consent recorded? |
| important | Carer consent mechanism undefined. | How does the resident give consent — uploaded signed form, a link to the resident's own account, or verification by an officer? |
| important | Auto-approval (6.6) is "should" and bypasses the Officer review in 6.2. | Is auto-approval in scope for go-live, and must those approvals still appear in the officer queue or audit trail? |
| important | Concession evidence types and verification not specified. | Which benefits qualify, what evidence is accepted, and is the concession re-verified at renewal? |
| important | Refund method and timing unspecified (refusal, cancellation, appeal success). | Are refunds automatic to the original card, and within what timescale? What happens if an appeal succeeds after a refund? |
| important | Visitor permits: cancellation, editing, overlapping sessions and refunds not defined. | Can a resident cancel or amend a visitor session, and is unused time refunded or returned to allowance? |
| important | Permit "year" not defined (rolling 12 months vs fixed council year with March renewal). | Is the permit year fixed (e.g. April–March) or rolling from issue date? This affects pro-rating. |
| important | MyHarrowmere sign-in: account linking with email accounts not described. | If a user already has an email account, can it be linked to the council identity? |
| minor | Medical professional permit listed with eligible applicant "Business". | Can individual medical professionals apply, or only via an employer? |
| minor | BUS-1 "evidence vehicle is essential to business" has no criteria. | What criteria do officers apply? |
| minor | Clause 9.5 labelled FOI but describes subject access export. | Is this a subject access request requirement? |
| minor | Business permit holders: number of vehicles and transfer between vehicles not specified. | Can a business permit cover more than one VRM? |
| minor | Mobile push notification opt-in and offline behaviour not covered. | Should the mobile app show the permit/visitor session offline? |

## Contradictions

1. **Officer functions channel vs assisted digital.**
   - "Officer functions are required on the web application only."
   - "Council contact centre staff shall be able to complete an application on behalf of a caller."
   (Soft contradiction / undeclared role: staff acting as applicants.)
2. **Mandatory officer review vs auto-approval.**
   - "Officers shall have a work queue showing submitted applications" / 2.3 "who verify proof of residency ... before issuing a permit"
   - "should be approved automatically without Officer review."
3. **Payment taken at submission vs free permits.** "Payment shall be taken at the time of submission." vs CAR-1 fee "Free" — the flow must skip payment for zero-fee permits (minor).

## Traps

- **Injected text:** none in this document.
- **Vague words:** "plain English", "where possible", "securely", "essential to business", "Complex cases".
- **Tables:** Table 1 has 10 rows with dual durations/fees in single cells (BUS-1, TRD-1), per-day pricing (VIS-D), "As RES-1" cross-references, and one free permit. A good parser must split dual-duration rows into separate options.
- **Out of scope:** PCN processing, enforcement, bay suspensions — must not appear as screens or stories.
- **Language notes:** UK English and UK-specific terms (VRM, CPZ, gazetteer, PCN); currency GBP.
- **Modal verbs:** "should" for auto-approval and "may" for refusal note should be marked as non-mandatory.

## Expected screens

| # | Screen | Role |
|---|--------|------|
| 1 | Sign in / create account (email or council identity) | Applicant |
| 2 | Eligibility checker (postcode, address, available permits) | Applicant / public |
| 3 | Applicant dashboard (permits, applications, visitor allowance) | Applicant |
| 4 | Manage addresses and vehicles | Applicant |
| 5 | New application wizard (type, vehicle, evidence, review) | Applicant |
| 6 | Payment and confirmation | Applicant |
| 7 | Application detail / status and information-request response | Applicant |
| 8 | Active permit detail (change vehicle, cancel, renew) | Applicant |
| 9 | Visitor session booking and allowance | Resident Applicant |
| 10 | Payments and receipts | Applicant |
| 11 | Business authorised users management | Business Applicant |
| 12 | Officer work queue with SLA highlighting | Parking Permit Officer |
| 13 | Application review / decision screen (evidence viewer, vehicle lookup, approve/refuse/request info/refer) | Parking Permit Officer |
| 14 | Permit search | Officer / Senior Officer |
| 15 | Referrals and appeals queue + decision | Senior Permit Officer |
| 16 | Zone (CPZ) configuration | Service Administrator |
| 17 | Permit types and fees configuration | Service Administrator |
| 18 | Staff users and roles | Service Administrator |
| 19 | Reports and CSV export | Administrator / Senior Officer |
| 20 | Assisted application on behalf of caller | Contact Centre Agent |

## Notes

Draft — needs human review.
