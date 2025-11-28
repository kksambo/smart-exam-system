import "../styles/loginPage.css";
import loginPic from "../assets/login2.png";
import { Link } from "react-router-dom";

function Login() {
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

          <input type="text" placeholder="email" className="input-field" />
          <input
            type="password"
            placeholder="Password"
            className="input-field"
          />

          <div className="options">
            <label>
              <input type="checkbox" /> Remember me
            </label>
            <a href="#" className="forgot">
              Forgot password?
            </a>
          </div>

          <button className="login-btn">Log In</button>

          <p className="register">
            Don't have account ? <Link to="/register">Register here</Link>
          </p>
        </div>
      </div>
    </div>
  );
}

export default Login;
