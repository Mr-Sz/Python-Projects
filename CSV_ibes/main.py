import os
import pandas as pd
from textblob import TextBlob
from datetime import datetime

class SentimentAnalyzer:
    def __init__(self, csv_file_path, col_to_analyze):
        self.csv_file_path = os.path.join("user_reviews", csv_file_path)
        self.col_to_analyze = col_to_analyze

    def load_csv(self):
        try:
            return pd.read_csv(self.csv_file_path)
        except FileNotFoundError:
            print(f"Error: File '{self.csv_file_path}' not found.")
            return None

    def perform_sentiment_analysis(self, dataframe):
        return [TextBlob(row[self.col_to_analyze]).sentiment.polarity for _, row in dataframe.iterrows()]

    def save_as_csv(self, dataframe):
        output_folder = "results"
        os.makedirs(output_folder, exist_ok=True)

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        output_file = os.path.join(output_folder, f"output_{timestamp}.csv")
        dataframe.to_csv(output_file, index=False)
        print(f"Sentiment analysis complete. Results saved to '{output_file}'.")

def main():
    csv_fpath = 'fake_generated_reviews_oct_dec_2023.csv'
    col_to_analyze = 'feedback'

    sentiment_analyzer = SentimentAnalyzer(csv_fpath, col_to_analyze)
    data = sentiment_analyzer.load_csv()

    if data is not None:
        sentiments = sentiment_analyzer.perform_sentiment_analysis(data)
        data['sentiment'] = sentiments
        sentiment_analyzer.save_as_csv(data)

if __name__ == "__main__":
    main()
