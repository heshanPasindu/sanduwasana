# Load the CSV file into a DataFrame
data = pd.read_csv('/content/death-rate-smoking new.csv')

# Filter the DataFrame to include only records related to Sri Lanka
sri_lanka_data = data[data['Entity'] == 'Sri Lanka']


# Display the filtered DataFrame
print(sri_lanka_data.head())

# Filter the DataFrame to include only records related to Sri Lanka
sri_lanka_data = data[data['Entity'] == 'Sri Lanka

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Model evaluation
train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
