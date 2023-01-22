<script>
  import Tabletotal from "./Tabletotal.svelte";
  import TableMenu from "./TableMenu.svelte";
  import Router from "svelte-spa-router";
  import { fade } from "svelte/transition";
  import TableHeader from "./TableHeader.svelte";
  const routes = {
    "/table": Tabletotal,
    "/table/total": Tabletotal,
    "/table/total/:": Tabletotal,
  };
</script>

<div class="row pb-3 db" transition:fade>
  <div class="menu"><TableMenu /></div>
  <div class="col">
    <TableHeader />
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
