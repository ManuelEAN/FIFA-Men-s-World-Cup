import pandas as pd
import tkinter as tk
from tkinter import filedialog
#Selecting File1 & File2

root1 = tk.Tk()
root1.withdraw()
file_1 = filedialog.askopenfilename()
root2 = tk.Tk()
root2.withdraw()
file_2 = filedialog.askopenfilename()
#print(f"Selected file: {file_1}")
#print(f"Selected file: {file_2}")

#importing both files and join the different rows

df = pd.read_csv(file_1)
df_sec = pd.read_csv(file_2)

df['Combined'] = df['Y'].astype(str) + df['changeset_id'].astype(str)
df_sec['Combined'] = df_sec['Y'].astype(str) + df_sec['changeset_id'].astype(str)

#Check Mismatching rows to get values that changed

mask = ~df['Combined'].isin(df_sec['Combined'])
print(df[mask][['changeset_user', 'changeset_version']])
