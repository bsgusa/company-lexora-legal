# Roadmap — AI-Job-Automation (Lexora AI LLC)

Document-preparation software with attorney referral. Honest public claims only
— no fabricated certifications, customers, funding, or models. The 90-day Lexora
focus (decided 2026-10-22): earn the legal right to charge, ship one product
honestly, win the first 3 paying customers, then prove repeatability.

Ownership: **Lexora AI LLC** (root ROADMAP.md, decided 2026-10-22).

## [NOW] — Earn the legal right to charge (Days 0–7)

- [x] Remove all fabricated claims from public site + wiki (SOC 2, ISO, HIPAA,
  FedRAMP, "500+ law firms", "2.4M+ documents", "98% satisfaction", a16z/Sequoia,
  LexLLM™, licensed immigration attorneys, 98% approval rate, 15K+ cases)
- [x] Reposition immigration page as document-preparation software + attorney
  referral; state plainly it is not a law firm and not affiliated with USCIS
- [x] `SECURITY.md` — each certification listed as "not held" / "not authorized"
- [x] `CHANGELOG.md` — correction notice added; retained as build record
- [ ] Attorney review of the immigration legal-services boundary (B-024 — attorney engaged)
- [x] Terms of service, privacy policy, refund policy drafted to match what the
  site actually does (B-026 launch kit) — live at `legal/terms.html`,
  `legal/privacy.html`, `legal/refund.html`, plus `legal/cookies.html`,
  `legal/dpa.html`, `legal/subprocessors.html`, `legal/security.html`. Every
  page carries a "draft — not yet reviewed by an attorney" banner, and CI fails
  if the banner is removed.
- [x] One-page attorney brief for the immigration boundary (B-027) —
  `docs/ATTORNEY_BRIEF.md`: what the software does, what it never does, where a
  human attorney is referred, seven open questions, sign-off checklist.
- [x] MSA draft for business customers (B-026) — `docs/legal/MSA-DRAFT.md`.
- [ ] Stripe live keys + Lexora business bank account (B-028) — not started; no
  payment is collected anywhere on the site and the pricing page says so.
- [x] Pricing page aligned exactly with refund policy (B-029) — pricing is now
  labelled "planned, not yet charging"; invented enterprise bullets (iManage /
  NetDocuments sync, SSO, 10K API calls, air-gapped deployment, 24/7 support,
  4-hour SLA) replaced with "✗ not built"; the public-sector tier states what
  we cannot do instead of pretending it is a tier. Billing bar links the
  Refund Policy and no longer promises "prorated refunds".
- [x] Footer no longer links Privacy/Terms/Cookie/DPA/Sub-processors to `#`;
  entity name corrected from "Lexora AI, Inc." to "Lexora AI LLC"; placeholder
  social links (LinkedIn/Twitter/GitHub with no accounts behind them) removed.
- [x] `scripts/check-claims.py` + CI step: fails the build on fabricated
  certification, customer, funding, or model claims. `npm run check:claims`.
- [ ] **Blocked on counsel:** remove the draft banners and record the date once
  the attorney signs off.

## [NEXT] — One product, honestly scoped (Days 8–30)

- [ ] Choose the chargeable unit: immigration document prep (per document)
  vs contract review (per review). Recommendation: document prep.
- [ ] Position as software + human referral — never "we are attorneys",
  never "guaranteed approval"
- [ ] Onboarding that works without you on the call
- [ ] PendingTracker dashboard wired to Supabase (auto-detect stale applications)
- [ ] AI integration: draft application documents, cover letters, and
  attorney-referral emails from the pending-items tracker

## [LATER] — First 3 customers + proof (Days 31–90)

- [ ] 10 conversations with people who actually have the problem
- [ ] 3 paid transactions, even at a discount
- [ ] Support inbox with a response-time promise you can keep
- [ ] Rehearse one refund, correctly, on purpose
- [ ] 3 written testimonials with permission
- [ ] Documented fulfilment: upload → delivered, step by step
- [ ] Unit economics: price, AI + payment cost per document, margin

## AI integration

- `lexora-ui/components/dashboard/PendingTracker.tsx` — AI-triaged pending-items
  dashboard with scoring, source labels, action icons, copy-to-clipboard drafts
- `.github/workflows/ci.yml` — secret scanning (rejects sbp_, ghp_, sk_ keys)
- AI drafts for client outreach, document prep, and attorney referral emails
- Truthful-claims CI check: rejects fabricated certifications, customers,
  funding, or models on every push

## Rules for this repo

- Work on a branch, never `main`. Small commits with clear messages.
- Before ending a session: update this roadmap, `backlog/priorities.md`, and
  append a dated entry to `reports/`.
- Never commit secrets. Env names in `.env.example`; values never in chat or git.
