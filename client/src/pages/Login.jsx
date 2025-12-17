import { useState } from "react";
import { login } from "../api/auth";
import "./Login.css";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [selectedRole, setSelectedRole] = useState("Faculty");
  const [isRoleDropdownOpen, setIsRoleDropdownOpen] = useState(false);
  const [activeMode, setActiveMode] = useState("Creation"); // Creation or Handling

  const roles = [
    "Faculty",
    "Course Coordinator",
    "Domain Mentor",
    "Head of Department",
    "Supervisor"
  ];

  const handleLogin = async () => {
    if (!email || !password) {
      alert("Please fill in all fields");
      return;
    }

    setIsLoading(true);
    try {
      await login(email, password);
      window.location.href = "/dashboard";
    } catch {
      alert("Invalid credentials");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="login-container">
      {/* Left Section - Featured Work */}
      <div className="featured-section">
        <div className="featured-content">
          <div className="featured-header">
            <h3>Selected Works</h3>
            <div className="auth-links">
              {/* Role Selector Dropdown */}
              <div className="custom-dropdown">
                <button 
                  className="dropdown-btn"
                  onClick={() => setIsRoleDropdownOpen(!isRoleDropdownOpen)}
                >
                  {selectedRole}
                  <span className="dropdown-arrow">▼</span>
                </button>
                {isRoleDropdownOpen && (
                  <div className="dropdown-menu">
                    {roles.map((role) => (
                      <div
                        key={role}
                        className={`dropdown-item ${selectedRole === role ? 'active' : ''}`}
                        onClick={() => {
                          setSelectedRole(role);
                          setIsRoleDropdownOpen(false);
                        }}
                      >
                        {role}
                      </div>
                    ))}
                  </div>
                )}
              </div>

              {/* Toggle Slider Button */}
              <div className="toggle-slider">
                <button
                  className={`toggle-option ${activeMode === "Creation" ? "active" : ""}`}
                  onClick={() => setActiveMode("Creation")}
                >
                  Creation
                </button>
                <button
                  className={`toggle-option ${activeMode === "Handling" ? "active" : ""}`}
                  onClick={() => setActiveMode("Handling")}
                >
                  Handling
                </button>
              </div>
            </div>
          </div>
          
          <div className="featured-image">
            <div className="image-placeholder">
              {/* Background image will be set via CSS */}
            </div>
          </div>
        </div>
      </div>

      {/* Right Section - Login Form */}
      <div className="login-section">
        <div className="login-header">
          <h1 className="logo">KGAPS</h1>
        </div>

        <div className="login-form">
          <h2>Dashboard</h2>
          <p className="welcome-text">Welcome to KGAPS</p>

          <div className="form-inputs">
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="input-field"
            />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="input-field"
            />
            <a href="/forgot-password" className="forgot-link">
              Forgot password?
            </a>
          </div>

          <button 
            className="login-btn" 
            onClick={handleLogin}
            disabled={isLoading}
          >
            {isLoading ? "Logging in..." : "Login"}
          </button>
        </div>
      </div>
    </div>
  );
}
