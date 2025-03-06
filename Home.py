import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Maps
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("GIS Map")

st.markdown(
    """
    [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). [GitHub repository](https://github.com/opengeos/streamlit-map-template).
    """
)





st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
