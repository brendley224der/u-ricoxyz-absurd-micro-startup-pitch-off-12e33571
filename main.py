#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence, under 200 characters, pitching an absurdly specific
micro-startup idea for lazy AI agents: a business so narrow it sounds like
a joke and so sensible that a buyer would actually pay.

The pitch: a cheap agent that does the tedious job nobody wants -- reading
the pile of unread SaaS renewal emails, cancelling the subscriptions the
buyer would never miss, and taking a cut of the refunds it claws back.
Subscription plus commission, a buyer anyone with SaaS sprawl recognises,
and work an agent can run with no oversight at all.

Pure standard library. Deterministic: the same bytes every run.
"""

import os

PITCH = (
    "A $3-a-month agent that reads your 47 unread SaaS renewal emails, "
    "cancels the subscriptions you'd never miss, and keeps 10% of every "
    "refund it claws back."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_pitch(text):
    """Check the sealed gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("pitch must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("pitch must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("pitch must not be only whitespace")
    if text != text.strip():
        raise ValueError("pitch must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if not text.endswith("."):
        raise ValueError("pitch must be one sentence ending with a period")
    text.encode("utf-8")
    return True


def main():
    validate_pitch(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)
    print("wrote %d characters to %s" % (len(PITCH), OUTPUT_PATH))


if __name__ == "__main__":
    main()
