from invoke import task
# pty=True taken away bc windows, will add back if needed

#poetry run invoke start
@task
def start(ctx):
    ctx.run("python3 src/index.py")

#poetry run invoke test
@task
def test(ctx):
    ctx.run("pytest src")

#poetry run invoke coverage-report
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

#poetry run invoke lint

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)