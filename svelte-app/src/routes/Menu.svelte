<script>
  import { pathName } from "../Store";

  const menuItems = [
    { name: "HOME", link: "#/", hotkey: "h" },
    {
      name: "TABLE",
      link: "#/table/0",
      hotkey: "t",
    },
    {
      name: "PAYMENT",
      link: "#/payment",
      hotkey: "p",
    },
    {
      name: "NOTICE",
      link: "#/noticelist",
      hotkey: "n",
    },
    {
      name: "DB",
      link: "#/db",
      hotkey: "d",
    },
    {
      name: "STATISTICS",
      link: "#/statistics",
      hotkey: "s",
    },
  ];
</script>

<div>
  <ul class="nav nav-tabs justify-content-start">
    {#each menuItems as menuItem}
      <li
        id={menuItem.name}
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
