<script>
  import { onMount } from "svelte";
  import store from "./store";
  import Toastal from "./Toastal.svelte";
  import Toast from "bootstrap/js/src/toast";
  import { fade } from "svelte/transition";

  let message = "";
  let messages = [];
  let count = 0;
  let users = [];
  $: closeuser = "";
  onMount(() => {
    store.subscribe((currentMessage) => {
      console.log(currentMessage);
      if (currentMessage.count) {
        count = currentMessage.count;
        users = currentMessage.users;
        closeuser = currentMessage.disuser;
      }
      if (currentMessage.message) {
        messages = [...messages, currentMessage];
      }
    });
  });

  const sendM = () => {
    if (message.length > 0) {
      store.sendMessage(message, "ch01");
      message = "";
    }
  };

  const toast = (index) => {
    const toastLiveExample = document.getElementById("liveToast" + index);
    const toast = new Toast(toastLiveExample);
    toast.show();
  };
</script>

<h1>현재 계정 아이디 : {store.username}</h1>
<h1>총 연결수 : {count}, 접속 계정 수 : {users.length}</h1>
<h2>접속 아이디 : {users}</h2>
<p>{messages.length}</p>
<input type="text" bind:value={message} />
<button id="summit" on:click|preventDefault={sendM}>send</button>

<div aria-live="polite" aria-atomic="true" class="position-relative">
  <div class="toast-container top-0 end-0 p-3" transition:fade>
    {#each messages as message, index}
      {#if message}
        <div on:load={toast(index)} />
        <Toastal {message} {index} />
      {/if}
    {/each}
  </div>
</div>
<p />
<h1>마지막 종료한 사용자 : {closeuser}</h1>

<style>
  li {
    margin: 10px;

    padding-left: 5;
    display: flex;
    justify-content: left;
    align-items: center;
    width: 400px;
    height: 40px;
    border-left: 5px solid rgba(0, 0, 0, 0.2);
    list-style: none;
  }
  li:hover {
    background-color: rgba(0, 0, 0, 0.2);
  }
</style>
