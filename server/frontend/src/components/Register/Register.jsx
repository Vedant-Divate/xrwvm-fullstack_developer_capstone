import React, { useState } from 'react';

function Register() {
  const [form, setForm] = useState({
    username: '',
    firstName: '',
    lastName: '',
    email: '',
    password: '',
  });
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    const res = await fetch('/api/register/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: form.username,
        first_name: form.firstName,
        last_name: form.lastName,
        email: form.email,
        password: form.password,
      }),
    });
    const data = await res.json();
    setMessage(data.message || data.error);
  };

  return (
    <div className="register-page">
      <h1>Sign Up</h1>
      <form onSubmit={handleRegister}>
        <label>Username
          <input type="text" name="username" value={form.username} onChange={handleChange} />
        </label>
        <label>First Name
          <input type="text" name="firstName" value={form.firstName} onChange={handleChange} />
        </label>
        <label>Last Name
          <input type="text" name="lastName" value={form.lastName} onChange={handleChange} />
        </label>
        <label>Email
          <input type="email" name="email" value={form.email} onChange={handleChange} />
        </label>
        <label>Password
          <input type="password" name="password" value={form.password} onChange={handleChange} />
        </label>
        <button type="submit">Register</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default Register;
