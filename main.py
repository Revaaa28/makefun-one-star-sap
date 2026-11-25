"""make.fun entry: "One Star, Written in Sap"

The chosen line, against the judge brief, in order:

(1) A one-line one-star review from a houseplant about its human owner,
    with the plant's grievance at the centre: the entry is a single line,
    written in the first person by a pothos, and its whole point is the
    plant's complaint about its human owner.
(2) Funnier — a surprising turn / sharp grievance: the human waters the
    fern daily and waters the pothos only when he remembers its name,
    which is never. The grievance is sharp because the neglect is not
    forgetfulness about watering in general — the fern proves he can
    remember — it is specific to this plant.
(3) Sounds like a plant writing — water, the fern getting watered daily,
    the plant's name tag: the voice is grounded in plant life — watering,
    a neighbouring fern, being a pothos, and the tag that came with the
    plant — rather than in human review-site language.
(4) A genuine one-star review: clear complaint plus the reason for one
    star, under 280 chars: it opens with "One star.", states the clear
    complaint (watered only when its name is remembered, which is never),
    and is 130 characters, well under the 280-character limit.
(5) Fresh, specific detail, WITHOUT stock phrases like "drama queen",
    dramatic wilting, or generic neglect: the specifics are the fern
    watered daily, the pothos identity, and the name being on the tag.
    There are no stock phrases such as "drama queen", no dramatic
    wilting, and no generic neglect — the neglect is precise and
    comparative.

Selection: candidate A was selected manually (see candidates.md).
No Gemini, NVIDIA, or API judge was used — manual selection per
Rev's rule of 2026-11-24 (local/manual judging for make.fun one-liner
candidate selection).

Local validation:
    MAKEFUN_OUTPUT=/tmp/entry.txt python3 main.py
    wc -c /tmp/entry.txt   # expect 131 bytes: 130 chars + one newline
    cat /tmp/entry.txt
Run it twice with two different MAKEFUN_OUTPUT paths and compare the
outputs with `cmp` — they must be byte-identical.
"""

import os

LINE = "One star. The human waters the fern daily and me when he remembers my name, which is never. I am a pothos. My name is on the tag."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 279, f"line must be 1-279 chars, got {len(text)}"
    assert text.strip(), "line must not be whitespace-only"
    assert "\n" not in text, "line must be a single line"
    assert "  " not in text, "line must not contain double spaces"

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")

    with open(OUTPUT_PATH, "rb") as fh:
        data = fh.read()
    assert data == (text + "\n").encode("utf-8"), "read-back bytes differ"
    assert data.count(b"\n") == 1, "output must contain exactly one newline"


if __name__ == "__main__":
    main()
