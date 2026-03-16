Tokenization:

Prefereence is for the sub word tokenization and modern transformer model used them  here is the reason

- word level tokenizer have fixed vocab and when new or rare works pop ins it gives [UNK]  but sub word break them into workds like 
tokeinzation, tokenizing , tokenized, into token then ##zation, or ##zing or ##ed.

- Character level well it is good but  increasing computational cost and training time.

