import { writable } from 'svelte/store';

export const user = writable(localStorage.getItem('user'));
export const access_token = writable(localStorage.getItem('access_token'));
export const refresh_token = writable(localStorage.getItem('refresh_token'));
export const theme = writable(localStorage.getItem('theme') ?? "g10")