from invoke import task

@task
def coverage(ctx):
	ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
	ctx.run("coverage html")

@task
def start(ctx):
	ctx.run("python3 src/index.py")

@task
def lint(ctx):
	ctx.run("pylint src")

@task
def format(ctx):
	ctx.run("autopep8 --in-place --recursive src")

