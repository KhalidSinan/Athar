from app import create_app
from app.models import manager
from app.extensions import db

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
