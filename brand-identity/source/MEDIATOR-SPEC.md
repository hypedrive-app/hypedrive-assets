# Mediator mockups: the real-logic spec (source: hypedrive repo `apps/mediator/src`, `packages/domain/src/mediator`, `docs/architecture/mediator-deals.md`, `docs/architecture/mediator-app/06-decisions.md`, `08-names.md`, mapped 2026-11-26)

The mediator mockups must follow this file. Every word, status and number comes from the real code or the owner-decided docs. Layouts and visual style are OURS: Bricolage display, Geist UI, white canvas, tactile cobalt, the calm-controls rules in BRIEF.md. Do not copy the mediator-app v3 layouts.

**Form factor: mobile-first.** "Hypedrive Mediator" is a web PWA (mediator.hypedrive.app) built phone-first. The phone has a bottom dock; the same app gets a left sidebar from 768 px. Mockups are 390 px phone frames, with one desktop frame at most. Rows are cards on a phone (a phone always draws rows or cards, never a table).

A mediator is an approved creator who brings shoppers to campaigns: they enroll shoppers on a deal, or share their store link and the shopper enrolls. The brand pays Hypedrive; Hypedrive pays the mediator; the mediator pays the shopper back off-platform and keeps the rest.

## How a mediator earns (the money model, owner-decided)
Source: `docs/architecture/mediator-deals.md` §2 and §7, `apps/mediator/src/pages/deal/slice-sheet.tsx`.
- **The pot.** Each campaign has a pot: a cashback percent of the order price plus a bonus in rupees. Glow serum: "60% cashback to split" and "₹200 bonus to split".
- **The slice** is what the mediator keeps. Cashback: whole points only, at most 49, and always below the campaign's cashback. The campaign's cashback can never be under 50%. Bonus: any rupee amount up to the whole bonus, and the shopper must keep at least ₹1 of it. The slice is rounded down to whole rupees.
- **The offer** is what the shopper gets: the payout minus the slice. Shoppers never see the slice: "Shoppers never see what you keep. The rupees are worked out on each real enrollment."
- **Glow serum example** (order ₹1,899):
  - Pot: 60% (₹1,139) + ₹200 = payout ₹1,339.
  - Kavya keeps 5% (₹94) + ₹50 = **You keep ₹144**.
  - The shopper is offered 55% + ₹150, shown as **"Get 55% + ₹150 back"** (about ₹1,195).
  - Deal row: "Shopper 55% back · You keep 5% + ₹50 bonus".
- **Lock.** The slice locks at the shopper's first tap, into the spot hold. A later slice edit does not change that shopper's offer.
- **Payback flow** (one record per enrollment):
  1. Brand approves. Hypedrive pays the mediator's wallet ("Paid by Hypedrive").
  2. The mediator pays the shopper off-platform (UPI or bank) and taps "Mark paid".
  3. The shopper answers "Did you get it?": "Yes", "Got less", or "Not yet".
  4. Outcomes: Confirmed · Partly paid · Disputed · Unpaid. Tolerance is the larger of ₹10 or 2%. Reminders go to the shopper on days 0, 7 and 25. Day 30 is final.
  - Non-payment levers: more than 5 unpaid enrollments pauses new orders and deals. A payout hold after 14 days of "Not yet" waits for a wallet-service hook (not built).
- **Withdrawing.** One shared Hypedrive wallet per account. A withdrawal needs a verified PAN, and is capped by the held payback still due ("Held"). Fee ₹0; minimum NOT CONFIRMED for mediators (the creator spec says ₹100, same wallet).
- **One server quote** produces every figure. Clients never compute money. The mediator sees three figures per deal: you get (payout), the shopper gets (offer), you keep.

## Vocabulary (exact)
- **Words to use** (`docs/architecture/mediator-app/08-names.md`; code wins where they differ):
  - **"deal"** is correct here: one mediator's priced campaign (mediator, campaign). "Deals", "My deals", "Add to store".
  - "campaign" for the brand's offer; "store" is the mediator's public page (not "hub"); "shopper" (never buyer or customer); "mediator"; "slice" in docs only. The screens say **"what you keep"**: "Set what you keep", "You keep".
  - "offer" is what the shopper gets. "payout" is Hypedrive paying the mediator. **"paid back" / "payback"** is the mediator paying the shopper.
  - "spots" ("8 spots left" at 10 or fewer left; "Full" at none). "proof" and "tasks". "code" is the 8-character reference.
  - **"enrollment"**, not "order": nav "Enrollments", "Enroll a shopper", "Cancel enrollment". (The decision doc says "order" for the shopper's side; the shipped mediator app says enrollment everywhere. Use enrollment.)
- **Nav (phone dock):** Today · Enrollments · **New** (centre disc: starts "Enroll a shopper") · Deals · Wallet. **More sheet:** TrustDrive · Shoppers. Settings behind the avatar.
  - Sidebar from 768 (daily): Today, Inbox, Enrollments, Deals, TrustDrive; bottom: Wallet, Settings. Shoppers is a directory reached from Enrollments, not a destination.
  - The docs still say a three-tab dock (Home, Store, Shoppers). Code is the truth (`apps/mediator/src/lib/nav.ts`).
- **Buttons (verbs):**
  - Deals: "Add to store", "Set what you keep", "Edit what you keep", "Save what you keep", "View public page", "Pause", "Resume", "Pin", "Unpin", "Remove", "Share".
  - Enrolling: "Enroll a shopper", "Pick a shopper", "Add a new shopper", "Add shopper", "Open enrollment", "Done".
  - Payback: "Mark paid" (sheet title "Mark Asha paid"; many: "Mark paid" and "Mark all N paid"), "Mark again", "Respond", "Submit" (tasks), "Cancel enrollment".
  - Money: "Withdraw", "Add an account", "Verify your PAN".
  - TrustDrive: "Reply", "Add number", "Claim listing", "Ask for ownership", "Withdraw request", "Send appeal".
  - Gate: "Become a mediator", "Apply again", "Get started", "Review terms".
- **Mediator role phases** (`mediator-phase.ts`): Under review [neutral] · Active [success] · PAN expired [warning] · Needs PAN [warning] · Suspended [warning] · Not approved [danger] · Rejected [neutral] · Ended [neutral].
- **Deal states** (`mediator-deal-copy.ts`, label and note):
  - Live "Showing in your store." · Paused "Paused. Shoppers can't see it in your store." · Full · Full for you "You've taken every place you can on this campaign." · Ended.
  - Off "Mediator deals are switched off on this campaign." · Store paused "Your store is hidden while your mediator role is suspended." · Edit my deal "The campaign's pricing changed and your slice no longer fits. Edit it to show this deal." · Not live "This campaign isn't taking orders right now."
  - Row word: "Live" is silent; a live deal shows "8 spots left" or "Ends in 3 days" (3 or fewer) in the warning tone instead.
- **Store tabs:** All · Live · Paused · Full. **Browse chips:** All · New · Saved · Ending soon. **Filters:** Show · Shop · Category. **Sort by:** Newest · Ending soon · Most back · Most cashback.
- **Enrollment status as the mediator reads it:**
  - Applied is never shown (a deal cannot be an apply-mode campaign).
  - Ready to join [your turn] · Submit tasks [your turn] · In review [their turn] · Fix tasks [your turn] · Paid [done] · Rejected · Cancelled · Expired.
  - Money override on an approved enrollment: Pay back [your turn] (owed) then "Awaiting confirmation" once marked.
  - List groups (same as everywhere): Ordered · Tasks sent · Fixes needed · Approved · Paid · Closed. Row tag when the mediator must act: "To do". Search "Enrollments".
- **Payback statuses** (`mediator-payback-model.ts`): Waiting for payout · To pay back · In progress · Disputed · Partly paid · Confirmed · Paid back · Unpaid.
  - Groups: To do (To pay back, Disputed, Partly paid) · Waiting (In progress, Waiting for payout) · Settled (Confirmed, Paid back, Unpaid).
  - Shopper's three answers: "Yes" · "Got less" · "Not yet". Settled stamp "Paid back"; line "Shopper confirmed payback, 21 Nov, 4:12 pm".
  - Home "To do" row states: "Payback due", "5d late" or "Overdue", "Due today", "Disputed" / "Got less", "Fix tasks", "Tasks due".
- **Policy refusals** (deal cannot be enrolled for a shopper):
  - "This is your own store. Order it for yourself instead."
  - "This campaign takes applications, so you can't enroll a shopper in it."
  - "Only some creators can join this campaign, so you can't enroll a shopper in it."
  - "{name} is already enrolled."
  - "Only {name} can do this one. Share it instead." (barter, check-in and content campaigns: the shopper does the steps).
- **Trust words:** TrustDrive stats "Paid back", "Rating", "Reviews", "Confirmed", "In progress", "Partly paid", "Disputed", "Complaints". Rating reads "None" below 5 reviews. Review row states "Needs reply" / "Replied". Trust tiers (creator/admin side): New · Low · Standard · Trusted · Elite.
- **Never write:** buyer, customer, downline, agent, reseller, commission, margin, cut, rebate, reimbursed / refunded / repaid, hub, listing (for a deal), place / seat / slot (use spot), "paid" for the payout (say "payout"), "Needs attention" / "Action required" (the tag is "To do"; the docs' "Needs you" is not what shipped), claim (except TrustDrive's "Claim listing"), "KYC" (say "Verify your PAN"), "order" for the mediator's own screens, emoji.
- **Style:** dates "20 Nov" in rows and "26 Nov 2026" in full; ₹ with Indian grouping; whole rupees on mediator figures (rounded down); "Morning, Kavya" greeting from the IST clock ("Welcome, Kavya" on first use); sentence case.

## Example data (agrees with the creator and brand specs)
- **Mediator: Kavya Nair**, Pune, Active, PAN verified (individual). Store "Kavya's store" at `orders.hypedrive.app/m/3VQJHP41` (code format from the docs; domain NOT CONFIRMED).
- **Shoppers** (a shopper is a creator-row person; a mediator may add one who has no account yet and who claims it later):
  - Asha Verma (has an account), Rohan Das, Meera Joshi, Sunita Pillai.
  - A new shell: Deepak (email only, "Waiting to join").
- **Deals in the store** (same campaigns as the other specs):
  - **Glow serum, 30 ml** · Nykaa · ₹1,899 · pot 60% + ₹200 · Shopper 55% back · You keep 5% + ₹50 bonus · "8 spots left" · closes 26 Nov 2026 (6 days, so no "Ends in" word).
  - Night cream, 50 g · Amazon · 50% cashback pot · Shopper 45% back · You keep 5%.
  - Daily cleanser trio · Nykaa · 55% + ₹100 · Shopper 50% + ₹60 back · You keep 5% + ₹40 bonus. Paused.
  - Not a deal: Clear skin set (barter and "By application", so the mediator cannot enroll for it: "This campaign takes applications, so it can't be a deal.").
  - Browse shows "60% cashback to split · ₹200 bonus to split" until it becomes a deal.
- **Today's enrollments:**
  - **Asha Verma on Glow serum:** enrolled 12 Nov, tasks sent, approved 20 Nov. The payout landed (₹1,339 in Kavya's wallet). Payback due ₹1,195 ("Payback due", "Mark paid"; "You keep ₹144").
  - Rohan Das on Night cream: "Fix tasks" (the brand asked for changes).
  - Meera Joshi on Daily cleanser trio: "Submit tasks" ("Due 28 Nov").
  - Sunita Pillai on Night cream: "Confirmed" (settled).
  - A fifth, "Got less": the shopper said it was ₹100 short.
- **Wallet:**
  - You can withdraw ₹3,240. To pay back ₹2,440 (2 enrollments). You keep in November ₹1,236.
  - Held ₹2,440. Incoming "Landing soon".
  - Payout account: UPI "kavya@okhdfc" or HDFC ••6093 (Needs a fix state: "Needs a fix").
- **Earnings:** "You keep in November": 9 placed. Month by month: Nov ₹1,236 · Oct ₹2,850 · Sep ₹1,490. By deal in November: Glow serum ₹720 · Night cream ₹330 · Daily cleanser trio ₹186.
- **TrustDrive:** Rating 4.8 · Reviews 31 · Paid back on 38 of 40 (95%) · Confirmed 36 · In progress 2 · Partly paid 1 · Disputed 1 · Complaints 0. To do: 2 reviews "Needs reply" and 1 "Takeover request, 2 days left".
- **Today:** Fri 20 Nov 2026.

## Screen set (mobile-first 390 px phone frames; one at a time, each shown to the owner before the next)
1. **Today (Home).**
   - Head: "Morning, Kavya" and the date line "Friday, 20 Nov". Money strip, three tiles: "You can withdraw" ₹3,240 · "To pay back" ₹2,440 · "You keep in November" ₹1,236 (each opens its page).
   - "To do" list (cards): Asha Verma · Glow serum · "Payback due ₹1,195" · "Mark paid"; Rohan Das · "Fix tasks"; Meera Joshi · "Tasks due · Due 28 Nov". "Mark all 2 paid" appears when two are owed. "View all N to do".
   - "Live deals" (up to 4) with "View all your deals". First-use variant: "Get your store ready" with the steps Application approved · Verify your PAN · Add your first deal · Share your store.
   - Dock with Today active and the centre "New" disc. Notice variant: "The mediator terms changed. Read them and accept the new version." with "Review terms".
2. **Deals, browse and the slice sheet.**
   - Head "Deals" with tabs Campaigns | My deals. Search plus filters (Show, Shop, Category, Sort by). Chips All · New · Saved · Ending soon with counts.
   - Campaign cards: photo, title, store mark, "₹1,899 · 60% cashback to split · ₹200 bonus to split", "8 spots left", "Add to store" button.
   - Then the sheet "Set what you keep" for Glow serum: two sliders, "Cashback you keep" ("Of the 60% to split, up to 49%", "You 5%, shopper 55%") and "Bonus you keep" ("Of the ₹200 bonus, none to all. What you leave goes to the shopper." "You ₹50, shopper ₹150"), "Drag to set your share". Overview: you get · shopper gets · you keep. Note "Shoppers never see what you keep." Save "Add to store" (edit mode "Save what you keep"). Server messages: "Keep 0% to 49% of the order price.", "Leave the shopper at least ₹1 of the bonus."
3. **My deals (store).**
   - Head "Deals", tab "My deals", store link card (link text, "Share", a switch for taking new enrollments with the note "Enrollments already made carry on. Switch on to take new ones."; locked state "Paused by Hypedrive for now").
   - Segments All · Live · Paused · Full; search appears from 10 deals.
   - Rows: photo, title, status word only when not plain Live (e.g. "8 spots left" in warning), "You keep 5% + ₹50 bonus", chevron. Empty: "No deals yet" / "Browse campaigns and add one to your store."
   - Deal page: stats "3 placed · ₹210", Pause / Pin / Remove, the share card.
4. **Enroll a shopper** (the New disc; a four-step sheet "Enroll a shopper", "Step 1 of 4").
   - Pick a shopper (search, "Add a new shopper", "Not enrolled yet") → "Pick a deal" ("Deals for Asha": offered deals, then refused ones with the reason lines) → "Buy it" (open the store link; spot held 10 minutes plus one 10-minute extension; "Asha's spot is no longer held." on expiry) → "Send the receipt" ("Your receipt must show": the purchase number · the product name and the price · the store and the purchase date; "Checking your receipt. This takes about 20 seconds. Keep this open.").
   - Result "This receipt matches" or "Check what we read", then "Asha is enrolled" with "Done" and "Open enrollment". Paused state: "Enrolling is paused".
   - The mediator is the one who buys. "Add a shopper" dialog fields: first name, mobile or email, consent tick "Tick this once they have agreed."
5. **Enrollments list and one enrollment with the payback.**
   - List: head "Enrollments", secondary "Enroll a shopper", chips All · Action required · In progress · Completed, group sections Ordered · Tasks sent · Fixes needed · Approved · Paid · Closed. Rows: shopper name, campaign, status word, "To do" tag. Empty: "No enrollments yet" / "Enroll a shopper in a deal and the enrollment shows up here."
   - Enrollment page (Asha, Glow serum): answer line "Pay back. Asha is owed ₹1,195."; offer block "55% back to Asha · ₹1,899 · You keep ₹144"; "Your shopper" card (contact: call, WhatsApp); journey; primary "Mark paid"; More: "Cancel enrollment" (dialog "Cancel this enrollment?" / "The shopper's spot is freed. This can't be undone.").
   - **Mark paid sheet:** "Mark Asha paid", "Amount sent to Asha" (₹1,195), "Payment reference (optional)", "Mark paid". After marking: "In progress" then "Awaiting confirmation".
   - **Settled ticket:** "Asha is paid back · Shopper confirmed payback, 21 Nov, 4:12 pm" with stamp "Paid back".
6. **Wallet (with earnings).**
   - Head "Wallet": balance block, "Withdraw". Tiles/list: "You can withdraw", "Held" ("Held money, see why": sheet "Held money" with a row per shopper) and "Incoming".
   - "How money gets here": 1 Enroll a shopper on a deal. 2 They buy it and submit tasks. 3 You approve it. The payout lands here. 4 Pay the shopper their payback. You keep the rest. (Step 3 is the source's own wording, though the brand approves; see Flags.)
   - "Withdrawals go to" (payout account row; "Needs a fix" state; "Add an account" needs a verified PAN, sheet "Payout accounts": "Add a bank account or UPI ID to withdraw."). Documents row. Activity (View all activity, ledger tabs All · Mediator · Creator, words "Said not paid yet", "Got less than owed").
   - Earnings page: "You keep in November" figure, "Month by month", "By deal in November". Empty: "Nothing earned yet" / "What you keep from each approved enrollment shows up here." Withdraw stops: "Nothing to withdraw yet", "Verify your PAN first".
7. **TrustDrive** (More sheet → TrustDrive; tabs Overview · Reviews · Requests · Listing).
   - Overview: "To do" ("Takeover request · 2 days left", review rows with stars, pseudonym, verified-enrollment mark, "Needs reply"); "How shoppers see you" (Paid back, Rating, Reviews, Confirmed, In progress, Partly paid, Disputed, Complaints).
   - Reviews: filter, rows, reply composer ("Thanks for your message. Here is how it works"). Listing: numbers ("Main number", "Shoppers can reveal it"), "Add number", claim flow ("Claim your listing", "Is this your listing?", "The listing is yours"), suggested edits.
   - Empty: "Nothing to do" / "New reviews and takeover requests show here."
8. **Apply and gates** (optional): "Become a mediator" ("Verify your PAN, agree to the terms and send your application."), "Your application is in review" (Hypedrive reads it · You hear by email · Verify your PAN, then start), "Not approved this time" with "Why", "Your mediator role has ended", "You're approved, Kavya" welcome sheet.

## Rules
- The mediator sees all three figures (you get, shopper gets, you keep). The shopper sees only the offer. Never draw "Shopper's offer" on a screen the shopper uses with the slice beside it.
- "Mark paid" appears only after the payout has landed, never before. The shopper's answer is theirs, not the mediator's.
- The mediator's own enrollments use "For myself": full cashback, no slice. The mediator cannot enroll in their own deal ("This is your own store").
- Phone first: one primary per screen, the dock always visible, sheets for every action, rows as cards, thumbs-reach buttons 44 tall. Figures never wrap.
- Barter, check-in and content campaigns can be deals but the shopper does the steps; the mediator can only share them.

## Flags (could not confirm or conflicts)
- **Nav drift:** `mediator-app/06-decisions.md` #4 says a three-tab dock (Home, Store, Shoppers); `apps/mediator/src/lib/nav.ts` ships Today, Enrollments, New, Deals, Wallet with TrustDrive and Shoppers in More. Code used.
- **"order" vs "enrollment":** `08-names.md` says "order" in the mediator app; the shipped screens say "enrollment" (`mediator-deals.md` §0: "Word: enrollment, not order"). Used enrollment.
- **Home wording:** the decisions doc plans one figure ("You keep this month") and "Needs you" rows; the shipped Home has three tiles and a "To do" list. Used shipped.
- The wallet copy "You approve it" (step 3 of "How money gets here") reads wrong, because the brand approves; kept verbatim as source, flag for the owner.
- Mediator withdraw minimum and fee, the store domain (`orders.hypedrive.app`), the "payment reference" length, and exact earnings numbers were not confirmed. Money rounds down to whole rupees per the doc, so a ₹94 slice (5% of ₹1,899) is used instead of ₹94.95.
- A shopper-side "Ask Hypedrive" link after 14 days of "Not yet" is blocked (decision 35): do not draw it.
- Shopper contact: shoppers see the mediator's account phone and email; there is no separate mediator contact field. A shopper's contact stays visible to the mediator until they remove the relationship; the 90-day erasure applies to unclaimed shells.
