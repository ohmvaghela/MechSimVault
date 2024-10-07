import React, { createContext, useContext } from 'react';

export const UserStateContext = createContext({
  stat: false,
  setStat: () => {},
});

export const UserDataContext = createContext({
  userData: [],
  setUserData: () => {},
});

export const BackendUrlContext = createContext({
  backendUrl: "",
  setBackendUrl: () => {},
});

export function useBackendUrlContext(){
  const backendUrlContext = useContext(BackendUrlContext);
  if(backendUrlContext.backendUrl === undefined){
    throw new Error('backendUrl undefined');
  }
  if(backendUrlContext.setBackendUrl === undefined){
    throw new Error('setBackendUrl undefined');
  }
  return backendUrlContext;
}

export function useUserContext(){
  const userContext = useContext(UserStateContext);
  if(userContext.stat === undefined){
    throw new Error('stat undefined');
  }
  if(userContext.setStat === undefined){
    throw new Error('setStat undefined');
  }
  return userContext;
}

export function useUserDataContext(){
  const userContext = useContext(UserDataContext);
  if(userContext.userData === undefined){
      throw new Error('userData not defined');
  }
  if(userContext.setUserData === undefined){
      throw new Error('setUserData not defined');
  }
  return userContext;
}
