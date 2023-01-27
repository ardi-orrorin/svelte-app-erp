<script>
  import Noticemini from "./notice/Noticemini.svelte";
</script>

<div class="row m-3 d-flex justify-content-center">
  <div class="col shadow m-2 component"><Noticemini /></div>
  <div class="col shadow m-2 component"><Noticemini /></div>
</div>

<style>
  .row {
    height: 30em;
  }
  /* div {
    border: 1px solid red;
  } */
  .component {
    border: 2px rgba(0, 0, 0, 1);
    width: 500px;
    min-width: 500px;
    max-width: 500px;
  }
</style>
