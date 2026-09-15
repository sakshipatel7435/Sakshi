## Task 1
**Three Recent Instagram Captions:**
1. "Chasing sunsets and good vibes!"
2. "Good food, better mood. 🍔"
3. "Living my best life!"

1. "Chasing sunsets and coffee in Goa! ☕️🌅"
2. "Coffee, sunsets, and endless laughter with the best crew."
3. "Goa dumps: good food, better sunsets, and pure peace."

**Manual Vocabulary List (ignoring case & punctuation):**
['chasing', 'sunsets', 'and', 'good', 'vibes', 'food', 'better', 'mood', 'living', 'my', 'best', 'life']

---

## Task 5
**Key Differences between Bag of Words (BoW) and TF-IDF:**
1. **Word Weighting vs. Counting:** BoW merely counts the frequency of words (meaning common words like "the" get huge scores), whereas TF-IDF penalizes highly frequent filler words and boosts the weight of rare, contextually important words.
2. **Semantic Understanding:** BoW assumes every word is equally important regardless of its meaning, while TF-IDF understands that a rare word uniquely identifies the core topic of a document.

**Real-World Example:**
If YouTube is trying to recommend a video based on text tags, TF-IDF is far more useful than BoW. If a creator's description says "How to edit a video tutorial" and uses the word "video" 10 times, BoW would think the video is primarily about "video". But because *every* YouTube description contains the word "video", TF-IDF suppresses the weight of "video" and highly boosts "tutorial" or "edit", allowing the recommendation algorithm to accurately categorize the clip.