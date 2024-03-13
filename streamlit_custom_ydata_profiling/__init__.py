import os
import streamlit as st
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
_RELEASE = True

if not _RELEASE:
    _render_component = components.declare_component(
        "streamlit_custom_ydata_profiling",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _render_component = components.declare_component("streamlit_custom_ydata_profiling", path=build_dir)


def st_profile_report(report, height=None, navbar=True, key=None):
    """Display a profile report.

    Parameters
    ----------
    report : ydata_profiling.ProfileReport
        The profile report instance to display.
    height : int or None
        Report height. If set to None, report will take full height, but
        navbar will be disabled. Defaults to None.
    navbar : boolean
        Show navbar if height is fixed.
    key : str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    """
    config = {
        "inline": True,
        "minify_html": True,
        "use_local_assets": True,
        "navbar_show": navbar if height is not None else False,
        "style": {
            "full_width": True
        }
    }

    try:
        report.set_variable("html", config)
    except AttributeError:
        report.config.html.inline = config["inline"]
        report.config.html.minify_html = config["minify_html"]
        report.config.html.use_local_assets = config["use_local_assets"]
        report.config.html.navbar_show = config["navbar_show"]
        report.config.html.full_width = config["style"]["full_width"]

    with st.spinner("Generating profile report..."):
        _render_component(html=report.to_html(), height=height, key=key, default=None)