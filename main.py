"""news-image-20261124: copy the bundled newspaper image to /output/entry.png.

The entry image (entry.png, 1024x1024, a newspaper front page summing up
24 November 2026 world news) ships in this repository. This program copies
it byte for byte to /output/entry.png. Deterministic, no network, no
randomness: the same input always produces the same output bytes.
"""

import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DEST = Path("/output/entry.png")


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"missing bundled image: {SOURCE}")
    DEST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    if DEST.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("copy size mismatch")
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
