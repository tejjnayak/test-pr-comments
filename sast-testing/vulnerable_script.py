import cPickle  # Importing the cPickle module
import sys

def deserialize(data):
    try:
        # Deserialize the data
        deserialized_data = cPickle.loads(data)
        print("Deserialization successful:", deserialized_data)
    except Exception as e:
        print("Error during deserialization:", e)

if __name__ == "__main__":
    # Simulating untrusted data from an untrusted source (e.g., a web request)
    user_input = sys.argv[1]

    # In a real-world scenario, this data should be sanitized and validated
    try:
        # Attempt to deserialize the input data
        deserialize(user_input)
    except Exception as e:
        print("Failed to deserialize data:", e)

