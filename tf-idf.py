# import necessary libraries
import pandas as pd
import math
from scipy import spatial

all_doc = [["Computer Networks", "Multimedia", "Database"],
           ["Computer Networks", "Multimedia", "OS"],
           ["Dataware Housing", "Datamining", "Database"],
           ]
wordDict = []
total = []

query = ["Computer Networks", "Computer Networks", "Database"]

for doc in all_doc:
    for word in doc:
        # join them to remove common duplicate words
        total.append(word)
total = set(total)

for i, doc in enumerate(all_doc, start=0):
    temp_dict = dict.fromkeys(total, 0)
    for word in doc:
        temp_dict[word] += 1
    wordDict.append(temp_dict)


# put them in a dataframe and then view the result:
pd.DataFrame(wordDict)


# Now writing the TF function:
def computeTF(wordDict, bow, index):
    print(f"Computing TF for Document-{index}")
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        print(f"TF for {word} = {count}/{float(bowCount)}", end=" ")
        tfDict[word] = count/float(bowCount)
        print(f" = {tfDict[word]}")
    return tfDict


tf = []
for i, doc in enumerate(all_doc, start=0):
    # running our sentences through the tf function:
    tf.append(computeTF(wordDict[i], doc, i))


# creating the log portion of the Excel table we saw earlier
def computeIDF(docList):
    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        print(f"IDF for {word} = log2({N}/{val})", end=" ")
        idfDict[word] = math.log2(N / float(val))
        print(f"= {idfDict[word]}")

    return idfDict


# inputing our sentences in the log file
idfs = computeIDF(wordDict)
print(idfs)


# The actual calculation of TF*IDF from the table above:
def computeTFIDF(tfBow, idfs, index):
    tfidf = {}
    print(f"Calculating TF-IDF for Document-{index}")
    for word, val in tfBow.items():
        print(f"TF-IDF for {word} = {val} * {idfs[word]})", end=" ")
        tfidf[word] = val * idfs[word]
        print(f" = {tfidf[word]}")
    return tfidf


# running our two sentences through the IDF:
idf = []
for i in range(0, len(all_doc)):
    idf.append(computeTFIDF(tf[i], idfs, i))

# Computing TF-ID for query
wordDictQ = dict.fromkeys(total, 0)
for word in query:
    wordDictQ[word] += 1

tfquery = computeTF(wordDictQ, query, "query")
query_idf = computeTFIDF(tfquery, idfs, "query")

# Test similarity with query document
def computeSimimalaity(vector1, vector2, index):
    distance = 1 - spatial.distance.cosine(list(vector1.values()), list(vector2.values()))
    print(f"Cosine Similarity for Document-{index} and Query = {distance}")


for i in range(0, len(all_doc)):
    computeSimimalaity(idf[i], query_idf, i)
