import html
import subprocess
import os
import sys
from typing import TypedDict


class Lecturer(TypedDict):
    first: str
    last: str


LECTURER_TEAMS: list[list[Lecturer]] = [
    [
        {"first": "Alice", "last": "Dvořáková"},
        {"first": "Bob", "last": "Novák"},
    ],
    [
        {"first": "Dominik", "last": "Eichenberger"},
        {"first": "Richard", "last": "Weber"},
        {"first": "Ondřej", "last": "Vašatko"},
    ],
    [
        {"first": "Oleksandr", "last": "Bobrov"},
        {"first": "Kateryna", "last": "Padusenko"},
    ],
    [
        {"first": "Michal", "last": "Matiáš"},
        {"first": "Tomáš", "last": "Dudáček"},
    ],
    [
        {"first": "Šimon", "last": "Brandner"},
        {"first": "Ondřej", "last": "Čopák"},
    ],
]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <output_directory>")
        sys.exit(1)

    output_directory = sys.argv[1]
    os.makedirs(output_directory, exist_ok=True)

    presentations = []

    for team in LECTURER_TEAMS:
        team.sort(key=lambda l: l["last"])
        pdf_name = f"slides-{'-'.join(l['last'].lower() for l in team)}.pdf"
        output_file_name = os.path.join(output_directory, pdf_name)
        lecturer_a_name = f"{team[0]['first']} {team[0]['last']}"
        lecturer_b_name = f"{team[1]['first']} {team[1]['last']}"

        cmd = [
            "typst",
            "compile",
            "main.typ",
            "--input",
            f"lecturer_a={lecturer_a_name}",
            "--input",
            f"lecturer_b={lecturer_b_name}",
        ]
        if len(team) > 2:
            lecturer_c_name = f"{team[2]['first']} {team[2]['last']}"
            cmd.extend([
                "--input",
                f"lecturer_c={lecturer_c_name}",
            ])
        cmd.append(output_file_name)

        subprocess.run(cmd, check=True)

        names = ", ".join(f"{l['first']} {l['last']}" for l in team)
        presentations.append(
            {
                "title": f"Presentation ({names}).pdf",
                "file": pdf_name,
            }
        )

    html_content = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        '    <meta charset="utf-8">',
        "    <title>Bootcamp Intro Presentations</title>",
        "</head>",
        "<body>",
        "    <h1>Bootcamp Intro Presentations</h1>",
        "    <ul>",
    ]
    for pres in presentations:
        html_content.append(
            f'        <li><a href="{html.escape(pres["file"])}">{html.escape(pres["title"])}</a></li>'
        )
    html_content.extend(
        [
            "    </ul>",
            f'    <a href="{html.escape("https://github.com/ProfiPoint/fel-programming-bootcamp-intro-presentation")}">{html.escape("Edit Source Code Here (GitHub)")}</a>',
            "</body>",
            "</html>",
            "",
        ]
    )

    with open(os.path.join(output_directory, "index.html"), "w", encoding="utf-8") as f:
        f.write("\n".join(html_content))
