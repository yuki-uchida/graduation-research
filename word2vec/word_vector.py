from gensim.models import word2vec

model = word2vec.Word2Vec.load("wiki.model")
print(model)
out = model.most_similar(positive=[u"東京", u"ドイツ"], negative=[u"日本"])
for x in out:
  print(x[0])

