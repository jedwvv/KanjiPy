import json
import cutlet

with open("databases/N1_1_100.json", "r", encoding="utf8") as f:
    data = json.load(f)

katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False

new_data = {}
for u, v in data.items():
    new_data[u] = tuple([v, katsu.romaji(v).lower().replace(" ", "")])

with open("databases/N1_1_100_v2.json", "w", encoding="utf8") as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)    