Calderbank Residential – repairs app – notes from kick-off + follow ups

(pasted together by Priya from the shared doc, sorry it's messy. Initials: GH = Gareth, PS = Priya, TM = Tom, LW = Leanne, SK = Sam)

---

**Mtg 1 – Tues 3rd, Calderbank office, GH / PS / TM / LW**

Why we're doing this
- GH: repairs currently come in by phone, email, text to Tom's mobile, sometimes via the landlord, sometimes tenants just tell the cleaner. nobody knows what's open. we've had 2 complaints to the property ombudsman this year, both about repairs left too long
- approx 1,450 units, mostly flats in 30-ish blocks + some HMOs + houses. ~600 landlords (some own 1 flat, some own 20+)
- want something tenants can use on their phone to report a repair, and contractors can update the job. and we can see everything in one place
- working name "FixLoop", GH not attached to it

Tenant side
- report a repair: what's wrong, where in the property, photos (TM: photos are a must, half the time we send the wrong trade)
- pick a category? plumbing, electrical, heating, roof, damp/mould, appliances, doors/locks/windows, pests, communal areas, other
- tenant should see the status of their repair and when someone is coming
- LW: some tenants don't speak much English. can it do other languages? GH: nice to have
- TM: they need to be able to say when they're in. half the jobs fail because they turn up and nobody's home
- also should be able to message about the job instead of ringing us

Priorities (TM)
- emergency – no heat in winter, no water, gas smell, flooding, unsafe electrics, can't lock front door. attend within 4 hours
- urgent – within 24 hours
- routine – within a week or so, depends
- tenants will mark everything as emergency. so we decide the priority not them. or they suggest and we confirm?
- gas smell – app should tell them to ring the gas emergency line FIRST before anything else

Contractors
- we use ~45 contractors, mix of one-man-bands and bigger firms. a few do most of the work
- TM assigns the job to a contractor. they should get it on their phone, accept or reject
- they update: on my way, on site, completed, needs parts / second visit, couldn't access
- photos before and after (PS: so we can prove it to the landlord)
- they need to upload their invoice against the job
- contractors must have valid insurance + gas certificate for gas work – PS keeps this in a spreadsheet atm, would be good if the system stops us assigning someone whose insurance has run out

Landlords
- GH: landlords have to approve anything over £250 unless it's an emergency
- LW: some landlords want to approve everything, some say just do it up to £500. so it's per landlord really
- do landlords get a login? GH thinks yes, at least to see jobs on their properties and approve quotes. LW not sure they'll use it, half of them are 70+

Actions
- PS to collect example jobs from last month
- TM to list contractors + trades
- SK to look at whether we can do it as an app or just a website

---

**Mtg 2 – Thurs 12th, video call, PS / TM / SK / LW**

- SK: app for tenants and contractors, web for the office. tenants could also use web if they don't want to download
- recap from last time – photos!! TM again: tenants must be able to upload photos and video if possible
- PS: who are "we" in the system? office team is me, Tom, two property managers (Hannah and Joel) and Leanne on accounts. property managers look after specific blocks. they should only see their blocks? or everything? TM: everything, we cover for each other
- LW: accounts needs to see invoices and match to jobs, then it goes into our accounts package (we export to csv now). approve invoice -> mark paid
- recharges: if the tenant caused the damage, cost gets recharged to the tenant. who decides? TM decides, LW bills them. needs flagging on the job
- block repairs (communal stuff, lifts, door entry, stairwell lights) – lots of tenants report the same thing. TM gets 15 reports of the same broken light. need to be able to link them to one job, and tell all of them when it's fixed
- some blocks have a freeholder/management company that isn't us – then we just pass it on. not sure how that works in the system
- SK: login for tenants – email + password? or text code? lots of tenants change phone numbers
- tenants move out – their access should stop. new tenant moves in – need to link them to the flat. LW: we have the tenancy list in the lettings system, can we sync? SK: maybe, need to check if it has an API

Contractor updates (again)
- they should be able to propose a time slot to the tenant and the tenant confirms
- if they can't get in, they mark no access, tenant gets a message, and the job goes back to TM
- if job needs a quote first (bigger jobs) contractor uploads quote, we send to landlord for approval if over the limit (GH said £300 last time? check)
- TM: want to see on a map or list which jobs are overdue vs the priority time

---

**Follow up – email thread pasted in, GH / PS, 15th**

GH: Thought about it more. The key things for me:
1. tenants report, with photos, and can see progress
2. we can see every open job and how long it's been open, red if it's past its deadline
3. contractors update from site
4. landlords approve over the threshold
5. reports for the monthly landlord statements – what was done on their property and what it cost
6. a record we can show the ombudsman if there's a complaint – who did what when

PS: agree. also
- tenants should get an automatic update when status changes, text or push or email, whichever they prefer
- after the job's done, ask them if they're happy with it. if not, job reopens?
- damp and mould – we have to treat these differently now (new rules), they need inspecting within a set time and we need to keep a record. Tom has the details
- out of hours – emergencies at night go to the out of hours service we pay for. they'd need a login too probably
- we want to be able to add jobs ourselves when someone phones in, on behalf of the tenant
- planned maintenance (annual gas safety checks, fire alarm tests) – could this go in too? GH: phase 2 maybe

GH: yes. keep it simple to start. needs to be easy for the tenants, a lot of them aren't techy. and quick for Tom.

PS: one more – landlords who live abroad. they get emails at weird times, approvals take days. can we auto approve if they don't reply in X days? GH: no. well, maybe for urgent. let's discuss.

---

open questions list (PS, not finished)
- who sets priority
- landlord approval limit – £250? £300? per landlord?
- do landlords log in
- languages
- out of hours provider access
- lettings system sync
