<script>
  import Tabletotal from "./Tabletotal.svelte";
  import TableMenu from "./TableMenu.svelte";
  import Router from "svelte-spa-router";

  import TableHeader from "./TableHeader.svelte";
  const routes = {
    "/table": Tabletotal,
    "/table/total": Tabletotal,
    "/table/total/:": Tabletotal,
  };
</script>

<div class="row pb-3 db">
  <div class="menu"><TableMenu /></div>
  <div class="col">
    <div class="tablesticky mb-2">
      <TableHeader />
    </div>
    <div>
      <Router {routes} />
    </div>
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

  .tablesticky {
    position: sticky;
    top: 0px;
    background-color: white;
    height: 50px;
    padding-top: 5px;
  }
</style>
