import {Navigate} from "react-router-dom"
import {jwtDecode} from "jwt-decode"
import api from "../api"
import { REFRESH_TOKEN, ACCESS_TOKEN} from "../constants"
import { useEffect, useState} from "react"

// So basically we need to first authorize a user before they can access this route
// if not then we'll redirect them to login before they can acess this route.
// Theoretically someone could bypass this but there are handlers in the backend, 
// this is just for good user experience.
function ProtectedRoute({children}){
    const [isAuthorized, setIsAuthorized] = useState(null)

    useEffect(()=> {
        auth().catch(()=>{
            setIsAuthorized(false)
        })
    },[])

    const refreshToken = async () => {
        const refreshToken = localStorage.getItem(REFRESH_TOKEN)
        try{
            const res = await api.post("/api/token/refresh/", {refresh: refreshToken})

            if(res.status == 200){
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                setIsAuthorized(true)
            }else{
                setIsAuthorized(false)
            }
        }catch (error){
            console.log(error)
            setIsAuthorized(false)
        }
    }

    // Here we check if our auth token is experied or not if it is then 
    // we refresh our token, but first we check if we have the token or not and 
    // set the authorization status accordingly.
    const auth = async ()=> {
        const token = localStorage.getItem(ACCESS_TOKEN)

        if(!token){
            setIsAuthorized(false)
            return
        }

        // We'll decode the tokena and check when is the expiration date.
        const decode = jwtDecode(token)
        const tokenExpiration = decode.exp
        const now = Date.now() / 1000 //To get it in seconds

        if(tokenExpiration < now){
            await refreshToken()
        }else{
            setIsAuthorized(true)
        }
    }

    if(isAuthorized === null){
        return (
            <div>Loading...</div>
        )
    }
    return isAuthorized ? children : (
            <Navigate to="/login"/>
        )
}

export default ProtectedRoute
