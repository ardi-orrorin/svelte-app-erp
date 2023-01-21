<script>
  import Footer from "./routes/Footer.svelte";
  import Header from "./routes/Header.svelte";
  import Menu from "./routes/Menu.svelte";
  import Login from "./routes/Login.svelte";
  import Main from "./routes/Main.svelte";
  import Table from "./routes/Table.svelte";
  import Db from "./routes/DB/Db.svelte";
  import Router from "svelte-spa-router";
  import "bootstrap/dist/css/bootstrap.min.css";
  import { isLogin } from "./Store.js";
  import { fade } from "svelte/transition";

  const routes = {
    "/": Main,
    "/table": Table,
    "/db": Db,
    "/db/:": Db,
  };
</script>

<div transition:fade>
  <button on:click={() => ($isLogin = !$isLogin)}>islogin</button>

  {#if !$isLogin}
    <Login />
  {:else}
    <div>
      <header><Header /></header>
      <nav><Menu /></nav>
      <main transition:fade><Router {routes} /></main>
      <footer><Footer /></footer>
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
</style>
