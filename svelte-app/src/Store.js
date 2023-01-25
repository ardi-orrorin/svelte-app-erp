import { writable } from "svelte/store";

export const isLogin = writable(true);
export const Account = writable("account");
export const pathName = writable("/");
export const popUp = writable(false);
export const selecttable = writable();
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

export const dateFomat = (date) => {
  date = new Date(date);
  let year = date.getFullYear().toString();
  let month = date.getMonth() + 1;
  month < 10 ? (month = "0" + month.toString()) : (month = month.toString());
  let day = date.getDate();
  day < 10 ? (day = "0" + day.toString()) : (day = day.toString());
  let hour = date.getHours();
  hour < 10 ? (hour = "0" + hour.toString()) : (hour = hour.toString());
  let minutes = date.getMinutes();
  minutes < 10 ? (minutes = "0" + minutes.toString()) : (minutes = minutes.toString());
  let seconds = date.getSeconds();
  seconds < 10 ? (seconds = "0" + seconds.toString()) : (seconds = seconds.toString());

  return year + "-" + month + "-" + day + "\n" + hour + ":" + minutes + ":" + seconds;
};
