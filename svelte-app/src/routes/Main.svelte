<script>
  import { fade } from "svelte/transition";
  import { isLogin } from "../Store";
  fade;
</script>

<div class="row">
  <div class="col-4"><p>1</p></div>
  <div class="col-4">2</div>
  <div class="col-4">3</div>
</div>

<style>
  .row {
    height: 30em;
  }
  div {
    border: 1px solid red;
  }
</style>
