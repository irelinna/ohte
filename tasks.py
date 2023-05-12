from invoke import task


#poetry run invoke start
@task
def start(ctx):
    a = ctx.run("python3 src/index.py")
    print(a)
    
    

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)

#poetry run invoke test
@task
def test(ctx):
    ctx.run("pytest src")

#poetry run invoke coverage-report
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

#poetry run invoke lint

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)