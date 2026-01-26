import React, { useEffect, useState } from 'react';

function Cart({ currentUser }) {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/cart/${currentUser}`)
      .then((res) => res.json())
      .then((data) => setItems(data.items))
      .catch(() => alert('Failed to load cart'));
  }, [currentUser]);
  return (
    <div>
      <h2>Cart</h2>

      {items.length === 0 && <p>Cart is empty</p>}

      {items.map((item, index) => (
        <div key={index}>
          <p>{item.name}</p>
          <p>₹{item.price}</p>
          <p>Qty: {item.quantity}</p>
        </div>
      ))}
      <button
        onClick={() => {
            fetch('http://127.0.0.1:8000/orders/place', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: currentUser
            })
            })
            .then((res) => res.json())
            .then(() => {
                alert('Order placed successfully');
                setItems([]);
            })
            .catch(() => alert('Failed to place order'));
        }}
        >
        Place Order
      </button>
    </div>
  );
}

export default Cart;
