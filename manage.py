# manage.py
from conduit import create_app
from conduit.extensions import db

app = create_app()

@app.cli.command("create_db")
def create_db():
    """Creates the database tables."""
    db.create_all()
    print("✅ Database created.")

if __name__ == "__main__":
    app.run()
