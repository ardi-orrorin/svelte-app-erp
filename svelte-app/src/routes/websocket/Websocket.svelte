<script>
  import { onMount } from "svelte";
  import store from "./store";

  import Toastal from "./Toastal.svelte";
  import Toast from "bootstrap/js/src/toast";

  let message = "";
  let messages = [];

  onMount(() => {
    store.subscribe((currentMessage) => {
      messages = [...messages, currentMessage];
    });
  });

  const sendM = () => {
    if (message.length > 0) {
      store.sendMessage(message);
      message = "";
    }
  };

  const toast = (index) => {
    const toastLiveExample = document.getElementById("liveToast" + index);
    const toast = new Toast(toastLiveExample);
    toast.show();
  };
</script>

<p>{messages.length - 1}</p>
<input type="text" bind:value={message} />
<button id="summit" on:click|preventDefault={sendM}>send</button>
<div aria-live="polite" aria-atomic="true" class="position-relative">
  <div class="toast-container top-0 end-0 p-3">
    {#each messages as message, index}
      {#if message}
        <div on:load={toast(index)} />
        <Toastal {message} bind:messages {index} />
      {/if}
    {/each}
  </div>
</div>

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
