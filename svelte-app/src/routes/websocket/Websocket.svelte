<script>
  import { onMount } from "svelte";
  import store from "./store";
  import { fade } from "svelte/transition";

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
  const delM = (message) => {
    messages = messages.filter((e) => e !== message);
  };
</script>

<p>{messages.length - 1}</p>
<input type="text" bind:value={message} />
<button id="summit" on:click|preventDefault={sendM}>send</button>

{#each messages as message}
  {#if message}
    <li transition:fade on:click={() => delM(message)}>&nbsp;&nbsp; {message}</li>
  {/if}
{/each}

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
