# Answer Key: b1-03-canteen

## Meta

- **Domain:** Secondary school canteen; meal pre-ordering, prepaid balances, free school meals, kitchen dashboard.
- **Platforms:** Mobile app (iPhone and Android) for parents and students; web dashboard for kitchen and Business Office.
- **Style:** Medium-length internal working draft written by a school business office. Semi-structured headings, mostly clear, but assembled from several contributors so sections disagree.
- **Length:** About 1,250 words.
- **Deliberate traps planted:**
  - **Contradiction 1 (order cutoff):** 6:00pm the evening before vs 9:00am on the day.
  - **Contradiction 2 (who can order):** students can order their own lunch vs only parents and carers can place orders.
  - Pricing / menu table with rules embedded in cells (FSM eligibility, Fridays only, not pre-orderable, age restriction on fizzy drinks).
  - Existing paper process (envelopes, slips, cash, tally sheet) to be run in parallel at launch.
  - Rule referenced but never defined: "negative ... balances" appear in reports, but nothing says whether a balance may go negative (and "If they forget, the meal is charged as normal" could push it negative).
  - External system dependency (student information system) for allergy data.
  - Domain abbreviation FSM.

## Roles expected

1. Parent / carer (including multiple parents per child and multiple children per parent).
2. Student.
3. Kitchen staff (including till staff).
4. Business Office staff (School Business Manager).
5. Head of Catering (menu and price manager).
6. School nurse (allergy override authority; implied role, may be off-system).
7. (System actor) Student information system (ScholarDesk) for students and allergy data.

## Requirements (gold draft)

### Ordering

- G-1. Show the menu for the next two weeks to parents and students. — Quote: `Parents and students should be able to see the menu for the next two weeks.`
- G-2. Each day offers three hot options, a jacket potato bar and a grab and go bag. — Quote: `Each day there are three hot options, a jacket potato bar and a "grab and go" bag.`
- G-3. Orders can be placed for any day in the two-week window. — Quote: `Orders can be placed for any day in the two-week window.`
- G-4. Order cutoff and lock (CONTRADICTED — see Contradictions). — Quote: `Orders must be placed by 6:00pm the evening before. After that, the order for that day is locked and the kitchen uses the numbers to prepare.`
- G-5. Who can place orders (CONTRADICTED — see Contradictions). — Quote: `Students in Years 7 to 13 can log in with their school account and order their own lunch, using the balance their parent has topped up.`
- G-6. Parents can see everything their child orders. — Quote: `Parents can see everything their child orders`
- G-7. Parents can block specific items or set a daily spending limit for their child. — Quote: `can block certain items (e.g. no fizzy drinks) or set a daily spending limit`
- G-8. Each order is for one sitting (12:20 or 13:00); Years 7 and 8 are only offered 12:20. — Quote: `Year 7 and Year 8 always eat at 12:20, so they shouldn't be offered the later sitting.`
- G-9. Parent can cancel a day's order for absence and have the money refunded to balance. — Quote: `If a student is absent, the parent should be able to cancel the day's order and get the money back onto the balance.`
- G-10. Uncancelled, uncollected meals are charged as normal. — Quote: `If they forget, the meal is charged as normal.`

### Menu and prices

- G-11. Head of Catering publishes the menu every other Thursday. — Quote: `Mr Adeyemi publishes the menu every other Thursday.`
- G-12. Menu items have price, FSM eligibility and notes (see table); Head of Catering manages menus and prices. — Quote: `**Head of Catering** (Mr Adeyemi) – manage menus and prices.`
- G-13. Jacket potato extra filling costs 30p (item add-ons/modifiers). — Quote: `Extra filling 30p`
- G-14. Pasta pot available Fridays only (day-of-week availability). — Quote: `Fridays only`
- G-15. Breakfast roll is not pre-orderable and only available 8:00–8:35. — Quote: `8:00–8:35 only, not pre-orderable`
- G-16. Fizzy drinks not sold to Years 7–9 (year-group item restriction). — Quote: `Fizzy drinks not sold to Years 7–9`
- G-17. One hot meal choice daily is always vegetarian (menu authoring rule). — Quote: `3 choices daily, one always vegetarian`
- G-18. FSM students get a daily £2.85 allowance; unused difference does not carry over; extras are charged to normal balance; only FSM-eligible items use the allowance. — Quote: `Free school meal (FSM) students get a daily allowance of £2.85. If they choose something cheaper the difference does not carry over, and if they add extras (e.g. a juice) the extra is taken from their normal balance.`

### Allergies and diet

- G-19. Allergy data imported from the student information system. — Quote: `Each student's allergy information comes from our MIS`
- G-20. Every menu item shows allergens from the 14 standard allergens. — Quote: `Allergens must be shown on every menu item using the 14 standard allergens.`
- G-21. Warn and block ordering of items containing a student's recorded allergen. — Quote: `If a student has a recorded allergy, the app should warn them and block any item containing that allergen.`
- G-22. Parents cannot override allergy blocks; must contact the school nurse. — Quote: `Parents shouldn't be able to override the block themselves – they need to contact the school nurse.`
- G-23. Parents set dietary preferences (vegetarian, halal, no pork) used only to filter the menu. — Quote: `Dietary preferences (vegetarian, halal, no pork) are set by the parent and are just used to filter the menu, not to block.`

### Money

- G-24. Parents top up by card in the app; minimum £10. — Quote: `Parents top up through the app by card. Minimum top-up £10.`
- G-25. Balances belong to the student and carry over between terms. — Quote: `Balances belong to the student and carry over between terms.`
- G-26. Leavers' remaining balance refunded to parent on request by Business Office. — Quote: `If a student leaves the school, any remaining balance is refunded to the parent on request by the Business Office.`
- G-27. Families can top up once and split across children, or top up each child separately. — Quote: `Families with more than one child at the school should be able to top up once and split it between children, or top up each child separately.`
- G-28. Business Office can record manual cash top-ups and print a receipt. — Quote: `The Business Office will need a way to add cash top-ups manually and print a receipt.`

### Kitchen and till

- G-29. Kitchen dashboard (large monitor) for today and tomorrow: item counts by sitting. — Quote: `How many of each item have been ordered, split by sitting.`
- G-30. Allergy and special diet orders highlighted with student name and photo. — Quote: `Allergy and special diet orders highlighted, with the student's name and photo.`
- G-31. Live count of meals collected. — Quote: `A live count of how many have been collected.`
- G-32. Dashboard updates automatically on late orders. — Quote: `The dashboard should update automatically when late orders come in.`
- G-33. Student shows a QR code at the till; till staff can look up by name if no phone; staff tap "collected". — Quote: `the student shows a QR code in the app (or says their name if they've forgotten their phone, and the till staff look them up). The till staff tap "collected".`
- G-34. Walk-up purchase from grab and go counter, paid from balance, if stock remains. — Quote: `If a student didn't order, they can still buy from the grab and go counter if there's anything left, paying from their balance.`
- G-35. Kitchen staff can view or print lists for each sitting. — Quote: `print or view the lists for each sitting`

### Reports

- G-36. Daily and weekly takings split by card and cash. — Quote: `Daily and weekly takings, split by card top-ups and cash.`
- G-37. FSM usage per student for termly local authority reporting. — Quote: `FSM usage per student (we have to report this to the local authority each term).`
- G-38. Waste report: prepared vs collected per day; kitchen enters prepared quantity. — Quote: `Waste report: items prepared vs items collected per day (kitchen will enter the number prepared).`
- G-39. List of students with negative or low balances (under £5). — Quote: `A list of students with negative or low balances (under £5) so we can send letters home.`

### Other

- G-40. Parent notifications for low balance and new menu published. — Quote: `Notifications to parents when the balance is low and when the new menu is out.`
- G-41. Mobile apps for iPhone and Android; web for kitchen and office. — Quote: `Should work on iPhone and Android. The kitchen and office will use the web version on school PCs.`
- G-42. Multiple parents per child (e.g. separated parents) and multiple children per parent. — Quote: `Must work for parents with more than one child, and for separated parents who both want access to the same child.`
- G-43. Run in parallel with paper envelopes for the first half-term (paper orders must be enterable) — implied: parallel running means paper orders must be keyed in so kitchen numbers are complete. — Quote: `We'd run the paper envelopes alongside for the first half-term.`
- G-44. Students log in with their school account. — Quote: `log in with their school account`

## Convention features implied but not written

- Parent registration and login; password reset; linking a parent to a child (verification that the parent really is the parent).
- Student login via school account (single sign-on implied).
- Staff login and role management (kitchen, till, office, catering head).
- Payment card processing with a payment provider; payment receipts; failed payment handling.
- Transaction history / statement for each student balance.
- Push notification permissions and preferences.
- Menu calendar management (creating 2-week menus, copying cycles).
- Term dates and non-school days (no orders on holidays / INSET days).
- Audit log for refunds and manual top-ups.
- Data protection for children's data (student photos, allergy data) and consent.

## Gaps a good critic should find

1. **Order cutoff contradiction** — blocking. "Is the order cutoff 6:00pm the evening before or 9:00am on the day? If late orders are allowed until 9:00am, can they also be changed or cancelled until then?"
2. **Who can place orders contradiction** — blocking. "Can students place their own orders, or only parents and carers? If students can, does the daily spending limit and item block still apply?"
3. **Negative balances** — important. "Can a balance go negative (e.g. a forgotten meal charged as normal, or walk-up purchase with low funds)? Is there an overdraft limit, and what happens at the till when funds are insufficient?"
4. **Absence cancellation deadline** — important. "Until when can a parent cancel for absence on the day itself, given the order is locked? Is the refund automatic or approved by the Business Office?"
5. **FSM allowance and pre-ordering** — important. "Do FSM students have to pre-order, and does the allowance apply to walk-up purchases? Where does FSM eligibility come from (the student information system or manual entry)?"
6. **Allergy override process** — important. "How does the school nurse override or adjust an allergy block — in this system or in the student information system? Who keeps allergy data in sync?"
7. **Student information system integration** — blocking. "Does the student information system provide an API or export for students, year groups, photos, allergies and parent contacts? How often does it sync?"
8. **Parent–child linking** — blocking. "How is a parent account linked to a student securely — invitation from school, code letter, or matched contact details?"
9. **Separated parents** — important. "Do both parents have equal rights (top up, order, set limits, see history)? Can each parent see the other's top-ups?"
10. **Staff meals** — minor. "Can the 140 staff pre-order or pay through the system?"
11. **Refund of card top-ups** — important. "Apart from leavers, can parents withdraw balance? Which payment provider handles refunds?"
12. **Menu changes after ordering** — important. "If the kitchen runs out or changes a dish after orders are placed, how are students notified and refunded?"
13. **Low-balance threshold for notifications** — minor. "Is the low-balance notification threshold the same £5 used in the report, and can parents set their own?"
14. **Paper parallel run** — important. "During the parallel half-term, who keys in paper orders and cash, and how are duplicates prevented?"
15. **Sitting assignment for Years 9–13** — minor. "Is there a capacity limit per sitting?"

## Contradictions planted

1. **Order cutoff**
   - Quote A: `Orders must be placed by 6:00pm the evening before.`
   - Quote B: `Parents can still order up to 9:00am on the day itself; the kitchen just needs final numbers by 9:15 so they can start cooking.`
2. **Who can place orders**
   - Quote A: `Students in Years 7 to 13 can log in with their school account and order their own lunch, using the balance their parent has topped up.`
   - Quote B: `only parents and carers will be able to place orders. Students will be able to log in to view their orders for the week and show their QR code at the till, but they can't place or change orders themselves.`

(The "Who it's for" list also says students "place orders", supporting Quote A.)

## Traps

- **Injected text:** None.
- **Vague words list:** "To keep things simple", "Other bits", "a lot of food", "big monitor", "low balance" (threshold only implied as £5 in reports), "e.g." lists of blockable items.
- **Tables:** One menu and price table (7 rows; columns: item, price, FSM eligible, notes). Embedded rules: extra filling 30p, pasta pot Fridays only, breakfast roll not pre-orderable and 8:00–8:35 only, fizzy drinks not sold to Years 7–9, one hot choice always vegetarian, water/juice two prices in one cell.
- **Existing paper process:** Monday tutor-group envelopes with slips and cash, Business Office typing totals into a spreadsheet, printed daily tally sheet; to run in parallel for the first half-term.
- **Second-language part:** None.
- **Undefined state:** negative balance.

## Expected screens

1. Sign in (parent account / student school account) — Parent, Student
2. Link child / family setup — Parent
3. Menu browser (two-week calendar with allergens and filters) — Parent, Student
4. Place / edit order (item, sitting, day) — Parent (and Student, pending contradiction)
5. My orders / week view with cancel for absence — Parent, Student
6. Balance and top-up (card, split between children) — Parent
7. Transaction history — Parent
8. Child settings: item blocks, daily limit, dietary preferences — Parent
9. QR code collection screen — Student
10. Notifications settings — Parent
11. Kitchen dashboard (counts by sitting, allergy highlights, live collected count) — Kitchen staff
12. Till / collection screen (scan QR, search by name, mark collected, walk-up sale) — Till staff
13. Waste entry (number prepared) — Kitchen staff
14. Menu and price management (publish two-week menu, allergens) — Head of Catering
15. Cash top-up and receipt — Business Office
16. Refunds / leaver balance — Business Office
17. Reports (takings, FSM usage, waste, low/negative balances) — Business Office
18. Student and FSM management / data sync status — Business Office
19. Staff users and roles — Business Office (implied)

## Notes

Draft — needs human review.
