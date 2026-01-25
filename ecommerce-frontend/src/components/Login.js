import React, { useState } from 'react';

function Login({ onLoginSuccess }) {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

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

            <button onClick={onLoginSuccess} >Login</button>
        </div>


    );
}

export default Login;