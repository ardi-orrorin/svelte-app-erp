import { writable } from "svelte/store";

const messageStore = writable("");

const socket = new WebSocket("ws://localhost:8000/api/ws");

socket.addEventListener("open", (e) => {
  console.log("open");
});

socket.addEventListener("message", (e) => {
  messageStore.set(e.data);
});

const sendMessage = (m) => {
  socket.send(m);
};

export default {
  subscribe: messageStore.subscribe,
  sendMessage: sendMessage,
};
