#!/bin/bash
echo "1. GET / :"
curl -s http://127.0.0.1:8000/
echo ""
echo "2. POST /api/menu/addItem :"
curl -s -X POST http://127.0.0.1:8000/api/menu/addItem \
    -H "Content-Type: application/json" \
    -d '{"id": 1, "name": "Espresso", "price": 2.50, "description": "Strong coffee", "image": "espresso.jpg"}'
echo ""
echo "3. POST /api/menu/addItem :"
curl -s -X POST http://127.0.0.1:8000/api/menu/addItem \
    -H "Content-Type: application/json" \
    -d '{"id": 2, "name": "Latte", "price": 4.00, "description": "Milk coffee", "image": "latte.jpg"}'
echo ""
echo "4. GET /api/menu/all :"
curl -s http://127.0.0.1:8000/api/menu/all
echo ""
echo "5. GET /api/menu/1 :"
curl -s http://127.0.0.1:8000/api/menu/1
echo ""
echo "6. POST /api/order/addOrder :"
curl -s -X POST http://127.0.0.1:8000/api/order/addOrder \
    -H "Content-Type: application/json" \
    -d '{"orderId": 1, "item": 1, "qty": 2}'
echo ""
echo "7. GET /api/order/all :"
curl -s http://127.0.0.1:8000/api/order/all
echo ""
