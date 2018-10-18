from gensim.models import word2vec

model = word2vec.Word2Vec.load("wiki.model")
print(model['りんご'])

#なんで200~300次元？？？
