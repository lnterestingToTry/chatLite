from flask.cli import FlaskGroup

from project import app, db


cli = FlaskGroup(app)


@cli.command("rebuild_db")
def rebuild_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("delete_db")
def delete_db():
    db.drop_all()
    db.session.commit()


if __name__ == "__main__":
    cli()