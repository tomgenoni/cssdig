import tinycss

parser = tinycss.make_parser()
stylesheet = parser.parse_stylesheet("body { background: red} ")

properties = []

for r in stylesheet.rules:
    for d in r.declarations:
        for tok in d.value:
            print d.name + ": " + tok.value + ";"
