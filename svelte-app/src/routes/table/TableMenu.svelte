<script>
  import { pathName } from "../../Store";
  const menuItems = [
    { name: "Total", link: "#/table/total" },
    { name: "NEW", link: "#/table/new" },
    { name: "DELETE", link: "#/table/delete" },
    { name: "4", link: "#/table/4" },
    { name: "5", link: "#/table/5" },
    { name: "6", link: "#/table/6" },
  ];
  let toggle = false;
</script>

<div class="list-group list-group-flush">
  <div>
    <a class="d-flex justify-content-between list-group-item list-group-item-action" on:click={() => (toggle = !toggle)}
      >M E N U<span>{!toggle ? "▼" : "▲"}</span></a
    >

    {#if toggle}
      {#each menuItems as menuItem}
        <a
          class="d-flex justify-content-between list-group-item list-group-item-action  {$pathName === menuItem.link
            ? 'active'
            : ''}"
          href={menuItem.link}
          on:click={() => ($pathName = menuItem.link)}
          >{menuItem.name}

          <span class="badge bg-danger rounded-pill">14</span>
        </a>
      {/each}
    {/if}
  </div>
</div>

<style>
  .list-group-item {
    color: black;
  }
  .active {
    color: white;
    background-color: rgba(0, 0, 0, 0.1) !important;
    border: 1px rgba(0, 0, 0, 0.4) !important;
    transition: 0.2s;
  }
</style>
