from smolagents import tool
import pandas as pd

#tool do smolagents que através de um tema, gera top 10 quotes
@tool
def generate_10_quotes(subject: str) -> pd.DataFrame:
    """A tool that fetches the top 10 quotes in the dataframe that are related to the subject.
    Args:
        subject: Item that will filter the dataframe).
    """
    try:
        df=pd.read_csv("./quotes.csv")
        df_filtered=df[df['category'].str.contains(subject, na=False)].head(10)
        return df_filtered
    except:
        return f"Error fetching quotes  for timezone '{subject}'"

