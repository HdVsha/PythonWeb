import json
with open("1.json", 'r') as file:
    # load is a decoder that allows to load json files into smth in python
    info = json.load(file)
    print(json.dumps(info, indent=4, sort_keys=True))
    tmp = info["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]
    tmp["week"] = 3
# --- implementation through json.dump()
# with open("1.json", "w") as file:
#     json.dump(data, file, indent=4)
with open("1.json", "w") as tmpfile:
    tmpfile.write(json.dumps(info, indent=4))
