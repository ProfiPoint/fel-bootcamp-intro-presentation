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
    output_directory = sys.argv[1]
    os.makedirs(output_directory, exist_ok=True)

    for team in LECTURER_TEAMS:
        team.sort(key=lambda l: l["last"])
        output_file_name = f"{output_directory}/slides-{team[0]["last"].lower()}-{team[1]["last"].lower()}.pdf"
        lecturer_a_name = f"{team[0]["first"]} {team[0]["last"]}"
        lecturer_b_name = f"{team[1]["first"]} {team[1]["last"]}"
        subprocess.run(
            [
                "typst",
                "compile",
                "main.typ",
                "--input",
                f"lecturer_a={lecturer_a_name}",
                "--input",
                f"lecturer_b={lecturer_b_name}",
                output_file_name,
            ]
        )
