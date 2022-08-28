from app import create_app
from app.config import config

flask_app = create_app(config["production"])


if __name__ == "__main__":
    flask_app.run()
