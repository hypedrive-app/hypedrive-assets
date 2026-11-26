# Creator mockups: the real-logic spec (source: hypedrive repo, mapped 2026-11-25)

The creator mockups must follow this file. Every word, status and number comes from the real code; the research report has the file:line references. Layouts and visual style are OURS: Bricolage display, Geist UI, white canvas, tactile cobalt, the calm-controls rules in BRIEF.md. Do not copy the creator-v9 layouts.

## Vocabulary (exact)
- **Words to use:**
  - "campaign", never "drop"
  - "enrollment" (nav "Enrollments", mobile tab "Enrolled")
  - "spots", never "slots"
  - "tasks"
  - "cashback", "N% back", "+₹X bonus"
  - "Get ₹X back", "You get back", "It costs you"
- **Buttons and states:**
  - Verbs: "Join campaign", "Join and earn ₹X", "Apply to join", "Send application", "Submit N tasks", "Resubmit N tasks", "Withdraw", "Verify PAN".
  - Statuses: Applied · Ready to join · Submit tasks · In review · Fix tasks · Paid · Not approved · Cancelled · Expired.
- **Never write:** drop, deal (creator side), claim, slots, KYC (say "Verify your PAN"), "next payout".
- **Style:** dates like "26 Nov 2026"; ₹ with Indian grouping; sentence case.

## Example data (online purchase, the main kind)
- Creator Riya Sharma, @riya.glows, Kolkata. Instagram is the only connected social.
- **Campaign "Glow serum, 30 ml"** by Lumen Labs, bought on Nykaa. Join mode: open.
  - Price ₹1,899. **60% back** = You get back ₹1,139, plus a **+₹200 bonus**. It costs you ₹560.
  - The spots line shows only at 10 or fewer remaining: "8 spots left".
  - Closes 26 Nov 2026.
  - Tasks:
    - 1 Instagram reel: link + screenshots, #ad and "Paid partnership" label.
    - 1 Nykaa review: link + screenshot, at least 40 words.
  - Posting window: 45 days after joining ("You'll have 45 days to post after you join.").
- **Other campaigns:**
  - Night cream, 50 g · Lumen Labs · Amazon · 50% back.
  - Daily cleanser trio · Lumen Labs · Nykaa · 55% back + ₹100 bonus.
  - Clear skin set · **barter**: "Free product · Worth ₹2,400", +₹500 bonus.
- **Wallet:**
  - Available ₹6,820 · "₹1,339 on hold" · Earned so far ₹24,610.
  - Payout to HDFC ••6093.
  - Withdraw: minimum ₹100. Fee ₹0. "Usually within minutes".
- **Today:** Fri 20 Nov 2026.

## Screen set (one at a time, each shown to the owner before the next)
1. Sign in: Logto; the welcome screen.
2. Onboarding: "Your profile" (first name, last name, gender, DOB), then "Verify your PAN · optional".
3. Home:
   - greeting and the "Finish setup" card
   - "To do" (Your turn) and "In review"
   - wallet strip: Available / On hold / Pending approval
   - "Picked for you"
4. Campaigns (browse):
   - chips: All · Ending soon · New · Saved
   - filters: Platform · Store · Category
   - sort: Cashback high to low
   - cards show "60% back", "+₹200 bonus", the spots line, "Joined"
5. Campaign page:
   - store chip and "Closes 26 Nov 2026"
   - payout calculator: You pay / You get back / It costs you, with "After the brand approves"
   - "How it works"
   - "What you'll create" task cards
   - Do and Don't
   - a sticky "Join campaign"
6. Join, part 1 (buy):
   - brief: "Buy it on Nykaa · Send 2 tasks · Get ₹1,339 back"
   - spot hold: "Spot held for you · 9:41 left", "Add 10 min"
   - "Buy on Nykaa"
   - "You can leave before you buy."
7. Join, part 2 (receipt):
   - upload the receipt or invoice
   - "Checking your receipt — This takes about 20 seconds."
   - then "Join and earn ₹1,339"
8. Enrollments list:
   - groups: Ordered · Tasks sent · Fixes needed · Approved · Paid · Closed
   - a "Your turn" tag
9. Enrollment detail:
   - next step "Submit 2 tasks"
   - per task: "Link to your reel", 1–6 screenshots
   - "Submit 2 tasks"
   - attestation line
   - due "Due in 41 days"
   - money block: You paid / Cashback / Bonus / You get
10. Wallet:
    - hero "Available ₹6,820", "₹1,339 on hold", Withdraw
    - tabs Activity · Statements
    - movement rows: Cashback / Withdrawal / On hold
    - rail "Payout to HDFC ••6093"
11. Withdraw:
    - amount, then account, then review ("Fee ₹0.00", "You receive"), then "Confirm it's you", then Requested
12. Inbox:
    - "Your earnings have landed"
    - "Your enrollment needs a change"
    - "Glow serum is open"
    - "Withdrawal requested"
    - "Mark all read"
13. Settings: Personal info · Verification (PAN) · Payout methods · Addresses · Sign-in & security · Devices · Notifications · Appearance.
14. Barter enrollment:
    - shipment card: Ship to · Carrier · Tracking number · "Track shipment"
    - states: Waiting for product → On the way → Delivered
    - "Received" button
    - tasks locked: "Opens when your order arrives."
