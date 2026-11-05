import json, glob

merged = []
for f in sorted(glob.glob("chat_*.json")):
    with open(f, encoding="utf-8") as fh:
        merged.append({"file": f, "chat": json.load(fh)})

with open("chat.json", "w", encoding="utf-8") as out:
    json.dump(merged, out, indent=2, ensure_ascii=False)