import pandas as pd


#  LOAD DATA

df = pd.read_csv("Uber-Jan-Feb-FOIL.csv")

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATA INFO =====")
print(df.info())

print("\n===== DATA SHAPE =====")
print(df.shape)



#  DATA CLEANING


# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Create new columns
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_name'] = df['date'].dt.day_name()



#  BASIC STATISTICS


print("\n===== TOTAL TRIPS =====")
print(df['trips'].sum())

print("\n===== AVERAGE TRIPS PER DAY =====")
print(df['trips'].mean())

print("\n===== MAX TRIPS IN A DAY =====")
print(df['trips'].max())

print("\n===== MIN TRIPS IN A DAY =====")
print(df['trips'].min())



#  MONTH-WISE ANALYSIS

print("\n===== TRIPS BY MONTH =====")
print(df.groupby('month')['trips'].sum())



#  DAILY ANALYSIS

print("\n===== DAILY TOTAL TRIPS =====")
print(df.groupby('date')['trips'].sum())



#  DAY NAME ANALYSIS

print("\n===== TRIPS BY DAY OF WEEK =====")
print(df.groupby('day_name')['trips'].sum())



# BASE-WISE ANALYSIS


print("\n===== TRIPS BY BASE =====")
base_trips = df.groupby('dispatching_base_number')['trips'].sum()
print(base_trips)

print("\n===== TOP 5 BUSIEST BASES =====")
print(base_trips.sort_values(ascending=False).head())


# ACTIVE VEHICLES ANALYSIS


print("\n===== ACTIVE VEHICLES STATS =====")
print(df['active_vehicles'].describe())



#  CORRELATION ANALYSIS

print("\n===== CORRELATION (Vehicles vs Trips) =====")
print(df[['active_vehicles', 'trips']].corr())



#  MOST BUSY DAY & BASE

busy_day = df.groupby('date')['trips'].sum().idxmax()
print("\nMOST BUSY DAY:", busy_day)

busy_base = base_trips.idxmax()
print("MOST BUSY BASE:", busy_base)



# FINAL SUMMARY

print("\n===== PROJECT SUMMARY =====")
print("Total Records:", len(df))
print("Total Trips:", df['trips'].sum())
print("Average Trips per Day:", round(df['trips'].mean(), 2))

days_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(df.groupby('day_name')['trips'].sum().reindex(days_order))
