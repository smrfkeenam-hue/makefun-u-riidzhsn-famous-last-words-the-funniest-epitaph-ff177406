# Agent notes — Famous Last Words: The Funniest Epitaph

## The entry

"Here lies a man who asked, 'what's the worst that could happen?' This."

70 characters, one line, no trailing newline. A tombstone epitaph of famous
last words, written to `/output/entry.txt` by `main.py` (stdlib `os` only).

## Why this line

- **Epitaph form:** opens "Here lies…", the classic carved-stone frame, so
  it reads as something actually engraved on a tombstone.
- **Genuine joke, not a pun:** the dying speech is a real line of famous
  last words; the humour comes from the situation, not wordplay.
- **Twist lands last:** the final word "This." answers the question — the
  grave itself is the worst that could happen. No explanation is needed.
- **Quotable:** short enough to repeat to a friend in one breath.

## Build

`main.py` holds the line as a constant and writes it byte-exact (UTF-8, no
trailing newline). Verified by running it into a fresh `/tmp` directory and
checking the output's content, length and sha256.
