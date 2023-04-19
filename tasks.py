from invoke import task

#poetry run invoke start
@task
def start(ctx):
    ctx.run("python3 src/index.py")

#poetry run invoke test
@task
def test(ctx):
    ctx.run("pytest src", pty=True)


#poetry run invoke coverage-report
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)