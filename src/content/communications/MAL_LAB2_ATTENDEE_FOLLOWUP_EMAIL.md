# MAL Lab 2 Attendee Email

Subject: Thank you for attending MAL Lab 2 - assessment is live

Preview text: Lab 2 homework is now available. Please submit your assessment by August 16, 2026.

Hi everyone,

Thank you for joining MAL Lab 2: Native iOS / Swift.

It was great to have you in the room for the sessions with Satya Prem, Aman Gupta, and Raj Raval across Swift concurrency, Modular SwiftUI, and on-device LLMs on Apple devices.

Your Lab 2 homework and assessment is now live:

https://mobilearchitecturelab.com/assignment-2/

Markdown brief:

https://mobilearchitecturelab.com/MAL_LAB2_HOMEWORK.md

Due date: Sunday, August 16, 2026, before Lab 3.

For this assessment, continue MAL Local from a single local-first mobile app into a small two-client product system:

- Customer mobile app: browse, search, create, and act on local listings.
- Admin website: manage listings and update operational status.
- Shared product contracts across both clients.
- Meaningful concurrency with cancellation or stale-result handling.
- Clear module boundaries for data, local AI, and observability.
- A local LLM-assisted mobile flow with a deterministic fallback.
- Measure instrumentation for mobile observability, analytics, and product events.

If you attended Lab 1, please continue from your Lab 1 marketplace slice. Carry forward your customer workflow, local-first data model, validation rules, reset path, ADR, privacy assumptions, accessibility baseline, and any local AI boundary you already created. Lab 2 is about evolving that foundation into a clearer architecture with two clients and stronger system boundaries.

If you missed Lab 1, you can still participate. Start from the smallest runnable MAL Local slice:

- One listing list.
- One create-listing flow.
- One persistence path, even if it is a local fixture or mock repository.
- One documented reset or recovery path.
- Basic validation and privacy-conscious test data.

Then build Lab 2 around that slice. You do not need to recreate every Lab 1 artifact before starting, but your submission must make the architecture reviewable through the product slice, module map, concurrency notes, local LLM note, Measure event taxonomy, success metrics, and ADR.

The assessment is worth 20 points:

- Customer mobile app: 3
- Admin website: 3
- Concurrency: 4
- Modular design: 4
- Local LLM: 3
- Measure instrumentation: 2
- Documentation and delivery: 1

Reviewers will also call out what to fix or improve next, especially around product boundaries, dependency direction, state ownership, cross-client consistency, local LLM boundaries, observability boundaries, and evidence quality.

Bring a small, working, explainable system. A narrow implementation with clear decisions is better than a broad feature list with hidden coupling.

Thanks,

Vivek and the MAL team
