customers:
- customer_id (PK)
- name
- email
- created_at

orders:
- order_id (PK)
- customer_id (FK)
- order_amount
- order_date
- status
