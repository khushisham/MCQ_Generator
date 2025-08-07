
import numpy as np
import pandas as pd
import spacy
import random
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

processed_data = spacy.load('en_core_web_sm')

def generated_mcq(text, num_questions):
    doc = processed_data(text)
    sentences = []

    for sent in doc.sents:
        (sent.text)
        sentences.append(sent.text)

    # num_questions = min(num_questions, len(sentences))
    sentences_selected = random.sample(sentences, num_questions)
    MCQ = []

    # Generating MCQ for each sentence
    for sentence in sentences_selected:
        sentence = sentence.lower()
        sentence_doc = processed_data(sentence)

        # Extract nouns from the sentence
        nouns = []
        for token in sentence_doc:
            if token.pos_ == "NOUN":
                nouns.append(token.text)

        if len(nouns) < 2:
            continue

        # Counting nouns
        count_noun = Counter(nouns)

        if count_noun:
            answer = count_noun.most_common(1)[0][0]
            answer_choices = [answer]

            # Generating the question by replacing the answer with a blank
            generated_question = sentence.replace(answer, "______")

            # Generating distractors
            distractors = random.sample(list(set(nouns) - set([answer])), min(3, len(nouns) - 1))
            answer_choices = [answer] + distractors
            random.shuffle(answer_choices)


            random.shuffle(answer_choices)

            # Getting the correct option
            correct_answer = chr(64 + answer_choices.index(answer) + 1)

            MCQ.append((generated_question, answer_choices, correct_answer))
            # print(MCQ)
    return MCQ

text="Urbanization also occurred as people moved from rural areas to cities in search of work. This rapid movement of people led to the growth of cities, but it also brought challenges such as overcrowding, pollution, and the spread of diseases. The working conditions in the factories were often harsh. Workers, including women and children, faced long hours, low pay, and dangerous environments. This eventually led to the rise of labor unions and movements advocating for workers' rights, seeking to improve wages, hours, and working conditions. In the realm of science and technology, the period saw significant advancements. Michael Faraday and James Clerk Maxwell made groundbreaking discoveries in electromagnetism, laying the groundwork for modern electrical engineering. Charles Darwin published his theory of evolution by natural selection, fundamentally changing the understanding of biological life. Louis Pasteur developed the germ theory of disease, leading to better hygiene practices and the development of vaccines. The Industrial Revolution also had a profound impact on agriculture. Innovations such as the seed drill invented by Jethro Tull, crop rotation, and selective breeding of livestock increased food production and supported a growing population.The revolution wasn't just technological; it had deep social and economic implications. Adam Smith's ideas on capitalism and free markets, detailed in his work \"The Wealth of Nations,\" gained prominence during this time. These ideas influenced economic policies that emphasized minimal government intervention in the economy, fostering competition and innovation."
output = generated_mcq(text, 5)
print("*******************************************ALL THE BEST******************************************************************")
for index, mcq in enumerate(output):
   generated_question, answer_choices, correct_answer = mcq
   print("Question", index + 1, ": ",(generated_question))
  # Add A, B, C, D labels to the answer choices
   labeled_choices = [f"[{chr(65+i)}] {choice}" for i, choice in enumerate(answer_choices)]

   # Print the choices, each on a new line
   print("Choices:")
   for choice in labeled_choices:
       print(choice)
   print("______________________________________________________________________________________________________________________")
   print("Correct Answer:",correct_answer)
   print("______________________________________________________________________________________________________________________")
print("****************************************************ALL THE BEST***********************************************************")

"""**Accuracy of Model**"""

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

predicted_answers = ['D', 'D', 'A', 'B', 'B']  # actual answer
correct_answers = ['D', 'A', 'A', 'B', 'B']    # correct answers from generated MCQs

# Generate confusion matrix
conf_matrix = confusion_matrix(correct_answers, predicted_answers, labels=['A', 'B', 'C', 'D'])

# Calculate accuracy, precision, recall, and F1 score
accuracy = accuracy_score(correct_answers, predicted_answers)
precision = precision_score(correct_answers, predicted_answers, average='macro')
recall = recall_score(correct_answers, predicted_answers, average='macro')
f1 = f1_score(correct_answers, predicted_answers, average='macro')

# Display the results
print("Confusion Matrix:\n", conf_matrix)
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")