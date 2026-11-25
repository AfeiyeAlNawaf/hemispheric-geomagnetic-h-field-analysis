#importing necessary libray to be used to plot graph of diurnal variation for HSA for data of 2011
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import winsound

#creating a dataframe that will be storing the datas read from an Excel sheet

#DAV dataframe
try:
    dav_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_DAV_Data_2011.xlsx")
    #dav_df.fillna(0, inplace=True)
    print("DAV excel opened successfully")
except Exception as e:
    print(f"Error: {e}")

#MUT dataframe
#try:
#    mut_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_MUT_Data_2011.xlsx")
#    mut_df.fillna(0, inplace=True)
#    print("MUT excel opened successfully")
#except Exception as e:
#    print(f"Error: {e}")

#YAP dataframe
try:
    yap_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_YAP_Data_2011.xlsx")
    #yap_df.fillna(0, inplace=True)
    print("YAP excel opened successfully")
except Exception as e:
    print(f"Error: {e}")

#testing area


#creating an array that contain name of the months
month_name = []

for key in dav_df.keys():
    month_name.append(key)

new_month_name = np.array(month_name)

#creating an array of time in hrs from 00hrs - 23hrs which make 24hrs in a day
time_hr = list(range(24))
new_time_hr = np.array(time_hr)

#creating x ticks and y ticks for the graph
x_label = []

for num in time_hr:
    if num % 2 == 0:
        x_label.append(num)

nx_label = np.array(x_label)

y_label = list(range(-20, 170, 20))
ny_label = np.array(y_label)

#plotting diurnal variation of data 2009 for LSA
num = 1
for item in new_month_name:
    plt.plot(new_time_hr, dav_df[f"{item}"], label='DAV', c='royalblue', marker='o', mfc='white', mec='royalblue',
             ms=7, lw=3, ls='-')
#    plt.plot(new_time_hr, mut_df[f"{item}"], label='MUT', c='crimson', marker='s', mfc='white', mec='crimson', ms=7,
#             lw=2, ls='--')
    plt.plot(new_time_hr, yap_df[f"{item}"], label='YAP', c='crimson', marker='s', mfc='white',
             mec='crimson', ms=9,lw=3, ls='--')
    plt.title(f'{item} Diurnal Variation of 2011 Data for HSA', pad=25, fontsize=16, fontweight="bold")
    plt.xlabel('Local Time (hrs)', labelpad=25, fontsize=16, fontweight="bold")
    plt.ylabel('Sq(H) (nT)', fontsize=16, fontweight="bold")
    plt.xticks(nx_label, fontsize=12, fontweight="bold")
    plt.yticks(ny_label, fontsize=12, fontweight="bold")
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.sans-serif"] = ["Times New Roman"]
    ax = plt.gca()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.legend(bbox_to_anchor=(0.5, 1.10), loc="upper center", ncol=6, fontsize=12, labelspacing=0.4, frameon=False)
    plt.tight_layout()
    plt.show()
    num += 1
else:
    print("Graph as been saved successfully")
    winsound.Beep(1000, 1000)
