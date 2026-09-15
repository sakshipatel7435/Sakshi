## Task 2
**Limitation of Traditional NLP Models (BoW / TF-IDF):**
One major limitation of traditional models like Bag of Words or TF-IDF is that they completely ignore word order and contextual meaning. For example, if a WhatsApp message says "The food was not good, it was bad" versus "The food was not bad, it was good", a Bag of Words model sees the exact same word counts for both sentences and cannot tell the difference between a compliment and a complaint!

---

## Task 4
**Popular Transformer Model:** RoBERTa (Robustly Optimized BERT Pretraining Approach)
**Difference from BERT:** 
RoBERTa is heavily based on BERT's architecture, but it modifies key hyperparameters by training with much larger mini-batches and removing BERT's "Next Sentence Prediction" (NSP) objective. Additionally, it trains on a vastly larger dataset for a longer period of time, which allows it to consistently outperform standard BERT on most text classification benchmarks.