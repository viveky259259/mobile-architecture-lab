# MAL Lab 2 Assignment

Two-week implementation brief for attendees after Lab 2: Native iOS / Swift.

Start: August 2, 2026  
Due: August 15, 2026, before Lab 3

## The assignment

Continue the same MAL Local product, but move from a single local-first app to a small system with two deliberate client surfaces:

1. A customer mobile app for discovering and using the neighborhood marketplace.
2. An admin website for managing listings, reviewing activity, and operating the marketplace.

The implementation must make four architectural ideas visible:

- **Concurrency:** independent work happens concurrently, can be cancelled, and cannot corrupt shared state.
- **Modular design:** customer mobile, admin web, product logic, data access, local AI, and observability have replaceable boundaries.
- **Local LLM:** at least one useful AI flow runs with a model in the local app/runtime, with a deterministic fallback when the model is unavailable.
- **Production signals:** the mobile app uses [Measure](https://measure.sh/) for observability, analytics, and product events.

This is an architecture assignment, not a request to build a large backend. A local API, mock server, shared fixture, or small development service is acceptable if the boundaries are clear and both clients can demonstrate the same product state.

## Where to continue from MAL 1

Start from the MAL 1 local-first marketplace slice. Do not throw it away and restart unless the code cannot be made runnable.

Carry forward:

- The core customer workflow: browse, search, create, save/contact/close a listing or request.
- The local-first data model, seed data, validation rules, and recovery/reset path.
- The Lab 1 ADR and product notes, especially the local storage boundary, privacy assumptions, accessibility baseline, and local AI boundary.
- Any working mobile UI, navigation, persistence, and local AI helper from Lab 1.

For Lab 2, evolve that base in four ways:

1. Extract the product model into a shared contract that both customer mobile and admin web can use.
2. Add the admin website as an operator surface for the same listings and statuses.
3. Make concurrency, module boundaries, local LLM fallback, and Measure instrumentation visible in code and docs.
4. Update the ADR instead of replacing the MAL 1 decision: explain what changed, what stayed local-first, and why the new two-client architecture is still small enough to reason about.

If the MAL 1 implementation is incomplete, continue from the smallest runnable slice: one listing list, one create flow, one persistence path, and one documented recovery path. Then add Lab 2 architecture around that slice.

## Product brief

Working title: **MAL Local**

Problem: Residents need a lightweight way to find, request, lend, sell, or share nearby goods and services. Marketplace operators need enough visibility to keep listings useful and safe.

### Customer mobile app

The customer can:

- Choose or see a coarse neighborhood.
- Browse and search active listings or requests.
- Open listing details.
- Create a listing or request with title, category, description, approximate area, and contact preference.
- Save, contact, or close a listing.
- Use the local LLM helper to improve, classify, search, or safety-check a listing.
- Continue the core flow when the local model is unavailable.

### Admin website

The admin can:

- See a management dashboard with listing counts and recent activity.
- Search and filter listings.
- Open a listing and change its operational status: active, flagged, hidden, or closed.
- Review the reason for a flag or local AI suggestion before taking action.
- See enough event or health information to understand the demo workflow; do not expose raw personal data.

The customer app and admin website must use the same domain concepts and data contract. A status change made by the admin must be visible to the customer after refresh, sync, or the documented local development flow.

## Scope rules

Keep the core workflow small and finishable. Payments, delivery, real identity verification, real-time chat, production authentication, multi-tenant billing, and a production cloud deployment are out of scope unless they already exist in your project and do not distract from this assignment.

Use seed data, mock data, or your own test entries. Do not commit API keys, model secrets, exact home addresses, precise live location, or real personal data.

Carry forward the Lab 1 baseline: keep the customer flow accessible, keep local data and AI privacy-conscious, validate inputs, and preserve a documented reset or recovery path. Lab 2 adds system boundaries and operational signals; it does not remove those expectations.

## Required implementation

### 1. Two clients, one product model

Build both a customer mobile app and an admin website. They may use different frameworks, but they must share or explicitly align on:

- Listing, category, neighborhood, contact preference, and status models.
- Validation rules and stable identifiers.
- A repository, API, fixture, or local service boundary.
- The state transition rules for active, flagged, hidden, and closed listings.

The admin surface must manage real demo data rather than displaying a disconnected static mockup.

Add `docs/product-slice.md` describing the customer workflow, admin workflow, shared model, and deliberate non-goals.

### 2. Concurrency

Implement at least two meaningful concurrent workflows. At least one must be in the mobile app and at least one must be in the admin website or shared data layer.

Good examples:

- Mobile home loads neighborhood context, cached listings, and local configuration concurrently.
- Mobile search cancels the previous request when a new query arrives and ignores stale results.
- Admin dashboard loads counts, recent listings, and flagged items concurrently.
- Saving a listing updates local state and schedules persistence without blocking the UI.

Your implementation must show:

- Structured tasks, actors, task groups, coroutines, workers, promises, or an equivalent concurrency primitive from your stack.
- Cancellation or stale-result handling for work that can outlive a screen or request.
- A clear ownership rule for mutable shared state.
- Bounded work: no unbounded task creation from a list, keystroke, or event stream.
- Tests for at least one race, cancellation, ordering, or failure case.

Do not count wrapping sequential code in `async` as the concurrency requirement. Add `docs/concurrency-notes.md` with a small diagram or table showing the work, dependencies, cancellation behavior, and failure policy.

### 3. Modular design

Make the module boundaries visible in the repository. The names can vary, but the responsibilities should resemble:

```text
customer-mobile/
  features/listings/
  features/local-ai/
  shared/observability/
admin-web/
  features/listing-management/
  features/dashboard/
shared/
  domain/
  contracts/
  validation/
  data/
```

Minimum boundary expectations:

- UI screens/components do not own persistence, networking, or model-runtime code.
- Product rules live outside individual views.
- Storage/API access is behind a repository or data-source interface.
- Local LLM access is behind a `LocalLlmService` or equivalent interface.
- Measure instrumentation is called through a small analytics/observability boundary rather than scattered vendor-specific calls.
- Admin-only actions are isolated from customer presentation code.

Add `docs/module-map.md` showing the modules, their owners, and the allowed dependency direction. Include one example of how a module could be replaced without rewriting its callers.

### 4. Local LLM

Implement one useful local LLM-assisted flow in the mobile app. Choose one:

- **Listing assistant:** suggest a category and rewrite a rough description into clear, editable text.
- **Search assistant:** turn a natural-language query into safe, editable filters.
- **Safety assistant:** flag potentially risky listing text before it is submitted.

An optional second flow may help the admin review listings, but it is not required.

Rules:

- The expected flow must run with a local model/runtime on the device, in the browser, or in a local development process.
- A deterministic fallback must work with the model removed, disabled, slow, or failed.
- AI output must be editable and must not silently publish or hide a listing.
- Do not send listing content to a hosted AI API for the expected flow.
- Do not commit large model files unless they are essential, license-safe, and documented.
- Keep prompts, model adapters, parsing, and fallback behavior out of UI components.

Add `docs/local-llm-note.md` with the chosen model/runtime, device or simulator, input/output shape, fallback behavior, observed latency, memory considerations, and privacy trade-offs.

### 5. Measure on mobile

Use the Measure mobile integration appropriate for your chosen mobile stack. Measure is required for the mobile app’s:

- **Observability:** crashes, errors, failed requests, local LLM failures, and important latency points.
- **Analytics:** screen or workflow usage needed to understand the customer funnel.
- **Events:** explicit product events with stable names and documented properties.

At minimum, instrument these mobile events:

| Event | When it fires | Safe properties to consider |
| --- | --- | --- |
| `customer_app_opened` | App reaches its usable state | app version, platform |
| `listing_feed_viewed` | Customer feed is visible | coarse neighborhood, result count |
| `listing_search_submitted` | Customer submits a search | query length, filter count |
| `listing_create_started` | Create flow opens | entry point |
| `listing_create_completed` | Listing passes validation and saves | category, duration bucket |
| `local_llm_requested` | Customer asks for AI help | feature, input length bucket |
| `local_llm_completed` | Local model or fallback returns | feature, provider=`local\|fallback`, latency bucket |
| `listing_contacted` | Customer chooses the contact action | listing category |

Also record enough context to diagnose the two concurrent workflows, such as duration buckets, cancellation, timeout, and failure reason. Keep event payloads free of listing descriptions, phone numbers, exact addresses, precise coordinates, tokens, and other unnecessary personal data.

Create `docs/observability-events.md` with the final event taxonomy, privacy review, measured flow, and a screenshot or short note showing how the events/errors were verified in Measure. If your stack uses a local debug sink before Measure is configured, document that temporary path and the final integration path.

### 6. Quality and evidence

Your repository must include:

- `README.md` with setup, run, test, and three-minute demo instructions.
- `docs/product-slice.md`
- `docs/concurrency-notes.md`
- `docs/module-map.md`
- `docs/local-llm-note.md`
- `docs/observability-events.md`
- `docs/adr/0002-two-client-concurrent-local-llm-architecture.md`
- A `.gitignore` or equivalent cleanup.

The ADR must explain why the product has two clients, where shared contracts live, how concurrency is owned and cancelled, why the LLM is local-first, and why Measure is isolated behind an observability boundary.

## Success metrics

Add `docs/success-metrics.md` with project-specific targets. Start with these reviewable examples:

| Area | Required metric | Example target | How to verify |
| --- | --- | --- | --- |
| Customer workflow | Find-to-action completion | Customer can search, open, and contact a listing in under 3 minutes | Fresh demo run |
| Admin workflow | Operational action completion | Admin can find and hide a listing in under 2 minutes | Fresh admin run |
| Shared state | Cross-client consistency | Admin status change appears in mobile after documented refresh/sync | Run both clients |
| Concurrency | Responsiveness and correctness | No stale search result or UI freeze during concurrent load | Test plus demo |
| Modularity | Replaceability | Swap the fake repository or LLM fallback without changing screens | Code review |
| Local LLM | Useful fallback | Same safe, editable flow works with model disabled | Disable model |
| Observability | Event coverage | Required mobile events and failures are visible with no sensitive payloads | Measure verification |
| Reliability | Repeatability | Customer and admin demo flows pass twice from a clean state | Run twice |

Add one metric based on your product angle, such as flagged-listing review time, category suggestion acceptance, or offline recovery time.

## Suggested 14-day plan

| Day | Focus | Output |
| --- | --- | --- |
| 01 | Re-scope the product | Customer/admin workflows and non-goals |
| 02 | Shared model | Domain entities, IDs, status transitions |
| 03 | Module map | Packages/features and dependency direction |
| 04 | Customer shell | Mobile feed and navigation |
| 05 | Admin shell | Dashboard, list, and detail views |
| 06 | Shared data boundary | Repository/API/fixture used by both clients |
| 07 | Concurrent loading | Parallel work with ownership and cancellation |
| 08 | Concurrent search/actions | Stale-result and failure tests |
| 09 | Local LLM boundary | Adapter, prompt/input contract, deterministic fallback |
| 10 | LLM workflow | Editable customer flow and latency measurement |
| 11 | Measure integration | Observability, analytics, and product event taxonomy |
| 12 | Cross-client hardening | Admin action reflected in mobile |
| 13 | Documentation | ADR, module map, concurrency and privacy notes |
| 14 | Demo rehearsal | Fresh setup, tests, evidence, known gaps |

## Review rubric — 20 points

| Area | Points | What good looks like |
| --- | ---: | --- |
| Customer mobile app | 3 | Core browse/search/create/action loop is usable |
| Admin website | 3 | Real listing management and status workflow works |
| Concurrency | 4 | Meaningful parallel work, cancellation/ownership, and tests |
| Modular design | 4 | Clear boundaries with replaceable data, AI, and observability layers |
| Local LLM | 3 | Local model path, deterministic fallback, editable/safe output |
| Measure instrumentation | 2 | Mobile observability, analytics, and events are implemented and privacy-reviewed |
| Documentation and delivery | 1 | Fresh setup works; ADR and evidence docs are easy to find |

Reviewers will value a small, explainable implementation over a broad feature list. A missing local model is acceptable only when the fallback is real, tested, and the model path is documented; a hosted AI API is not an acceptable substitute for the expected flow.

## What to fix or work on after assessment

Use the assessment to identify the next architecture improvement, not only to assign a score. Reviewers should give each team two or three concrete fixes from this list:

| Architecture area | What to look for | What to fix or work on |
| --- | --- | --- |
| Product boundary | Customer and admin flows use different models, labels, or status meanings | Create one shared domain contract for listing, category, neighborhood, contact preference, and status transitions |
| Module boundaries | Screens directly call persistence, network, local model, or Measure APIs | Move those calls behind repository, `LocalLlmService`, and observability interfaces |
| Dependency direction | Admin, mobile, shared data, and AI code import each other in both directions | Define allowed dependency direction in `docs/module-map.md` and break cycles with interfaces or adapters |
| Concurrency ownership | Async work updates shared state from multiple places or survives after the screen/request ends | Add one owner for mutable state, cancellation rules, stale-result handling, and a race/cancellation test |
| Cross-client consistency | Admin changes are not visible in mobile, or the sync path is undocumented | Make both clients use the same repository/API/fixture and document the refresh or sync behavior |
| Local LLM boundary | Prompting, parsing, fallback, or model-runtime code lives inside UI components | Move AI behavior into a service with typed input/output, editable results, deterministic fallback, and failure events |
| Observability boundary | Measure calls are scattered across screens or include sensitive payloads | Route events through one analytics boundary and document safe properties in `docs/observability-events.md` |
| Evidence quality | Reviewers cannot understand the decisions without reading all the code | Tighten the ADR, module map, concurrency notes, and demo script so the architecture can be reviewed in minutes |

High-priority fixes are the ones that reduce future rewrite risk: shared contracts, dependency direction, state ownership, and service boundaries. Polish or extra features should wait until those are clear.

## Three-minute demo

1. Open the customer mobile app and show the Measure-backed app-open/feed events.
2. Search and open a listing; show the concurrent loading or cancellation behavior.
3. Create or improve a listing with the local LLM, then disable the model and show the deterministic fallback.
4. Open the admin website, find the same listing, and change its status.
5. Refresh/sync the mobile app and show the status change.
6. Show the module map, concurrency test, event taxonomy, and ADR.

## Submission checklist

- One repository or packaged project that contains both client surfaces.
- Setup commands for the mobile app and admin website.
- Test command(s), seed data instructions, and three-minute demo script.
- Required docs and ADR included.
- Measure integration and event verification documented.
- No secrets, precise location, real personal data, dependency folders, generated build output, or unnecessary model files.
- Known gaps and future work listed in `README.md`.
