import React  from "react";
import { useState} from "react";
import Login from './components/Login';
import Register from './components/Register';
import "./App.css";

function App() {
  const [mode, setMode] = useState("login");

  return(
    <div className = "app">
      <h1>E-Commerce Website</h1>


      {mode === 'login' && <Login onLoginSuccess= {() => setMode('products')} />}
      {mode === 'register' && <Register onRegisterSuccess= {() => setMode('login')} />}
      {mode === 'products' && <p>Products Screen</p>}
      {mode === 'cart' && <p>Cart Screen</p>}

      <div style={{marginBottom: '20px'}}>
        <button onClick= {() => setMode('login')}>Login</button>
        <button onClick= {() => setMode('register')}>Register</button>
        <button onClick ={() => setMode('products')}>Products</button>
        <button onClick = {() => setMode('cart')}>Cart</button>
      </div>

    </div>
  );
}

export default App;