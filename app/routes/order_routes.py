from flask import Blueprint, jsonify, request
from app.db.connection import db
from app.models import Order
from app.schemas import OrderSchema, OrderUpdateSchema
from pydantic import ValidationError

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['POST'])
def create_order():
    try:
        data = request.get_json()
        order_data = OrderSchema(**data)
        
        new_order = Order(
            product_name=order_data.product_name,
            quantity=order_data.quantity,
            price=order_data.price
        )
        db.session.add(new_order)
        db.session.commit()
        
        return jsonify({"message": "Order created", "order": order_data.dict()}), 201
    
    except ValidationError as e:
        return jsonify(e.errors()), 400

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    result = [{"id": order.id, "product_name": order.product_name, "quantity": order.quantity,
               "price": order.price, "status": order.status, "created_at": order.created_at,
               "updated_at": order.updated_at} for order in orders]
    return jsonify(result), 200

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order:
        return jsonify({"id": order.id, "product_name": order.product_name, "quantity": order.quantity,
                        "price": order.price, "status": order.status, "created_at": order.created_at,
                        "updated_at": order.updated_at}), 200
    else:
        return jsonify({"message": "Order not found"}), 404

@order_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        data = request.get_json()
        order_data = OrderUpdateSchema(**data)
        
        order = Order.query.get(order_id)
        if not order:
            return jsonify({"message": "Order not found"}), 404
        
        for key, value in order_data.dict(exclude_unset=True).items():
            setattr(order, key, value)
        
        db.session.commit()
        
        return jsonify({"message": "Order updated", "order": order_data.dict()}), 200
    
    except ValidationError as e:
        return jsonify(e.errors()), 400

@order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({"message": "Order deleted"}), 200
    else:
        return jsonify({"message": "Order not found"}), 404
