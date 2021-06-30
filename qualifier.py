from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    r = list(map(list, rows))

    if centered:
        padding = str.center
    else:
        padding = str.ljust
    
    columns = len(r[0])

    if labels:
        r.insert(0, labels.copy())
    table = ["" for i in range(len(r)+2)]
    table[0] = "┌"
    table[-1] = "└"

    for i in range(len(r)):
        for j in range(columns):
            r[i][j] = str(r[i][j])

    # generating top/bottom line
    max_lens = [0 for i in range(columns)]
    for i in range(columns):
        max_len = 0
        for row in r:
            max_len = max(len(row[i]), max_len)
        max_len += 2
        max_lens[i] = max_len
        table[0] += "─"*max_len + "┬"
        table[-1] += "─"*max_len + "┴"
    table[0] = table[0][:-1] + "┐"
    table[-1] = table[-1][:-1] + "┘"

    # generating text
    for i in range(len(r)):
        table[i+1] = "│"
        for j in range(columns):
            table[i+1] += " " + padding(r[i][j], max_lens[j]-2) + " │"
        
    # generating label line
    if labels:
        line = "├"
        for max_len in max_lens:
            line += "─"*max_len + "┼"
        line = line[:-1] + "┤"
        table.insert(2, line)

    final_table = ""
    for row in table:
        final_table += row + "\n"
    return final_table[:-1]



rows = [
    ["Lemon", 18_3285, "Owner"],
    ["Sebastiaan", 18_3285.1, "Owner"],
    ["KutieKatj", 15_000, "Admin"],
    ["Jake", "MoreThanU", "Helper"],
    ["Joe", -12, "Idk Tbh"]
]
labels = ["User", "Messages", "Role"]
correct = """
┌────────────┬───────────┬─────────┐
│    User    │  Messages │   Role  │
├────────────┼───────────┼─────────┤
│   Lemon    │   183285  │  Owner  │
│ Sebastiaan │  183285.1 │  Owner  │
│ KutieKatj  │   15000   │  Admin  │
│    Jake    │ MoreThanU │  Helper │
│    Joe     │    -12    │ Idk Tbh │
└────────────┴───────────┴─────────┘
""".strip()
assert make_table(rows, labels, centered=True) == correct