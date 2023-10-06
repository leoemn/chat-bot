import os
import pandas as pd

def clean_data(file_path):
    conversations = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            user_message, bot_response = line.strip().split('\t')
            conversations.append({'user_message': user_message, 'bot_response': bot_response})

    df = pd.DataFrame(conversations)

    # Get the directory of the raw data file
    directory = os.path.dirname(file_path)

    # Create the path for the cleaned data
    cleaned_data_path = os.path.join(directory, 'cleaned_data.csv')

    # Save the cleaned data
    df.to_csv(cleaned_data_path, index=False)

    return df

if __name__ == '__main__':
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)  # move one directory up to the root folder
    file_path = os.path.join(root_dir, 'data', 'data.txt')
    clean_data(file_path)
