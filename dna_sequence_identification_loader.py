import pickle

model_data = None
with open('dna_sequence_identification.pickle', 'rb') as f:
    model_data = pickle.load(f)

classifier = model_data['classifier']
label_encoder_promoter = model_data['label_encoder_promoter']
label_encoder_identification = model_data['label_encoder_identification']
vectorizer = model_data['vectorizer']

sequence = input("Enter DNA sequence: ")
sample_vectorized = vectorizer.transform([sequence])
predicted = classifier.predict(sample_vectorized)

predicted_promoter_label = label_encoder_promoter.inverse_transform(predicted[:, 0])
predicted_identification_label = label_encoder_identification.inverse_transform(predicted[:, 1])

print(f"Predicted Promoter: {predicted_promoter_label[0]}")
print(f"Predicted Identification: {predicted_identification_label[0]}")
