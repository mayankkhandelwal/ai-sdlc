# Answer Key: h-04-tutoring

## Meta

- **Domain:** Two-sided language tutoring marketplace: tutor onboarding, discovery, booking/scheduling across timezones, payments, multi-currency payouts, reviews, migration from a legacy app.
- **Platforms:** Web + iOS/Android for learners and tutors; web back-office for staff.
- **Style:** Long, collaborative brief with two stakeholder sections (Product vs Finance) that disagree on several points; an "open points" list; a quoted passage in Spanish with a rough translation; legacy-system migration section.
- **Length:** ~2,550 words.
- **Traps:** Stakeholder disagreements that must be surfaced as contradictions/decisions rather than silently resolved; multi-currency charge vs payout currencies; Spanish quote containing requirements (weekly payout, local currency, pre-payout visibility, Spanish UI); out-of-scope list (group lessons, referrals, courses, AI partner); under-18 option that is "not sure for release 1"; legacy package expiry conflict; undefined badge criteria.

## Roles expected

1. Learner
2. Tutor (and Tutor Applicant before approval)
3. Tutor Success staff
4. Learner Support staff
5. Content Moderator
6. Finance user (preparer) and Finance approver (four-eyes)
7. Admin
8. (Conditional, likely out of release 1) Parent/guardian booking for a minor

## Requirements gold draft

| ID | Requirement | Support |
|----|-------------|---------|
| G-1 | Learner sign-up via email, Google or Apple with minimal profile (name, target language, level A1–C2, timezone auto-detected/editable). | "Sign up with email, Google or Apple" / "just name, the language they want to learn, their current level (we use A1–C2) and their timezone" |
| G-2 | Tutor search and filters: language, price, availability, country, other languages, specialities, rating. | "Search and filter tutors by language, price, availability ... and rating" |
| G-3 | Tutor profile with intro video, bio, prices, reviews and calendar in learner's timezone. | "a calendar showing open slots in the learner's own timezone" |
| G-4 | Timezone-correct scheduling for all bookings. | "learners and tutors regularly turn up at different times because of timezone bugs. That cannot happen in TalkPath." |
| G-5 | Trial lesson, one per tutor per learner, tutor opt-in (price disputed). | "one per tutor per learner" / "Tutors can choose whether they offer trials." |
| G-6 | Single lessons and packages of 5/10/20 with tutor-set discount max 20%; discount funded by tutor. | "packages of 5, 10 or 20 lessons with the same tutor at a discount the tutor sets (max 20% off)" / "Package discounts are funded by the tutor" |
| G-7 | Recurring lesson booking. | "Book recurring lessons (e.g. every Tuesday 19:00 for 8 weeks)." |
| G-8 | Reschedule and cancel (policy disputed). | "Reschedule or cancel." |
| G-9 | Learner–tutor messaging with PDF/image/audio attachments. | "Messages should allow attachments (PDF, images, audio)." |
| G-10 | Join lesson from app: built-in video preferred; auto-attached external link acceptable for release 1. | "external links are acceptable as long as the link appears in the booking automatically" |
| G-11 | Ratings 1–5 and written reviews only by learners who completed a lesson with that tutor. | "only learners who have actually completed a lesson with that tutor can review" |
| G-12 | Learner sees history, upcoming lessons, remaining packages, receipts. | "See their lesson history, upcoming lessons, packages remaining and receipts." |
| G-13 | Tutor application (ID, photo, video, languages + proficiency, certificates, demo) reviewed by Tutor Success. | "The application includes ID, a profile photo, intro video..." |
| G-14 | Tutor availability: weekly recurring blocks plus exceptions; two-way Google Calendar sync; Outlook optional. | "Availability must sync both ways with Google Calendar; Outlook would be nice." |
| G-15 | Tutor sets price per lesson length (30/45/60/90) in own currency; learners see converted price. | "Set their own price per lesson length (30, 45, 60, 90 minutes) in their own currency" |
| G-16 | Tutor sets minimum booking notice. | "Set a minimum notice period for bookings" |
| G-17 | Auto-accept or manual approval of a new learner's first booking. | "Accept bookings automatically, or choose to approve each new learner's first booking manually." |
| G-18 | Tutor earnings, upcoming payouts, history and downloadable statements. | "See earnings, upcoming payouts and payout history, and download statements" |
| G-19 | Tutor reports learner no-show after 10 minutes; tutor paid in full. | "If the learner doesn't turn up within 10 minutes, the tutor gets paid in full." |
| G-20 | Configurable commission with tiering by volume (rates disputed). | "Tutors who teach more than 100 hours in a rolling 3-month period could drop to 12%." / "I could accept a tiered model" |
| G-21 | Tutor Success: approve/reject applications with reason, suspend tutors. | "review tutor applications, approve or reject with a reason, suspend tutors" |
| G-22 | Learner Support: look up bookings, refunds/credits, dispute resolution. | "look up bookings, issue refunds or lesson credits, resolve disputes" |
| G-23 | Moderators review reported messages and reviews. | "review reported messages and reviews" |
| G-24 | Admin manages languages, specialities, lesson lengths, commission, staff accounts. | "manage languages, specialities, lesson lengths, commission settings and staff accounts" |
| G-25 | Learners must be 18+. | "Learners must be 18 or over." |
| G-26 | Flag (not block) off-platform contact/payment attempts in messages. | "we don't want to block them automatically, but we want them flagged" |
| G-27 | Migrate active tutors, learners, profiles, reviews, upcoming bookings, unused packages, balances (no double payment). | "must be paid out correctly ... but never twice" |
| G-28 | Parallel run ~1 month; no new legacy bookings after cut-over. | "run both systems in parallel for about a month, with no new bookings in Chatterbox Tutors after cut-over" |
| G-29 | UI in English and Spanish at launch; Portuguese and German later. | "available in English and Spanish at launch, with Portuguese and German soon after" / "la aplicación tiene que estar en español también" |
| G-30 | Tutors see expected payout amount before each payout. | "queremos ver claramente cuánto vamos a recibir antes de cada pago" (Spanish quote) |
| G-31 | Email and push notifications for listed events; non-essential can be turned off. | "Users must be able to turn off non-essential notifications." |
| G-32 | Reminders 24h and 1h before lesson. | "reminders 24 hours and 1 hour before the lesson" |
| G-33 | Lesson notes by tutor visible to learner; learner goals; tutor-updated estimated level. | "write short lesson notes after each lesson ... that the learner can see in the app" |
| G-34 | Tutor badges carried over (Top Rated, Fast Responder, 500+ lessons); Fast Responder = 90% within 12h over 30 days. | "replying to 90% of new learner messages within 12 hours over the last 30 days" |
| G-35 | Learners pay upfront at booking/package purchase; no pay-after. | "Learners must pay upfront at the time of booking (or package purchase)." |
| G-36 | Payment methods: card, Apple Pay, Google Pay; PIX and UPI desirable. | "Card payments, Apple Pay and Google Pay are required; PIX for Brazil and UPI for India would be valuable" |
| G-37 | Payout currencies EUR, GBP, USD, MXN, BRL, INR, PLN, COP; others USD. | "Initially: EUR, GBP, USD, MXN, BRL, INR, PLN and COP. Others receive USD." |
| G-38 | Minimum payout balance 20 USD equivalent; roll over smaller balances. | "minimum balance of 20 USD (or equivalent)" |
| G-39 | Exchange rate locked at payout calculation and shown on statement. | "locked at the time the payout is calculated and shown on the tutor's statement" |
| G-40 | Provider payout fees shown to tutor. | "Payout fees charged by the provider should be shown to the tutor" |
| G-41 | Tax info and payout account required before first payout; annual statements; US year-end tax form. | "tutors must provide tax information ... and bank or payout-account details" |
| G-42 | Refund to original method only for tutor fault/platform failure; otherwise credit expiring after 12 months. | "Otherwise refunds are given as TalkPath credit that expires after 12 months." |
| G-43 | Reason codes on all refunds, credits, adjustments. | "Every refund, credit and manual adjustment must have a reason code" |
| G-44 | Daily payment reconciliation and monthly earnings/commission/credit-liability reports. | "Daily reconciliation report" / "Monthly report of tutor earnings, commission, refunds, credits issued and credits outstanding" |
| G-45 | Payout run prepared by one Finance user, approved by a second (four-eyes). | "a second Finance user must approve it before it is sent (four-eyes principle)" |
| G-46 | Hold individual tutor payouts. | "put an individual tutor's payouts on hold" |
| G-47 | Amounts always stored with currency; no implicit cross-currency totals. | "All amounts stored with their currency; no mixing of currencies in totals" |
| G-48 | Accounting export (CSV). | "Export to our accounting system (CSV is fine to start)." |
| G-49 | Tax-inclusive learner prices; VAT at learner's country rate for EU/UK consumers. | "Prices shown to learners must be tax-inclusive." |
| G-50 | Package expiry 12 months after purchase (Finance), legacy packages decision pending. | "Unused package lessons expire 12 months after purchase." |

## Convention features implied

- Password reset, account settings, profile edit, account deletion (privacy).
- Language switcher for UI.
- Timezone settings for both roles.
- Payment method management and checkout.
- Booking confirmation screens, calendar views.
- Dispute case records and status.
- Staff role-based access control and audit log.
- Report/flag button on messages and reviews.
- Credit balance / wallet display (implied by credits).

## Gaps a good critic should find

| Importance | Gap | Question |
|------------|-----|----------|
| blocking | Trial price unresolved. | Is the trial free or 50% of the tutor's price, and is there a cap of 3 trials per 30 days? |
| blocking | Commission rate and tier rules unresolved. | What are the base commission and tier thresholds, and is the tier calculated per lesson or applied retroactively? |
| blocking | Payout frequency unresolved (weekly / twice-monthly with 14-day hold / monthly). | Which payout schedule and holding period apply at launch? |
| blocking | Cancellation policy unresolved (2h free vs 24h tiered). | Which cancellation windows and refund forms (cash vs credit) apply, and do they differ for packages and trials? |
| blocking | Learner charge currencies unresolved (local vs EUR/USD/GBP). | Are learners charged only in EUR/USD/GBP with indicative local prices? How are FX differences between charge and display handled? |
| important | Under-18 learners in release 1. | Is the parent-books-for-teen flow in or out of release 1? |
| important | Migrated package expiry. | Do migrated legacy packages keep no expiry, or get 12 months from migration? |
| important | Payout fee absorption open. | Does the company absorb provider payout fees or pass them to tutors? |
| important | Tax handling for India and Brazil unknown. | Which tax rules apply to learners in India and Brazil, and who will advise? |
| important | Tutor no-show and technical failure handling. | What happens to the learner and tutor payment when the tutor doesn't show or the connection fails? Who decides? |
| important | Built-in video vs external link for release 1. | Which video option is in scope for release 1, and which external tool? |
| important | Rescheduling rules not defined separately from cancellation. | Is a reschedule treated as a cancellation for policy purposes? How late can it be done? |
| important | "Top Rated" and "500+ lessons" badge criteria. | What exactly qualifies for Top Rated? |
| minor | Tutor application demo format. | Is the "short demo" a recorded video or a live session with staff? |
| minor | Recurring bookings payment timing. | Are recurring lessons charged all upfront or per lesson? |
| minor | Tutors' lesson price in currencies not supported for payout. | Can a tutor in an unsupported country set prices in their local currency even though payouts are in USD? |
| minor | Off-platform flagging: who reviews flags and what actions exist. | Do moderators review flagged messages, and what are the sanctions? |

## Contradictions

1. **Trial lesson price.** "In my view the trial should be **free and 30 minutes**" vs "**Trial lessons cannot be free** to the learner."
2. **Commission.** "I want to drop this to **15%** for TalkPath" vs "Commission should stay at **20%** on regular lessons, not 15%."
3. **Payout frequency.** "I'd like weekly payouts every Monday for all lessons completed the previous week." (also the Spanish quote "cobrar cada semana") vs "Payouts must be **monthly**, on the 5th working day".
4. **Cancellation window.** "**free cancellation up to 2 hours before the lesson**" vs "Free cancellation up to **24 hours** before the lesson."
5. **Learner pricing currency.** "Learners see the price converted to their currency." vs "charge learners in a small number of currencies only: EUR, USD and GBP" (partially reconciled by "showing an indicative local price is fine").
6. **Trial commission.** "for trial lessons we take nothing (they're free anyway)" vs "the tutor receives their usual share of that amount" (implies commission on trials).
7. **Package expiry vs migration.** "Unused package lessons must carry over." vs "Unused package lessons expire 12 months after purchase. (Note: Chatterbox Tutors packages never expired...)"
8. **Tutor paid in full on learner no-show** vs Finance holding period / disputes — soft tension, not direct.

## Traps

- **Injected text:** none.
- **Second language:** Two Spanish quoted paragraphs in B8 containing requirements; an English rough translation follows; closing "Gracias". The product should extract G-29/G-30 and the weekly-payout preference from them, and should not treat the translation as new requirements beyond the Spanish source.
- **Vague words:** "more or less", "clunky", "within a few minutes", "fairly and on time", "generous", "would be nice", "straightforward from a safeguarding point of view", "Nothing fancy", "soon after", "could drop", "valuable", "about a month", "every few lessons".
- **Tables:** none (lists only).
- **Out of scope (release 1):** group lessons, tutor referral programme, self-paced courses, AI conversation partner — must not be generated as screens.
- **Existing app:** legacy app must be referenced only in migration stories; features to keep = badges.
- **Currencies:** eight payout currencies, three charge currencies, indicative local display — a good output keeps charge, display and payout currencies distinct.
- **Stakeholder disagreement:** Part D explicitly lists open points; the product should present both options, not pick one silently.

## Expected screens

| # | Screen | Role |
|---|--------|------|
| 1 | Sign up / sign in (email, Google, Apple) and onboarding | Learner |
| 2 | Tutor search and filters | Learner |
| 3 | Tutor profile with calendar | Learner |
| 4 | Booking and checkout (single, trial, package, recurring) | Learner |
| 5 | My lessons (upcoming, history, reschedule/cancel, join) | Learner |
| 6 | Messages / conversation | Learner, Tutor |
| 7 | Review a lesson | Learner |
| 8 | Learning journal / progress and goals | Learner (Tutor writes notes) |
| 9 | Tutor application | Tutor applicant |
| 10 | Tutor availability and calendar sync | Tutor |
| 11 | Tutor pricing, packages and booking settings | Tutor |
| 12 | Tutor bookings / requests and no-show report | Tutor |
| 13 | Tutor earnings, payouts, statements and tax/payout details | Tutor |
| 14 | Tutor application review queue | Tutor Success |
| 15 | Booking lookup, refunds/credits and disputes | Learner Support |
| 16 | Moderation queue (reported/flagged messages, reviews) | Content Moderator |
| 17 | Payout run preparation and approval | Finance |
| 18 | Finance reports and reconciliation | Finance |
| 19 | Admin settings (languages, specialities, lesson lengths, commission, staff) | Admin |
| 20 | Notification preferences and language settings | Learner, Tutor |

## Notes

Draft — needs human review.
