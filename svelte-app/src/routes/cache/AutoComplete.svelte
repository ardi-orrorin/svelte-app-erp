<script>
  import axios from "axios";
  import { serverhost } from "../../Store";

  $: url = serverhost + "/api/sqlcache/cache_name";
  $: keyword = "";
  $: result = axios({ method: "get", url: url, params: { name: keyword } }).then((res) => res.data);
</script>

<input type="text" bind:value={keyword} class="w-100" />
{#await result then result}
  <ul>
    {#each result?.result as item}
      <li on:click={() => (keyword = item)}>
        {item.toLowerCase().indexOf(keyword.toLowerCase()) === 0
          ? ""
          : item.toLowerCase().split(keyword.toLowerCase())[0]}<span class="test">{keyword}</span>{item
          .toLowerCase()
          .indexOf(keyword.toLowerCase()) !== 0 && item.toLowerCase().split(keyword.toLowerCase())[1] === undefined
          ? ""
          : item.toLowerCase().split(keyword.toLowerCase())[1]}
      </li>
    {/each}
  </ul>
{/await}

<style>
  .test {
    color: blue;
    font-weight: bold;
  }
  li {
    padding: 5px;
    list-style: none;
    width: 500px;
    height: 50px;
    vertical-align: middle;
    border-bottom: 0.2px solid rgba(0, 0, 0, 0.2);

    vertical-align: middle;
  }
  li:hover {
    background-color: rgba(100, 100, 100, 0.2);
  }
</style>
