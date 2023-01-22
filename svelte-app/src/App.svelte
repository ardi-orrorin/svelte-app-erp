<script>
  import Footer from "./routes/Footer.svelte";
  import Header from "./routes/Header.svelte";
  import Menu from "./routes/Menu.svelte";
  import Account from "./routes/account/Account.svelte";
  import Main from "./routes/Main.svelte";
  import Table from "./routes/table/Table.svelte";
  import Db from "./routes/db/Db.svelte";
  import Router from "svelte-spa-router";
  import "bootstrap/dist/css/bootstrap.min.css";
  import { isLogin, popUp } from "./Store.js";
  import Dbdetail from "./routes/db/Dbdetail.svelte";

  const routes = {
    "/": Main,
    "/table": Table,
    "/table/:": Table,
    "/table/:/:": Table,
    "/db": Db,
    "/db/create": Dbdetail,
    "/db/:": Db,
    "/db/id/:": Dbdetail,
  };
</script>

<div>
  {#if !$isLogin}
    <Account />
  {:else}
    <div>
      {#if !$popUp}
        <header><Header /></header>
        <nav><Menu /></nav>
      {/if}
      <main><Router {routes} /></main>
      {#if !$popUp}
        <footer><Footer /></footer>
      {/if}
    </div>
  {/if}
</div>

<style>
  header {
    width: 100%;
  }
  main {
    width: 100%;
    margin-top: 1em;
    margin-bottom: 1em;
  }

  footer {
    width: 100%;
    height: 4em;
  }
  div {
    overflow: hidden;
  }
</style>
