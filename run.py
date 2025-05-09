from web import app, db

# To start the server
# Run py run.py
if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)