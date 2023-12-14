from pathlib import Path
from random import shuffle

_people = [
    "Audrey",
    "Shane",
    "Kayla",
    "Jane",
    "Lindsay",
    "Cole",
    "Harriet",
    "Rowan",
    "Jerome",
    "Olivia",
]
_output_dir = Path("outputs")
_output_dir.mkdir(exist_ok=True, parents=True)


def main():
    shuffle(_people)
    pairs = [
        (santa, recipient)
        for santa, recipient in zip(
            [_people[-1]] + _people[:-1],
            _people,
        )
    ]
    with open("template.txt", "r") as f:
        template = f.read()

    for santa, recipient in pairs:
        with open(_output_dir / f"{santa}.txt", "w") as f:
            f.write(
                template.format(
                    santa=santa.capitalize(), recipient=recipient.capitalize()
                )
            )


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
