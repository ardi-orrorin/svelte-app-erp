<script>
  import { pathName } from "../Store";

  const menuItems = [
    { id: "HOME", name: "HOME(H)", link: "#/", hotkey: "h" },
    { id: "TABLE", name: "TABLE(T)", link: "#/table/0", hotkey: "t" },
    { id: "PAYMENT", name: "PAYMENT(P)", link: "#/payment", hotkey: "p" },
    { id: "NOTICE", name: "NOTICE(N)", link: "#/noticelist", hotkey: "n" },
    { id: "DB", name: "DB(D)", link: "#/db", hotkey: "d" },
    { id: "STATISTICS", name: "STATISTICS(S)", link: "#/statistics", hotkey: "s" },
  ];
</script>

<div>
  <ul class="nav nav-tabs justify-content-start">
    {#each menuItems as menuItem}
      <li
        id={menuItem.id}
        class="nav-item"
        on:click={() => {
          $pathName = menuItem.link;
          window.location.href = menuItem.link;
        }}
      >
        <a class="nav-link {menuItem.link === $pathName ? 'active' : ''}" aria-current="page"
          ><h4>{menuItem.name}</h4></a
        >
      </li>
    {/each}
  </ul>
</div>

<style>
  a {
    color: black;
  }
  .active {
    color: white !important;
    background-color: rgba(0, 0, 0, 0.1) !important;
  }
  .nav-link:hover {
    text-decoration: none;
    color: white !important;
    background-color: rgba(0, 0, 0, 0.1) !important;
  }
</style>
