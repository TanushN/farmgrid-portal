// Api.js
import axios from "axios";
import { API_URL } from "./api_config";
import { user } from "../stores";

axios.defaults.withCredentials = true

// Create a instance of axios to use the same base url.
const axiosAPI = axios.create({
  baseURL : API_URL, 
});

// implement a method to execute all the request from here.
const apiRequest = (method, url, request, times_tried = 0) => {
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
        return Promise.resolve(res.data);
      })
      .catch(err => {
        // if(times_tried >= 0){
        //   return Promise.reject(err);
        // }
        if(err.response.status == 401 || err.response.status == 422){
          localStorage.removeItem("user");
          user.set(null);
        }
        return Promise.reject(err);
      });
};

// function to execute the http get request
const get = async (url: string, request) => apiRequest("get", url, request);

// function to execute the http delete request
const deleteRequest = (url, request) =>  apiRequest("delete", url, request);

// function to execute the http post request
const post = (url, request) => apiRequest("post", url, request);

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