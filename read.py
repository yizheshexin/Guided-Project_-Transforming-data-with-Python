import pandas as pd
def load_data():
    data = pd.read_csv('hn_stories.csv',names = ['submission_time','upvotes','url','headline'])
    return data
    
if __name__ == "__main__":
   # This will call load_data if you run the script from the command line.
    data = load_data()
    print(data.head(5))