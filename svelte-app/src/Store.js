import { writable } from "svelte/store";

export const isLogin = writable(true);
export const Account = writable("account");
export const pathName = writable("/");
export const popUp = writable(false);

let winpopup;
const screenWidth = window.screen.availWidth * (2 / 5);
export const winPopup = (path) => {
  if (winpopup) {
    winpopup.close();
  }
  winpopup = window.open(
    path,
    "_blank",
    "width = 450,height = 600, top=400 location=no, menubar=no, toolbar=no,resizeable=no,status=no, left=" + screenWidth
  );
  winpopup.focus();
};
