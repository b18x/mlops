from invoke import task
import os

@task
def python(ctx):
    """ """
    ctx.run("which python" if os.name != "nt" else "where python")


@task
def git(ctx, message="no commit message"):
    ctx.run("git add *")
    ctx.run("git commit -m '{message}'")
    ctx.run("git push")

@task
def conda(ctx, name: str = "dtu_mlops", env_file: str = "environment.yml"):
    ctx.run(f"conda env create --name {name} --file {env_file}", echo=True)
    ctx.run(f"conda activate {name}", echo=True)
    ctx.run(f"pip install -e .", echo=True)