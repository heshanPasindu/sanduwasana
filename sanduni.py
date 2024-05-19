# Load the CSV file into a DataFrame
data = pd.read_csv('/content/death-rate-smoking new.csv')

# Filter the DataFrame to include only records related to Sri Lanka
sri_lanka_data = data[data['Entity'] == 'Sri Lanka']


# Display the filtered DataFrame
print(sri_lanka_data.head())

# Filter the DataFrame to include only records related to Sri Lanka
sri_lanka_data = data[data['Entity'] == 'Sri Lanka

# Predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
