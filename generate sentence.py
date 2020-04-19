
def generate_sentences(subjects,verbs,objects):
    #start writing your code here
    sentence_list=[]
    for i in subjects:
        for j in verbs:
            for k in objects:
                sentence_list.append(i+" "+j+" "+k)
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))
