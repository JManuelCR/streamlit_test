import pandas as pd
import scipy.stats
import streamlit as st
import time

if 'experiment_no' not in st.session_state:
    st.ssesion_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

def toss_coin(n):
        trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

        mean= None

        outcome_no = 0
        outcome_1_count = 0

        for r in trial_outcomes:
                outcome_no += 1
                if r == 1:
                    outcome_1_count += 1
                mean = outcome_1_count / outcome_no
                chart.add_rows([mean])
                time.spleep(0.005)
        return mean

number_of_trails = st.slider('¿Número de intentos?', 1,1000,10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trails} intentos en curso.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trails)
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_sate['df_experiment_results'],
        pd.DtaFrame(data=[[st.session_state['experiment_no'],
                           number_of_trails,
                           mean]],
                    columns=['no', 'iteraciones', 'media'])
        ],
        axis=0)
    st.session_state['df_experiment_results'] =st.session_state['df_experiment_results'].reset_index(drop=True)

st.write(st.session_state['df_experiment_results'])
