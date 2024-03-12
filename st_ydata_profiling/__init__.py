import os
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from ydata_profiling import ProfileReport

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

# _render_component = declare_component("st_ydata_profiling", url="https://localhost:3001")

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_ydata_profiling",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_ydata_profiling", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def st_ydata_profiling(data, height=None, navbar=True, key=None):
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
            "full_width": True,
        }
    }

    try:
        report = ProfileReport(data, progress_bar=True)
        report.set_variable("html", config)
        st.write(report)
    except AttributeError:
        report.config.html.inline = config["inline"]
        report.config.html.minify_html = config["minify_html"]
        report.config.html.use_local_assets = config["use_local_assets"]
        report.config.html.navbar_show = config["navbar_show"]
        report.config.html.full_width = config["style"]["full_width"]
    
    with st.spinner("Generating profile report..."):
        _component_func(html=report.to_html(), height=height, key=key, default=None)