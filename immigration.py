import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import os

# url --> https://www.stats.govt.nz/information-releases/international-migration-may-2026/

data="dataset/international-migration-may-2026-citizenship-by-visa-by-country-of-last-permanent-residence.csv"
OUTPUT="plot_of_analysis"
os.makedirs(OUTPUT, exist_ok=True)

# LOAD DATA
# -----------------------------

def load_data(data):
    df=pd.read_csv(data)
    return df

def inspect_data(df):
    print("\n--- HEAD ---")
    print(df.head(10))

    print("\n--- TAIL ---")
    print(df.tail(10))

    print("\n--- DESCRIBE ---")
    print(df.describe())

    print("\n--- INFO ---")
    print(df.info())
    """
     #   Column                Non-Null Count   Dtype
---  ------                --------------   -----
 0   year_month            366535 non-null  str  
 1   month_of_release      366535 non-null  str  
 2   passenger_type        366535 non-null  str  
 3   direction             366535 non-null  str  
 4   citizenship           366535 non-null  str  
 5   visa                  366535 non-null  str  
 6   country_of_residence  366535 non-null  str  
 7   estimate              366535 non-null  int64
 8   standard_error        366535 non-null  int64
 9   status                366535 non-null  str  
 """

    print("\n--- COLUMNS ---")
    print(df.columns)

    print("\n--- CORR ---")
    print(df.corr(numeric_only=True))

    print("\n--- ISNULL ---")
    print(df.isnull().sum()) # no null entries

    print("\n--- DUPLICATED ---")
    print(df.duplicated().sum()) # 0

    print("\n--- STANDART ERROR VALUE COUNTS ---")
    print(df["standard_error"].value_counts())
    """
    --- STANDART ERROR VALUE COUNTS ---
    standard_error
    0      352353
    1        7366
    2        2417
    3        1135
    4         661
        ...  """


    print("\n---  PASSANGER TYPE VALUE COUNTS ---")
    print(df["passenger_type"].value_counts())
    """
    ---  PASSANGER TYPE VALUE COUNTS ---
    passenger_type
    Long-term migrant    366535"""

    print("\n---  DIRECTION VALUE COUNTS ---")
    print(df["direction"].value_counts())
    """
    ---  DIRECTION VALUE COUNTS ---
    direction
    Arrivals    366535
    """

# CLEAN DATA
# -----------------------------

def clean_data(df):
    df=df[df["standard_error"]==0]
    df.drop(columns=["standard_error","month_of_release","passenger_type","direction"],inplace=True)
    df=df[df["estimate"]!=0]

    return df

# CITIZENSHIP ANALYSIS 
# -----------------------------

def analysis_citizenship(df):

    citizen=df["citizenship"].value_counts()
    sb.barplot(x=citizen.index,y=citizen.values)
    plt.title("Number of Migrants by Citizenships")
    plt.xlabel("Citizenships")
    plt.ylabel("Number of Migrants")
    plt.tight_layout()
    plt.grid(axis="y")
    plt.savefig(f"{OUTPUT}/analysis_citizenship.png")
    plt.show()

# VISA ANALYSIS 
# -----------------------------

def analysis_visa(df):

    visa=df["visa"].value_counts()
    plt.figure(figsize=(8,7))
    sb.barplot(x=visa.index,y=visa.values)
    plt.title("Number of Migrants by Visa")
    plt.xticks(rotation=45,ha="right")
    plt.xlabel("Visa")
    plt.ylabel("Number of Migrants")
    plt.tight_layout()
    plt.grid(axis="y")
    plt.savefig(f"{OUTPUT}/analysis_visa.png")
    plt.show()

# COUNTRY OF RESIDENCE ANALYSIS 
# -----------------------------

def analysis_country_of_residence_top40(df):

    country_of_residence=df["country_of_residence"].value_counts().sort_values(ascending=False).head(40)
    plt.figure(figsize=(10,7))
    sb.barplot(y=country_of_residence.index,x=country_of_residence.values)
    plt.title("Top 40 Immigrant Numbers by Country of Residence")
    plt.xlabel("Number of Migrants")
    plt.ylabel("Country of Residence")
    plt.tight_layout()
    plt.grid()
    plt.savefig(f"{OUTPUT}/analysis_country_of_residence_top40.png")
    plt.show()

# ESTIMATE ANALYSIS 
# -----------------------------

def analysis_estimate_max30(df):

    estimate=df["estimate"].value_counts().sort_index(ascending=True).head(30)
    plt.figure(figsize=(20,7))
    sb.barplot(x=estimate.index,y=estimate.values)
    plt.title("Number of Migrants by Estimate (MAX 30)")
    plt.xlabel("Estimate")
    plt.ylabel("Number of Migrants")
    plt.tight_layout()
    plt.grid()
    plt.savefig(f"{OUTPUT}/analysis_estimate_max30.png")
    plt.show()

# STATUS ANALYSIS 
# -----------------------------

def analysis_status(df):

    status=df["status"].value_counts()
    sb.barplot(x=status.index,y=status.values)
    plt.title("Number of Migrants by Status")
    plt.xlabel("Status")
    plt.ylabel("Number of Migrants")
    plt.tight_layout()
    plt.grid()
    plt.savefig(f"{OUTPUT}/analysis_status.png")
    plt.show()

# TIME ANALYSIS 
# -----------------------------

def analysis_time(df):

    year_month=df["year_month"].value_counts().sort_index().tail(60)
    plt.figure(figsize=(15,6))
    sb.lineplot(x=year_month.index,y=year_month.values)
    plt.title("The Number of Immigrants Who Arrived In The Last 5 Years")
    plt.xticks(rotation=45,ha="right")
    plt.xlabel("Time")
    plt.ylabel("Number of Migrants")
    plt.tight_layout()
    plt.grid()
    plt.savefig(f"{OUTPUT}/analysis_time.png")
    plt.show()

# COMPREHENSIVE ANALYSIS
# -----------------------------

def Migrants_with_Provisional_Status_In_The_Highest_Numbers(df):

    df_f=df[df["status"]=="Provisional"]
    provisional=df_f["country_of_residence"].value_counts().sort_values(ascending=False).head(30)
    plt.figure(figsize=(15,6))
    sb.barplot(y=provisional.index,x=provisional.values)
    plt.title("The Nationalities of Migrants with 'Provisional' Status In The Highest Numbers")
    plt.xlabel("Number of Migrants")
    plt.ylabel("Country of Residence")
    plt.tight_layout()
    plt.grid()
    plt.savefig(f"{OUTPUT}/Migrants_with_Provisional_Status_In_The_Highest_Numbers.png")
    plt.show()

# COMPREHENSIVE ANALYSIS
# -----------------------------

def The_Citizenship_Most_Frequently_Held_by_Immigrants_With_Dual_Citizenship(df):

    df_f=df[df["citizenship"]=="TOTAL"]
    total=df_f["country_of_residence"].value_counts().sort_values(ascending=False).head(40)
    plt.figure(figsize=(15,6))
    sb.barplot(y=total.index,x=total.values)
    plt.title("The Citizenship Most Frequently Held by Immigrants With Dual Citizenship (excluding New Zealand)")
    plt.xlabel("Country of Residence")
    plt.ylabel("Number of Migrants")
    plt.tight_layout()
    plt.grid()
    plt.savefig(f"{OUTPUT}/The_Citizenship_Most_Frequently_Held_by_Immigrants_With_Dual_Citizenship.png")
    plt.show()

# COMPREHENSIVE ANALYSIS
# -----------------------------

def The_Most_Common_Citizenship_Held_by_Immigrants_Arriving_on_Student_Visas(df):

    df_f=df[df["visa"]=="Student"]
    total=df_f["country_of_residence"].value_counts().sort_values(ascending=False).head(40)
    plt.figure(figsize=(15,6))
    sb.barplot(y=total.index,x=total.values)
    plt.title("The Most Common Citizenship Held by Immigrants Arriving on Student Visas")
    plt.xlabel("Number of Migrants")
    plt.ylabel("Country of Residence")
    plt.tight_layout()
    plt.grid()
    plt.savefig(f"{OUTPUT}/The_Most_Common_Citizenship_Held_by_Immigrants_Arriving_on_Student_Visas.png")
    plt.show()    

# MAIN PIPELINE
# -----------------------------

def main():
    df=load_data(data)
    inspect_data(df)
    df=clean_data(df)

    analysis_citizenship(df)
    analysis_visa(df)
    analysis_country_of_residence_top40(df)
    analysis_estimate_max30(df)
    analysis_status(df)
    analysis_time(df)
    Migrants_with_Provisional_Status_In_The_Highest_Numbers(df)
    The_Citizenship_Most_Frequently_Held_by_Immigrants_With_Dual_Citizenship(df)
    The_Most_Common_Citizenship_Held_by_Immigrants_Arriving_on_Student_Visas(df)

# RUN
# -----------------------------

if __name__=="__main__":
    main()