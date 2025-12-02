import "../styles/registerPage.css";
import { Link } from "react-router-dom";
import { useState } from "react";

function Register() {
  const [showModal, setShowModal] = useState(false);
  const [selectedFaculty, setSelectedFaculty] = useState("");
  const [selectedYear, setSelectedYear] = useState("");
  const [selectedModules, setSelectedModules] = useState<string[]>([]);

  // 🔹 Faculties + Modules
  const facultyModules: Record<string, string[]> = {
    "ICT": [
      "Internet Programming",
      "Web Development",
      "Mobile Computing",
      "Computer Architecture",
      "Principles of Programming A",
      "Principles of Programming B",
      "Computer Fundamentals A",
      "Computer Fundamentals B",
      "Maths",
    ],
    "Engineering": [
      "Physics",
      "Engineering Maths",
      "Electrical Systems",
      "Mechanics",
      "Thermodynamics",
    ],
    "Business": [
      "Accounting",
      "Economics",
      "Business Management",
      "Marketing",
      "Entrepreneurship",
    ],
  };

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
          <img src="/login2.png" alt="Login Illustration" className="login-image" />
        </div>

        {/* RIGHT */}
        <div className="right">
          <h1>Create Account</h1>
          <p className="subtitle">Register to access the university platform.</p>

          <input type="text" placeholder="Full Names" className="input-field" />
          <input type="email" placeholder="Email" className="input-field" />
          <input type="text" placeholder="Student Number" className="input-field" />
          <input type="text" placeholder="Cell Number" className="input-field" />
          <input type="password" placeholder="Password" className="input-field" />

          {/* FACULTY SELECTION */}
          <select
            className="input-field"
            value={selectedFaculty}
            onChange={(e) => {
              setSelectedFaculty(e.target.value);
              setSelectedModules([]); // reset modules
            }}
          >
            <option value="">Select Faculty</option>
            <option value="ICT">ICT</option>
            <option value="Engineering">Engineering</option>
            <option value="Business">Business</option>
          </select>

          {/* YEAR OF STUDY */}
          <select
            className="input-field"
            value={selectedYear}
            onChange={(e) => setSelectedYear(e.target.value)}
          >
            <option value="">Select Year of Study</option>
            <option value="1st Year">1st Year</option>
            <option value="2nd Year">2nd Year</option>
            <option value="3rd Year">3rd Year</option>
            <option value="4th Year">4th Year</option>
          </select>

          {/* MODULE SELECT BUTTON */}
          <button
            className="md-btn"
            disabled={!selectedFaculty}
            onClick={() => setShowModal(true)}
          >
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

      {/* MODULE SELECTION MODAL */}
      {showModal && (
        <div className="modal-md">
          <div className="modal">
            <button
              onClick={() => setShowModal(false)}
              className="close-btn"
            >
              ×
            </button>

            <h2>Select Your Modules</h2>

            {/* List all modules for chosen faculty */}
            <div className="module-list">
              {selectedFaculty &&
                facultyModules[selectedFaculty].map((module) => (
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
