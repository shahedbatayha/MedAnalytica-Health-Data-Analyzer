import streamlit as st
import pandas as pd
from file1labdata import LabTestRef,TestResult,loaddata 

def create(k,v,min_l,max_l,u):
    pass
st.set_page_config(
    page_title="MedAnalytica Program", 
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded")
a=loaddata()
n=list(a.keys())
st.title("🔬MedAnalytica - Health data analyzer") 
st.sidebar.header("enter all test data")
if 'input_values' not in st.session_state:
    st.session_state['input_values']={}
i_d={}


with st.sidebar.container():
    for k, r_o in a.items():
        i_d[k]=st.number_input(
            f"{k}({r_o.unit}):",
            min_value=0.0, 
            step=0.1,
            format="%.2f",
            key=f"input_{k}")

b=st.sidebar.button("Analyze Results")
t1,t2,t3=st.tabs(["Analysis summary","Advice","Reference table"]) 
r_l=[]



if b:
    for k,v in i_d.items():
        if v > 0:
            t_r=a[k]
            r_o_b=TestResult(t_r, v)
            s=r_o_b.finalres()
            r_l.append(s)

    with t1:
        st.header("Result Summary")
        if r_l:
            d_f=pd.DataFrame(r_l)
            st.dataframe(d_f,use_container_width=True)
        else:
            st.warning("enter at least one result.")


    with t2:
        st.header("Advice")
        if r_l:
            c=st.columns(3)
            i = 0
            for s in r_l:
                with c[i % 3]:
                    st.markdown(f"{s['Test Name']} ({s['Status']})")
                    st.write(f"Advice: {s['Advice']}")
                    r_o_b_2=a[s['Test Name']]
                    st.write(f"Normal Range: {r_o_b_2.minlimit} - {r_o_b_2.maxlimit} {r_o_b_2.unit}")
                i+=1
        else:
            st.info("No results to display for you.")


with t3:
    st.header("Reference Ranges Table")
    d_f_t=[t.get_dict() for t in a.values()]
    d_f_r=pd.DataFrame(d_f_t)
    st.table(d_f_r.set_index("Test Name")) 
