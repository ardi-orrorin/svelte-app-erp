<script>
  import DbMenu from "./DbMenu.svelte";
  import Dbcontents from "./Dbcontents.svelte";
  import Router from "svelte-spa-router";

  const routes = { "/db": Dbcontents, "/db/1": Dbcontents };
</script>

<div class="row pb-3">
  <div class="menu"><DbMenu /></div>
  <div class="col">
    <Router {routes} />
  </div>
</div>

<style>
  .menu {
    width: 15em;
    margin: 0.5em;
  }
</style>
