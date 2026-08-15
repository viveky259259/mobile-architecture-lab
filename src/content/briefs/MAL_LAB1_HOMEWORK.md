# MAL Lab 1 Homework

Two-week implementation plan for attendees after Lab 1: Flutter & Foundations.

Start: July 12, 2026  
Due: July 25, 2026, before Lab 2  

## Who This Is For

This homework is for MAL Lab 1 attendees who want to continue building the same product arc through all five labs. You do not need to use Flutter. Pick a stack that helps you make architecture decisions visible.

## What To Share

Share one project repository or zipped project folder containing:

- The app or system project.
- A `README.md` with setup, run, and demo instructions.
- The documentation files listed in this homework.
- `docs/success-metrics.md` with project-specific success metrics.
- A short note on the language, framework, and local storage approach used.
- A three-minute demo script or screen recording link if requested by the organizers.
- A `.gitignore` or equivalent cleanup so generated build outputs, dependency folders, local secrets, and machine-specific files stay out of the shared project.

The project does not need to be deployed publicly. It should run locally or on the target platform from the shared instructions.

## GitHub Project Hygiene

If you share a GitHub repository, make it understandable from the repository home page. Organizers should be able to understand the product, run the project, and find the evidence documents without needing private context.

Your `README.md` should include:

- Project name and one-sentence product summary.
- Platform, language, framework, and local storage choice.
- Setup command.
- Run command.
- Test command, if available.
- Three-minute demo script.
- Known gaps or unfinished work.
- Links to the required docs in `docs/`.

Keep these out of the shared project:

- API keys, tokens, or secrets.
- `node_modules`, build folders, simulator artifacts, or generated dependency caches.
- Large model files unless they are essential, license-safe, and clearly documented.
- Real personal data, exact addresses, or personal contact details.

## Before You Start

Choose your platform and stack on Day 1. Keep the choice boring and practical. This homework is about the product and architecture slice, not proving a new framework.

Recommended prerequisites:

- A working development setup for your chosen stack.
- Git or another way to package and share your project.
- A simulator, emulator, browser, device, or desktop runtime where you can demo the app.
- Use seed data, mock data, or your own test entries only.

You may use AI coding tools, templates, starter kits, and open-source libraries. Be prepared to explain the architecture, accessibility, security, and local AI decisions in your own project.

## Goal

Build the first usable slice of the MAL series product: a hyperlocal marketplace app/system that works locally first and includes explicit product, accessibility, security, and local AI decisions.

By the end of this homework, each attendee should have a small working app that can run on web, Android, iOS, desktop, or another chosen platform. Any language or framework is welcome if the implementation is demoable and the architecture decisions are clear.

The app should be able to:

- Show hyperlocal listings for one neighborhood.
- Let a user create a listing or request.
- Persist data locally on the device, browser, or local runtime.
- Run one local AI-assisted flow, with a clean deterministic fallback if a local model is not available.
- Meet a basic accessibility checklist.
- Include a security baseline and one architecture decision record.

## Platform Policy

Attendees may build with any stack, for example:

- Flutter, React Native, Swift, Kotlin, or native mobile.
- Web with HTML/CSS/JavaScript, React, Vue, Svelte, Angular, or another frontend stack.
- Desktop or local-first app frameworks.
- Any language, as long as the app can be run and demoed by the attendee.

The homework evaluates architecture, product judgment, accessibility, security, local persistence, and local AI boundaries. It does not evaluate a specific framework.

## Product Brief

Working title: MAL Local

Problem: People in a neighborhood need a lightweight way to discover, request, lend, sell, or share nearby goods and services without depending on a heavy marketplace experience.

Primary user: A resident of a Mumbai neighborhood who wants to find or post something nearby.

Initial product slice: A local-first listing board for one neighborhood.

Payments, delivery, chat, moderation dashboards, real KYC, and backend infrastructure are intentionally out of scope for this homework. Those are later architecture decisions.

## Project Success Metrics

Each project should define its own success metrics in `docs/success-metrics.md`. These metrics should be small enough to evaluate during a demo or review, but concrete enough to guide product and architecture decisions.

Use this structure:

| Metric Area | Required Metric | Example Target | How To Measure |
| --- | --- | --- | --- |
| Product usefulness | Main user workflow completion | User can create and find a neighborhood listing in under 3 minutes | Run the demo script from a fresh app state |
| Activation | First useful action | User can create their first listing/request without help | Manual demo or usability check |
| Local-first behavior | Offline/local persistence | Listing remains available after refresh, restart, or app relaunch | Create listing, close app/browser, reopen |
| Accessibility | Core flow accessibility | Listing feed and create form are usable with screen reader or platform accessibility tooling | Manual accessibility pass documented in `docs/accessibility-check.md` |
| Security/privacy | Data minimization | Avoids exact address, precise live location, secrets, and hosted AI API keys | Review local data model and repo |
| Local AI | Helpful AI action with fallback | AI helper produces editable output and fallback works without network access | Disable network or model path, run the same flow |
| Architecture | Clear boundaries | UI, storage, product logic, and AI are separated enough to replace later | Explain using ADR and code structure |
| Reliability | Main flow stability | No crash during feed, create, persist, reopen, and detail view flow | Run demo script twice |

Add one project-specific metric based on your own product angle. Examples:

- For a lending-focused app: "User can mark an item as borrowed or returned."
- For a food-sharing app: "User can see pickup time and expiry status."
- For a services app: "User can filter by service category and availability."
- For a safety-focused app: "Risky listing text is flagged before save."

Avoid vanity metrics for this homework. Metrics like downloads, signups, revenue, or daily active users only make sense when the app has a deployed distribution path and real users.

## Help And Scope Rules

If you get stuck, reduce scope before adding more infrastructure. A complete local listing loop with clear docs is better than a large unfinished app.

Allowed:

- Mock data and seed listings.
- Local browser storage, local files, SQLite, Hive, Core Data, Room, IndexedDB, or any equivalent local store.
- Simple deterministic AI fallback instead of a real model.
- Minimal UI, as long as it is usable and accessible.

Keep these out of the homework scope:

- Hosted AI APIs for the expected AI flow.
- Production secrets or API keys in the repo.
- Exact home addresses or precise live location.
- Backend-dependent core workflow.
- Payment, delivery, or real identity verification.

## Required Implementation

### 1. Product

Implement the smallest useful marketplace loop:

- User can select or see their current neighborhood.
- User can view a list of nearby listings or requests.
- User can create a listing with title, category, description, approximate area, and contact preference.
- User can open listing details.
- User can mark a listing as saved, contacted, or closed.
- Apply relevant learnings from MAL Lab 1 and add one small product feature you personally want to solve.

Add a short product note at `docs/product-slice.md` covering:

- Target user.
- Problem being solved.
- The one workflow implemented.
- What was deliberately left out.
- Link to or summary of `docs/success-metrics.md`.

### 2. Accessibility

Implement accessibility in the actual app, not just as a checklist:

- All tappable controls have clear labels.
- Listing cards are readable by screen readers in a useful order.
- Forms show visible error messages, not only color changes.
- Tap targets are at least 48 x 48 CSS/logical pixels, or the platform-recommended minimum.
- Text remains usable with larger system font settings.
- App works in both light and dark mode, or has a documented reason if only one theme exists.
- Apply relevant learnings from the MAL Lab 1 accessibility session.

Add `docs/accessibility-check.md` with:

- Screens checked.
- Issues found.
- Fixes made.
- Remaining known limitations.

### 3. Security

Implement a basic privacy and security baseline:

- Keep secrets out of the shared project.
- Use manual neighborhood selection or coarse mock location instead of precise location.
- Avoid storing exact home addresses.
- Validate listing input before saving.
- Keep local data storage behind a repository or data source interface.
- Add a simple data deletion/reset option for local app data.
- Apply relevant learnings from the MAL Lab 1 security session.

Add `docs/security-baseline.md` with:

- Data collected.
- Data stored locally.
- Data deliberately not collected.
- Trust boundaries.
- Top 3 risks and mitigations.

### 4. Local AI

Implement one local AI-assisted feature. Choose one:

- Listing helper: suggest a category and rewrite a clearer listing description.
- Search helper: convert a natural language query into filters such as category, area, and listing type.
- Safety helper: flag risky listing text before saving.
- Apply relevant learnings from the MAL Lab 1 local AI session.

Implementation rule:

- Put AI behavior behind an interface such as `LocalAiService`.
- Provide a deterministic fallback implementation that works without a model.
- If you use an actual local model, keep it on the user's device, in the browser, in the app runtime, or locally during development. Use the deterministic fallback when a local model is not available.

Add `docs/local-ai-note.md` with:

- Feature chosen.
- Model or fallback used.
- Inputs and outputs.
- Latency observed on your device, browser, simulator, emulator, or local runtime.
- Privacy trade-off.

### 5. Architecture

Add one ADR at `docs/adr/0001-local-first-marketplace-slice.md`.

It should answer:

- Why this slice is local-first.
- Where product logic lives.
- Where local storage lives.
- How AI is isolated from UI.
- What can change in later labs without rewriting the whole app.
- Apply relevant architecture learnings from MAL Lab 1.

## Suggested App Structure

Use the structure that fits your stack, but keep boundaries visible. The names below are illustrative, not required.

```text
src/ or lib/
  app entrypoint
  features/
    listings/
      data/
      domain/
      presentation/
    neighborhood/
    local_ai/
  shared/
    accessibility/
    storage/
    theme/
docs/
  adr/
  product-slice.md
  success-metrics.md
  accessibility-check.md
  security-baseline.md
  local-ai-note.md
```

## Daily Plan

### Day 1 - Product Slice

Define the exact user loop and create `docs/product-slice.md`.

Output:

- Product note saved in the project.
- `docs/success-metrics.md` created.
- Three listing categories selected.
- Required success metrics and one project-specific metric written.

Acceptance criteria:

- The scope can be demoed in under three minutes.
- At least three things are explicitly out of scope.
- Success metrics can be evaluated without real users or production deployment.

### Day 2 - App Skeleton

Create or clean up the project structure for your chosen platform.

Output:

- App launches.
- Home screen route exists.
- Basic light/dark theme or single documented theme exists.
- Setup/run command is documented.

Acceptance criteria:

- The documented run command reaches the first screen.
- Project has clear feature folders or an equivalent architecture.

### Day 3 - Domain Model

Create the marketplace domain model.

Suggested entities:

- `Neighborhood`
- `Listing`
- `ListingCategory`
- `ListingStatus`
- `ContactPreference`

Output:

- Domain models added.
- Sample seed listings added.

Acceptance criteria:

- Models do not depend on UI framework widgets/components.
- Listing status supports at least active and closed.

### Day 4 - Listing Feed

Build the listing feed for one neighborhood.

Output:

- Feed screen.
- Listing card component.
- Empty state.

Acceptance criteria:

- User can scan title, category, area, and status.
- Screen reader or platform accessibility tooling reads each listing as one understandable item.

### Day 5 - Listing Details

Build listing detail view.

Output:

- Detail screen.
- Save/contact/close action placeholder.

Acceptance criteria:

- Detail screen uses route arguments or typed navigation.
- Actions update visible state, even if only locally.

### Day 6 - Create Listing Form

Build listing creation.

Output:

- Form with title, category, description, area, and contact preference.
- Validation errors.

Acceptance criteria:

- Invalid input is handled before save.
- Errors are visible as text.
- Keyboard flow is usable.

### Day 7 - Local Persistence

Persist listings locally.

Output:

- Local storage implementation.
- Repository or data source abstraction.
- Reset local data action.

Acceptance criteria:

- Data remains after app restart.
- UI does not directly call storage APIs.
- User can clear local data.

### Day 8 - Accessibility Pass

Audit and fix accessibility issues.

Output:

- `docs/accessibility-check.md`.
- Semantic labels and focus order improvements.

Acceptance criteria:

- Core screens are usable with screen reader or equivalent platform accessibility basics.
- Tap targets are at least 48 x 48 CSS/logical pixels, or the platform-recommended minimum.
- Form errors are announced or easy to discover.

### Day 9 - Security Baseline

Add privacy and security guardrails.

Output:

- `docs/security-baseline.md`.
- Input validation tightened.
- No precise address or exact location stored.

Acceptance criteria:

- API keys and secrets stay out of the repo.
- Local data fields are documented.
- Top 3 risks have concrete mitigations.

### Day 10 - AI Interface

Create the AI boundary.

Output:

- `LocalAiService` or equivalent interface.
- Fallback implementation.
- Unit tests or simple deterministic checks for fallback behavior.

Acceptance criteria:

- UI depends on the interface, not a concrete model.
- Fallback works without network access.

### Day 11 - AI Feature Integration

Connect the AI helper to one workflow.

Output:

- AI helper visible in listing creation, search, or safety review.
- `docs/local-ai-note.md` started.

Acceptance criteria:

- User can accept, reject, or edit AI output.
- AI output never saves automatically without user confirmation.

### Day 12 - ADR

Write the first architecture decision record.

Output:

- `docs/adr/0001-local-first-marketplace-slice.md`.

Acceptance criteria:

- ADR has context, decision, consequences, and alternatives considered.
- It explains what can change in later labs.

### Day 13 - Demo Hardening

Make the app demoable.

Output:

- Seed data polished.
- Loading, empty, and error states reviewed.
- Basic manual test script written in the README or docs.

Acceptance criteria:

- Demo can be completed in three minutes.
- App does not crash during the main workflow.

### Day 14 - Final Review

Run final checks and prepare the project for sharing.

Output:

- Final commit, tagged branch, or packaged project folder.
- Short demo notes.
- Known gaps listed.

Acceptance criteria:

- App launches from a fresh checkout or fresh project copy.
- Run instructions are clear for the chosen platform.
- Homework docs are complete.
- Product, accessibility, security, and AI work are visible in the app or docs.

## Final Submission Checklist

- App runs locally or on the chosen target platform.
- Language/framework choice is documented.
- README includes setup, run, demo, known gaps, and links to docs.
- Shared repo/package excludes secrets, dependency folders, and generated build artifacts.
- Listing feed works.
- Listing creation works.
- Local persistence works.
- One AI-assisted flow works with offline fallback.
- Accessibility check exists and at least three fixes were made.
- Security baseline exists and exact location is not stored.
- Success metrics exist and include one project-specific metric.
- ADR exists.
- Demo script exists.

## Demo Script

Keep the demo under three minutes:

1. Open the app and show the selected neighborhood.
2. Show the listing feed.
3. Create a listing or request.
4. Use the AI helper.
5. Save the listing and show it in the feed.
6. Open details and change status.
7. Point to one accessibility improvement and one security decision.

## Organizer Review Guide

Judges or event organizers can review each project with a consistent 10-15 minute flow. The goal is not to reward the largest app. The goal is to recognize a working, explainable product slice that applies the Lab 1 themes.

### Review Inputs

Recommended review inputs:

- Project repo link or packaged project folder.
- `README.md` with setup and run instructions.
- `docs/product-slice.md`.
- `docs/success-metrics.md`.
- `docs/accessibility-check.md`.
- `docs/security-baseline.md`.
- `docs/local-ai-note.md`.
- `docs/adr/0001-local-first-marketplace-slice.md`.
- Three-minute demo script or recording.

### Step 1 - Review Readiness

Start the review with these readiness checks:

- The project opens from a fresh checkout or fresh project copy.
- Setup/run instructions are present.
- The chosen platform and framework are documented.
- The expected docs exist.
- README links to the required docs and includes known gaps.
- Secrets, dependency folders, and generated build outputs are kept out of the shared project.
- The attendee has listed known gaps honestly.

If a project cannot run because of missing instructions, organizers can still review the docs and give focused feedback on what to fix before Lab 2.

### Step 2 - Demo Validation

Run or watch the three-minute demo and check:

- App opens to a usable first screen.
- Neighborhood context is visible or selectable.
- Listing feed is visible.
- New listing/request can be created.
- Listing persists after refresh, restart, or relaunch.
- Details/status interaction works.
- AI helper is shown in one workflow.
- AI output can be accepted, rejected, or edited.
- One accessibility decision and one security decision are explained.

### Step 3 - Evidence Checks

Reviewers should look for evidence, not just claims:

- Product: `docs/product-slice.md` names the user, problem, workflow, out-of-scope items, and success metrics.
- GitHub hygiene: `README.md` explains setup, run, demo, known gaps, and links to required docs.
- Success metrics: `docs/success-metrics.md` includes the required metric areas and one project-specific metric.
- Accessibility: app has visible error messages, usable labels, reasonable tap targets, and documented checks.
- Security: app avoids exact address, precise live location, secrets, hosted AI API keys, and backend dependency for the core flow.
- Local AI: the AI boundary exists in code or design, and fallback works without network access.
- Architecture: ADR explains local-first choice, storage boundary, product logic, AI boundary, and future change points.

### Step 4 - Risk Checks

These issues should be called out clearly during review:

- Core workflow depends on a backend to function.
- Hosted AI API is used for the expected local AI flow.
- Exact home address or precise live location is stored.
- Secrets or API keys are present in the shared project.
- Dependency folders or generated build artifacts are shared as source.
- App cannot create a listing/request.
- Local persistence is missing.
- Architecture decision record is missing.

## Evaluation Rubric

Score out of 20 points.

| Area | Points | What Good Looks Like |
| --- | ---: | --- |
| Product | 3 | Clear user, problem, scoped workflow, and one small personal product addition |
| Core Workflow | 4 | Feed, create listing/request, details/status, and local persistence work |
| Accessibility | 3 | Implemented in UI, not only documented |
| Security | 3 | Data minimization and local storage risks are addressed |
| Local AI | 3 | AI feature has a fallback and does not require hosted APIs |
| Architecture | 2 | Feature boundaries are visible, storage and AI are isolated, ADR is clear |
| Success Metrics | 1 | Metrics are specific, testable during review, and include one project-specific metric |
| Delivery | 1 | Runs from a fresh checkout or project copy and can be demoed in three minutes |

Suggested interpretation:

- 18-20: Strong Lab 1 outcome; good candidate to demo at Lab 2.
- 14-17: Solid project; may need targeted cleanup.
- 10-13: Partial outcome; main gaps should be fixed before Lab 2.
- Below 10: Not yet ready; the attendee can reduce scope and complete the core loop first.

## Stretch Options

Explore these only after the core checklist is complete:

- Add simple full-text search over local listings.
- Add offline sync queue interface without a backend.
- Add image attachment placeholder without uploading images.
- Add analytics event names in documentation only.
- Add UI/component/form tests for the listing form.
