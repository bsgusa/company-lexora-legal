# Attorney Brief — Lexora AI LLC legal-services boundary

**Prepared:** 2026-11-01
**For:** licensed counsel reviewing the Lexora AI website and service model
**Status:** internal working document, not legal advice
**Owner:** Shiv Goud, Lexora AI LLC

---

## 1. What we need from you

A short written opinion (one to two pages is enough) on four questions:

1. Does the current public copy cross the line into the **unauthorized practice of law (UPL)** in any state where we market, and if so which sentence?
2. Is the **document-preparation + attorney-referral** model defensible as software, or does it need a licensed-attorney sign-off on every output?
3. Is our **referral arrangement** structured so it does not violate fee-splitting or lawyer-advertising rules (we charge and receive nothing for the referral)?
4. Do the draft **Terms of Service**, **Privacy Policy**, and **Refund Policy** now live at `/legal/*` need changes before we accept a payment?

Anything you flag, we will change the copy or the flow rather than argue about it.

---

## 2. What the software actually does

There are two surfaces.

**A. Public website** (`index.html`, `immigration.html`, `auth.html`, `/legal/*`)

- Describes AI-assisted document review and drafting.
- Offers a free immigration intake form: name, email, phone, form type, current status, priority date, country of birth, country of citizenship, free-text description, and which documents the person says they have.
- The intake form does **not** ask for an A-number, Social Security number, passport number, or payment card.
- Submitting the form creates either a demo/contact request (anonymous visitor) or an intake record tied to an account (signed-in user).
- No payment is collected anywhere on the site today.

**B. Authenticated workspace** (`dashboard.html`)

- Magic-link sign-in (no passwords).
- Case records, document upload, and AI-assisted drafts, all behind row-level security.
- A person reviews every output before it is used. Nothing is filed automatically.

**What the AI does:** extracts fields, quotes source text, flags missing or inconsistent information, and drafts suggested language. It is a drafting and checking tool.

---

## 3. What the software never does

These are commitments we have made on the public site. Please tell us if any of them is insufficient to keep us outside the practice of law.

- It does not give legal advice or an opinion about a person's legal rights.
- It does not tell anyone whether to file, what to file, or whether they qualify.
- It does not predict approval or quote an approval rate.
- It does not represent anyone before USCIS, an immigration court, or any agency.
- It does not sign as attorney or agent, and does not create an attorney–client relationship.
- It does not accept or transmit government filing fees; the applicant pays the agency directly.
- It does not select the forms for a person's situation; the person tells us which form they need, or a human confirms it in a call.

---

## 4. Where a human attorney comes in

- If a user needs legal advice, strategy, a waiver argument, or representation, we **refer them to a licensed attorney**.
- The referral is separate: the attorney is engaged by the user, under the attorney's own engagement letter and fee agreement.
- **Lexora AI charges nothing for the referral and receives nothing from the attorney.** This is deliberate, to stay clear of fee-splitting rules. Please confirm that is the right structure, and whether any state requires a written disclosure of the referral.
- We do not currently have a named referral partner. Until we do, the copy says "a licensed attorney must be engaged separately" without naming anyone.

---

## 5. Current public copy — the sentences that matter

Quoted from the live pages so you can mark them up.

**`immigration.html`**
> "We prepare immigration paperwork. We are not a law firm and we do not give legal advice."

> "Initial intake is free. Our service fees depend on the forms involved and are agreed before any work begins. USCIS filing fees are separate and paid directly to USCIS. If you need legal advice, a licensed attorney must be engaged separately."

**`index.html` (hero, solutions, results, security)**
> "AI-assisted document review and drafting for legal and career paperwork. Grounded retrieval, structured risk analysis, and a recorded human approval on every outbound action."

> "We're Early. No Results to Show Yet." — the results section deliberately publishes no customer outcomes, no accuracy benchmark, and no certifications.

**`legal/terms.html`**
> "Lexora AI LLC is a software company. We are not a law firm, we are not attorneys, and using this site or our software does not create an attorney–client relationship."

---

## 6. Facts counsel will ask for

| Item | Answer |
|---|---|
| Legal entity | Lexora AI LLC (US limited liability company) |
| State of formation | **Needs confirmation** — the draft Terms assume Florida (see §7) |
| Ownership | Lexora AI LLC is part of the Balamonis Group; `AI-Job-Automation` is a Lexora AI LLC asset |
| Certifications held | None. No SOC 2, ISO 27001, HIPAA, or FedRAMP |
| Insurance | Not yet purchased — E&O and cyber quotes outstanding |
| Payment processing | None live. No Stripe account connected to this site |
| Data location | United States (Supabase, Vercel) |
| Marketing channels | Website, phone, WhatsApp, email |
| States marketed to | Nationwide (US), no geo-targeting |
| Minors | Service limited to 18+ |
| Languages | English only at present |

---

## 7. Open questions we already know about

These are flagged in the drafts themselves; we are not hiding them.

1. **Governing law / venue.** The Terms assume Florida (Pinellas County) because the business phone number is a Florida number. If the LLC is organized elsewhere, this needs to change.
2. **Liability cap.** Currently the greater of fees paid in the last 12 months or US$100. Counsel to confirm this is enforceable for a consumer-facing service.
3. **Refund policy and consumer law.** The policy gives a 14-day full refund on a first subscription payment. Confirm this satisfies FTC and state consumer-protection expectations, and whether a per-document engagement needs a longer window.
4. **"Human review" wording.** We say a person checks every field. Confirm whether that person must be a licensed attorney in any state, or whether a trained non-lawyer reviewer is enough for document preparation.
5. **Referral disclosure.** Whether any state requires a written disclosure that we are not a law firm and receive no referral fee.
6. **Testimonials.** We publish none yet. When we do, confirm consent and disclaimer language.
7. **Data processing.** Whether the current DPA is adequate for a customer who is itself a law firm with confidentiality obligations to its own clients.

---

## 8. What we are asking you to sign off

- [ ] The public copy does not constitute legal advice or hold out as a law firm
- [ ] The document-preparation + referral model is permissible as structured
- [ ] The referral arrangement does not violate fee-splitting or advertising rules
- [ ] The draft Terms, Privacy Policy, and Refund Policy are fit to publish before taking payment
- [ ] Any sentence you want changed — marked up and returned

Once signed off, we remove the "Draft — not yet reviewed by an attorney" banner from the `/legal/*` pages and record the date in `reports/LOG.md`.
