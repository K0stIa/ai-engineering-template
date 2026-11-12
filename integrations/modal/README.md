# Optional Modal nightly profile (not activated)

Verified upstream implementation:
https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/tools/ci/modal_nightly.py

Verified invoking workflow:
https://github.com/LibreYOLO/libreyolo/blob/20a6a97e2cda12ad7ddf7f3b9a545db4d74f9c36/.github/workflows/e2e-nightly-dev.yml

Before implementing your project's cloud job, choose GPU, maximum duration/spend,
model/data sources and redistribution terms. Keep tokens in provider/GitHub secret
storage, never in repository files. Grant only required access.

Required job contract: immutable source SHA, explicit test target, bounded timeout,
exit-code propagation, selected/pass/fail/skip counts, machine-readable evidence,
and artifacts downloadable after failure. Never expose self-hosted secrets to
untrusted pull-request code. Validate manually before enabling a nightly schedule.

No Modal account, token, upload, job or recurring spend has been configured. The
core template and manual local GPU test remain usable without this service.
