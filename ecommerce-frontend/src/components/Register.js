import React, { useState } from 'react';

function Register( { onRegisterSuccess }) {

    const [firstname, setFirstname] = useState('');
    const [ lastname, setLastname ] = useState('');
    const [ mobilenumber, setMobilenumber ] = useState('');
    const [ username, setUsername ] = useState('');
    const [ password, setPassword ] = useState('');
    const [ confirmpassword, setConfirmpassword] = useState('');

    return(
        <div>
            <h2>Register</h2>
            <div>
                <label>FirstName</label> <br />
                <input type="text" value= {firstname} onChange= {(e) => setFirstname(e.target.value)}></input>
            </div>
            <div>
                <label>LastName</label> <br />
                <input type="text" value= {lastname} onChange= {(e) => setLastname(e.target.value)}></input>
            </div>
            <div>
                <label>MobileNumber</label> <br />
                <input type="text" value ={mobilenumber} onChange = {(e) => setMobilenumber(e.target.value)}></input>
            </div>
            <div>
                <label>UserName</label> <br />
                <input type="text" value ={username} onChange = {(e) => setUsername(e.target.value)}></input>
            </div>
            <div>
                <label>password</label> <br />
                <input type="text" value ={password} onChange = {(e) => setPassword(e.target.value)}></input>
            </div>
            <div>
                <label>confirmpassword</label> <br />
                <input type="text" value ={confirmpassword} onChange = {(e) => setConfirmpassword(e.target.value)}></input>
            </div>

            <button onClick={onRegisterSuccess}>Register</button>
        </div>
    );
}

export default Register;