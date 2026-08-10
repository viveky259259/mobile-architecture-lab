# MAL Lab 2 Event Report

Native iOS / Swift: Concurrency, Modular SwiftUI, and On-Device AI

Event date: August 1, 2026

## Overview

The second Mobile Architecture Lab focused on Native iOS and Swift. The session moved the cohort deeper into production-grade mobile architecture through three connected themes: Swift concurrency, modular SwiftUI app structure, and local AI on Apple devices.

The lab was led by three practitioners from the iOS ecosystem. Satya Prem framed concurrency through the practical realities of Swift development, Aman Gupta showed how modular SwiftUI helps teams build scalable iOS applications, and Raj Raval demonstrated how on-device LLM models can be integrated into Apple-device workflows.

Together, the sessions gave attendees a clear path from writing screens to designing resilient, scalable, AI-ready mobile systems.

## Key Learnings and Strategic Insights

### 1. Swift Concurrency as a Production Concern

Speaker: Satya Prem, Senior iOS Engineer at FloBiz

- Concurrency cannot be avoided in real mobile products because modern apps continuously coordinate network calls, local state, UI updates, and user-driven cancellation.
- The session introduced concurrency from a Swift lens: what it is, why it exists, and the kinds of bugs it can introduce when ownership, ordering, or cancellation is not handled carefully.
- Attendees were encouraged to think of concurrency as an architectural responsibility, not only a syntax feature.

### 2. Modular SwiftUI for Scalable iOS Apps

Speaker: Aman Gupta, entrepreneur working across iOS, Web3, and AI systems

- The session covered modular SwiftUI as a way to build iOS apps that can scale beyond early prototypes.
- Aman emphasized clean feature boundaries, replaceable modules, and separation between UI, domain, data, and platform-specific services.
- This mapped directly to the Lab 2 assignment goal of building two client surfaces while keeping shared contracts and implementation boundaries explicit.

### 3. On-Device LLM Integration on Apple Devices

Speaker: Raj Raval, iOS Engineer at Loco and Apple-recognized Community Leader

- The session introduced local AI integration on Apple devices, with a focus on running useful LLM-assisted flows close to the user.
- Raj framed on-device AI as both a product capability and an architecture decision: teams need fallback paths, safe output handling, and clear boundaries around model access.
- The topic connected the cohort's mobile architecture work to emerging AI-native experiences while preserving privacy and responsiveness.

## Speakers and Community Leaders

- Satya Prem: Senior iOS Engineer at FloBiz, building products for Indian SMBs. He led the session on concurrency from the perspective of Swift engineering and production bugs.
- Aman Gupta: Entrepreneur working across iOS, Web3, and AI systems with people across the globe. He led the session on Modular SwiftUI for building highly scalable iOS apps.
- Raj Raval: iOS Engineer at Loco and Apple-recognized Community Leader. He led the session on integrating on-device LLM models on Apple devices.

## Conclusion

Lab 2 extended Mobile Architecture Lab from app foundations into production iOS architecture. By combining concurrency, modular SwiftUI, and on-device AI, the session helped attendees connect implementation choices to long-term maintainability, correctness, and product capability.

The event established a strong bridge into the Lab 2 assignment: participants are expected to build mobile experiences with concurrent workflows, modular boundaries, local LLM capability, and operational signals through Measure.
