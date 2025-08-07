# MCQ Generator using Natural Language Processing

This project is an automatic Multiple Choice Question (MCQ) generator built using Natural Language Processing (NLP). It generates MCQs from a given paragraph of text by identifying important nouns, masking them in context, and producing distractor choices from nearby words.

---

## Project Highlights

- Automatically generates multiple-choice questions from any input paragraph.
- Uses NLP techniques to extract key nouns and construct fill-in-the-blank style questions.
- Randomly selects sentences and creates relevant distractors for each question.
- Evaluates MCQ quality and prediction accuracy using classification metrics.
- Demonstrates the use of spaCy, NLTK, and Scikit-learn for NLP and evaluation.

---

## Tech Stack

- **Language:** Python
- **Libraries:** spaCy, NLTK, sklearn, pandas, numpy
- **Techniques:** POS tagging, tokenization, random sampling, MCQ generation, model evaluation

---

## How It Works

1. Load and process the input text using spaCy's language model.
2. Split the text into sentences and select a subset randomly.
3. For each sentence, identify the most frequent noun to mask.
4. Replace the noun with a blank and create distractor options from other nouns in the sentence.
5. Return a structured MCQ with options and the correct answer.
6. Optionally, evaluate the accuracy of predicted answers using sklearn metrics like accuracy, precision, recall, and F1 score.

