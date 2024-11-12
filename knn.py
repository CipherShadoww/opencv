import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


df = pd.read_csv('IMDB Dataset.csv')


df = df.rename(columns={'review': 'text', 'sentiment': 'class'})


df['text'] = df['text'].str.replace('[^a-zA-Z]', ' ').str.lower()
df['text'] = df['text'].apply(lambda x: x.split())


X_train, X_test, y_train, y_test = train_test_split(df['text'], df['class'], test_size=0.002, random_state=42)


vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train.apply(lambda x: ' '.join(x)))
X_test = vectorizer.transform(X_test.apply(lambda x: ' '.join(x)))


clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = clf.score(X_test, y_test)
print('Accuracy:', accuracy)
print()



# Calculate precision and recall
report = classification_report(y_test, y_pred, target_names=['negative', 'positive'])
print(report)
