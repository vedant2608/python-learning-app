import subprocess
import streamlit as st
import re
import os
from streamlit_ace import st_ace

st.set_page_config(
    page_title="Python Sandbox",
    page_icon=":memo:",
    layout="wide",
    initial_sidebar_state="collapsed",

)


st.sidebar.title(":memo: Editor settings")
st.title("Learn Python")
st.write("Play with Python live in the browser!")
st.markdown("##### To use the modules you have created, you have to use `allmodules.<your_module_name>`")
st.write()
st.warning("##### Before switching to files, do save your code with ctrl+enter, else your code will be reset.")
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
lessons, editor = st.columns([5, 5])


#STRING TO BE WRITTEN ON EACH NEW FILE WO CODE WHNE FILE DOES EXIST
NEW_FILE_STRING_CODE='''
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
prompts = re.findall(r'input\s*\((["\\'])(.*?)\\1', code)

# Prompt user for input values based on extracted prompts
input_values = []
for prompt in prompts:
    input_value = st.text_input(prompt[1])
    input_values.append(input_value)


def writePythonCodeToFile(code, custom_input=None):
    if os.path.exists(f"pages/{os.path.basename(__file__)}"):
        with open(f"allmodules/{os.path.basename(__file__)}", "w") as file:
            file.write(code.strip())

custom_input = '\\n'.join(input_values)
output=writePythonCodeToFile(code, custom_input)
'''






# Function to execute Python code
def execute_python_code(code, custom_input=None):
    if custom_input is not None:
        output = subprocess.run(['python', "codefile.py"], input=custom_input, capture_output=True, text=True)
    else:
        output = subprocess.run(['python', "codefile.py"], capture_output=True, text=True)

    
    return output


# Function to launch editor
def launch_editor(initial_code, height):
    code = st_ace(
        value=initial_code,
        language="python",
        placeholder=initial_code,
        theme=st.sidebar.selectbox("Theme", options=THEMES, index=26),
        keybinding=st.sidebar.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
        height=st.sidebar.slider("Editor height", 300, 700),
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

    with open("codefile.py", "w") as file:
        file.write(code.strip())

    # Extract input prompts from input() statements
    prompts = re.findall(r'input\s*\((["\'])(.*?)\1', code)

    # Prompt user for input values based on extracted prompts
    input_values = []
    for prompt in prompts:
        input_value = st.text_input(prompt[1])
        input_values.append(input_value)

    run = st.button("Run code")
    if run:
        custom_input = '\n'.join(input_values)
        output=execute_python_code(code, custom_input)
        filtered_output = output.stdout
        error = output.stderr
        
        if error:
            st.error(output.stderr)
        else:
                
            for prompt in prompts:
                filtered_output = filtered_output.replace(prompt[1], '')


            st.code(filtered_output)
HEIGHT = 400

with lessons:
    with st.expander("Python Introduction"):
        with open("lessons/Introduction.md", "r") as file:
            text = file.read()
            st.markdown(text)
            
    with st.expander("Syntax and Structure"):
        with open("lessons/SyntaxAndStructure.md", "r") as file:
            text = file.read()
            st.markdown(text)
           
    with st.expander("Variables and Data Types"):
        with open("lessons/VariablesAndDatatypes.md", "r") as file:
            text = file.read()
            st.markdown(text)

    with st.expander("print() function"):
        with open("lessons/PrintFunction.md","r") as file:
            text = file.read()
            st.markdown(text)
     
    with st.expander("Basic Operations (Arithmetic, Logical, Comparison)"):
        with open("lessons/BasicOperator.md", "r") as file:
            text = file.read()
            st.markdown(text)
            
    with st.expander("input() function"):
        with open("lessons/InputFunction.md","r") as file:
            text = file.read()
            st.markdown(text)

    with st.expander("Documentations and comments"):
        with open("lessons/CommentsAndDocumentation.md","r") as file:
            text = file.read()
            st.markdown(text)
    with st.expander("If-Else-Elif"):
        with open("lessons/IfElse.md","r") as file:
            text = file.read()
            st.markdown(text)
    with st.expander("Loops"):
        with open("lessons/Loops.md","r") as file:
            text = file.read()
            st.markdown(text)
    with st.expander("Control flow statements"):
        with open("lessons/ControlFlowStatements.md","r") as file:
            text = file.read()
            st.markdown(text)
    with st.expander("Functions"):
        with open("lessons/Functions.md","r") as file:
            text = file.read()
            st.markdown(text)
    with st.expander("Functions arguments and Return value"):
        with open("lessons/FunctionArgumentsAndReturnValue.md","r") as file:
            text = file.read()
            st.markdown(text)


with editor:
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True


    st.button('Create new File', on_click=click_button)

    if st.session_state.clicked:
        fileName=st.text_input('Enter File name')
        if fileName:
            if not os.path.exists(f"pages/{fileName}.py"):    
                with open(f"pages/{fileName}.py","w") as file:
                    file.write(NEW_FILE_STRING_CODE)
                    st.session_state.clicked=False
            else:
                st.error("File already exist")

    with open("codefile.py","r") as file:
        fileContent=file.read()
        launch_editor(fileContent, int(HEIGHT))
