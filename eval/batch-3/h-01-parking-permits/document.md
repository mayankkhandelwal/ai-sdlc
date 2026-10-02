# Harrowmere City Council

## Statement of Requirements: Online Parking Permit Service ("Kerbside Permits")

**Document reference:** HCC/PT/2026/041
**Version:** 1.3 (Issued for Tender)
**Owner:** Directorate of Highways and Parking Services
**Classification:** OFFICIAL

---

### 1. Introduction

1.1 Harrowmere City Council ("the Council") invites suppliers to provide a digital service, to be known as Kerbside Permits, through which residents, businesses and other eligible persons may apply for, pay for, renew and manage on-street parking permits within the Council's Controlled Parking Zones ("CPZs").

1.2 The service shall replace the current paper and email based process, under which applications are posted or emailed to the Parking Services Office and entered manually by staff into the Council's back-office enforcement system.

1.3 The service shall be delivered as (a) a responsive web application and (b) a mobile application for iOS and Android. Both channels shall provide equivalent functionality for applicants. Officer functions are required on the web application only.

1.4 In this document, "shall" denotes a mandatory requirement, "should" denotes a desirable requirement, and "may" denotes an optional requirement.

### 2. Background

2.1 The Council administers fourteen (14) CPZs, identified by the codes HZ-A to HZ-N. Each CPZ has its own hours of operation and eligibility boundary, defined by street and property number range.

2.2 Approximately 31,000 permits are issued annually. Peak demand occurs in March, when annual resident permits fall due for renewal.

2.3 Applications are currently reviewed by Parking Permit Officers ("Officers"), who verify proof of residency or business occupancy and vehicle details before issuing a permit. Complex cases are referred to a Senior Permit Officer.

### 3. Users of the Service

3.1 The service shall support the following categories of user:

  (a) **Resident Applicant** — an individual whose main residence is within a CPZ;
  (b) **Business Applicant** — a person applying on behalf of a business operating from premises within a CPZ;
  (c) **Carer Applicant** — a person providing regular care to a resident within a CPZ, applying with the resident's consent;
  (d) **Parking Permit Officer** — Council staff who review and decide applications;
  (e) **Senior Permit Officer** — Council staff who decide referred cases and appeals and may override fees;
  (f) **Service Administrator** — Council staff who maintain zones, fees and system configuration.

3.2 A Resident Applicant may also purchase Visitor permits for use by their visitors.

### 4. Permit Types and Fees

4.1 The service shall support the permit types set out in Table 1. Fees are those set by the Council's Fees and Charges Schedule 2026/27 and shall be configurable by the Service Administrator without supplier involvement.

**Table 1: Permit types and fees (2026/27)**

| Code | Permit type | Eligible applicant | Duration | Fee | Evidence required |
|------|-------------|--------------------|----------|-----|-------------------|
| RES-1 | Resident permit (first vehicle) | Resident | 12 months | £68.00 | Proof of residency; vehicle registration document |
| RES-2 | Resident permit (second vehicle) | Resident | 12 months | £112.00 | As RES-1 |
| RES-3 | Resident permit (third and subsequent vehicle) | Resident | 12 months | £165.00 | As RES-1 |
| RES-E | Resident permit, zero-emission vehicle | Resident | 12 months | £20.00 | As RES-1, plus confirmation of zero-emission status |
| VIS-D | Visitor permit, daily | Resident | 1 day | £3.20 per day | None (account holder must hold valid residency verification) |
| VIS-H | Visitor permit, half-day | Resident | 4 hours | £1.80 | As VIS-D |
| BUS-1 | Business permit | Business | 12 months or 6 months | £420.00 / £230.00 | Business rates bill or lease; vehicle registration document; evidence vehicle is essential to business |
| CAR-1 | Carer permit | Carer | 12 months | Free | Letter from GP, social worker or care agency; resident's signed consent |
| TRD-1 | Trades and contractor permit | Business | 1 week or 1 month | £35.00 / £105.00 | Evidence of works at an address within the CPZ |
| MED-1 | Medical professional permit | Business | 12 months | £60.00 | Professional registration number |

4.2 Visitor permits shall be issued as virtual permits linked to a vehicle registration mark ("VRM") and a start time. A resident shall be limited to 120 visitor days per permit year. The visitor allowance shall be configurable per CPZ.

4.3 The number of resident permits per household shall be limited in accordance with each CPZ's Traffic Management Order. Where the limit is reached, the service shall prevent further applications for that address.

4.4 Fees for 12-month permits shall be pro-rated by whole remaining months where an application is made part-way through a permit year, except for BUS-1 6-month permits, which shall not be pro-rated.

4.5 Concessions: applicants in receipt of a qualifying means-tested benefit shall receive a 50% reduction on RES-1 only. Evidence of entitlement shall be required.

### 5. Functional Requirements: Applicants

5.1 **Account**

5.1.1 Applicants shall create an account using an email address and password, or sign in using the Council's existing resident identity service ("MyHarrowmere").

5.1.2 Applicants shall be able to record one or more addresses and one or more vehicles against their account.

5.1.3 A Business Applicant account shall support more than one authorised user acting for the same business.

5.2 **Eligibility check**

5.2.1 Before starting an application, the applicant shall be able to enter a postcode and select an address to confirm whether the address falls within a CPZ, and which permit types are available at that address.

5.2.2 Where an address is not eligible, the service shall explain why in plain English and shall not allow an application to proceed.

5.3 **Application**

5.3.1 The applicant shall select a permit type, select or add a vehicle by VRM, upload evidence and pay the applicable fee.

5.3.2 The service shall validate the VRM format and shall look up the vehicle make, colour and CO2 emissions band from the national vehicle register interface made available by the Council.

5.3.3 Evidence uploads shall accept PDF, JPG and PNG files up to 10 MB each. The mobile application shall allow evidence to be captured using the device camera.

5.3.4 The applicant shall be able to save an incomplete application and return to it within 30 days, after which it shall be deleted.

5.3.5 Payment shall be taken at the time of submission. Where the application is subsequently refused, the fee shall be refunded in full.

5.3.6 On submission, the applicant shall receive an on-screen confirmation and an email with a reference number.

5.4 **Tracking and management**

5.4.1 The applicant shall be able to view the status of each application: Draft, Submitted, Under Review, Awaiting Information, Approved, Refused, Cancelled.

5.4.2 Where an Officer requests further information, the applicant shall be notified by email and, on mobile, by push notification, and shall be able to respond by uploading documents or by message.

5.4.3 An applicant shall be able to change the vehicle on an active permit no more than twice per permit year, free of charge. Further changes shall incur an administration fee of £12.00.

5.4.4 An applicant shall be able to cancel an active permit. Refunds for cancelled 12-month permits shall be calculated for whole unused months, less an administration fee of £12.00.

5.4.5 Applicants shall receive renewal reminders 28 days and 7 days before expiry.

5.4.6 Residents shall be able to book visitor sessions by entering a visitor VRM, date and start time, and shall be able to view remaining visitor allowance.

5.4.7 Applicants shall be able to download a receipt for any payment.

### 6. Functional Requirements: Officers

6.1 Officers shall have a work queue showing submitted applications, ordered by submission date, filterable by CPZ, permit type and status.

6.2 Officers shall be able to open an application, view evidence, view the vehicle lookup result and record a decision of Approve, Refuse, or Request Information.

6.3 A refusal shall require the Officer to select a refusal reason from a configurable list and may include a free-text note to the applicant.

6.4 Officers shall be able to refer an application to a Senior Permit Officer with a note.

6.5 Officers shall decide applications within 5 working days of submission. The service shall highlight applications approaching or exceeding this target.

6.6 Applications for RES-1, RES-2 and RES-3 where the address and vehicle have previously been verified within the last 12 months, and no details have changed, should be approved automatically without Officer review.

6.7 Officers shall be able to search for any permit by reference, VRM, address or applicant name.

6.8 Every decision, change and override shall be recorded in an audit trail showing the user, date and time and the previous value.

### 7. Functional Requirements: Senior Permit Officers and Administrators

7.1 Senior Permit Officers shall be able to decide referred applications, and to apply a fee waiver or reduction with a mandatory reason.

7.2 Applicants shall be able to appeal a refusal within 28 days of the decision. Appeals shall be decided by a Senior Permit Officer who did not make the original decision.

7.3 The Service Administrator shall be able to maintain CPZs (codes, names, hours, street and number ranges), permit types, fees, visitor allowances, refusal reasons and notification templates.

7.4 The Service Administrator shall be able to manage staff user accounts and assign the Officer, Senior Permit Officer and Administrator roles.

7.5 The service shall provide reports on applications received, decision times, permits in force by CPZ, and income by permit type, exportable to CSV.

### 8. Integrations

8.1 The service shall transmit details of every active permit (VRM, CPZ, valid from, valid to, permit type) to the Council's enforcement system so that Civil Enforcement Officers can verify permits using handheld devices. Updates shall be transmitted within 15 minutes of a change.

8.2 Payments shall be processed through the Council's contracted payment service provider. The supplier shall not store card details.

8.3 Address validation shall use the Council's Local Land and Property Gazetteer.

### 9. Legal and Regulatory Requirements

9.1 The service shall comply with the Data Protection Act and UK GDPR. Personal data shall be retained for 6 years after the expiry of the last permit held, then deleted, except where required for an ongoing appeal or legal proceedings.

9.2 The service shall present a privacy notice at account creation and at application, and shall record the applicant's acknowledgement.

9.3 Permit eligibility rules are set by the Council's Traffic Management Orders. The service shall not issue a permit where doing so would contravene the relevant Order.

9.4 Evidence documents shall be stored securely within the United Kingdom and shall be accessible only to staff users with a role permitting access.

9.5 The Council is subject to Freedom of Information requests; the service shall allow an Administrator to export all data held for an individual within 10 working days of request.

### 10. Accessibility Requirements

10.1 The web and mobile applications shall conform to WCAG 2.2 Level AA and shall meet the Public Sector Bodies Accessibility Regulations. An accessibility statement shall be published.

10.2 All functions shall be operable by keyboard alone and by screen reader (including NVDA, JAWS, VoiceOver and TalkBack).

10.3 Content shall be written in plain English to a reading age of 9 where possible.

10.4 The service shall not use time limits on any page shorter than 20 minutes without warning the user and allowing extension.

10.5 An assisted digital route shall be available: Council contact centre staff shall be able to complete an application on behalf of a caller.

### 11. Non-Functional Requirements

11.1 Availability of 99.5% measured monthly, excluding planned maintenance notified 5 working days in advance.

11.2 The service shall support 2,000 concurrent users during the March renewal period.

11.3 Pages shall load in under 3 seconds on a 4G connection.

11.4 Staff users shall sign in using the Council's single sign-on with multi-factor authentication.

### 12. Out of Scope

12.1 Penalty Charge Notice processing, enforcement and suspension of parking bays are outside the scope of this procurement.

---
*End of Statement of Requirements*
