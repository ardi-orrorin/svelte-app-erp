import { writable } from "svelte/store";

const messageStore = writable("");
const username = "chenkathleen";
const channel = "ch01";
const hostserver = "ws://localhost:8000/api/ws";
let socket = new WebSocket(hostserver + "?username=" + username + "&channel=" + channel);

socket.addEventListener("open", (e) => {
  console.log("open");
});

socket.addEventListener("message", (e) => {
  messageStore.set(e.data);
});

const sendMessage = (m, channel) => {
  let send = JSON.stringify({ message: m, channel: channel, create_date: new Date() });

  socket.send(send);
};

export default {
  subscribe: messageStore.subscribe,
  sendMessage: sendMessage,
  username: username,
};
