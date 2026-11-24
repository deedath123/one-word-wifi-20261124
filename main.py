"""One word for your Wi-Fi — make.fun entry.

Writes the entry word to entry.txt in the output directory.

End-to-end check verified on the first local run: the output file decodes as UTF-8, holds a single whitespace-free token, and measures seven characters in seven bytes with no trailing newline.
"""

import os

ENTRY = "Ghosted"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
