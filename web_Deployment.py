import pickle
import streamlit as st

log_reg = pickle.load(open('log_model.pkl','rb'))
dt = pickle.load(open('dt_model.pkl','rb'))
dt2 = pickle.load(open('dt2_model.pkl','rb'))
rf = pickle.load(open('rf_model.pkl','rb'))
rf2 = pickle.load(open('rf2_model.pkl','rb'))

st.title("Brain Stroke Web App")
html_temp = """
    <div style="background-color:orange ;padding:10px">
    <h2 style="color:Green;text-align:center;">Stroke Classification</h2>
    </div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

activities = ['Log_Reg','DT','DT2','RF','RF2']
option = st.sidebar.selectbox('Which model would you like to use?',activities)
st.subheader(option)

ag = st.slider('Select age group', 0.0, 2.0)
glu = st.slider('Select avg_glucose_level', 0.0, 100.0)
ss = st.slider('Select Smoking status', 0.0, 1.0)
bmi = st.slider('Select BMI',0.0,100.0)
wt =st.slider('Select Work Type',0.0,1.0)

inputs=[[ag,glu,ss,bmi,wt]]

if st.button('Classify'):
    if option=='DT':
        st.success(dt.predict(inputs))
    elif option=='DT2':
        st.success(dt2.predict(inputs))
    elif option=='RF':
       st.success(rf.predict(inputs))
    elif option=='RF2':
           st.success(rf2.predict(inputs))
    else:
        st.success(log_reg.predict(inputs))