# Brand mockups: the real-logic spec (source: hypedrive repo `apps/brand/src`, `packages/domain`, `packages/ui`, `packages/features`, mapped 2026-11-26)

The brand mockups must follow this file. Every word, status and number comes from the real code or the design docs under `docs/design/`. Layouts and visual style are OURS: Bricolage display, Geist UI, white canvas, tactile cobalt, the calm-controls rules in BRIEF.md. Do not copy brand-app-v3 or v6 layouts.

**Form factor:** the brand app is a responsive, multi-tenant web app: desktop-first (left rail from 768 px, phone tab bar under it). Mockups are desktop. Every URL lives under `/{orgId}`.

## The one rule that changes the numbers
A brand never sees what a creator receives (`docs/design/brand-creator-payout-visibility.md`). Brand screens show what the **brand pays**: its own proposal, its cost per enrollment, GST, its totals. Never show "creator gets", "creator cashback", "creator bonus", "platform fee", or any split from which the creator's amount can be derived. The creator spec's "You get back ₹1,139 + ₹200" must NOT appear on a brand screen as what the creator receives.

## Vocabulary (exact)
- **Words to use:**
  - "campaign", "creators" (the count unit: "112 of 120 creators"), "joined", "enrollment" (nav "Enrollments"; phone dock "Enrolled"), "tasks", "product" (nav "Products"), "workspace" (the brand's account: "Choose a workspace", "Name your workspace"), "wallet", "Add money", "On hold", "Your cost", "Reward", "Bonus per creator".
  - "Hypedrive" reviews and prices every campaign: "Hypedrive reviews every campaign before it goes live" and "Hypedrive sets the final price when it approves."
  - Reward in the composer: "You pay 60% of the order" and "Bonus per creator". The brand proposes; Hypedrive prices at approval. After approval the campaign shows "Your cost".
- **Nav (left rail, in this order):** Home · Inbox | Work: Campaigns · Enrollments · Products · Disputes (always shows its count, 0 included) | Finance: Wallet (shows the balance as a trail) · Invoices | Workspace: Team · Settings. Top bar: Search, Help. Phone tabs: Home · Campaigns · Enrolled · Wallet. (`apps/brand/src/lib/nav.ts`)
- **Buttons (verbs):**
  - Page heads: "Create campaign" (phone "New"), "Add money", "Withdraw", "Invite members", "Add product", "Export CSV", "Open wallet", "All campaigns".
  - Queue: "Review 9" (head primary, plays the queue), "Select", "Approve 3", "Reject".
  - Review: "Approve & pay ₹1,580", "Send back 1 task" / "Send back 2 tasks", "Send back", "Reject", "Looks good", "Needs a change", "Add ₹X to approve" (wallet short), "Next: Riya Sharma", "Undo".
  - Applications: "Accept" (dialog "Accept this application?"), "Decline" (dialog "Decline this application?", "Decline application").
  - Barter: "Mark shipped", "Delivered", "Re-ship", "Mark returned", "Couldn't ship".
  - Campaign: "Submit for review", "Resubmit", "Edit & fix", "Pause", "Resume", "Resume anyway", "End", "Archive", "Unarchive", "Discard", "Edit campaign", "Share campaign", "Add places", "Extend the end date", "Top up wallet", "Start over", "Discard draft", "Send for review", "View campaign".
  - Composer: "Continue", "Use this product", "Review", "Back", "Edit", "Add task", "Clear all".
  - Team: "Invite members", "Send invite" / "Send 3 invites", "Resend", "Invite again", "Cancel invite", "Copy invite link", "New link", "Turn off link", "Create link".
  - Money: "Send certificate", "Download", "Bank transfer details", "Hide amounts" / "Show amounts".
- **Campaign statuses** (`packages/domain/src/status/campaign-status.ts`; tone in brackets): Draft [neutral] · In review [info] · Changes requested [warning] (the card and row say "Sent back") · Rejected [danger] · Scheduled [info] · Live [success] · Paused [warning] · Ended [neutral] · Archived [neutral] · Discarded [neutral].
  - Row overrides: a live campaign with work waiting shows "9 to review" [warning]; "Full" when joined >= max; "Ends in 3 days" [warning] in the last 7 days (dashboard); paused for low funds shows "Paused" plus the banner "Paused: wallet balance too low".
- **Campaign list tabs:** All · Active (scheduled, live, paused) · Action required (sent back, rejected) · Draft and in review · Ended (ended, archived). Sort label "Recent" (default), more from the server list. Search "Search campaigns". Board groups (grouped view): To do · Live · Not live · Past campaigns. Columns: Creators · Spent.
- **Campaign availability, as the brand sees it:** "Open to all" (join mode open) or "By application" (join mode apply); a switch "Visible in creator app" (off: "Only creators with the link can join."); live campaigns take creators until the end date or until full. The server's availability states (upcoming, open, ending_soon within 3 India days, full, paused, closed) feed the creator side; the brand reads the status words above instead.
- **Enrollment statuses as the brand sees them** (`packages/domain/src/enrollment/enrollment-vocabulary.json`; whose turn in brackets):
  - Applied [your turn] · Accepted [their turn] · With creator [their turn] · Needs review [your turn] · Waiting on fixes [their turn] · Paid [done] · Rejected [bad end] · Cancelled · Expired.
  - Barter overrides: Ship product [your turn] · Shipped [their turn] · Resolve return [your turn] · Not delivered [closed]. Money: Approved [done] when payout is in flight · Payout failed [your turn].
  - List groups, in this order, the same for everyone: **Ordered · Tasks sent · Fixes needed · Approved · Paid · Closed**. An application is listed under Ordered. Whoever must act gets the tag "Your turn" on the row, never a group of their own.
  - Filter chips over the list: All · Action required · In progress · Completed. List columns: "Waiting for", "On approval" (the amount), Actions. Search "Search enrollments".
  - Task words: To do · Sent · Fix needed · Locked. Verdicts per task: "Looks good" · "Needs a change".
- **Reject reasons (category picker, then free text 10 to 1000 characters):**
  - Proof is unclear · Order amount does not match · Wrong product · Order date is wrong · Task not done as asked · Order could not be verified · Something else.
  - Chip short forms: Proof unclear · Amount doesn't match · Wrong product · Wrong order date · Task not done · Fraud suspected · Other.
  - Error: "Pick what went wrong." / "Tell the creator what was wrong, in at least 10 characters." Dialog: "Reject this enrollment?" body "The creator isn't paid and the escrow returns to your wallet." consequence "They can raise a dispute until {date}."
- **Send-back reason chips** (add a sentence to the note, per task): Screenshot unclear · Not about the product · Under 40 words · Hashtags missing · Tag missing · Product not tagged · No partnership label · Link doesn't open. Note label "Your note to Riya". Rule: "Add a note on at least one task first." Consequence: "The creator gets until {date} to fix these."
- **Never write:** drop, deal (that is the mediator word), slots / seats / places (the code leaks all three, e.g. "Add places"; use "creators"), claim, KYC (the brand verifies GST), "creator receives", "platform fee", "creator cashback", round numbers or "Round 2" (v14 removed round words), "Action required" as a status (it is a tab and chip only), emoji, exclamation marks.
- **Style:** dates "26 Nov 2026" in full, "26 Nov" in rows; ranges "20 Nov to 26 Nov" or "1–30 Nov"; ₹ with Indian grouping and "₹1,58,500" in figures; times IST; sentence case; "Good morning, Neha" greeting from the IST clock.

## Example data (agrees with the creator spec)
- **Workspace:** Lumen Labs (skincare, Bengaluru). GSTIN verified, legal name "Lumen Labs Private Limited". Signed in as **Neha Kapoor**, Owner.
- **Team:**
  - Neha Kapoor, Owner, "Active now".
  - Arjun Mehta, Campaign manager, "Active today".
  - Divya Rao, Finance manager, "Active yesterday".
  - Sanjay Iyer, Viewer, "Active 3 days ago".
  - One pending invite: aman@lumenlabs.in, Campaign manager, "Sent on WhatsApp", expires in 7 days.
- **Hero campaign "Glow serum, 30 ml":**
  - Product: Glow serum, 30 ml, listed ₹1,899 on Nykaa. Type: Online purchase. Enrollment type: Open to all. Status Live.
  - Brand proposal and cost: **60% of the order** + **₹200 bonus per enrollment** + **18% GST**.
  - One approval costs about ₹1,339 + ₹241 GST = **₹1,580**. This is the creator spec's 60% (₹1,139) + ₹200, shown here only as the brand's cost.
  - Creators **112 of 120**. Closes **26 Nov 2026** ("Ends 26 Nov"). Action required **9**.
  - Spent ₹1,16,920 (74 approved × ₹1,580). On hold ₹60,040 (38 in flight × ₹1,580).
  - Tasks: Order receipt (always required) · 1 Instagram reel (link and screenshots, #ad, "Paid partnership" label) · 1 Nykaa review (link and screenshot, at least 40 words). Posting window 45 days after joining.
  - Brief title "Try the Glow serum". Do: "Show the texture on skin". Don't: "No before and after claims".
- **Other campaigns:**
  - Night cream, 50 g: Live, Amazon, 50% of the order, 80 creators.
  - Daily cleanser trio: Live, Nykaa, 55% of the order + ₹100 bonus.
  - Clear skin set: Live, barter ("We ship it to them"), +₹500 bonus per creator, By application, worth ₹2,400.
  - Sunscreen SPF 50, 50 ml: In review (sent 19 Nov).
  - Hair oil, 100 ml: Sent back (Changes requested).
  - Vitamin C drops, 15 ml: Draft.
  - Lip balm duo: Ended 31 Oct.
- **Creators:** Riya Sharma @riya.glows (Kolkata, Instagram) joined Glow serum; sent 2 tasks on 18 Nov; "Needs review", "Waiting 2 days", trust word "Trusted". Others: Meera Joshi, Kabir Singh, Ananya Das, Tanvi Shah (applicants on Clear skin set).
- **Dashboard "For you today":**
  - Review submissions 9 ("Oldest waited 2 days", "Approve or send back each one").
  - Review applications 4 ("For 1 campaign", "Accept or reject each one").
  - Ship products 3 ("Oldest waited 1 day", "Creators' days to post start on delivery").
  - Reply to disputes 1 ("Reply by 24 Nov").
  - Head sentence: "4 things need you today."
  - Wallet: Available ₹1,84,500 · On hold ₹96,320.
  - Last 30 days: Creators approved 61 · Reviews published 52 · Average per creator ₹1,580.
- **Invoices:**
  - Weekly GST tax invoice, one per week. Example: week "9 Nov to 15 Nov", 31 enrollments, total ₹1,41,120.00, GST (18%) ₹21,527, status Paid.
  - FY section "FY 2026-27". Tiles: Invoiced · GST (18%) · Credit notes.
  - Invoice number format NOT CONFIRMED: use a monospace placeholder like "LL/2627/0042".
- **Today:** Fri 20 Nov 2026.

## Funding model (what the wallet does)
Source: `docs/design/brand-funding-2026-11.md`, `apps/brand/src/pages/wallet`, `packages/domain/src/wallet`. The funding screens (wallet, add money) are built; the "approve now, pay when funds arrive" model is designed and only Tier 1 is live. `apps/brand/src/routes/_authed/$orgId/funding-preview.tsx` is an untracked preview of it, so do not draw it as shipped.
- **Prepaid wallet.** The brand adds money to its Hypedrive wallet. The ledger keeps real money only: top-up, hold, settle, withdraw, refund.
- **Hold (escrow of money that exists).** When a creator joins, the cost of that enrollment is put on hold ("On hold" tile, held since join). Nothing moves to the creator yet.
- **Approve pays.** "Approve & pay ₹1,580" settles the hold: the creator is paid, Hypedrive's share and GST are split off, and the brand's activity shows "Enrollment paid". Approval is refused while the wallet cannot cover it. The primary becomes "Add ₹X to approve" or "Add money to approve", with the line "Your wallet can't cover this. Ask an owner or admin to add money." for roles that cannot fund.
- **Reject, expire or a failed shipment:** the held money returns to the wallet ("Hold released", "Returned to wallet +₹X").
- **Postpaid (credit) brands:** only for vetted brands, the limit set by an admin by hand. The wallet then shows three more tiles: Credit limit · Used · Left. Lumen Labs is prepaid, so draw no credit tiles.
- **Below zero:** "Every payment is blocked until an owner or admin adds money." Campaigns auto-pause: "Paused: wallet balance too low", "Your wallet couldn't cover a creator's commitment. Top up before resuming, or it pauses again on the next enrollment." The composer refuses a new campaign: "Your wallet is below zero" / "Clear your wallet first".
- **GST:** 18%, added to the brand's cost ("+ 18% GST"). Invoice totals include it (GST = 18/118 of the total). "Input tax credit available: ₹X." with a GSTIN, else "Add your GSTIN in Settings to claim input tax credit on this invoice."
- **TDS (quarterly):**
  - Invoices tab 2, "TDS certificates". Tiles: TDS deducted · TDS credited. Rows per quarter: Q1 Apr–Jun, Q2 Jul–Sep, Q3 Oct–Dec, Q4 Jan–Mar. Quarter words: Open · Overdue · In review · Rejected · "Credited 12 Nov".
  - Notice: "TDS certificate for Q3 (Oct–Dec) is due by {date}. Send it to have the TDS deposited credited to your wallet."
  - "Send certificate" sheet fields: TAN (format "MUMH03189E"), certificate number (TRACES), PDF, Tax deducted, Tax deposited.
  - The direction is INFERRED from copy: the brand deducts TDS on its payments and gets the deposited amount credited back. Not confirmed in backend code.
- **Add money** (sheet, steps Amount → Review → result):
  - Methods: "Bank transfer" (virtual account: Name, Account, IFSC, Amount, "Virtual account", copy and download) or "UPI or card" (via Razorpay).
  - Helper "Between ₹X and ₹Y". The limits come from the server and are NOT CONFIRMED.
  - Review lines: Amount · Via Razorpay · You pay. Results: Added · Payment failed · Request expired · Requested.
  - Empty state "Bank details are being set up". Wallet menu item "Bank transfer details".
- **Withdraw** (sheet): Amount and account → Review → "Confirm it's you" (step-up: secure sign-in, authenticator code, you return with the withdrawal still set up) → "Requested".
  - Review lines: Amount · Bank account · Estimated arrival ("Usually within minutes" or "After review, usually within a few hours") · Balance after withdrawal. Notices "Verified" / "Not verified".
  - Rules: "No fee."; bank account must be "in your company's legal name"; limits "Min ₹X, max ₹Y per transaction" (numbers NOT CONFIRMED). Empty: "Add a bank account to withdraw".
- **Wallet activity row words:** Money added · Enrollment paid · On hold · Hold released · Withdrawal · Refund · Compensation · Adjustment. Counterparty meta: "Razorpay", "HDFC Bank ••6093", or a creator name. Tabs Activity · Statements; "No activity yet" empty; statements per financial year ("FY 2026-27 statement", "Every month, one file", "Available on {date}", "Getting it ready").

## Team roles (`apps/brand/src/lib/permissions/definitions.ts`, `features/team/role-copy.ts`)
| Role | One-line description (exact) |
|---|---|
| Owner | "Everything, and the only one who can hand the brand on." |
| Admin | "Everything: campaigns, money, people and settings." |
| Campaign manager | "Runs campaigns and listings, reviews work, answers disputes. Sees the wallet." |
| Finance manager | "Runs the wallet, withdrawals, invoices and bank accounts. Sees campaigns." |
| Viewer | "Sees everything, changes nothing." |
- Owner is never offered in an invite ("Ownership moves only by transfer"); Transfer ownership is its own dialog.
- Campaign manager never adds money. Finance manager adds money, withdraws, files TAN and TDS. Only an owner or admin manages people and settings.
- Hidden, not disabled: Add money for roles that cannot fund; Team for roles that cannot manage members; Invoices without invoice read. A role that cannot review sees "Reviewing needs the review permission."

## Screen set (desktop 1440 wide, one at a time, each shown to the owner before the next; real order of the nav)
1. **Home (dashboard).**
   - Head "Good morning, Neha", the sentence "4 things need you today.", primary "Create campaign".
   - Chips under the head: Review 9 · Reply 1 · Ship 3 · Resolve 0 (zero stays quiet).
   - Main column "For you today" (the four rows above, each with its verb button) then "Last 30 days".
   - Side column: "View wallet" card (Available balance, On hold, "Open wallet", "Add money") and "Live campaigns" rows ("112/120 joined", "Ends in 3 days" on the one that is close) with "All campaigns".
   - First-run variant: "Welcome, Neha" with the steps to add money and create the first campaign. Empty: "Nothing needs you today".
2. **Campaigns list.**
   - Head "Campaigns", primary "Create campaign", overflow Export CSV. Tabs All · Active · Action required · Draft and in review · Ended with counts.
   - Search plus sort. Rows: photo, title, status word, dates, store mark, "112 of 120 creators", Spent.
   - Show: Live with "9 to review", Live, Sent back, In review, Draft, Ended. Select mode for bulk Pause, Resume, Archive.
3. **Campaign detail** (Glow serum).
   - Head: title, status Live, "Ends 26 Nov", primary "Review 9", overflow Pause · Add places · Extend the end date · Edit campaign · Share campaign · Copy campaign ID.
   - Stats strip: Creators 112 of 120 · Action required 9 · Spent · On hold.
   - Groups, in this order: Brief (Do, Don't), Tasks, Details (Product, Campaign type, Enrollment type, Posting period, Start date, Ends, Visible in creator app, share link), Reward and spend (Your cost "60% of each order" + "₹200 bonus per enrollment" + "18% GST", "Listed at ₹1,899 on Nykaa", spend lines Order funding · Bonus funding · Total spent, Export CSV), Variants if any.
   - Tab strip: Enrollments (rows of this campaign; the "check-in" tab only for check-in campaigns).
   - Also draw the banners as small states: "Hypedrive is reviewing this campaign" (In review), "Changes requested" with admin notes, bullet action items, "Edit & fix" and "Resubmit", and "Paused: wallet balance too low" with "Top up wallet" and "Resume anyway".
4. **New campaign composer, 3 steps** (focus mode: top bar with close "Leave the composer", title "New campaign", step track Product · Set up · Review with icons, "Draft saved", "1 of 3", More: Start over, Discard draft; the summary card beside Set up and Review from 1024 px).
   - **Product:** "Which product is this campaign for?" / "Pick one of yours, or paste a marketplace link to add a new one." Pick "Vitamin C drops, 15 ml" (Nykaa, ₹1,299). Footer line "Choosing a product takes you straight to the set-up." Add-by-link states: "Reading the page…", "We couldn't read that page", "Add it by hand".
   - **Set up** ("Set up the campaign", note "Filled in from your last Nykaa campaign. Change anything."). Cards in order:
     - Reward: Campaign type segmented Online purchase / Barter / Store check-in / Content post, with the line "They buy it with their own money. You fund cashback on what they spent."; "You pay 50 % of the order ≈ ₹650" with chips 100% · 75% · 50%; "Your proposal. Hypedrive sets the final price when it approves."; "Bonus per creator (optional) ₹100".
     - Creators ("You can add more later"): stepper 60 and chips 10 · 25 · 50 · 100.
     - Dates: Starts (chips Today · Tomorrow · Next Monday), Runs for (2 weeks · 30 days · 60 days · Custom), aside "23 Nov to 22 Dec · 30 days".
     - Tasks ("Creators do them in this order"): Order receipt locked ("Order ID, product, value and date · Always required"), Instagram reel, Nykaa review, "Add task".
     - What creators read: Title, Do, Don't, Reference photos, Links.
   - **Review** ("Review and send", "Hypedrive reviews every campaign before it goes live. You can still edit it until then."): one card of lines (Reward · Creators · Dates · Tasks · Brief), each with "Edit"; flags "Filled in for you, check it"; the line "The campaign type can't be changed once Hypedrive approves the campaign."; card "How creators see it"; primary "Send for review".
   - **Sent** ("Sent for review"): "We review “Vitamin C drops, 15 ml”, usually within 1 day." Three numbered steps: We check it. · It goes live. · You approve the work. Buttons "Create campaign", "View campaign".
5. **Review queue and one submission review.**
   - 5a Enrollments list: head "Enrollments", count, primary "Review 9", overflow Select, Export CSV. Chips All · Action required · In progress · Completed. Group tabs Ordered · Tasks sent · Fixes needed · Approved · Paid · Closed. Rows: creator, campaign, status word, "Your turn" tag, "Waiting 2 days", "On approval ₹1,580". Selection mode bar: "₹14,220 on approval", "Reject", "Approve 9" (up to 50 at once).
   - 5b Review (focus mode, no rail): queue bar with close, "Needs review", "1 of 9", Back and Next. Head: avatar, "Riya Sharma", "Needs review · Waiting 2 days · Trusted", Details.
     - Panes: tasks and order (Order block: product, Nykaa, ₹1,899, "✓ Matches", order id, Receipt) · proof stage with files and "Full size" · check panel with "Looks good" / "Needs a change" per task and the note box "Your note to Riya".
     - Decision band: money sentence, "Next: Meera Joshi", More, Reject, Send back, primary "Approve & pay ₹1,580" (becomes "Send back 1 task" once a task is flagged, "Add ₹X to approve" when the wallet is short).
     - Pay confirm: "Approve and pay?" with task lines, GST and total, "This releases the payment to the creator. It can't be undone.", then an Undo toast "Approved Riya" (8 s).
     - Reject dialog: category chips then reason. End of queue: "You're all caught up", "New submissions show here as they arrive."
   - 5c Application row: "Accept or decline Tanvi Shah's application. Decide by 22 Nov." with "Accept" and "Decline"; an estimate card "Payment · Estimate": Listed price · Reward · GST.
6. **Wallet and funding (with invoices).**
   - Wallet: head "Wallet", primary "Add money", secondary "Withdraw", overflow Bank transfer details · Hide amounts. Tiles Available balance ₹1,84,500 · On hold ₹96,320. Tabs Activity · Statements. Activity rows per the words above.
   - Sheets to draw: Add money (Bank transfer vs UPI or card, then Review) and Withdraw (amount, review, "Confirm it's you", "Requested").
   - Invoices: tiles Invoiced · GST (18%) · Credit notes; weekly invoice rows under "FY 2026-27" with Paid status, GST (18%), Total, Download; tab TDS certificates (the quarter rows and the notice).
7. **Team and settings.**
   - Team: head "Team", primary "Invite members"; tabs Members · Invites; rows with avatar, name, contact, role, "Active today"; role menu with the descriptions above; invite dialog (Email or mobile / Invite link / Add directly, "Invites expire after 7 days.", role picker, "Send invite"). Invite link row "Anyone with it joins as the role you pick."
   - Settings (two groups): Workspace: Workspace · Tax (GSTIN, TAN) · Bank account · Notifications | You: Profile · Security.
8. **Inbox and disputes** (optional, only if time allows).
   - Inbox: page "Inbox" with the notification list. Tab names NOT CONFIRMED for the brand. The Inbox/To do/Money tab decision in memory is for another app.
   - Disputes: head "Disputes", tabs All · Open · Decided · Withdrawn, rows with the decision and "Disputed amount". Dispute reasons for brands are the enrollment ones (see vocabulary JSON: "Hypedrive reviews both sides before deciding.").
   - Dispute states: "Waiting for the creator" · "To dor response" (typo in source, see Flags) · "With Hypedrive" · "Hypedrive asks" · "In review" · "Settling the payout" · "Decided" · "Withdrawn".

## Rules
- Brand sees its own cost only. Money lines on a brand screen are: Reward / Order funding / Bonus funding / GST / Total / Your cost. Never the creator's net.
- Two decisions per submission, no more: Approve & pay, or Send back with a note. Reject is a separate danger outline, disabled until the review has been looked at and its reason is typed.
- The review order is fixed by the server (`available_actions`): the same verbs and the same words everywhere. Do not invent verbs ("Approve" alone appears only on the phone dock).
- Desktop mockups only. One screen at a time; light first, then dark.
- Buttons stay flat cobalt with a quiet press edge; the ink button is the one primary per view; danger is an outline.

## Flags (could not confirm or conflicts)
- The brand's 60% "of the order" and the creator's "60% back" are drawn as the same number for continuity. In the real system the brand's funding rate and the creator's public cashback can differ by the platform fee (`brand-creator-payout-visibility.md` decision 2, owner call open). The ₹1,580 per approval is therefore illustrative. The real `brand_total` and `brand_gst` come from the server.
- Whether the hold equals the full ₹1,580 (gross plus GST) is not confirmed. The v14 doc says "the escrow is taken at join" and "held since" is the join date.
- Words "slots", "places", "seats" and "creators" are all in brand code (`campaign-action-dialogs.tsx`: "Add enrollment slots", "Creator slots"; `campaign-head.tsx`: "Add places"; `campaign-photo-card.tsx`: "38 of 50 seats"). Board and detail use "creators". Mockups use "creators".
- The dispute vocabulary JSON contains the typo "To dor response" (`enrollment-vocabulary.json`, `dispute_responder.open`). Mockups should write "To respond" and the typo should be fixed in source.
- Add-money and withdraw limits, invoice number format, brand Inbox tab names, and the brand creator-preview numbers inside "How creators see it" were not confirmed.
- The Review focus-mode layout (v14 plan, `docs/design-system/brand-enrollment-v14-plan.md`) is in code (`packages/features/src/enrollment-review/*`), but that plan lists "Undo after a full refresh" as not possible.
- TDS direction (see above) is inferred from copy only.
