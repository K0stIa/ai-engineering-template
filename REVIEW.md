# Review contract

Review actual changed behavior, not the author's confidence.
- Reproduce a finding with file, failure scenario and consequence.
- Verify return codes, output meaning, and that tests actually selected work.
- Separate unit/mock evidence from installed/runtime/model evidence.
- Check interfaces against docs/adr and explain shared-code blast radius.
- Check input boundaries, missing files, unavailable services and empty datasets.
- Check provenance, license compatibility and inadvertent secrets.
- Reject claims that a skipped hardware/child test passed.
- Do not approve, merge or publish on the user's behalf without authority.
