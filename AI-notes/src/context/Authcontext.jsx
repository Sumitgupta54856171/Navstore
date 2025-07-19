import {useState,useEffect,createContext} from 'react';
export const UserContext = createContext();

export const UserProvider = ({children})=>{
    const [user,setUser] = useState(false);
useEffect(()=>{
   const checkAuthentication=async ()=>{
    const response = await axios.get('http://localhost:8000/api/token', {withCredentials: true});
    console.log(response);
    console.log(response.data)
    console.log('successfull');
    if(response.data.user.username !== null && response.data.user.username !== undefined){
        setUser(true);
    }
}
checkAuthentication();
},[user])
    return(
        <UserContext.Provider value={{user,}}>
            {children}
        </UserContext.Provider>
    )
}