"""Check PR provenance presence, not its truth or legal adequacy."""

import re
import sys


def has_provenance(body: str) -> bool:
    body = re.sub(r"<!--[\s\S]*?-->", "", body)
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if re.fullmatch(r"\s*#{1,6}\s+code provenance\s*", line, flags=re.I):
            section = []
            for following in lines[index + 1 :]:
                if re.match(r"\s*#{1,6}\s+", following):
                    break
                section.append(following)
            text = "\n".join(section).strip()
            return bool(text) and text.casefold() not in {"todo", "tbd", "n/a", "..."}
    return False


if __name__ == "__main__":
    valid = has_provenance(sys.stdin.read())
    print(
        "Provenance statement present; human review still required."
        if valid
        else "Missing or empty Code provenance statement."
    )
    sys.exit(0 if valid else 1)
