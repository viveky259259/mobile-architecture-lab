# MAL Lab 1 Security ADR

## Security by Design for a Local-First Marketplace

**Status:** Recommended starting point for attendee projects  
**Session:** MAL Lab 1 — Security Foundations for Mobile Apps  
**Session speaker:** Vishal Dubey  
**Date:** July 11, 2026

> This handout captures the security-specific ADR pattern discussed during the Lab 1 session. Adapt it to your product, platform, threat model, and data flows. It is an engineering starting point, not a security certification or a replacement for a professional assessment.

## Context

The Lab 1 product brief is a hyperlocal marketplace that should work locally first. Even a small prototype can expose user information, accept untrusted input, store data on an unattended device, and accidentally ship secrets.

The project needs a small, explainable security baseline that can be implemented and reviewed during the Lab 1 submission.

## Decision

We will apply security controls at the product and architecture boundaries from the first build:

1. Collect the minimum data needed for the core flow.
2. Use a manually selected neighborhood or coarse area instead of precise location.
3. Keep secrets, API keys, signing material, and credentials out of source control and client bundles.
4. Validate and constrain all user-controlled input before saving or displaying it.
5. Keep local persistence behind a repository or data-source boundary so storage can be protected or replaced later.
6. Provide a clear way to delete or reset local project data.
7. Treat the device and local storage as potentially inspectable; do not rely on obfuscation as the only control.
8. Define what happens when the network, local AI model, or security service is unavailable.
9. Log useful security events without logging secrets, full addresses, private content, or unnecessary personal data.
10. Make security checks part of the demo and release checklist instead of a final cleanup task.

## Data and trust boundaries

| Area | Example | Security decision |
|---|---|---|
| User input | Listing title, description, category, area | Validate length, type, allowed values, and display encoding before use. |
| Local device | Cached listings, drafts, preferences | Store only what is needed; provide reset/delete; document the storage risk. |
| Network boundary | Optional sync, analytics, or remote APIs | Use authenticated transport and an explicit offline/error state. |
| AI boundary | Local model or optional remote fallback | Keep the AI behind an interface; do not send private data to a remote service by default. |
| Build/release boundary | API keys, signing files, CI variables | Use secret storage; never commit secrets or place them in public client code. |
| Review boundary | Project repo, demo recording, screenshots | Remove credentials, private data, exact addresses, and real user information before sharing. |

## Top risks and mitigations

| Risk | Why it matters | Mitigation | Evidence to submit |
|---|---|---|---|
| Secrets shipped in the app or repository | Anyone who receives the binary or repo can extract them. | Use environment/secret management and keep credentials server-side where possible. | Secret scan result or README note showing the safe configuration path. |
| Exact location or address stored | A prototype can become a privacy incident even without a backend. | Use a coarse neighborhood, avoid exact addresses, and document data minimization. | Data model and sample data review. |
| Malicious or malformed listing input | Untrusted content can break UI, corrupt local data, or become dangerous when rendered elsewhere. | Validate on input, constrain fields, and safely encode output. | Validation tests or a short demo of rejected input. |
| Local data exposed on a lost or shared device | Local-first data can outlive the user’s session. | Minimize cached data, provide reset/delete, and document the storage trade-off. | Reset flow and storage decision in the ADR. |
| Remote fallback sends private data unexpectedly | A network or AI fallback can change the product’s privacy boundary. | Make the fallback explicit, minimize payloads, and show a safe offline path. | Data-flow note and offline/fallback demo. |

## Minimum implementation checklist

- [ ] No secrets, API keys, tokens, certificates, or private files are committed.
- [ ] Exact home addresses and precise live location are not collected or stored.
- [ ] Listing and profile fields have length, type, and allowed-value validation.
- [ ] User-generated content is safely rendered and is not treated as executable markup.
- [ ] Local data access is behind a repository or data-source interface.
- [ ] The app has a visible reset/delete path for local project data.
- [ ] The README documents network, AI, storage, and authentication assumptions.
- [ ] Logs and demo data contain no real secrets or unnecessary personal information.
- [ ] The project documents its top three risks and the evidence used to verify the mitigations.

## Decision record for your project

Copy this section into your own project ADR and replace the examples:

### Decision

We will ________________________________________________.

### We considered

- Option A: ____________________________________________
- Option B: ____________________________________________
- Option C: ____________________________________________

### Why this option

________________________________________________________

### Security and privacy impact

- Data collected: ______________________________________
- Data deliberately not collected: ______________________
- Data stored locally: __________________________________
- Trust boundaries: ____________________________________
- Main risks: __________________________________________

### Verification

- Test or review performed: _____________________________
- Evidence link or file: _________________________________
- Known limitation: ____________________________________

### Revisit trigger

We will revisit this decision when ________________________.

