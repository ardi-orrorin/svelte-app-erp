<script>
  import { pathName } from "../../Store";
  const menuItems = [
    { name: "TOTAL", link: "#/table/total" },
    { name: "DIRECTOR", link: "#/table/director" },
    { name: "DELETE", link: "#/table/delete" },
    { name: "4", link: "#/table/4" },
    { name: "5", link: "#/table/5" },
    { name: "6", link: "#/table/6" },
  ];
  let toggle = true;
</script>

<div class="list-group">
  <div>
    <a class="d-flex justify-content-between list-group-item list-group-item-action" on:click={() => (toggle = !toggle)}
      >M E N U</a
    >

    {#each menuItems as menuItem}
      <a
        class="d-flex justify-content-between list-group-item list-group-item-action  {$pathName === menuItem.link
          ? 'bg-secondary text-white'
          : ''}"
        href={menuItem.link}
        on:click={() => ($pathName = menuItem.link)}
        >{menuItem.name}

        <span class="badge bg-danger rounded-pill">14</span>
      </a>
    {/each}
  </div>
</div>

<style>
  .list-group-item {
    color: black;
  }
</style>
