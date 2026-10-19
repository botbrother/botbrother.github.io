import json

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)
  
data = [s for s in data if s["section_title"] != "Featured"]

for s in data:
    s["categories"] = [c for c in s["categories"] if c["category"] not in ("Animal", "Animals")]

colourful = next(s for s in data if s["section_title"] == "Colourful")
allcol = next(s for s in data if s["section_title"] == "All Collections")
nature = next(c for c in allcol["categories"] if c["category"] == "Nature")
allcol["categories"] = [c for c in allcol["categories"] if c["category"] != "Nature"]
colourful["categories"].append(nature)

with open("data_new.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
