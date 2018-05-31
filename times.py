from dateutil.parser import parse
import read
def extract_time(time):
    return parse(time).hour

data3 = read.load_data()
data3['hour'] = data3['submission_time'].apply(extract_time)
most_hour = data3['hour'].value_counts()
print(most_hour)