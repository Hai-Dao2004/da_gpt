import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

def main():
    st.set_page_config(
        page_title = "Interactive Visualization Tools",
        page_icon = "",
        layout = "wide"
    )
    if session_state.get("df") is not None:
        pyg_app = StreamlitRenderer(st.session_state.df)
        pyg_app.explorer()
    else:
        st.info("Please upload your data to begin using interactive visualization tools")


if __name__ = "__main__":
    main()