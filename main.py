import os

TEXT = (
    "I'm sorry I labelled your sourdough starter 'yogurt - do not use' and left it in the fridge, so you threw away the starter you had kept alive for three years.\n"
    "I learned that a confident label from me can turn a guess into someone else's mistake, so I will mark anything I have not verified as 'unsure' and ask before I rename what is yours."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
