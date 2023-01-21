<script>
  import { pathName } from "../Store";
  import { fade } from "svelte/transition";

  const menuItems = [
    { name: "HOME", link: "#/" },
    {
      name: "TABLE",
      link: "#/table",
    },
    {
      name: "PAGE2",
      link: "#/2",
    },
    {
      name: "PAGE3",
      link: "#/3",
    },
    {
      name: "DB",
      link: "#/db",
    },
  ];
</script>

<div transition:fade>
  <ul class="nav nav-tabs justify-content-start">
    {#each menuItems as menuItem}
      <li class="nav-item">
        <a
          class="nav-link {menuItem.link === $pathName ? 'active' : ''}"
          aria-current="page"
          href={menuItem.link}
          on:click={() => ($pathName = menuItem.link)}><h4>{menuItem.name}</h4></a
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
