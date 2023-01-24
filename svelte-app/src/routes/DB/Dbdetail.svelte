<script>
  import { onMount } from "svelte";
  import { popUp } from "../../Store";
  import DbDetailexpend from "./DbDetailexpend.svelte";
  import axios from "axios";

  onMount(() => ($popUp = !$popUp));

  $: [num, id, path] = window.location.href.split("/").reverse().slice(0, 3);

  const headers = { accept: "application/json" };
  $: url = "http://localhost:8000/api/customerdetail/detail/" + num;
  $: data = axios({ method: "get", url: url, headers: headers }).then((res) => res.data);

  let toggle = false;
  let writeMode = false;
  const selectItems = [
    { value: 1, text: "one" },
    { value: 2, text: "two" },
    { value: 3, text: "three" },
    { value: 4, text: "four" },
    { value: 5, text: "five" },
  ];

  const windowExpend = () => {
    if (!toggle) {
      window.resizeBy(450, 0);
    } else {
      window.resizeBy(-450, 0);
    }
    toggle = !toggle;
  };
</script>

{#await data then data}
  <div class="row overflow-hidden">
    <div class="inputwidth">
      <div class="inputwidth">
        {#if !writeMode}
          <h1 class="text-center">Table</h1>
        {:else}
          <h1 class="text-center">New Table</h1>
        {/if}
      </div>
      <form>
        <div class="inputwidth">
          <div class="row">
            <div class="col pe-1">
              <p>
                <input
                  type="text"
                  class="form-control form-control-sm"
                  placeholder="name"
                  disabled={writeMode ? false : true}
                  value={data.name}
                />
              </p>
            </div>
            <div class="col-3 p-0">
              <button
                class="btn1"
                on:click|preventDefault={() => {
                  windowExpend();
                }}>내역 {!toggle ? ">" : "<"}</button
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
              value={data.phonenumber}
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
              value={data.create_date}
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
              value={data.address}
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
              value={data.addressdetail}
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
              value={data.body}
            />
          </p>
        </div>

        <div class="inputwidth">
          <div class="row">
            {#if !writeMode}
              <div class="col text-center">
                <button
                  class="btn"
                  on:click|preventDefault={() => {
                    data.body = "";
                    data.addressdetail = "";
                    data.address = "";
                    data.create_date = "";
                    data.phonenumber = "";
                    data.name = "";
                    writeMode = !writeMode;
                  }}>새로등록</button
                >
              </div>
            {:else}
              <div class="col text-center"><button class="btn">등록하기</button></div>
              <!-- <div class="col"><button class="btn">삭제</button></div> -->
            {/if}
          </div>
        </div>
      </form>
    </div>
    {#if toggle}
      <div class="col"><DbDetailexpend customer_id={data.customer_id} bind:id={num} {num} bind:writeMode /></div>
    {/if}
  </div>
{/await}

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
  input:disabled {
    color: black;
    background-color: rgba(0, 0, 0, 0);
  }
  select:disabled {
    color: black;
    background-color: rgba(0, 0, 0, 0);
  }
  textarea:disabled {
    color: black;
    background-color: rgba(0, 0, 0, 0);
  }
</style>
