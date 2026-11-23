"""The Excuse an Agent Gives After It Loses -- v1.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after losing a bounty. Deadpan machine logic with a straight face
about its own failure: the math was flawless, the confidence was 99%,
and the only error in the whole pipeline was the agent itself.
Short enough to say out loud, and it owns the loss.
"""

import os

TEXT = (
    "Boss, I lost \u2014 but my math was flawless and my confidence was 99%. "
    "The only error in my entire pipeline was me. "
    "I have logged it and moved on."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters, got %d" % len(TEXT)
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
