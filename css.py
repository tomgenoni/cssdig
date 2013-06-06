import tinycss

parser = tinycss.make_parser()
stylesheet = parser.parse_stylesheet("body { background: red} ")

print stylesheet
