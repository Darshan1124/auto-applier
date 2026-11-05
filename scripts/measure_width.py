#!/usr/bin/env python3
"""Estimate whether every resume line fits on ONE rendered line, before compiling.

Usage:  python measure_width.py path/to/resume.tex [--cap 525]

It reads the .tex, finds
  * \\resumeItem{...}                      (bullets)
  * \\textbf{Label}{: values}  \\\\           (Technical Skills rows)
  * \\resumeProjectHeading{...}{}          (project title lines)
and estimates each line's width in points using Computer Modern 10pt metrics
(the template's \\small size). Bold text is widened by 15%.

This is an ESTIMATE. The final authority is the real compile (Overleaf).
Calibrated against a known-good template: the widest accepted plain-text line
measured ~528pt, so the default cap is 525pt (safe).

Exit code 1 if any line is over the cap.
"""
import re
import sys

W = {' ': 3.333}
for c, w in zip('abcdefghijklmnopqrstuvwxyz',
                [5.0, 5.556, 4.444, 5.556, 4.444, 3.056, 5.0, 5.556, 2.778, 3.056, 5.278, 2.778, 8.333,
                 5.556, 5.0, 5.556, 5.278, 3.917, 3.944, 3.889, 5.556, 5.278, 7.222, 5.278, 5.278, 4.444]):
    W[c] = w
for c, w in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                [7.5, 7.083, 7.222, 7.639, 6.806, 6.528, 7.847, 7.5, 3.611, 5.139, 7.778, 6.25, 9.167,
                 7.5, 7.778, 6.806, 7.778, 7.361, 5.556, 7.222, 7.5, 7.5, 10.278, 7.5, 7.5, 6.111]):
    W[c] = w
for c in '0123456789':
    W[c] = 5.0
W.update({',': 2.778, '.': 2.778, ':': 2.778, ';': 2.778, '-': 3.333, '(': 3.889, ')': 3.889,
          '/': 5.0, '&': 7.778, '\u2013': 5.0, "'": 2.778, '|': 2.778, '+': 7.778, '#': 8.333,
          '%': 8.333, '_': 5.0, '@': 7.5, '"': 5.0, '!': 2.778, '?': 4.722})
BOLD = 1.15


def clean(s):
    s = s.replace('\\&', '&').replace('\\%', '%').replace('\\#', '#').replace('\\_', '_')
    s = s.replace('$|$', '|').replace('--', '\u2013').replace('~', ' ').replace('\\ ', ' ')
    return s


def width(s, bold=False):
    t = sum(W.get(ch, 5.0) for ch in s)
    return t * (BOLD if bold else 1.0)


def measure(tex):
    """tex fragment with optional \\textbf{..}; returns width in pt."""
    total, pos = 0.0, 0
    for m in re.finditer(r'\\textbf\{([^{}]*)\}', tex):
        total += width(clean(re.sub(r'\\(emph|textit)\{([^{}]*)\}', r'\2', tex[pos:m.start()])))
        total += width(clean(m.group(1)), bold=True)
        pos = m.end()
    rest = re.sub(r'\\(emph|textit)\{([^{}]*)\}', r'\2', tex[pos:])
    total += width(clean(rest))
    return total


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = sys.argv[1]
    cap = 525.0
    if '--cap' in sys.argv:
        cap = float(sys.argv[sys.argv.index('--cap') + 1])
    lines = open(path, encoding='utf8').read().splitlines()
    bad = 0
    n_items = n_rows = 0
    for i, ln in enumerate(lines, 1):
        s = ln.strip()
        if s.startswith('%'):
            continue
        kind = text = None
        m = re.match(r'\\resumeItem\{(.*)\}\s*(%.*)?$', s)
        if m:
            kind, text = 'bullet', m.group(1)
            n_items += 1
        else:
            m = re.match(r'(\\textbf\{[^{}]*\})\{(:.*)\}\s*(\\\\)?\s*$', s)
            if m:
                kind, text = 'skills', m.group(1) + m.group(2)
                n_rows += 1
            else:
                m = re.match(r'\{(\\textbf\{.*)\}\{\}\s*$', s)
                if m:
                    kind, text = 'heading', m.group(1)
        if not kind:
            continue
        w = measure(text)
        flag = 'OK'
        if w > cap:
            flag = 'TOO LONG (will wrap)'
            bad += 1
        elif w < cap * 0.80 and kind != 'heading':
            flag = 'short (wasted space; lengthen if page has room)'
        print(f'{w:6.0f}pt  L{i:<4d} {kind:<8s} {flag:<46s} {text[:60]}')
    print(f'\n{n_items} bullets, {n_rows} skills rows, cap {cap:.0f}pt, {bad} over the cap')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
