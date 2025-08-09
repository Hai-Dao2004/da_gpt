import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
def execute_plt_code():
    try:
        local_vars = {"plt": plt, "df": df}
        compiled_code = compile(code, "<string>", "exec")
        exec(compiled_code, globals[], local_vars)
        return plt.gcf()

    except Exception as e:
        st.error("Error excuting plt code: {e}")