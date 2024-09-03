from app.db.connection import create_app
from app.routes.order_routes import order_bp

app = create_app()

app.register_blueprint(order_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
