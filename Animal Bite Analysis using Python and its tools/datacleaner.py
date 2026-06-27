import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1. Loading the csv file
raw_df=pd.read_csv("Health_AnimalBites.csv")
df=pd.read_csv("Health_AnimalBites.csv")

print("STARTING THE DATA ANALYSIS AYY!!!")

#2. Cleaning the data ( Zip code logic )
# Making sure all zip codes are clean text
df['victim_zip'] = df['victim_zip'].astype(str).str.strip()
df['victim_zip'] = df['victim_zip'].replace(['nan', 'NAN', ''], 'UNKNOWN')

#Fix casing so that words match up like 'Dog' and 'DOG'
df['SpeciesIDDesc'] = df['SpeciesIDDesc'].astype(str).str.upper().str.strip().replace(['NAN', 'nan', ''], 'UNKNOWN')

#3. Visualization
#Setup the visual style for Seaborn
sns.set_theme(style = 'whitegrid')

#Chart 1 : Top Biting Species (Seaborn Bar Chart)
print("Generating Chart 1 : Top Species... ")
plt.figure(figsize = (8, 5))

#Garb the top 7 animal species with the most incidents
top_species = df['SpeciesIDDesc'].value_counts().head(7)

#Build a clean horizontal bar chart
sns.barplot(x=top_species.values, y=top_species.index, hue=top_species.index, palette='Blues_r', legend=False)
plt.title('Top 7 Animal Species involved in Bite Incidents', fontsize=20, fontweight='bold')
plt.xlabel("Number of Reported Bites", fontsize=11)
plt.ylabel("Species", fontsize=11)

plt.tight_layout()
#Ask the user if they want the graph saved
if input("Want to download the image?(Y/N)").upper() == 'Y':
    plt.savefig('Top_biting_species.png', dpi=300)
    print("💾 Image successfully saved as 'Top_biting_species.png'!")
plt.show() #Shows the output

plt.close()

print("Half way done.")
