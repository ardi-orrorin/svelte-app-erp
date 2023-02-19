import { writable, get } from "svelte/store";
import { host, port, wsprotocal } from "../../Store";

const messageStore = writable("");
/* const userStore = writable(""); */
const username = writable(Math.floor(Math.random() * 10));
const channel = "ch01";
const hostserver = wsprotocal + "://" + host + ":" + port;
/* const hostserver = "wss://tysct.kr:12001/api"; */
let socket = new WebSocket(hostserver + "/api/ws?username=" + get(username) + "&channel=" + channel);
/* let usercount = new WebSocket(hostserver + "/usercount"); */

socket.addEventListener("open", (e) => {
  console.log("open");
});

socket.addEventListener("message", (e) => {
  messageStore.set(JSON.parse(e.data));
});

/* usercount.addEventListener("open", (e) => {
  console.log("usercount open");
});
usercount.addEventListener("message", (e) => {
  userStore.set(e.data);
}); */

const sendMessage = (m, channel) => {
  let send = JSON.stringify({ message: m, channel: channel, create_date: new Date() });
  socket.send(send);
};

export default {
  subscribe: messageStore.subscribe,
  /* usersubscribe: userStore.subscribe, */
  sendMessage: sendMessage,
  username: get(username),
};
