# NLTK

Not used in the modern NLP problems:
reason:
NOt trainable as it use the pre-trained fix model (punkt)tokenizer based on the penn Treebank corups so we cant update it with the new words.

so the new vocab or rare owrd is tkenizaed as [UNK] 

we used it only for the tesching , prototyping or rule-based task.

not used in deep learning models like bert or gpt due to lack of sub weord handeling and fixed behabiors

