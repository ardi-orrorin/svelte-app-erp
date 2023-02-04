<script>
  import { onMount } from "svelte";
  import { popUp, serverhost } from "../../Store";
  import DbDetailexpend from "./DbDetailexpend.svelte";
  import axios from "axios";
  import Paymentnew from "../payment/Paymentnew.svelte";

  onMount(() => ($popUp = !$popUp));

  export let params;

  $: deatilPage = "";
  $: url = serverhost + "/api/customerdetail/detail/" + params.id;
  $: data = axios({ method: "get", url: url }).then((res) => res.data);

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
    window.resizeBy(500, 0);
    toggle = true;
  };
  const windowReduce = () => {
    window.resizeBy(-500, 0);
    toggle = false;
  };

  const viewChange = (currentPage, newPage) => {
    if (!deatilPage & !toggle) {
      windowExpend();
      deatilPage = newPage;
    } else if ((deatilPage === currentPage) & toggle) {
      deatilPage = newPage;
    } else {
      windowReduce();
      deatilPage = "";
    }
  };
  const bodyFocus = () => {
    document.getElementById("dbdetailbody").focus();
  };
</script>

{#await data then data}
  <div class="row overflow-hidden">
    <div class="inputwidth">
      <div class="inputwidth">
        {#if !writeMode}
          <h1 class="text-center">TABLE</h1>
        {:else}
          <h1 class="text-center">NEW TABLE</h1>
        {/if}
      </div>
      <form>
        <div class="inputwidth p-0">
          <div class="row">
            <div class="col">
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
            {#if !writeMode}
              <div class="col-3 p-0">
                <button
                  id="dbdetail"
                  class="btn1"
                  on:click|preventDefault={() => {
                    viewChange("payment", "dbdetail");
                  }}>내역 조회(1)</button
                >
              </div>
            {/if}
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
              id="dbdetailbody"
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
                <input
                  id="dbdetailnew"
                  type="button"
                  class="new"
                  value="새로등록(n)"
                  on:click|preventDefault={async () => {
                    writeMode = !writeMode;
                    data.body = "";
                    data.addressdetail = "";
                    data.address = "";
                    data.create_date = "";
                    data.phonenumber = "";
                    data.name = "";

                    await viewChange("dbdetail", "payment");
                    bodyFocus();
                  }}
                />
              </div>
            {:else}
              <div class="col text-center">
                <button
                  class="new"
                  on:click={() => {
                    window.close();
                  }}>등록하기</button
                >
              </div>
              <!-- <div class="col"><button class="btn">삭제</button></div> -->
            {/if}
          </div>
        </div>
      </form>
    </div>
    {#if toggle}
      <div class="col">
        {#if deatilPage === "dbdetail"}
          <DbDetailexpend customer_id={data.customer_id} bind:id={params.id} num={params.id} bind:writeMode />
        {:else if deatilPage === "payment"}
          <Paymentnew id={params.id} detail_id={data.id} />
        {/if}
      </div>
    {/if}
  </div>
{/await}

<style>
  h1 {
    font-size: 2.5em;
    margin-bottom: 0.5em;
    letter-spacing: 0.3em;
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
  input:focus {
    outline: 1px solid rgba(98, 105, 113, 0.5);
  }
  textarea:focus {
    outline: 1px solid rgba(98, 105, 113, 0.5);
  }

  .new {
    width: 200px;
    border: 1px solid rgba(98, 105, 113, 1);
    background-color: white;
    color: rgba(98, 105, 113, 1);
    border-radius: 2px;
  }
  .new:hover,
  .new:focus {
    background-color: rgba(98, 105, 113, 1);
    color: white;
  }
</style>
