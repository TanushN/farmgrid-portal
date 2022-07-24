// Api.js
import axios from "axios";
import { API_URL } from "./api_config";

import { access_token, refresh_token } from "../stores";

axios.defaults.withCredentials = true

// Create a instance of axios to use the same base url.
const axiosAPI = axios.create({
  baseURL : API_URL, 
});

// implement a method to execute all the request from here.
const apiRequest = (method, url, request, useAuth = true, times_called = 0) => {
    const headers = {};
    //using the axios instance to perform the request that received from each http method
    return axiosAPI({
        method,
        url,
        data: request,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'Content-Type': 'application/json'
        }
      }).then(res => {
        if(!useAuth) {
          axiosAPI.defaults.headers['x-csrf-token'] = res.data.csrf_token;
        }
        return Promise.resolve(res.data);
      })
      .catch(err => {
        return Promise.reject(err);
      });
};

// function to execute the http get request
const get = async (url: string, request) => apiRequest("get", url, request);

// function to execute the http delete request
const deleteRequest = (url, request) =>  apiRequest("delete", url, request);

// function to execute the http post request
const post = (url, request, useAuth = true) => apiRequest("post", url, request, useAuth);

// function to execute the http put request
const put = (url, request) => apiRequest("put", url, request);

// function to execute the http path request
const patch = (url, request) =>  apiRequest("patch", url, request);

// expose your method to other services or actions
const API ={
    get,
    delete: deleteRequest,
    post,
    put,
    patch
};
export default API;