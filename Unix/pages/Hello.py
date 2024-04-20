
import os
import streamlit as st
import re
from streamlit_ace import st_ace

st.set_page_config(
    page_title="Python Sandbox",
    page_icon=":memo:",
    layout="wide",
    initial_sidebar_state="collapsed",

)

st.sidebar.title(":memo: Editor settings")
st.title("Learn Python")
st.write("This is the module that you have created, try not o inlcude the input() in this.")
st.write("This module will be stored in the allmodules. To aceess this module in this app use the allmodules.<YourScriptName>")
st.write("To go to the main app, you can navigate to the app.py")
THEMES = [
    "dracula", "ambiance", "chaos", "chrome", "clouds", "clouds_midnight",
    "cobalt", "crimson_editor", "dawn", "dreamweaver", "eclipse", "github",
    "gob", "gruvbox", "idle_fingers", "iplastic", "katzenmilch", "kr_theme",
    "kuroir", "merbivore", "merbivore_soft", "mono_industrial", "monokai",
    "nord_dark", "pastel_on_dark", "solarized_dark", "solarized_light",
    "sqlserver", "terminal", "textmate", "tomorrow", "tomorrow_night",
    "tomorrow_night_blue", "tomorrow_night_bright", "tomorrow_night_eighties",
    "twilight", "vibrant_ink", "xcode",
]

KEYBINDINGS = ["emacs", "sublime", "vim", "vscode"]


def getTextForValueOfEditor(): 
    if os.path.exists(f"allmodules/{os.path.basename(__file__)}"):
        with open(f"allmodules/{os.path.basename(__file__)}","r") as file:
            return file.read()
    return ""
code = st_ace(
        value=getTextForValueOfEditor(),
        language="python",
        placeholder="",
        theme=st.sidebar.selectbox("Theme", options=THEMES, index=26),
        keybinding=st.sidebar.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
        height=st.sidebar.slider("Editor size", 300,600),
        font_size=st.sidebar.slider("Font size", 5, 24, 14),
        tab_size=st.sidebar.slider("Tab size", 1, 8, 4),
        wrap=st.sidebar.checkbox("Wrap lines", value=False),
        show_gutter=True,
        show_print_margin=True,
        auto_update=st.sidebar.checkbox("Auto Update", value=False),
        readonly=False,
        key=os.path.basename(__file__),
    )


st.write("Hit `CTRL+ENTER` to refresh the code first and then click on the run button")

# Extract input prompts from input() statements
prompts = re.findall(r'input\s*\((["\'])(.*?)\1', code)

# Prompt user for input values based on extracted prompts
input_values = []
for prompt in prompts:
    input_value = st.text_input(prompt[1])
    input_values.append(input_value)


def writePythonCodeToFile(code, custom_input=None):
    if os.path.exists(f"pages/{os.path.basename(__file__)}"):
        with open(f"allmodules/{os.path.basename(__file__)}", "w") as file:
            file.write(code.strip())

custom_input = '\n'.join(input_values)
output=writePythonCodeToFile(code, custom_input)
