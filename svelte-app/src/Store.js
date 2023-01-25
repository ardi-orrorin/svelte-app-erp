import { writable } from "svelte/store";
export const serverhost = "http://localhost:8000";
export const isLogin = writable(true);
export const Account = writable("account");
export const pathName = writable("/");
export const popUp = writable(false);
export const selecttable = writable();
export const ascRegExp = new RegExp(/asc/);
export const descRegExp = new RegExp(/desc/);
export const params = writable({
  page: 0,
  size: 10,
  order: "id-desc",
  startdate: new Date(new Date().setDate(new Date().getDate() - 10)),
  enddate: new Date(),
  keyword: "",
  select_keyworld: "body",
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
    "width = 450,height = 585, top=400 location=no, menubar=no, toolbar=no,resizeable=no,status=no, left=" + screenWidth
  );
  winpopup.focus();
};
