import pickle

# Create a sample dictionary
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Serialize the dictionary using pickle
serialized_data = pickle.dumps(data)

# Print the serialized data
print("Serialized Data:", serialized_data)

# Deserialize the data back into a Python object
deserialized_data = pickle.loads(serialized_data)

# Print the deserialized data
print("Deserialized Data:", deserialized_data)
