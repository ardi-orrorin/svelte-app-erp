<script>
  import Tabletotal from "./Tabletotal.svelte";
  import TableMenu from "./TableMenu.svelte";
  import Router from "svelte-spa-router";
  import { fade } from "svelte/transition";

  const routes = { "/table": Tabletotal, "/table/total": Tabletotal };
</script>

<div class="row pb-3 db" transition:fade>
  <div class="menu"><TableMenu /></div>
  <div class="col">
    <Router {routes} />
  </div>
</div>

<style>
  .menu {
    width: 15em;
    margin: 0.5em;
  }
  .db {
    min-width: 800px;
  }
</style>
