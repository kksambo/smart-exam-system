import "../styles/loginPage.css";
import loginPic from "../assets/login2.png";
import { useState } from "react";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  return (
    <div className="login-wrapper">
      <div className="card">
        <div className="left">
          <img
            src={loginPic}
            alt="Login Illustration"
            className="login-image"
          />
        </div>

        <div className="right">
          <h1>Welcome Back!</h1>
          <p className="subtitle">
            Login to access your account and all features.
          </p>

          <input
            type="text"
            placeholder="email"
            className="input-field"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            className="input-field"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <div className="options">
            <label>
              <input type="checkbox" /> Remember me
            </label>
            <a href="#" className="forgot">
              Forgot password?
            </a>
          </div>

          <button
            className="login-btn"
            onClick={() => {
              fetch("http://localhost:8000/auth/login", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  username: username,
                  password: password,
                }),
              })
                .then((response) => {
                  if (!response.ok) {

                    return "login failed";
                  }
                  return response.json();
                })
                .then((data) => {

                    setMessage(data.message)

                  console.log("Success:", data);
                })
                .catch((error) => {
                  console.error("Error during fetch operation:", error);
                });
            }}
          >
            Log In
          </button>
          <p>{message}</p>

          <p className="register">
            Don't have account ? <a href="#">Register here</a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default Login;
