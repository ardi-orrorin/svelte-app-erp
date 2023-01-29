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
  import { location } from "svelte-spa-router";

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
  };

  window.onkeyup = (e) => {
    if (document.activeElement.tagName === "INPUT" || document.activeElement.tagName === "TEXTAREA") {
      switch (e.key) {
        case "Escape":
          $storeParams.keyword = "";
          document.getElementById("search").blur();
          break;
      }
    } else {
      switch (e.key) {
        case "Enter":
          if ($location === "/notice/create") {
            document.getElementById("summit").click();
          }
          document.getElementById("search").focus();

          break;
        case "h":
          document.getElementById("HOME").click();
          break;
        case "t":
          document.getElementById("TABLE").click();
          break;
        case "n":
          document.getElementById("NOTICE").click();
          break;
        case "p":
          document.getElementById("PAYMENT").click();
          break;
        case "d":
          document.getElementById("DB").click();
          break;
        case "s":
          document.getElementById("startdate").focus();
          break;
        case "e":
          document.getElementById("enddate").focus();
          break;
        case "c":
          document.getElementById("create").click();
          break;
        case "1":
          if ($location === "/notice/create") {
            document.getElementById("important").click();
            console.log(document.activeElement.tagName);
            break;
          }
          $storeParams.size = 10;
          break;
        case "2":
          if ($location === "/notice/create") {
            document.getElementById("pin").click();
            break;
          }
          $storeParams.size = 20;

          break;
        case "3":
          $storeParams.size = 50;

          break;
        case "4":
          $storeParams.size = 100;

          break;
        case "ArrowLeft":
          document.getElementById("prev").click();
          break;
        case "ArrowRight":
          document.getElementById("next").click();
          break;
      }
    }
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
