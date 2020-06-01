from invoke import task

@task
def run_all_tests(c):
    c.run("python -m unittest tests/**/*.py")
