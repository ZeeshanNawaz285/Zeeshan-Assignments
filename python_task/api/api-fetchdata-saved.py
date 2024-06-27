#The purpose of this code is to demonstrate how to: Fetch Data from a Public API:  Handle Errors Gracefully:  Save the Fetched Data to a File:
#In simple terms, this code retrieves data from an online API and saves it to a file named "output.js". It includes error handling to manage any issues that might occur during these processes.

import requests

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            file.write(str(data))
            
        print(f"Data saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while saving data to {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Specify the URL of the publicly available API
    api_url = "https://jsonplaceholder.typicode.com/posts"

    # Fetch data from the API
    api_data = fetch_data_from_api(api_url)
    
    # Save data to a text file
    if api_data:
        save_data_to_file(api_data, "output.js")
