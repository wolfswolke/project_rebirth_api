import os.path
import webbrowser

from invoke import task


# This is a PLACEHOLDER file for the tasks.py.
# No unit tests are implemented yet.

@task
def run_unit_tests(c):
    print("Running unit tests...")
    with c.prefix("cd test"):
        c.run("coverage run -m unittest discover")
        c.run("coverage html")
        webbrowser.open(os.path.abspath("test/index.html"), new=2)
