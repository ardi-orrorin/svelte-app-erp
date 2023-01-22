<script>
  import { onMount } from "svelte";
  import { popUp } from "../../Store";
  let writeMode = true;
  onMount(() => ($popUp = !$popUp));
  const writeModeChange = () => {
    writeMode = !writeMode;
  };
  const selectItems = [
    { value: 1, text: "one" },
    { value: 2, text: "two" },
    { value: 3, text: "three" },
    { value: 4, text: "four" },
    { value: 5, text: "five" },
  ];
</script>

<div class="container">
  {#if writeMode}
    <h1 class="text-center" on:click={() => writeModeChange()}><p>Add Table</p></h1>
  {:else}
    <h1 class="text-center" on:click={() => writeModeChange()}><p>Modify Table</p></h1>
  {/if}

  <div>
    <p>
      <input type="text" class="form-control form-control-sm" placeholder="name" disabled={writeMode ? false : true} />
    </p>
  </div>
  <div>
    <p>
      <input
        type="text"
        class="form-control form-control-sm"
        placeholder="phone-number"
        disabled={writeMode ? false : true}
      />
    </p>
  </div>
  <div>
    <p>
      <input
        type="text"
        class="form-control form-control-sm"
        placeholder="phone-number"
        disabled={writeMode ? false : true}
      />
    </p>
  </div>
  <div>
    <p>
      <select
        class="form-select form-select-sm"
        aria-label=".form-select-sm example"
        disabled={writeMode ? false : true}
      >
        {#each selectItems as selectItem}
          <option value={selectItem.value}>{selectItem.text}</option>
        {/each}
      </select>
    </p>
  </div>
  <div>
    <p>
      <input
        type="text"
        class="form-control form-control-sm"
        placeholder="address"
        disabled={writeMode ? false : true}
      />
    </p>
  </div>
  <div>
    <p>
      <input
        type="text"
        class="form-control form-control-sm"
        placeholder="address-detail"
        disabled={writeMode ? false : true}
      />
    </p>
  </div>
  <div>
    <p>
      <textarea
        rows="6"
        type="text"
        class="form-control form-control-sm"
        placeholder="contents"
        disabled={writeMode ? false : true}
      />
    </p>
  </div>
  <div class="row">
    {#if writeMode}
      <div class="col text-center"><button class="btn">등록</button></div>
    {:else}
      <div class="col text-end"><button class="btn">수정</button></div>
      <div class="col"><button class="btn">삭제</button></div>
    {/if}
  </div>
</div>

<style>
  div {
    overflow: hidden;
  }
</style>
