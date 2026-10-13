# LeetCode Solutions

A personal archive of my accepted LeetCode submissions. I keep the code alongside each problem statement so I can revisit the question, compare attempts, and review my approach later.

## Browse the solutions

Open the [leetcode](leetcode/) folder and choose a problem. Each problem has its own folder:

```text
leetcode/
└── maximum-nesting-depth-of-the-parentheses/
    ├── README.md      # Question, examples, constraints, and LeetCode link
    └── 2155568441.py  # Accepted submission; filename is its LeetCode submission ID
```

If I submit another accepted solution for the same problem, it gets a new file named with its submission ID. This keeps earlier attempts available for comparison.

## Supported submission languages

The sync extension currently accepts these LeetCode languages:

| Language | Recognized variants | Saved extension |
| --- | --- | --- |
| Python | Python, Python 2, Python 3, `py` | `.py` |
| Java | Java | `.java` |
| JavaScript | JavaScript, JavaScript (Node.js), Node.js, `js` | `.js` |
| SQL | MySQL, Microsoft SQL Server, Oracle, PostgreSQL, SQLite, generic SQL | `.sql` |

Other LeetCode languages are not currently synced.

## How this repository is updated

A local Chrome extension detects an accepted LeetCode submission and adds its source file and the problem's `README.md` to this repository through GitHub's Contents API. It is a Manifest V3 extension built with vanilla JavaScript, HTML, and CSS; it has no external server, application framework, database, package dependencies, or GitHub OAuth flow.

The problem README includes the original question text, examples, constraints, difficulty, and a link back to LeetCode. Existing solution files and problem READMEs are left in place, so later syncs do not overwrite accepted submissions or personal notes.

Problem statements are from [LeetCode](https://leetcode.com/); the solution code is my own.
