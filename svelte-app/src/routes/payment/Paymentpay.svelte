<script>
  export let data;
  /* money = Number(money.replaceAll(",", "")).toLocaleString("ko-kr");
  /* bankANumber = bankANumber.replaceAll("-", ""); */
  const bankList = ["SelectBank", "WooriBank", "KBBank", "NH", "KBank"];
  $: paymentSave = true;
</script>

<h1 class="text-center">PAYMENT</h1>

<form>
  <div class="mt-4 mb-3">
    <p class="text-end">Director : {data.user.name}</p>
    <select class="w-100" disabled={!paymentSave ? false : true} required>
      {#each bankList as bank}
        <option value={bank} selected={data.bank_name === bank ? true : false}>{bank}</option>
      {/each}
    </select>
  </div>
  <div class="mt-3 mb-3">
    <input
      class="w-100"
      value={data.corp_name}
      type="text"
      placeholder="Corparate Name"
      disabled={!paymentSave ? false : true}
      required
    />
  </div>
  <div class="mt-3 mb-3">
    <input
      class="w-100"
      type="text"
      value={data.bank_account}
      placeholder="Bank Account Name"
      required
      disabled={!paymentSave ? false : true}
    />
  </div>
  <div class="mt-3 mb-3">
    <input
      class="w-100"
      type="text"
      value={data.bank_number}
      placeholder="Bank Account Number Excluded Characters {'"-"'}"
      required
      disabled={!paymentSave ? false : true}
    />
  </div>

  <div class="mt-3 mb-3">
    <input
      class="w-100"
      type="text"
      value={data.money.toLocaleString("ko-kr")}
      placeholder="Money"
      disabled={!paymentSave ? false : true}
      required
    />
  </div>
  <div>
    <textarea class="w-100" rows="10" value={data.memo} placeholder="Memo" disabled={!paymentSave ? false : true} />
  </div>
  <div class="mt-2 text-center">
    <button on:click|preventDefault={() => (paymentSave = !paymentSave)}>{!paymentSave ? "Save" : "Modify"} </button>
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
  input:disabled,
  select:disabled,
  textarea:disabled {
    background-color: rgba(98, 105, 113, 0.8);
    color: white;
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
