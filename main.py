from pathlib import Path

ROAST = "It's 1 a.m., I'm standing here in my socks, and the fridge just told me the kitchen is closed for maintenance. It has exactly one job, and somehow also a curfew."


def main():
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
