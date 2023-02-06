import { writable } from "svelte/store";
import axios from "axios";

export const host = "http://192.168.0.49:8000";
export let serverhost;
axios
  .get(host + "/api/check")
  .then((res) => {
    if (res.status === 200) {
      serverhost = "http://192.168.0.49:8000";
    }
  })
  .catch((serverhost = "http://192.168.0.49:8001"));

export const isLogin = writable(true);
export const Account = writable("account");
export const pathName = writable("/");
export const popUp = writable(false);
export const selecttable = writable();
export const ascRegExp = new RegExp(/asc/);
export const descRegExp = new RegExp(/desc/);
export const userID = writable(15);
export const storeParams = writable({
  page: 0,
  size: 20,
  order: "create_date-desc",
  startdate: new Date(),
  enddate: new Date(),
  keyword: "",
});

export const dbdetailExpendParams = writable({ order: "create_date-desc", keyword: "" });
let winpopup;
const screenWidth = window.screen.availWidth * (2 / 5);

export const winPopup = (path) => {
  if (winpopup) {
    winpopup.close();
  }
  winpopup = window.open(
    path,
    "_blank",
    "width = 450,height = 630, top=400 location=no, menubar=no, toolbar=no,resizeable=no,status=no, left=" + screenWidth
  );

  winpopup.focus();
};
export const winPopup900 = (path) => {
  if (winpopup) {
    winpopup.close();
  }
  winpopup = window.open(
    path,
    "_blank",
    "width = 900,height = 650, top=400 location=no, menubar=no, toolbar=no,resizeable=no,status=no, left=" + screenWidth
  );
  winpopup.focus();
};
