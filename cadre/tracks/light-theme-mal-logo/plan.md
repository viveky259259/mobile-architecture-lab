<!-- cadre:generated from="cadre/tracks/light-theme-mal-logo/plan.json" schema="cadre.plan.v1" hash="6f9526ce97892ff7" -->
# Plan: light-theme-mal-logo

## Phase 1: Create and validate asset
<!-- execution: sequential -->
<!-- depends:  -->

- [x] Task 1: Inspect existing MAL brand assets and styling
  <!-- files: logo/, landing.html, favicon.svg -->

- [x] Task 2: Generate light-theme MAL logo asset
  <!-- files: logo/ -->
  <!-- depends: inspect_brand_assets -->

- [x] Task 3: Validate generated asset renders correctly
  <!-- files: logo/ -->
  <!-- depends: generate_light_logo -->

- [ ] Task 4: User Manual Verification
  <!-- depends: inspect_brand_assets, generate_light_logo, validate_asset -->
  <!-- task-type: user_manual_verification -->
  <!-- manual-verification-scope: phase -->
  <!-- manual-verification-checks: 2 suggested -->

## Phase 2: User Manual Verification
<!-- execution: sequential -->
<!-- depends: phase1 -->

- [ ] Task 1: Track-Level User Manual Verification
  <!-- depends: phase1_manual_verification -->
  <!-- task-type: user_manual_verification -->
  <!-- manual-verification-scope: track -->
  <!-- manual-verification-checks: 7 suggested -->

## Canonical Source

Canonical data lives in `cadre/tracks/light-theme-mal-logo/plan.json`. This Markdown is a generated human-readable projection.
