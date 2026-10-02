# Project Brief: Brightfern Pawprint

**Client:** Brightfern Veterinary Partners
**Prepared by:** Helena Okafor, Head of Client Experience
**Version:** 1.2 (circulated to shortlisted agencies)
**Date:** 14 August 2026

---

## 1. About us

Brightfern Veterinary Partners operates seven small-animal clinics across the Thornbury and Lower Vale region, with an eighth (Harrowgate) opening next spring. We employ around 40 veterinary surgeons, 55 registered veterinary nurses and roughly 30 reception and practice support staff. Between our clinics we see about 1,900 appointments a week, the large majority of which are dogs and cats, with a growing number of rabbits, guinea pigs and other small mammals. We do not treat horses or farm animals.

Today, clients book appointments by phone or by walking in. Our receptionists use our practice management system, VetCore, to manage the diary and clinical notes. VetCore is reliable for clinical work but has no client-facing features worth using, and our phone lines are overwhelmed between 8:00 and 10:00 every morning. We regularly hear from pet owners that they gave up waiting on hold.

## 2. What we want

We want a client-facing product, which we are calling **Brightfern Pawprint**, that lets pet owners book and manage appointments and see their pets' health information without calling us. It should be available as a website and as a mobile app for iPhone and Android. We would like the web and mobile experiences to offer the same core features, although we accept that some things (like push notifications) only make sense on the phone.

Alongside the client side, our clinic staff need a simple back-office view so that they can see what has been booked online, confirm or adjust appointments, and publish information to the pet's record (for example, vaccination dates).

Our goals for the first year:

- At least 40% of routine appointments booked online rather than by phone.
- A noticeable drop in missed appointments (currently about 7% of bookings are no-shows).
- Fewer calls asking "when is my dog's booster due?"

## 3. Who will use it

**Pet owners (our clients).** Ages range widely, from students with their first cat to retired couples with three dogs. Many are not confident with technology. Some households share pets, for example a couple who both bring the dog in, so we need more than one person to be able to manage the same pet.

**Reception staff.** They will see online bookings arrive, deal with requests that need confirmation, and help clients who get stuck. They work at a busy front desk and will usually have the back-office screen open all day.

**Veterinary surgeons and nurses.** They mostly work in VetCore but will need to publish selected information to the client side, such as vaccination records, weight checks and post-operative instructions. They should not have to type things twice if we can avoid it.

**Clinic managers.** Each clinic has a manager who sets that clinic's opening hours, decides which appointment types are bookable online, and wants to see basic numbers (bookings, cancellations, no-shows).

**Head office.** A small team (including me) who will manage settings that apply to all clinics, such as the list of appointment types and the wording of reminder messages.

## 4. Pet owner features

### 4.1 Account and pets

A pet owner should be able to register with their email address or mobile number. When they register, we want to match them to their existing client record in VetCore where possible, using their surname, postcode and phone number. If we cannot find a match, they should still be able to register, and reception will link them to the right record later.

Once registered, the owner should see a list of their pets with a photo, name, species, breed, date of birth and their usual clinic. Owners should be able to add a new pet themselves (for example, a new puppy that has never been seen) but the pet should be marked as "new" until a staff member has checked it.

An owner can invite another person to share a pet. The invited person gets the same booking rights but should not be able to remove the original owner.

### 4.2 Booking an appointment

The booking flow should be: choose the pet, choose the appointment type, choose the clinic (defaulting to their usual clinic), then choose a date and time from the slots available. Owners should be able to choose a specific vet if they wish, or pick "any available vet".

Not every appointment type should be bookable instantly. The table below shows the types we offer and how we want each one handled online.

| Appointment type | Typical length | Who sees the pet | Bookable online? | Deposit | Notes |
|---|---|---|---|---|---|
| Routine consultation | 15 min | Vet | Yes, instantly | None | Most common type |
| Annual vaccination and health check | 20 min | Vet | Yes, instantly | None | Reminder sent 4 weeks before due date |
| Nurse clinic (weight, nails, dental check) | 15 min | Nurse | Yes, instantly | None | |
| Puppy and kitten first visit | 30 min | Vet then nurse | Yes, instantly | None | Only for pets under 6 months |
| Second opinion / complex case | 30 min | Senior vet | Request only | None | Reception confirms within one working day |
| Neutering and spaying | Day admission | Surgical team | Request only | £50 | Pre-op check must be completed first |
| Dental procedure under anaesthetic | Day admission | Surgical team | Request only | £50 | |
| Euthanasia | 30 min | Vet | No, phone only | None | We want a gentle message directing owners to call |

"Request only" means the owner picks a preferred date and the booking stays pending until reception confirms it or offers an alternative. Where a deposit applies, the owner should pay it online when the request is confirmed, not when it is first made.

For anything urgent, the app must always show our emergency phone number and make clear that online booking is not for emergencies.

### 4.3 Managing appointments

Owners should see their upcoming and past appointments. They can cancel or rebook an upcoming appointment up to 24 hours before it starts. Inside 24 hours, they should be told to phone the clinic. We do not want to charge cancellation fees at this stage.

We want reminders before each appointment: one at 48 hours and one on the morning of the appointment. Owners should be able to choose whether reminders arrive by push notification, SMS or email, and turn them off entirely if they want.

### 4.4 Pet health record

For each pet, owners should be able to see:

- Vaccination history and the date the next vaccination is due.
- Weight history, shown as a simple chart.
- Current and recent prescriptions (name of medicine, dose, start date). We do not want online prescription ordering in this phase.
- Documents shared by the clinic, such as post-operative care sheets or vaccination certificates, which they can download as PDF.

We do not want owners to see the full clinical notes. Only information that a vet or nurse has chosen to publish should appear.

### 4.5 Payments

Apart from deposits for procedures, we are not asking for online payment of bills in this phase. However, it would be helpful if owners could see past invoices (amount and date) for their pets, read-only.

## 5. Staff features

### 5.1 Reception

Reception staff need a daily view per clinic showing online bookings, pending requests, and cancellations. For pending requests they should be able to confirm, decline with a reason, or propose another time. They also need to link unmatched new registrations to existing VetCore client records, and approve or merge pets that owners added themselves.

### 5.2 Vets and nurses

Clinical staff need a way to publish items to a pet's record: vaccinations given, weights, prescriptions and documents. Ideally vaccinations and weights would come across from VetCore automatically each night, and only documents would be uploaded by hand. They should be able to un-publish something added by mistake.

### 5.3 Clinic managers

Managers need to set opening hours and closures (bank holidays, staff training afternoons), choose which appointment types are bookable at their clinic, and set how many online slots are released per day. They also want a simple report showing bookings by channel (online versus phone), cancellations and no-shows for a chosen date range.

### 5.4 Head office

Head office needs to manage the master list of appointment types, the wording of reminder messages and the emergency contact details for each clinic. We also want to be able to add the new Harrowgate clinic ourselves without needing a developer.

## 6. Integration with VetCore

VetCore remains our system of record for the diary and clinical history. Bookings made in Pawprint must appear in the VetCore diary, and appointments booked by phone in VetCore must appear in the owner's Pawprint account. VetCore has an API, and their support team have told us it supports reading and writing appointments and reading vaccination and weight data. We will put the chosen agency in touch with them.

If VetCore is unavailable, owners should still be able to see their existing appointments and pet records, but new bookings should be paused with a clear message rather than risk a double booking.

## 7. Other expectations

- **Accessibility.** Many of our clients are older. Text must be readable at large sizes, buttons must be easy to tap, and the whole product should meet WCAG 2.1 AA.
- **Branding.** We will supply our brand guidelines. We use a forest green and cream palette.
- **Privacy.** We hold personal data on owners and their pets and must comply with UK GDPR. Owners should be able to download their data and ask for their account to be closed.
- **Languages.** English only for now, but please do not make it impossible to add Welsh later.
- **Availability.** Booking should be available 24 hours a day, though staff will only process requests during opening hours.

## 8. Out of scope for this phase

- Online prescription ordering and repeat medication.
- Video consultations.
- Pet insurance claims.
- A loyalty or health plan subscription scheme (we may add this next year).

## 9. Timeline and next steps

We would like a first release in time for the Harrowgate opening, ideally by the end of March next year. Please include in your response how you would phase the work, what you would need from us, and any questions about this brief. I am happy to arrange a visit to our Thornbury clinic so you can see the front desk at its busiest.

Helena Okafor
Head of Client Experience, Brightfern Veterinary Partners
