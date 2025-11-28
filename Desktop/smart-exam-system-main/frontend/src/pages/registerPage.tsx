import "../styles/registerPage.css";
import loginPic from "../assets/login2.png";
import { Link } from "react-router-dom";
import { useState } from "react";

function Register() {
  const [showModal, setShowModal] = useState(false);
  const [selectedModules, setSelectedModules] = useState<string[]>([]);

  const modules = [
    "Internet Programming",
    "Principles of Programming A",
    "Principles of Programming B",
    "Web Development",
    "Computer Architecture",
    "Computer Fundamentals A",
    "Computer Fundamentals B",
    "Mobile Computing",
    "Maths",
  ];

  const toggleModule = (module: string) => {
    if (selectedModules.includes(module)) {
      setSelectedModules(selectedModules.filter((m) => m !== module));
    } else {
      setSelectedModules([...selectedModules, module]);
    }
  };

  return (
    <div className="register-container">
      <div className="register-card">

        {/* LEFT */}
        <div className="left">
          <img
            src={loginPic}
            alt="Register Illustration"
            className="register-image"
          />
        </div>

        {/* RIGHT FORM */}
        <div className="right">
          <h1>Create Account</h1>
          <p className="subtitle">Register to access the university platform.</p>

          <input type="text" placeholder="Full Names" className="input-field" />
          <input type="email" placeholder="Email" className="input-field" />
          <input type="text" placeholder="Student Number" className="input-field" />
          <input type="text" placeholder="Cell Number" className="input-field" />
          <input type="password" placeholder="Password" className="input-field" />

          <button className="md-btn" onClick={() => setShowModal(true)}>
            Select Registered Modules
          </button>

          {selectedModules.length > 0 && (
            <div className="selected-modules">
              <strong>Modules:</strong>
              <ul>
                {selectedModules.map((m) => (
                  <li key={m}>{m}</li>
                ))}
              </ul>
            </div>
          )}

          <button className="register-btn">Register</button>

          <p className="login-link">
            Already have an account? <Link to="/login">Login here</Link>
          </p>
        </div>
      </div>

      {/* MODAL */}
      {showModal && (
        <div className="modal-md">
          <div
            className="modal"
            style={{
              position: "relative",
              width: "400px",
              background: "white",
              padding: "20px",
              borderRadius: "10px",
              boxShadow: "0 0 15px rgba(0,0,0,0.3)",
              animation: "fadeIn 0.3s ease",
            }}
          >
            
            <button
              onClick={() => setShowModal(false)}
              style={{
                position: "absolute",
                top: "10px",
                right: "12px",
                background: "transparent",
                border: "none",
                fontSize: "22px",
                cursor: "pointer",
                fontWeight: "bold",
              }}
            >
              ×
            </button>

            <h2 style={{ marginTop: "30px" }}>Select Your Modules</h2>

            <div className="module-list">
              {modules.map((module) => (
                <label key={module} className="module-item">
                  <input
                    type="checkbox"
                    checked={selectedModules.includes(module)}
                    onChange={() => toggleModule(module)}
                  />
                  {module}
                </label>
              ))}
            </div>

            <button className="save-btn" onClick={() => setShowModal(false)}>
              Save Selection
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Register;
