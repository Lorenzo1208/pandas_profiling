import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.title('Pandas Profiling Report')

# Upload CSV data
with st.sidebar.header('1. Télécharger votre fichier CSV'):
    uploaded_file = st.sidebar.file_uploader("Importer votre fichier CSV", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('Input DataFrame')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('En attente du téléchargement du fichier CSV.')
    if st.button("Appuyez pour utiliser l'ensemble de données d'exemple"):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('Input DataFrame')
        st.write(df)
        st.write('---')
        st.header('Pandas Profiling Report')
        st_profile_report(pr)
