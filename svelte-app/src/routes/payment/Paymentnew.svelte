<script>
  import { afterUpdate } from "svelte";

  afterUpdate(() => {
    money = Number(money.replaceAll(",", "")).toLocaleString("ko-kr");
    bankANumber = bankANumber.replaceAll("-", "");
  });

  $: money = "";
  $: bankANumber = "";
  $: bankAName = "";
  $: corporateName = "";
  $: paymentSave = false;
  $: selectBank = "SelectBank";
  $: memo = "";
  const bankList = ["SelectBank", "WooriBank", "KBBank", "NH", "KBank"];

  const confirmdata = () => {
    if (!bankAName && !bankANumber && !corporateName && money === "0" && selectBank === "SelectBank") {
      window.alert("수정된 내용이 없습니다");
    } else if (!bankAName || !bankANumber || !corporateName || money === "0" || selectBank === "SelectBank") {
      window.alert("필수 항목이 모두 입력되지 않았습니다");
    } else {
      paymentSave = !paymentSave;
    }
  };
</script>

<h1 class="text-center">PAYMENT</h1>
<form>
  <div class="mt-4 mb-3">
    <select class="w-100" bind:value={selectBank} disabled={!paymentSave ? false : true} required>
      {#each bankList as bank}
        <option value={bank}>{bank}</option>
      {/each}
    </select>
  </div>
  <div class="mt-3 mb-3">
    <input
      class="w-100"
      type="text"
      bind:value={corporateName}
      placeholder="Corparate Name"
      disabled={!paymentSave ? false : true}
      required
    />
  </div>
  <div class="mt-3 mb-3">
    <input
      class="w-100"
      type="text"
      bind:value={bankAName}
      placeholder="Bank Account Name"
      required
      disabled={!paymentSave ? false : true}
    />
  </div>
  <div class="mt-3 mb-3">
    <input
      class="w-100"
      type="text"
      bind:value={bankANumber}
      placeholder="Bank Account Number Excluded Characters {'"-"'}"
      required
      disabled={!paymentSave ? false : true}
    />
  </div>

  <div class="mt-3 mb-3">
    <input
      class="w-100"
      type="text"
      bind:value={money}
      placeholder="Money"
      disabled={!paymentSave ? false : true}
      required
    />
  </div>
  <div>
    <textarea class="w-100" rows="10" placeholder="Memo" disabled={!paymentSave ? false : true} bind:value={memo} />
  </div>
  <div class="mt-2 text-center">
    <button on:click={() => confirmdata()}>{!paymentSave ? "Save" : "Modify"} </button>
  </div>
</form>

<style>
  h1 {
    letter-spacing: 0.3em;
  }
  input,
  select,
  textarea {
    font-size: 12px;
    padding-left: 0.5em;
    letter-spacing: 0.1em;
  }

  input:focus {
    outline: 1px solid rgba(98, 105, 113, 0.5);
  }
  textarea:focus {
    outline: 1px solid rgba(98, 105, 113, 0.5);
  }

  button {
    width: 200px;
    border: 1px solid rgba(98, 105, 113, 1);
    background-color: white;
    color: rgba(98, 105, 113, 1);
    border-radius: 2px;
  }
  button:hover {
    background-color: rgba(98, 105, 113, 1);
    color: white;
  }
</style>
