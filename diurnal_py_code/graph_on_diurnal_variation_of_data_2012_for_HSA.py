#importing necessary libray to be used to plot graph of diurnal variation for HSA for data of 2012
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import winsound

#creating a dataframe that will be storing the datas read from an Excel sheet

#DAV dataframe
#try:
#    dav_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_DAV_Data_2012.xlsx")
#    dav_df.fillna(0, inplace=True)
#    print("DAV excel opened successfully")
#except Exception as e:
#    print(f"Error: {e}")

#MUT dataframe
try:
    mut_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_MUT_Data_2012.xlsx")
    #mut_df.fillna(0, inplace=True)
    print("MUT excel opened successfully")
except Exception as e:
    print(f"Error: {e}")

#YAP dataframe
try:
    yap_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_YAP_Data_2012.xlsx")
    #yap_df.fillna(0, inplace=True)
    print("YAP excel opened successfully")
except Exception as e:
    print(f"Error: {e}")
#testing area


#creating an array that contain name of the months
month_name = []

for key in mut_df.keys():
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

y_label = list(range(0, 170, 20))
ny_label = np.array(y_label)

#plotting diurnal variation of data 2009 for LSA
num = 1
for item in new_month_name:
#    plt.plot(new_time_hr, dav_df[f"{item}"], label='DAV', c='royalblue', marker='o', mfc='white', mec='royalblue',
#             ms=7, lw=2, ls='-')
    plt.plot(new_time_hr, mut_df[f"{item}"], label='MUT', c='crimson', marker='s', mfc='white', mec='crimson', ms=7,
             lw=2, ls='--')
    plt.plot(new_time_hr, yap_df[f"{item}"], label='YAP', c='seagreen', marker='^', mfc='white', mec='seagreen',
             ms=7,lw=2, ls='-.')
    plt.title(f'{item} Diurnal Variation of 2012 Data for HSA')
    plt.xlabel('Local Time (hrs)')
    plt.ylabel('Sq(H) (nT)')
    plt.xticks(nx_label)
    plt.yticks(ny_label)
    plt.legend()
    plt.tight_layout()
    plt.savefig(rf'C:\Users\P C\Documents\schoolWork\original_project\project\project_pics\diurnal_graph\graph_on_diurnal_variation_of_data_2012_for_HSA\{num}_diurnal_variation_of_2012_data_{item}.png', dpi=600, bbox_inches='tight')
    plt.close()
    num += 1
else:
    print("Graph as been saved successfully")
    winsound.Beep(1000, 1000)
