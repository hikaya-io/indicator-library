# Code developed during SCT 18 hackathon
import re
import urllib.request

import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

res = "C:\\Users\\Don\\PycharmProjects\\Zalando_Hackathon\\Res\\"

# download if needed
# nltk.download('stopwords', res + "nltk")
# nltk.download('punkt', res + "nltk")

input_text = "I'm working on a WASH project in a refugee camp and we are improving hygiene practices and access to safe, clean water."
# input_text = "I'm working on a USG funded program in education and I would like to track students enrolled in courses"
# input_text = "I am looking for an output indicator that let's me track who is knowledgable about the gender practices"

stop_words = set(stopwords.words('english'))

word_tokens_input = word_tokenize(input_text.lower())
filtered_sentence_input = [w for w in word_tokens_input if w not in stop_words]

correlations = []

csv_data = pd.read_csv("indicator_new.csv")
# print(csv_data.columns)
for i in range(1, 2055):  # TODO:
# for i in range(460, 470):  # TODO:
    data = csv_data[csv_data["id"] == i]
    # print(i)
    indicator = ""
    if not pd.isna(csv_data["Indicator"].iloc[i]):
        indicator += csv_data["Indicator"].iloc[i]
    if not pd.isna(csv_data["Sector"].iloc[i]):
        indicator += csv_data["Sector"].iloc[i]
    if not pd.isna(csv_data["Definition"].iloc[i]):
        indicator += csv_data["Definition"].iloc[i]
    indicator = re.sub(r'[^0-9a-z ]+', '', indicator.lower())
    word_tokens_indicator = word_tokenize(indicator)
    filtered_sentence_indicator = [w for w in word_tokens_indicator if w not in stop_words]

    correlation = [(w, filtered_sentence_input.count(w)) for w in filtered_sentence_input if w in filtered_sentence_indicator]
    correlation = set(correlation)
    # print(correlation)
    score = 0
    for w, count in correlation:
        count *= filtered_sentence_indicator.count(w)
        score += count
    # score = len(correlation)  # Perhaps a better score?
    correlations.append({"id": i, "score": score})


print(correlations)
sorted_correlations = sorted(correlations, key=lambda x: x["score"], reverse=True)
print(sorted_correlations)
print(input_text)

for i in range(min(10, len(sorted_correlations))):
    id = sorted_correlations[i]["id"]
    print(i+1, "(%d)" % sorted_correlations[i]["score"], "-", csv_data["Indicator"].iloc[id])
