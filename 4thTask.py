import json
with open("1.json", 'r') as file:
    # load is a decoder that allows to load json files into smth in python
    info = json.load(file)
    print(json.dumps(info, indent=4, sort_keys=True))
    tmp = info["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]
    tmp["week"] = 3
with open("1.json", "w") as tmpfile:
    tmpfile.write(json.dumps(info, indent=4))
