import { Routes, Route } from "react-router-dom";
import Login from "./pages/loginPage.tsx";
import Register from "./pages/registerPage.tsx";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;
