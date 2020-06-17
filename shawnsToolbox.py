import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def prepare(sheepnr):
    s0 = pd.read_csv("sheeps/"+sheepnr+"Sensor0.csv", sep=";", decimal=",")
    s1 = pd.read_csv("sheeps/"+sheepnr+"Sensor1.csv", sep=";", decimal=",")
#s32 = d.concat([s0_32['Timestamp(ms)'], s0_32['c']], axis=1, keys=['df1', 'df2'])
# create new column sum (sum up all sensorcells for s0 and s1)
    s0["sum0"] = s0["SensorCell000"]+s0["SensorCell001"]+s0["SensorCell002"]+s0["SensorCell003"]+s0["SensorCell004"]+s0["SensorCell005"]+s0["SensorCell006"]+s0["SensorCell007"]
    s0["sum0_0"] = s0["SensorCell000"]+s0["SensorCell001"]+s0["SensorCell002"]+s0["SensorCell003"]
    s0["sum0_1"] = s0["SensorCell004"]+s0["SensorCell005"]+s0["SensorCell006"]+s0["SensorCell007"]
    s1["sum1"] = s1["SensorCell000"]+s1["SensorCell001"]+s1["SensorCell002"]+s1["SensorCell003"]+s1["SensorCell004"]+s1["SensorCell005"]+s1["SensorCell006"]+s1["SensorCell007"]
    s1["sum1_0"] = s1["SensorCell000"]+s1["SensorCell001"]+s1["SensorCell002"]+s1["SensorCell003"]
    s1["sum1_1"] = s1["SensorCell004"]+s1["SensorCell005"]+s1["SensorCell006"]+s1["SensorCell007"]
# set index
    s0 = s0.set_index('Timestamp(ms)')
    s1 = s1.set_index('Timestamp(ms)')
# create new Dataframe with just two columns and one index
    s = pd.concat([s0['sum0'],s0['sum0_0'],s0['sum0_1'], s1['sum1'],s1['sum1_0'],s1['sum1_1']], axis=1, keys=['sum0','sum0_0','sum0_1', 'sum1','sum1_0','sum1_1'])
    return s
    
def clean(sheep):
    sheep['sum1'] = sheep['sum1']-(sheep['sum1_0'][0]+sheep['sum1_1'][0])
    sheep['sum0'] = sheep['sum0']-(sheep['sum0_0'][0]+sheep['sum0_1'][0])
    sheep['sum1_0'] = sheep['sum1_0']-(sheep['sum1_0'][0])
    sheep['sum1_1'] = sheep['sum1_1']-(sheep['sum1_1'][0])
    sheep['sum0_0'] = sheep['sum0_0']-(sheep['sum0_0'][0])
    sheep['sum0_1'] = sheep['sum0_1']-(sheep['sum0_1'][0])
    # cast to kg
    sheep['sum0'] = sheep['sum0']*6.4/9.81
    sheep['sum1'] = sheep['sum1']*6.4/9.81
    sheep['sum1_0'] = sheep['sum1_0']*6.4/9.81
    sheep['sum1_1'] = sheep['sum1_1']*6.4/9.81
    sheep['sum0_0'] = sheep['sum0_0']*6.4/9.81
    sheep['sum0_1'] = sheep['sum0_1']*6.4/9.81
    return sheep

def show(sheep,sheepnr):
    #fig = px.line()
    fig = go.Figure()
    fig.add_scatter(x=sheep.index, y=sheep['sum0'], name='Summe0 rechts')
    fig.add_scatter(x=sheep.index, y=sheep['sum1'], name='Summe1 links')
    fig.add_scatter(x=sheep.index, y=sheep['sum0_0'], name='rechts (außen)?')
    fig.add_scatter(x=sheep.index, y=sheep['sum0_1'], name='rechts (innen)?')
    fig.add_scatter(x=sheep.index, y=sheep['sum1_0'], name='links (außen)?')
    fig.add_scatter(x=sheep.index, y=sheep['sum1_1'], name='links (innen)?')
    
    fig.update_layout(
    title=("Belastung der Hinterläufe bei "+sheepnr),
    xaxis_title="Zeit (ms)",
    yaxis_title="Gewicht (kg)",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
        )
    )
    
    fig.show()