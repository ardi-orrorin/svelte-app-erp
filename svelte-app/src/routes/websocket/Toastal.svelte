<script>
  import { fade } from "svelte/transition";
  export let message;
  export let index;
  export let messages;
  let min = 0;
  let sec = 0;
  setInterval(() => {
    sec += 1;
    if (sec % 60 === 0) {
      min += 1;
      sec = 0;
    }
  }, 1000);
  const sublist = () => {
    messages = messages.filter((e) => e !== message);
  };
</script>

<div
  id={"liveToast" + index}
  class="toast "
  role="alert"
  aria-live="assertive"
  aria-atomic="true"
  on:click={async () => await sublist()}
>
  <div class="toast-header" transition:fade>
    <strong class="me-auto">Notify</strong>
    <small>{min} Miunuts {sec} Seonds</small>
    <!-- <button
      type="button"
      class="btn-close"
      data-bs-dismiss="toast"
      aria-label="Close"
      on:click|preventDefault={() => sublist()}
    /> -->
  </div>
  <div class="toast-body">{message}</div>
</div>

<style>
</style>
