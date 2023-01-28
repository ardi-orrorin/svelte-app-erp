<script>
  import { fade } from "svelte/transition";
  import Noticemini from "./notice/Noticemini.svelte";

  $: noticeToggle = true;
</script>

<div class="row m-3 d-flex justify-content-center">
  {#if noticeToggle}
    <div class="col shadow m-2 component" transition:fade><Noticemini bind:noticeToggle /></div>
  {/if}
  {#if noticeToggle}
    <div class="col shadow m-2 component" transition:fade><Noticemini bind:noticeToggle /></div>
  {/if}
</div>

<style>
  .row {
    height: 30em;
  }

  .component {
    border: 2px rgba(0, 0, 0, 1);
    width: 500px;
    min-width: 500px;
    max-width: 500px;
  }
</style>
