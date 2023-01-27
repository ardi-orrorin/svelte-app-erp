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
  import Notice from "./routes/notice/Notice.svelte";
  import Noticelist from "./routes/notice/Noticelist.svelte";

  const routes = {
    "/": Main,
    "/table": Table,
    "/table/:": Table,
    "/table/:/:": Table,
    "/db": Db,
    "/db/create": Dbdetail,
    "/db/:": Db,
    "/db/id/:": Dbdetail,
    "/noticelist": Noticelist,
    "/notice/create": Notice,
    "/notice/id/:": Notice,
  };
</script>

{#if !$isLogin}
  <Account />
{:else}
  <div>
    {#if !$popUp}
      <div>
        <header><Header /></header>
      </div>
      <div>
        <nav><Menu /></nav>
      </div>
    {/if}
    <main><Router {routes} /></main>
    {#if !$popUp}
      <footer><Footer /></footer>
    {/if}
  </div>
{/if}

<style>
  header {
    width: 99%;
  }
  main {
    width: 99%;
    margin-top: 1em;
  }

  footer {
    width: 99%;
    height: 4em;
  }
</style>
