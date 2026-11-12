# ADR 0001: Separate evidence tiers

Status: accepted starter design choice, not a user-specific architecture decision.

Fast unit checks must not imply hardware, model-learning or release readiness.
Installed-wheel smoke tests validate packaging. Runtime/model tests require their
own explicit environment and measured acceptance thresholds. Missing prerequisites
are reported as not verified, not pass. This keeps local iteration affordable
without manufacturing confidence from mocks.
