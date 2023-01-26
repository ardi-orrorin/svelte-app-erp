<script>
  import { DateInput, localeFromDateFnsLocale } from "date-picker-svelte";
  import { ko } from "date-fns/locale";
  import { winPopup, params } from "../../Store";
  const maxPage = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000];
  $: locale = localeFromDateFnsLocale(ko);
</script>

<div>
  <div class="row st">
    <div class="cal me-3">
      <DateInput bind:value={$params.startdate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="cal">
      <DateInput bind:value={$params.enddate} {locale} format="yyyy-MM-dd" />
    </div>
    <div class="col d-flex justify-content-center">
      <div class="col-10">
        <input
          type="text"
          id="tablesearch"
          class="form-control text-center"
          bind:value={$params.keyword}
          placeholder="Search"
        />
      </div>
    </div>
    <div class="sel me-3">
      <select class="form-select" aria-label="Default select example" bind:value={$params.size}>
        {#each maxPage as page}
          <option value={page}>{page}</option>
        {/each}
      </select>
    </div>
    <div class="btn1 me-4">
      <button class="btn1 btn btn-outline-secondary" type="button" on:click={() => winPopup("#/db/create")}
        >Create</button
      >
    </div>
  </div>
</div>

<style>
  .cal {
    width: 120px;
  }
  .sel {
    width: 120px;
    padding-left: 11px;
    padding-right: 0px;
  }

  .st {
    position: sticky;
    top: 0;
  }
  .btn1 {
    width: 120px;
  }
</style>
