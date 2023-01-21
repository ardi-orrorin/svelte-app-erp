import { writable } from "svelte/store";

export const isLogin = writable(true);
export const Account = writable("account");
export const pathName = writable("/");
