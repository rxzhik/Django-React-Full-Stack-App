import React from "react";
import { BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Login from "./pages/Login";
import Register from "./pages/Register";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import ProtectedRoute from "./components/ProtectedRoute";


function Logout(){
   localStorage.clear()
   return <Navigate to="/login"/>
}

// So instead of just returning a register we first want to make sure that the
// tokens are cleared so that we don't have any potential errors. So that we don't
// have any old access tokens lingering around.
function RegisterAndLogout(){
   localStorage.clear()
   return <Register/>
}

function App() {
   return (
    <>
      <BrowserRouter>
         <Routes>
            <Route path="/" element={<ProtectedRoute>
               <Home/>
            </ProtectedRoute>}/>
            <Route  path="/logout" element={<Logout/>}/>
            <Route path="/login" element={<Login/>}/>
            <Route path="/register" element={<Register/>}/>
            <Route path="*" element={<NotFound/>}/>
         </Routes>
      </BrowserRouter>
    </>
   )
}

export default App