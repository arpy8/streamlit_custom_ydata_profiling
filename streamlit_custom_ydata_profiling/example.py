import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_custom_ydata_profiling import st_profile_report

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`

# st.subheader("Component with constant args")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
# num_clicks = my_component("World")
# st.markdown("You've clicked %s times!" % int(num_clicks))

# st.markdown("---")
# st.subheader("Component with variable args")

# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
# name_input = st.text_input("Enter a name", value="Streamlit")

if __name__=="__main__":
    data = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
    report = ProfileReport(data)
    st_profile_report(report)