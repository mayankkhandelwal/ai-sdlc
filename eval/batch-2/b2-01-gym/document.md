# Kettlebrook Fitness – Member App & Club Admin Platform

**Project brief – v0.3 (draft for shortlisted agencies)**
Prepared by: Operations & Member Experience team, Kettlebrook Fitness Ltd
Circulated: 14 August

---

## 1. About us

Kettlebrook Fitness runs 11 clubs across the north-west, from small 24-hour "express" sites in retail parks to our two flagship clubs at Harrowgate and Millbank, which have pools, a spa area and four studios each. We have roughly 18,000 active members and around 140 staff, plus about 60 freelance instructors and personal trainers who work across one or more clubs.

Today we run on a patchwork. The membership system is a desktop program at each front desk that only staff can use. The class timetable is a spreadsheet that each club manager edits, prints and pins on the wall every Sunday. Members book classes by phoning the club or turning up early and writing their name on a clipboard. Personal trainers mostly manage their own diaries through WhatsApp and their own phones. Head office has no single view of anything – we find out how a club did last month when the manager emails us a spreadsheet.

We want to replace all of this with one product that we are calling **Kettlebrook Move** internally (the name may change before launch). It will be:

- a **member app** for iOS and Android, and
- a **web admin portal** for club staff, trainers and head office.

We are open to the trainer side being part of the member app (with a different login) or a separate app – please recommend.

## 2. What success looks like

- Members can book, cancel and join waitlists for classes themselves, from their phone, any time of day.
- Studios are full. At the moment our popular classes are "full" on the clipboard but a third of the people don't turn up, while people who wanted to come were turned away.
- Trainers and instructors keep their schedules in our system, not in their personal WhatsApp.
- Club managers spend less time on admin and more time on the gym floor.
- Head office can see attendance, class popularity and membership numbers across every club, in one place, without waiting for emails.
- The app should feel modern and premium, in line with our brand refresh.

## 3. Memberships

### 3.1 Membership tiers

We currently sell five tiers. Prices below are standard monthly prices and change roughly once a year; promotions are run on top of these.

| Tier | Monthly price | Club access | Class bookings | Advance booking window | Guest passes | PT sessions included |
|---|---|---|---|---|---|---|
| Off-Peak | £19.99 | Home club only, before 4pm on weekdays and all day at weekends | 4 per month | 3 days | None | None |
| Core | £29.99 | Home club only, any time | 8 per month | 5 days | None | None |
| Student | £22.00 | Home club only, any time | 8 per month | 5 days | None | None |
| Plus | £39.99 | All clubs, any time | Unlimited | 7 days | 2 per month | None |
| Elite | £59.99 | All clubs plus spa areas at Harrowgate and Millbank | Unlimited | 10 days | 4 per month | 1 per month |

Notes on the tiers:

- Student membership requires a valid student card, which front desk staff currently check by eye. We would like members to be able to upload a photo of their student card when they join and have staff approve it.
- Monthly class allowances reset on the 1st of each month. Unused bookings do not roll over.
- Guest passes let a member bring a friend for a day. The friend should get a QR code by text or email. Guests can't book classes.
- The included PT session for Elite members is one 45-minute session per calendar month with any PT at their home club.

### 3.2 Joining

Members can join online in the app or in person at the front desk. When joining they choose a home club and a tier. We collect name, date of birth, address, mobile, email, emergency contact and a short health questionnaire (PAR-Q). If they answer yes to any of the health questions, they should be told to speak to a member of staff before training, and the club should be flagged.

There is a £15 joining fee, which is often waived during promotions. Head office should be able to set up a promo code that waives the joining fee or gives a discount on the first month.

Monthly payments will be taken by direct debit through our existing provider.

### 3.3 Changing membership

- Members can upgrade their tier at any time and it takes effect immediately.
- Downgrades take effect from the next billing date.
- Members should be able to freeze their membership for up to 3 months per year. Frozen members can't book classes or enter the club.
- Members can change their home club once every 3 months.
- Cancellation needs 30 days' notice. Members can request cancellation in the app.

### 3.4 Membership card and entry

Every member gets a digital membership card in the app with a QR code. This is scanned at the turnstiles at all clubs. The turnstiles are supplied by GatePass Systems and they have an API, but we haven't looked at the details yet. If a member's membership doesn't give them access to a club or at that time of day (e.g. Off-Peak member at 6pm on a Tuesday), the turnstile should not open and the member should see why on their phone.

## 4. Classes

This is the most important part of the project for us and where most of the complaints come from today, so we have gone into detail.

### 4.1 What a class is

We run about 900 classes a week across all clubs. A class has:

- a class type (e.g. Spin 45, HIIT Blast, Yoga Flow, Pilates Reformer, Aqua Fit, BoxFit, Barbell Strength, Mobility, Kids Swim)
- a club and a studio/room (or pool)
- a date, start time and duration
- an instructor
- a capacity, which is usually the studio capacity but can be set lower
- an intensity level (1 to 5)
- what to bring / equipment provided
- a short description and a photo for the class type

Some classes need specific equipment that is numbered – Spin bikes and Pilates Reformer beds. For those classes members should be able to pick their bike or bed number from a layout of the room when they book, like choosing a seat at the cinema. Each studio's layout is different.

### 4.2 Timetable

- Club managers build the weekly timetable in the admin portal. Most weeks are the same as the previous week, so they need to be able to copy a week or set a class to repeat weekly until a given date.
- Timetables are published for 2 weeks ahead. Members only see classes inside their tier's advance booking window as bookable; classes further out should still be visible but marked "booking opens on…".
- Booking for a class opens at 7am on the day the window opens, not at midnight. We have had complaints about people staying up to book.
- Members browsing the timetable should be able to filter by club, class type, instructor, time of day and intensity, and save favourite classes and favourite instructors.
- Members on Plus and Elite can see and book classes at all clubs. Off-Peak, Core and Student members only see their home club.

### 4.3 Booking

- A member books a class with one tap (two if they have to pick a bike/bed).
- Each booking uses one of the member's monthly class allowance if their tier has a limit.
- A member can't book two classes that overlap in time.
- A member can hold a maximum of 10 future bookings at any one time.
- After booking, the class appears in "My bookings" and they get a confirmation notification. We'd also like an "add to calendar" option.

### 4.4 Waitlist

- When a class is full, members can join the waitlist. The waitlist has a maximum length of 10 per class.
- When a place becomes free, the first person on the waitlist is automatically booked in and notified. This happens up until 1 hour before the class starts.
- Inside the last hour, instead of automatic booking, everyone on the waitlist is notified that a place is free and the first one to tap "take it" gets it.
- Joining a waitlist does not use an allowance. Being promoted from the waitlist does.
- If a member is promoted from the waitlist but they've already got another class at the same time, skip them and move to the next person.

### 4.5 Cancelling and no-shows

- Members can cancel up to 2 hours before the class start without penalty, and the allowance is given back.
- Late cancellations and no-shows count as a strike. Three strikes in 30 days and the member cannot book for 7 days.
- Members should be able to see their strikes in the app and when they expire.
- Club managers can remove a strike (for example, if the member was ill or there was a family emergency).

### 4.6 Checking in to a class

- Instructors take attendance at the start of the class from a tablet or their phone, by ticking names on the class list or scanning the member's QR code.
- Anyone booked but not checked in within 10 minutes of the start time is marked as a no-show automatically.
- Walk-ins: if there's space, instructors can add a member who turns up without booking. It still counts towards their allowance.

### 4.7 Club cancels a class

- If a club has to cancel a class (instructor ill, broken air-con, pool closed), the manager cancels it in the admin portal with a reason. Every booked member and everyone on the waitlist is notified straight away by push notification and SMS. Allowances are given back. Nobody gets a strike.
- If the instructor changes but the class goes ahead, booked members should be notified of the new instructor – some members follow particular instructors.

### 4.8 After the class

- Members get a prompt about an hour after the class to rate it (1–5 stars) and leave an optional comment.
- Ratings are visible to club managers and head office, not to other members. Instructors can see their own average rating but not individual comments.

### 4.9 Kids classes

Kids Swim and a couple of junior classes are booked by a parent who is a member. The parent adds their children to their profile (name and date of birth) and books on their behalf. Children don't have their own login.

## 5. Trainers and instructors

We have two groups of people who teach:

- **Class instructors** – teach group classes. Some are employees, many are freelance and work across several clubs.
- **Personal trainers (PTs)** – do one-to-one sessions. PTs are self-employed and rent space from the club monthly. Some PTs also teach classes.

### 5.1 Instructor schedules

- Instructors should see their own timetable for all clubs they work at, a week at a time, with the class list and number booked for each class.
- Instructors set their regular weekly availability (e.g. "Mon/Wed evenings at Millbank, Saturday mornings at Leyfield") and any dates they're away. Club managers use this when building the timetable – the timetable builder should only offer instructors who are available.
- If an instructor can't make a class, they request cover in the system. Other instructors qualified to teach that class type get notified and can accept. The club manager approves the swap. If nobody has accepted cover 24 hours before the class, the manager gets an alert.
- We need to record which class types each instructor is qualified to teach, and the expiry date of their certifications (first aid, and branded programme licences). The system should warn managers 30 days before a certification expires and stop them being scheduled when it has expired.
- At the end of each month club managers need a report of classes taught per instructor, which we use to pay freelancers. We don't need the system to pay them.

### 5.2 Personal training

- Members can browse PTs at their home club (or all clubs on Plus/Elite) with a photo, bio, specialisms and qualifications.
- PTs set their available slots. Members request a session in a free slot and the PT accepts or declines.
- Elite members can use their included monthly session through the app.
- PTs can block out time, see their upcoming sessions, and add short private notes against each client.
- PTs should be able to message their clients in the app so they don't need to use WhatsApp. Messages should be visible only to the PT and the member.

## 6. Web admin portal

### 6.1 Who uses it

- **Front desk staff** – sign up new members, look up a member, check guests in, approve student cards, handle general enquiries.
- **Club managers** – everything front desk can do for their club, plus timetable, rooms and studio layouts, instructor rotas, cancellations, strike removal, reports for their club.
- **Area managers** – we have two area managers who each look after 5–6 clubs. They need to see their clubs' reports. Not sure yet whether they should be able to edit timetables.
- **Head office** – all clubs. Membership tiers and prices, promo codes, class types, app content and announcements, all reports.
- **Instructors and PTs** – see section 5.

### 6.2 Member lookup

Staff should be able to search members by name, email, mobile or membership number, and see their tier, status (active, frozen, cancelling, cancelled), home club, bookings, strikes, visit history and notes. Staff can add notes to a member record (e.g. "prefers to be called Jo").

### 6.3 Reports

Head office wants a dashboard with:

- active members by club and tier, joiners and leavers per month
- class attendance and fill rate by club, class type, instructor and time slot
- no-show and late cancellation rate
- waitlist demand (classes that are regularly full with a waitlist)
- average class ratings
- club visits by hour of day (from the turnstiles)

Reports should be exportable to Excel. Club managers see the same reports filtered to their club.

### 6.4 Announcements

Head office and club managers can post announcements to the app (e.g. "Millbank pool closed Thursday for maintenance"), targeted at one club, several clubs, or all members, and optionally send it as a push notification.

## 7. Notifications

Members should receive notifications for:

- booking confirmed
- waitlist promotion / place available
- class cancelled or instructor changed
- reminder 1 hour before the class (members can turn this off)
- strike received, and booking suspension
- PT session requested/accepted/declined
- announcements

Instructors should be notified of cover requests, timetable changes affecting them and cert expiry. Most of these should be push notifications; class cancellations should also go by SMS.

## 8. Other requirements

- English only for now.
- Branding: we'll provide the new brand guidelines, logo, fonts and colours.
- The app must be fast and easy to use, including for our older members.
- GDPR – we hold health information from the questionnaire.
- We need to bring across our existing members from the current system. We can export to CSV.
- We would like to launch at Harrowgate as a pilot in November and roll out to all clubs in January, which is our busiest month.

## 9. Not in scope (for now)

- Selling merchandise or supplements in the app.
- Nutrition plans or workout tracking.
- Integration with fitness watches – maybe phase 2.
- Paying freelancers through the system.

## 10. Next steps

Please send us your proposal, including an outline of the screens you'd expect to build, a rough timeline and a cost estimate, by the end of the month. Questions to Dana Whitlow, Head of Member Experience.
