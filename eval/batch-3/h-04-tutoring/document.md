# Brightquill Learning — Brief for the new tutoring marketplace ("TalkPath")

*Compiled by the Product team, with a section from Finance. Version 2, October 2026.*

---

## Part A — Context

Brightquill Learning runs a language tutoring service that connects independent tutors with adult learners. We started in 2019 with a small app called **Chatterbox Tutors**, built quickly by a freelance team. It still works, more or less, but it has become very hard to change, it only runs on the web, and the payment logic is a patchwork of spreadsheets and manual bank transfers.

Today we have roughly 1,400 active tutors and 19,000 learners who have taken at least one lesson in the last 12 months. Most lessons are 1:1 video lessons of 30 or 60 minutes. The most popular languages are English, Spanish, German, French, Portuguese and Japanese, but tutors can teach anything they can prove they are qualified in.

Our tutors live in more than 40 countries. Learners are concentrated in Western Europe, the US, Brazil, Mexico and India.

We want to replace Chatterbox Tutors with a new marketplace called **TalkPath**, available as a web app and as mobile apps (iOS and Android) for both learners and tutors. Internal staff will use a web back-office.

This brief has two parts written by different people. Part B is from me (product). Part C is from our Finance lead. We have not fully agreed on everything yet — we would rather you see both views than have us pretend we have a single answer.

---

## Part B — Product view (Hannah Moretti-Kwan, Head of Product)

### B1. What success looks like

Learners should find a tutor they like within a few minutes, book a lesson that suits their timezone, and come back week after week. Tutors should feel that TalkPath respects their time and pays them fairly and on time. Our support team should spend far less time fixing bookings and chasing payments by hand.

The single biggest complaint about Chatterbox Tutors is that booking is clunky and that learners and tutors regularly turn up at different times because of timezone bugs. That cannot happen in TalkPath.

### B2. Learners

A learner should be able to:

- Sign up with email, Google or Apple. We don't want to force a long profile at the start — just name, the language they want to learn, their current level (we use A1–C2) and their timezone (detected automatically, but editable).
- Search and filter tutors by language, price, availability (e.g. "weekday evenings"), the tutor's country, other languages the tutor speaks, specialities (exam preparation, business, conversation, kids — although learners must be adults, some parents book for teenagers, see B6), and rating.
- Open a tutor profile with a short intro video, a bio, their prices, reviews, and a calendar showing open slots in the learner's own timezone.
- Book a **trial lesson** with a new tutor. In my view the trial should be **free and 30 minutes**, one per tutor per learner, because it is the single best conversion tool we have. Tutors can choose whether they offer trials.
- Book single lessons or buy **packages** of 5, 10 or 20 lessons with the same tutor at a discount the tutor sets (max 20% off).
- Book **recurring lessons** (e.g. every Tuesday 19:00 for 8 weeks).
- Reschedule or cancel. I want this to be generous: **free cancellation up to 2 hours before the lesson**. After that the lesson is charged.
- Message their tutor before and after booking. Messages should allow attachments (PDF, images, audio).
- Join the lesson from the app. We currently use links to an external video tool; for TalkPath we'd like video built in, but if that is too much for the first release, external links are acceptable as long as the link appears in the booking automatically.
- Leave a rating (1–5 stars) and a written review after each lesson; only learners who have actually completed a lesson with that tutor can review.
- See their lesson history, upcoming lessons, packages remaining and receipts.

### B3. Tutors

A tutor should be able to:

- Apply to join. The application includes ID, a profile photo, intro video, languages taught with level of proficiency, any teaching certificates, and a short demo. Our Tutor Success team reviews applications; currently about 30% are accepted.
- Set their availability as weekly recurring blocks plus one-off exceptions (holidays, a day off). Availability must sync both ways with Google Calendar; Outlook would be nice.
- Set their own price per lesson length (30, 45, 60, 90 minutes) in **their own currency**. Learners see the price converted to their currency.
- Set a minimum notice period for bookings (e.g. "no bookings less than 12 hours ahead").
- Accept bookings automatically, or choose to approve each new learner's first booking manually.
- See earnings, upcoming payouts and payout history, and download statements for their tax returns.
- Get paid **weekly**. Tutors in Chatterbox Tutors are paid monthly and it's the second most common reason good tutors leave us for other platforms. I'd like weekly payouts every Monday for all lessons completed the previous week.
- Report a learner no-show. If the learner doesn't turn up within 10 minutes, the tutor gets paid in full.

### B4. Commission

Today we take 18% of every lesson. I want to drop this to **15%** for TalkPath to attract tutors, and for trial lessons we take nothing (they're free anyway). Tutors who teach more than 100 hours in a rolling 3-month period could drop to 12%.

### B5. Internal staff

- **Tutor Success** — review tutor applications, approve or reject with a reason, suspend tutors, handle tutor queries.
- **Learner Support** — look up bookings, issue refunds or lesson credits, resolve disputes between learners and tutors (e.g. "the tutor didn't show up", "the connection failed").
- **Content moderators** — review reported messages and reviews.
- **Finance** — see Part C.
- **Admins** — manage languages, specialities, lesson lengths, commission settings and staff accounts.

### B6. Safety

Learners must be 18 or over. Some parents want to book lessons for teenagers, and we're open to a "parent books for a 13–17 year old" option, but only if it's straightforward from a safeguarding point of view. Tutors who teach minors would need an extra background check. Honestly, I am not sure we should do this in release 1.

Messages must be scanned for attempts to take contact or payments off-platform (phone numbers, emails, payment links) — we don't want to block them automatically, but we want them flagged.

### B7. Migration from Chatterbox Tutors

- All active tutors and learners must be migrated with their profiles, reviews and upcoming bookings.
- Unused package lessons must carry over.
- Tutors' current balances (lessons done but not yet paid) must be paid out correctly — either in the last Chatterbox Tutors payment run or in the first TalkPath run, but never twice.
- We'd like to run both systems in parallel for about a month, with no new bookings in Chatterbox Tutors after cut-over.

### B8. A note from our tutor community lead

Our tutor community lead, Lucía Ferrándiz, asked me to include this as she wrote it, because it reflects what many of our Spanish-speaking tutors are telling us:

> "Para muchos tutores de Latinoamérica, cobrar cada semana y en su moneda local es lo más importante. Con Chatterbox perdemos mucho dinero en comisiones bancarias y en el tipo de cambio. También queremos ver claramente cuánto vamos a recibir antes de cada pago, sin sorpresas."

> "Y por favor: la aplicación tiene que estar en español también, no solo en inglés."

(Rough translation: tutors in Latin America care most about weekly payment in local currency; bank fees and exchange rates eat into their income; they want to see clearly what they will receive before each payout; and the app must be available in Spanish, not only English.)

### B9. Languages of the interface

The app interface should be available in English and Spanish at launch, with Portuguese and German soon after. Tutors' profiles can be written in any language.

### B10. Notifications

Email and push notifications for: booking confirmed, booking request (when manual approval), reminders 24 hours and 1 hour before the lesson, cancellation, reschedule, new message, review received, payout sent. Users must be able to turn off non-essential notifications.

### B11. Learner progress

Tutors should be able to write short lesson notes after each lesson (what was covered, homework, new vocabulary) that the learner can see in the app. Over time this becomes the learner's learning journal. Learners can also set a goal ("pass B2 exam in June", "speak confidently at work") and the tutor can update the learner's estimated level every few lessons. Nothing fancy — we are not building a course platform — but learners tell us that seeing progress is what keeps them booking.

### B12. Things we know we don't need in release 1

- Group lessons (we have had requests, but 1:1 is 97% of our volume).
- A tutor referral programme.
- Self-paced courses or recorded content.
- An AI conversation partner — the board keeps asking about this, but it is a separate project.

### B13. What we would like to keep from Chatterbox Tutors

Not much, to be honest. The tutor "badges" (Top Rated, Fast Responder, 500+ lessons) are popular and tutors would be upset to lose them, so please carry those concepts over. Fast Responder means replying to 90% of new learner messages within 12 hours over the last 30 days.

---

## Part C — Finance view (Rajiv Szabo, Finance Director)

I support the move to a new platform. The current manual payment process costs us the equivalent of two full-time people and creates real risk. But some of the product proposals above would hurt our margins or our cash position, and I want the supplier to understand the financial constraints before designing anything.

### C1. How learners pay

Learners must pay **upfront** at the time of booking (or package purchase). We will not offer pay-after-lesson. Card payments, Apple Pay and Google Pay are required; PIX for Brazil and UPI for India would be valuable because they have very low fees.

We should **charge learners in a small number of currencies only: EUR, USD and GBP**. Learners elsewhere pay in USD. Supporting many charge currencies means holding balances in many currencies, which our treasury setup cannot handle today. (I'm aware this conflicts with Hannah's wish to show local prices — showing an *indicative* local price is fine, as long as the charge is in one of our three currencies.)

### C2. Tutor payouts

- Tutors are paid in their own currency where our payout provider supports it. Initially: **EUR, GBP, USD, MXN, BRL, INR, PLN and COP**. Others receive USD.
- Payouts must be **monthly**, on the 5th working day, for lessons completed in the previous calendar month. Weekly payouts multiply our transfer fees and we have had a number of cases in which learners dispute a charge with their bank several weeks after the lesson. If we've already paid the tutor, we lose the money.
- I could accept **twice-monthly** payouts as a compromise, with a **14-day holding period** after each lesson before its earnings become payable.
- A tutor must have a minimum balance of 20 USD (or equivalent) to receive a payout; smaller balances roll over.
- The exchange rate used for each payout must be locked at the time the payout is calculated and shown on the tutor's statement.
- Payout fees charged by the provider should be shown to the tutor; whether we absorb them or pass them on is still open.
- Before receiving their first payout, tutors must provide tax information (country of tax residence, tax ID where applicable) and bank or payout-account details. We need to produce annual earnings statements for tutors and, for US-based tutors, the relevant year-end tax form.

### C3. Commission and pricing

- Commission should stay at **20%** on regular lessons, not 15%. Our current 18% does not cover payment processing, support and marketing. I could accept a tiered model (20% → 15% for high-volume tutors) if Product can show it improves retention.
- **Trial lessons cannot be free** to the learner. A free trial has no payment-processing cost, but it still costs support time and we see abuse (people booking free trials with dozens of tutors). My proposal: the trial is paid at **50% of the tutor's normal price**, the tutor receives their usual share of that amount, and a learner may book a maximum of 3 trials in any 30-day period.
- Package discounts are funded by the tutor, not by Brightquill (commission is on the discounted price).

### C4. Cancellations and refunds

- Free cancellation up to **24 hours** before the lesson. Between 24 and 2 hours: 50% refunded as lesson credit, not cash. Less than 2 hours or no-show: no refund. I understand Product wants 2 hours; I think that is too generous for tutors who have blocked out their time.
- Refunds to the original payment method only when a lesson did not happen because of the tutor or a technical fault on our side. Otherwise refunds are given as TalkPath credit that expires after 12 months.
- Unused package lessons expire 12 months after purchase. (Note: Chatterbox Tutors packages never expired — we need a decision on migrated packages.)
- Every refund, credit and manual adjustment must have a reason code and be visible in the finance reports.

### C5. Reporting and controls

- Daily reconciliation report of learner payments received vs. bookings created, by currency.
- Monthly report of tutor earnings, commission, refunds, credits issued and credits outstanding (as a liability).
- Payout run screen: Finance prepares a payout run, reviews totals by currency, and a second Finance user must approve it before it is sent (four-eyes principle).
- Ability to put an individual tutor's payouts on hold (e.g. during a dispute or investigation).
- All amounts stored with their currency; no mixing of currencies in totals without an explicit conversion and rate.
- Export to our accounting system (CSV is fine to start).

### C6. VAT and sales taxes

We are registered in Ireland. Digital services sold to consumers in the EU require VAT at the learner's country rate, and similar rules apply in the UK. Prices shown to learners must be tax-inclusive. We need help working out what applies to India and Brazil.

---

## Part D — Open points we already know about

1. Free vs. paid trial (Product: free; Finance: 50% price).
2. Commission rate (Product: 15%; Finance: 20%).
3. Payout frequency (Product: weekly; Finance: monthly, maybe twice monthly with a hold).
4. Cancellation window (Product: 2 hours; Finance: 24 hours with tiers).
5. Local-currency pricing for learners (Product: local; Finance: EUR/USD/GBP only).
6. Under-18 learners.

We will try to settle these with our CEO before the design phase, but please come back to us with your recommendations and any questions.

## Part E — Timeline

We would like the learner and tutor apps in beta with a group of 100 tutors by **March 2027**, and full migration from Chatterbox Tutors completed by **June 2027**, before the summer peak.

Gracias, thanks,
Hannah & Rajiv
