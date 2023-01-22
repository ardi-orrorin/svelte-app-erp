<script>
  import { onMount } from "svelte";
  import { popUp } from "../../Store";
  import DbDetailexpend from "./DbDetailexpend.svelte";

  let toggle = true;
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

  const windowExpend = () => {
    if (toggle) {
      window.resizeBy(450, 0);
    } else {
      window.resizeBy(-450, 0);
    }
    toggle = !toggle;
  };
</script>

<div class="row overflow-hidden">
  <div class="inputwidth">
    <div>
      {#if writeMode}
        <h1 class="text-center">Add Table</h1>
      {:else}
        <h1 class="text-center">Modify Table</h1>
      {/if}
    </div>
    <div class="inputwidth">
      <div class="row">
        <div class="col-9 pe-1">
          <p>
            <input
              type="text"
              class="form-control form-control-sm"
              placeholder="name"
              disabled={writeMode ? false : true}
            />
          </p>
        </div>
        <div class="col p-0">
          <button
            class="btn1"
            on:click={() => {
              writeModeChange();
              windowExpend();
            }}>내역 {toggle ? ">" : "<"}</button
          >
        </div>
      </div>
    </div>
    <div class="inputwidth">
      <p>
        <input
          type="text"
          class="form-control form-control-sm"
          placeholder="phone-number"
          disabled={writeMode ? false : true}
        />
      </p>
    </div>
    <div class="inputwidth">
      <p>
        <input
          type="text"
          class="form-control form-control-sm"
          placeholder="phone-number"
          disabled={writeMode ? false : true}
        />
      </p>
    </div>
    <div class="inputwidth">
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
    <div class="inputwidth">
      <p>
        <input
          type="text"
          class="form-control form-control-sm"
          placeholder="address"
          disabled={writeMode ? false : true}
        />
      </p>
    </div>
    <div class="inputwidth">
      <p>
        <input
          type="text"
          class="form-control form-control-sm"
          placeholder="address-detail"
          disabled={writeMode ? false : true}
        />
      </p>
    </div>
    <div class="inputwidth">
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
    <div class="inputwidth">
      <div class="row">
        {#if writeMode}
          <div class="col text-center"><button class="btn">등록</button></div>
        {:else}
          <div class="col text-end"><button class="btn">수정</button></div>
          <div class="col"><button class="btn">삭제</button></div>
        {/if}
      </div>
    </div>
  </div>
  {#if !toggle}
    <div class="col"><DbDetailexpend /></div>
  {/if}
</div>

<style>
  h1 {
    font-size: 2.5em;
    margin-bottom: 0.5em;
  }
  .inputwidth {
    width: 27em;
    margin-right: 1em;
  }
  .btn1 {
    width: 8em;
    height: 2.4em;
    background-color: white;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 4px;
    font-size: 0.8em;
  }
</style>
