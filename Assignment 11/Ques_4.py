import pandas as pd

def calculate_days_til_party(df):
    party_days = (df['John'] & df['Judy']).astype(int)
    days_until = []
    
    for i in range(len(df)):
        if party_days[i] == 1:
            days_until.append(0)
        else:
            future_parties = [j - i for j in range(i + 1, len(df)) if party_days[j] == 1]
            days_until.append(min(future_parties) if future_parties else None)
    
    df['days_til_party'] = days_until
    return df

# Taking user input
days = []
for i in range(10):
    john = input(f"Is John visiting on day {i+1}? (yes/no): ").strip().lower() == 'yes'
    judy = input(f"Is Judy visiting on day {i+1}? (yes/no): ").strip().lower() == 'yes'
    days.append({'John': john, 'Judy': judy})

df = pd.DataFrame(days)
df = calculate_days_til_party(df)
print(df)
