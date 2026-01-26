import React, { useState } from 'react';

function Login({ onLoginSuccess }) {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async () => {
        const response = await fetch('http://127.0.0.1:8000/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username, password
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert('Login Successful');
            onLoginSuccess(username);
    } else {
        alert(data.detail || 'Login failed');
    }
};

    return(
        <div>
            <h2>Login</h2>

            <div>
                <label>UserName</label> <br />
                <input type = "text" value ={username} onChange={(e) => setUsername(e.target.value)}></input>
            </div>
            
            <div>
                <label>Password</label> <br />
                <input type = "text" value ={password} onChange={(e) => setPassword(e.target.value)}></input>
            </div>

            <button onClick={handleLogin} >Login</button>
        </div>


    );
}

export default Login;