# Copyright (C) 2021-2022 Archingen, PLC DBA PermitZIP.

import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand


@click.group(
    cls=HelpColorsGroup, help_headers_color="yellow", help_options_color="green"
)
@click.version_option(
    version="0.0.1",
    prog_name="UPDATE_THIS",
)
@click.pass_context
def UPDATE_THIS_MAIN_FUNCTION_NAME(ctx, set_token):
    """UPDATE THIS NAME."""
    print(set_token)
