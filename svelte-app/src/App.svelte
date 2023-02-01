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
  import { isLogin, popUp, storeParams } from "./Store.js";
  import Dbdetail from "./routes/db/Dbdetail.svelte";
  import Notice from "./routes/notice/Notice.svelte";
  import Noticelist from "./routes/notice/Noticelist.svelte";
  import Noticenew from "./routes/notice/Noticenew.svelte";
  import Paymentlist from "./routes/payment/Paymentlist.svelte";
  import Payment from "./routes/payment/Payment.svelte";
  import Statistics from "./routes/statistics/Statistics.svelte";
  import Hotkey from "./Hotkey.svelte";

  const routes = {
    "/": Main,
    "/table": Table,
    "/table/:": Table,
    "/db": Db,
    "/db/create": Dbdetail,
    "/db/:": Db,
    "/db/id/:id": Dbdetail,
    "/noticelist": Noticelist,
    "/notice/create": Noticenew,
    "/notice/id/:id": Notice,
    "/payment": Paymentlist,
    "/payment/id/:id": Payment,
    "/statistics": Statistics,
  };
</script>

<Hotkey />
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
