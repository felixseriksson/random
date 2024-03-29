import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

''''''''' Forest Plot '''''''''

# Parameters

# Only model_estimate and text are mandatory. Other parameters are optional.

# 1. model_estimate - Model whose forest plot is to be made.
#                     Should be a dataframe with column names as Study,value1,value2,mean and weight (weight column is optional).
#                     Study - name of the Studies done.
#                     value1 - lower limit of forest plot.
#                     value2 - upper limit of forest plot.
#                     mean - mean value or position of model estimates.
#                     weight - weight of the Studies done (optional).

# 2. text - Data to be represented in tabular form - Should be a dataframe with column names as text,info,O1 and O2 (O1 and O2 are Optional).
#           text - column1 header of the table and name of Studies.
#           info - data about the mean,lower and upper limits of forest plot.
#           O1 and O2 are treatment and control group ratios.

# 3. save_location - location and name of the forestplot to be saved (default - saves as png file with the name 'forestplot' in the working directory).

# 4. zero - Location of the null line (default - 1).

# 5. clip - Limit after which the line is to be clipped into arrow. Should be a list - [lower_clip_limit, upper_clip_limit] (default - [0,10]).

# 6. xlab - Label for the x-axis (default - Lab)

# 7. colour - Set the colors for all the elements. Should be a list - [model_estimate_colour,reported_estimate_colour] (default - ['b','r']).

# 8. x_scale - Set the scaling of the x-axis (default - 'linear').

# 9. title - Title of the forest plot (default - '').

# 10. grid - To add grids to the forest plot if required (default - False).

# 11. is_summary - To select whether the table is to be viewed along with the plot (default - False).

# 12. fontsize - Set the font size of the data displayed in the table (default - 14).

# 13. dpi - Set the resolution of the forest plot being saved (default - 500)

# 14. reported_estimate - Reported estimate for model whose forest plot is to be made.
#                         Should be a dataframe with column names as Study,value1,value2,mean and weight (weight column is optional). (default - pd.DataFrame()).


def forestplot(model_estimate,text,save_location='forestplot.png',zero=-2,clip=[-100,100],xlab='Lab',colour=['b','r'],x_scale='linear',title='',grid=True,is_summary=True,fontsize=14,dpi=500):
       sns.set_style("darkgrid")
       # if(not('weight' in model_estimate)):
       #     model_estimate['weight'] = 50/((model_estimate['value2']-model_estimate['value1']))
       # Overall = model_estimate[model_estimate['Study'] == 'Overall'].reset_index()
       
       if len(colour) == 1 :
           colour.append('r')
       
       print(len(model_estimate))
       for i in range(len(model_estimate)):
              line_range_model_estimate = [model_estimate['value1'][i],model_estimate['value2'][i]]  
              label = [i,i]
              study = [model_estimate['mean'][i],model_estimate['mean'][i]]
              plt.plot(line_range_model_estimate,label, color=colour[0])
              plt.scatter(study,label,marker='s', color = colour[0])#,s=model_estimate['weight'][len(model_estimate)-i-2], color=colour[0])
                         
       sns.set_style('darkgrid') 
       # plt.fill([Overall['value1'][0],Overall['mean'][0],Overall['value2'][0],Overall['mean'][0]],[0,-0.25,0,0.25], colour[0])       
       plt.xscale(x_scale)
       # plt.axvline(x=zero)
       # plt.xlim(xmin=clip[0],xmax=clip[1])
       plt.xlabel(xlab)
       plt.title(title,y=1.1)
       plt.subplots_adjust(top=0.84, bottom=0.11, left=0.205, right=0.9, hspace=0.2, wspace=0.2)
       plt.tick_params(axis='y', which='both',labelsize =0)
       if grid == False:
           plt.grid()
       
       # Tables
       
       if is_summary :
           left_table_data = text.loc[:,['text','info']]
           left_cell_value = []
           for i in range(len(left_table_data)):
                  left_cell_value.append([left_table_data['text'].tolist()[i],left_table_data['info'].tolist()[i]])
                  
       #     left_table = plt.table(cellText=left_cell_value,
       #                  cellLoc='left', colWidths=[0.5,0.5],
       #                  rowLoc='left', colLoc='left',
       #                  loc='left', bbox=[-0.65, 0, 0.55, 1.1],
       #                  edges='open')
       #     left_table.auto_set_font_size(False)
       #     left_table.set_fontsize(fontsize)
       plt.grid(True)
       plt.show()


import pandas as pd
import os


# Importing data required for plotting

model_estimate = pd.read_csv(os.getcwd() + '/model_estimate.csv')
model_estimate.
text = pd.read_csv(os.getcwd() + '/text.csv')

# Create Forest plot
forestplot(model_estimate=model_estimate,text=text,clip=[0.2,7],xlab='x-values',colour=['r','g'],title='Forest plot',grid=True,is_summary=True)