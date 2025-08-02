# ---
# jupyter:
#   jupytext:
#     formats: sh:percent
#     text_representation:
#       extension: .sh
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Bash
#     language: bash
#     name: bash
# ---

# %% [markdown]
# Set up a new Python package

# %%
uv init --package

# %% [markdown]
# Add the `.python-version` file to `.gitignore`

# %%
grep -qxF '/.python-version' .gitignore || echo '/.python-version' >> .gitignore

# %% [markdown]
# Add a project dependency, like `xarray` for example.

# %%
uv add xarray

# %% [markdown]
# Install the package into your current environment in editable mode.

# %%
pip install -e .