

def alert_cout(df, num):
    for i in range(len(df)):
        if df['降雨量'][i] >= 4:
            df[f"Alert_{num}"][i] = 1
        else:
            df[f"Alert_{num}"][i] = 0  
        return df