from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

    from app.models import User
    if not User.query.filter_by(username="admin").first():
        from seed import seed_data
        seed_data()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
