try:
    from word.models import Word
except ImportError:
    from data.models import Word

type1 = 'p'
type2 = 'r'

output_filename = "article_%s_%s.txt" % (type1, type2)

words1 = Word.objects.filter(prss__type=type1)
words2 = Word.objects.filter(prss__type=type2)

mixed = words1 & words2

pairs = [(word.prss.get(type=type1).key, word.prss.get(type=type2).key) for word in mixed]

plain = " ".join([" ".join(pair) for pair in pairs])

with open(output_filename, 'w') as infile:
    infile.write(plain)
