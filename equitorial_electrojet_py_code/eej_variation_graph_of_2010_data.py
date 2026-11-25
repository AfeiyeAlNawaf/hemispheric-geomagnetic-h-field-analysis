#importing necessary libray to be used to plot graph of EEJ variation for LSA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import winsound

#creating a dataframe that will be storing the datas read from an Excel sheet

#DAV dataframe
try:
    dav_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_DAV_Data_2010.xlsx")
    #dav_df.fillna(0, inplace=True)
    print("DAV excel opened successfully")
except Exception as e:
    print(f"Error: {e}")

#MUT dataframe
try:
    mut_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_MUT_Data_2010.xlsx")
    #mut_df.fillna(0, inplace=True)
    print("MUT excel opened successfully")
except Exception as e:
    print(f"Error: {e}")

#YAP dataframe
try:
    yap_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_YAP_Data_2010.xlsx")
    #yap_df.fillna(0, inplace=True)
    print("YAP excel opened successfully")
except Exception as e:
    print(f"Error: {e}")

#creating an array that contain name of the months
month_name = []

for key in dav_df.keys():
    month_name.append(key)

new_month_name = np.array(month_name)

#print(new_month_name)

#extracting all the column out from DAV into a dict
dav_dict = {}
for key, value in dav_df.items():
    dav_dict[key] = np.array(value.tolist())

#print(dav_dict)

#extracting all the column out from MUT into a dict
mut_dict = {}
for key, value in mut_df.items():
    mut_dict[key] = np.array(value.tolist())

#print(mut_dict)

#extracting all the column out from YAP into a dict
yap_dict = {}
for key, value in yap_df.items():
    yap_dict[key] = np.array(value.tolist())

#print(yap_dict)

#calculation for Electoral Electrojet (EEJ)
#finding the EEJ between YAP and DAV
yap_vs_mut = {}
for key in yap_dict.keys():
    yap_vs_mut[key] = yap_dict[key] - mut_dict[key]

print(yap_vs_mut, "\n \n")

#finding the EEJ between YAP and MUT
dav_vs_mut = {}
for key in dav_dict.keys():
    dav_vs_mut[key] = dav_dict[key] - mut_dict[key]

print(dav_vs_mut)

#creating an array of time in hrs from 00hrs - 23hrs which make 24hrs in a day
time_hr = list(range(24))
new_time_hr = np.array(time_hr)


#creating x ticks and y ticks for the graph
x_label = []

for num in time_hr:
    if num % 2 == 0:
        x_label.append(num)

nx_label = np.array(x_label)

y_label = list(range(-60, 170, 20))
ny_label = np.array(y_label)

#plotting the graph for EEJ
num = 0
plot_color = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta', 'olive', 'gold' ]
plot_marker = ['o', 's', '^', 'v', 'D', 'x', '+', '*', 'p', 'h', '|', '_']
for item in new_month_name:
    #plt.plot(new_time_hr, yap_vs_mut[item], label=new_month_name[num], c=plot_color[num], marker=plot_marker[num],
    #        mfc='white', mec=plot_color[num],ms=5, lw=1.5, ls='-')
    #num += 1
    plt.plot(new_time_hr, dav_vs_mut[item], label=new_month_name[num], c=plot_color[num], marker=plot_marker[num],
             mfc='white', mec=plot_color[num],ms=5, lw=1.5, ls='-')
    num += 1
plt.title(f'DAV EEJ Variation of 2010 Data LSA', pad=25)
plt.xlabel('Local Time (hrs)', labelpad=75, fontweight="bold")
plt.ylabel('EEJ (nT)', fontweight="bold")
plt.xticks(nx_label)
plt.yticks(ny_label)
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.sans-serif"] = ["Times New Roman"]
ax = plt.gca()
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.legend(bbox_to_anchor=(0.5, 1.10), loc="upper center", ncol=6, fontsize=9, labelspacing=0.4, frameon=False)
plt.tight_layout()
plt.savefig(rf'C:\Users\P C\Documents\schoolWork\original_project\project\project_pics\eej_graph\graph_on_eej_variation_of_data_2010_for_LSA\DAV_eej_variation.png',
                dpi=600, bbox_inches='tight')
plt.close()

print("successfully plot the graph")

#alarm
winsound.Beep(1000, 1000)