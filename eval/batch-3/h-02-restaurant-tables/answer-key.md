# Answer Key: h-02-restaurant-tables

## Meta

- **Domain:** Multi-venue restaurant table reservations, waitlist and host-stand operations.
- **Platforms:** Guest mobile app; host tablet app; manager functions (device unspecified).
- **Style:** Very short, informal, enthusiastic email-style brief; heavy on vague adjectives; almost no business rules or numbers.
- **Length:** ~430 words.
- **Traps:** Vague quality words; "maybe"/"open to ideas" features (deposits) that must not be turned into firm rules; "smart" wait-time estimate with no method; manager platform not stated; no numbers for party size, booking window, cancellation cutoff, or hold times; a deadline that is relative ("before the holiday season").

## Roles expected

1. Guest (app user making reservations / joining waitlist)
2. Host (tablet at host stand)
3. Restaurant Manager (per venue; reporting and setup)
4. (Possibly) Group-level admin / Operations Director across the four venues — implied, not stated.

## Requirements gold draft

| ID | Requirement | Support |
|----|-------------|---------|
| G-1 | Guest can browse/select one of the group's four restaurants. | "people can find one of our restaurants" |
| G-2 | Guest can book a table by choosing time and party size. | "pick a time and book a table" / "say how many people" |
| G-3 | Guest can add special occasion and dietary notes to a booking. | "any special occasion (birthdays are huge for us!), and maybe dietary stuff" |
| G-4 | Guests receive booking reminders. | "They should get reminders so they don't forget" |
| G-5 | Guest can modify or cancel a booking. | "be able to change or cancel easily" |
| G-6 | Guest can join a waitlist remotely from their phone. | "Guests can join it from their phone, even when they're standing outside" |
| G-7 | Guest notified when waitlist table is nearly ready. | "get a message when their table is nearly ready" |
| G-8 | Guest can see approximate waitlist position. | "see roughly where they are in the line" |
| G-9 | System estimates waitlist wait times. | "We'd love it to be smart about estimating wait times" (aspirational) |
| G-10 | Host tablet shows floor plan with table states (free, seated, about to free up). | "show the floor plan with all the tables, which ones are free, seated, or about to free up" |
| G-11 | Host sees tonight's bookings. | "the bookings coming in for the night" |
| G-12 | Host can seat walk-ins. | "seat walk-ins quickly" |
| G-13 | Host can move parties between tables. | "move people around" |
| G-14 | Host can combine tables for large groups. | "combine tables for bigger groups" |
| G-15 | Host manages the waitlist from the tablet. | "handle the waitlist" |
| G-16 | Recognise repeat guests and show host notes/preferences. | "recognise regulars" / "Notes like \"likes the window table\"" |
| G-17 | (Tentative) Deposit or card hold for large groups or busy nights. | "maybe some kind of deposit or card hold for bigger groups or busy nights, but we're open to ideas" |
| G-18 | Manager nightly report: covers, no-shows. | "see how each night went — covers, no-shows" |
| G-19 | Manager configures tables (floor plan) and opening hours. | "set up their tables and opening hours" |
| G-20 | No-show tracking. | implied — needed for G-18 and the stated no-show problem. |
| G-21 | Branding: copper and deep green, warm and elegant. | "warm, elegant, our copper and deep green colours" |

## Convention features implied

- Guest account sign-up / sign-in (or guest checkout with phone number) — implied by reminders, regulars, change/cancel.
- Booking confirmation screen and message.
- "My bookings" list.
- Push/SMS notification preferences.
- Host sign-in on shared tablet, venue selection.
- Booking status lifecycle (booked, confirmed, seated, completed, no-show, cancelled) — implied.
- Phone/walk-in booking entry by host (implied by current phone bookings).

## Gaps a good critic should find

| Importance | Gap | Question |
|------------|-----|----------|
| blocking | Deposits/card holds are undecided. | Do you want deposits or card holds at launch? If so, for what party size, which nights/venues, what amount, and what is the refund/no-show charge policy? |
| blocking | No booking rules (slot length, booking window, max party size, lead time). | How far ahead can guests book, what slot intervals and dining durations apply per venue, and what is the maximum party size online? |
| important | Cancellation/modification policy not defined ("easily"). | Up to when can a guest change or cancel, and are there any penalties? |
| important | Waitlist notification channel and hold time unknown. | Is the "message" SMS, push or both, and how long is a table held after notifying a guest? |
| important | Wait-time estimation method unspecified ("smart"). | Is a simple manual host estimate acceptable at launch, or is a calculated estimate required? |
| important | Regular recognition criteria undefined ("a bunch of times"). | How many visits make a regular, and what do you mean by treating them "special" — a tag, perks, priority? |
| important | Phone and Instagram bookings — still accepted? | Should hosts enter phone/DM bookings into the system manually? |
| important | Manager platform and group-level access not stated. | Do managers use the tablet, a web dashboard or a phone? Does someone need cross-venue reporting? |
| important | Guest identity — account required or phone-only? | Must guests create an account, or can they book with just a name and phone number? |
| minor | Reminder timing. | When should reminders be sent? |
| minor | Dietary info handling ("maybe"). | Is dietary info free text or structured allergens? Any sensitivity/consent rules? |
| minor | Launch date vague. | What is the exact target launch date? |
| minor | Venue differences (rooftop, weather) not covered. | Does Ember Terrace need weather-related closures or indoor/outdoor seating preferences? |

## Contradictions

None explicit. Soft tension: "book a table in like two taps" vs collecting party size, occasion, dietary details and possibly a deposit.

## Traps

- **Injected text:** none.
- **Vague words:** "modern", "slick", "super easy", "really premium", "boutique hotel app", "two taps", "easily", "roughly", "smart", "fast", "crazy", "a bunch of times", "a bit special", "amazing", "maybe", "that kind of thing", "warm, elegant", "fun but classy", "if at all possible", "open to ideas".
- **Tables:** none.
- **Language notes:** English, informal; exclamation marks; tentative language must be flagged as optional/assumption, not hard requirements.

## Expected screens

| # | Screen | Role |
|---|--------|------|
| 1 | Restaurant list / venue picker | Guest |
| 2 | Venue detail with availability | Guest |
| 3 | Booking flow (date, time, party size, occasion, dietary) | Guest |
| 4 | Booking confirmation | Guest |
| 5 | My bookings (view, modify, cancel) | Guest |
| 6 | Join waitlist | Guest |
| 7 | Waitlist status (position, estimate) | Guest |
| 8 | Sign in / profile | Guest |
| 9 | Host floor plan with live table states | Host |
| 10 | Tonight's reservations list | Host |
| 11 | Seat walk-in / assign table (incl. combine tables) | Host |
| 12 | Waitlist management | Host |
| 13 | Guest profile with visit history and notes | Host |
| 14 | Nightly report (covers, no-shows) | Manager |
| 15 | Floor plan / table setup | Manager |
| 16 | Opening hours and booking settings | Manager |

## Notes

Draft — needs human review.
