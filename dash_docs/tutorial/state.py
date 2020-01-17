import dash_core_components as dcc
import dash_html_components as html

from dash_docs import tools
from dash_docs import reusable_components

examples = {
    'basic-input': tools.load_example('tutorial/examples/basic-input.py'),
    'basic-state': tools.load_example('tutorial/examples/basic-state.py'),
    'prevent-update': tools.load_example('tutorial/examples/prevent_update.py'),
    'prevent-update-button': tools.load_example('tutorial/examples/prevent_update_button.py'),
}

layout = html.Div([
    html.H1('Dash State and PreventUpdate'),

    reusable_components.Markdown('''
        ## Dash State
        > This is the *4th* chapter of the [Dash Tutorial](/).
        > The [previous chapter](/getting-started-part-2) covered Dash Callbacks
        > and the [next chapter](/interactive-graphing) covers interactive
        > graphing and crossfiltering.
        > Just getting started? Make sure to
        > [install the necessary dependencies](/installation).
    '''),

    reusable_components.Markdown('''
        In the previous chapter on
        [basic Dash callbacks](/getting-started-part-2),
        our callbacks looked something like:
    '''),
    reusable_components.Syntax(examples['basic-input'][0]),
    reusable_components.Example(examples['basic-input'][1]),

    reusable_components.Markdown('''
        In this example, the callback function is fired whenever any of the
        attributes described by the `dash.dependencies.Input` change.
        Try it for yourself by entering data in the inputs above.

        `dash.dependencies.State` allows you to pass along extra values without
        firing the callbacks. Here's the same example as above but with the
        `dcc.Input` as `dash.dependencies.State` and a button as
        `dash.dependencies.Input`.
    '''),
    reusable_components.Syntax(examples['basic-state'][0]),
    reusable_components.Example(examples['basic-state'][1]),

    reusable_components.Markdown('''
        In this example, changing text in the `dcc.Input` boxes won't fire
        the callback but clicking on the button will. The current values of
        the `dcc.Input` values are still passed into the callback even though
        they don't trigger the callback function itself.

        Note that we're triggering the callback by listening to the
        `n_clicks` property of the `html.Button` component. `n_clicks` is a
        property that gets incremented every time the component has been
        clicked on. It is available in every component in the
        `dash_html_components` library.

        ## Using PreventUpdate in Callback

        In certain situations, you don't want to update the callback output. You can
        achieve this by raising a `PreventUpdate` exception in the callback function.
    '''),
    reusable_components.Syntax(examples['prevent-update-button'][0]),
    reusable_components.Example(examples['prevent-update-button'][1]),

    reusable_components.Markdown('''
        This example illustrates how you can show an error while keeping the previous
        input, using `dash.no_update` to update the output partially.
    '''),
    reusable_components.Syntax(examples['prevent-update'][0]),
    reusable_components.Example(examples['prevent-update'][1]),

    dcc.Link(
        'Dash Tutorial Part 5. Interactive Graphing',
        href=tools.relpath('/interactive-graphing')),

])
