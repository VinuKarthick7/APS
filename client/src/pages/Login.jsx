import { useState } from "react";
import { login } from "../api/auth";

export default function Login() {
  const [uid, setUid] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      await login(uid, password);
      window.location.href = "/dashboard";
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input placeholder="UID" onChange={e => setUid(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}
