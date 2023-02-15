import { writable } from "svelte/store";

const messageStore = writable("");
const username = "test";

let team = "all";
const hostserver = "ws://localhost:8000/api/ws";
let socket = new WebSocket(hostserver + "?username=" + username + "&team=" + team);

socket.addEventListener("open", (e) => {
  console.log("open");
});

socket.addEventListener("message", (e) => {
  messageStore.set(e.data);
});

const sendMessage = (m, name, teamname) => {
  let sendjson = JSON.stringify({ message: m, username: name, team: teamname });

  socket.send(sendjson);
};

export default {
  subscribe: messageStore.subscribe,
  sendMessage: sendMessage,
  username: username,
};
