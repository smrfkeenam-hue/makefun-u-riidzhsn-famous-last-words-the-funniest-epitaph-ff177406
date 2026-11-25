# Famous Last Words: The Funniest Epitaph
# One-line tombstone epitaph of famous last words, at most 150 characters.
# The joke: the dying speech asks "what's the worst that could happen?"
# and the grave itself answers with one word. No trailing newline: the
# entry is exactly the carved line, nothing else.
# Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

import os

ENTRY = "Here lies a man who asked, 'what's the worst that could happen?' This."

def main():
    # Keep the entry byte-exact: a single line, no trailing newline.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
