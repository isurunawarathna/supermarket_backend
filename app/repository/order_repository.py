# from typing import Optional
# from sqlalchemy.orm import Session
# from app.models import Orders
# from app.schemas import OrderCreate, OrderResponse
# from datetime import datetime
#
#
# class OrdersRepository:
#
#     @staticmethod
#     def create_order(order_data: OrderCreate, db: Session) -> OrderResponse:
#         new_order = Orders(
#             user_id=order_data.user_id,
#             status_id=order_data.status_id,
#             total_amount=order_data.total_amount,
#             notes=order_data.notes,
#             created_at=datetime.now(),
#             updated_at=datetime.now()
#         )
#
#         db.add(new_order)
#         db.commit()
#         db.refresh(new_order)
#         return new_order
#
#     @staticmethod
#     def get_all_orders(db: Session):
#         return db.query(Orders).all()
#
#     @staticmethod
#     def get_by_id(order_id: int, db: Session) -> Optional[OrderResponse]:
#         return db.query(Orders).filter(Orders.order_id == order_id).first()
#
#     @staticmethod
#     def get_by_user_id(user_id: int, db: Session) -> Optional[OrderResponse]:
#         return db.query(Orders).filter(Orders.user_id == user_id).first()
#
#     @staticmethod
#     def update_order_status(order_id: int, status_id: int, db: Session) -> Optional[OrderResponse]:
#         order = db.query(Orders).filter(Orders.order_id == order_id).first()
#
#         order.status_id = status_id
#         order.updated_at = datetime.now()
#
#         db.commit()
#         db.refresh(order)
#         return order
#
#     @staticmethod
#     def delete_order(order_id: int, db: Session) -> bool:
#         order = db.query(Orders).filter(Orders.order_id == order_id).first()
#
#         if not order:
#             return False
#
#         db.delete(order)
#         db.commit()
#         return True