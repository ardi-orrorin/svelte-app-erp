<script>
  export let data;

  const selectItems = [
    { value: 1, text: "one" },
    { value: 2, text: "two" },
    { value: 3, text: "three" },
    { value: 4, text: "four" },
    { value: 5, text: "five" },
  ];
</script>

<div class="row overflow-hidden">
  <div class="inputwidth">
    <div class="inputwidth">
      <h1 class="text-center">TABLE</h1>
    </div>
    <form>
      <div class="inputwidth mt-4">
        <p class="text-end">Director : {data.customerdetail.user.name}</p>
        <p>
          <input
            type="text"
            class="form-control form-control-sm"
            placeholder="name"
            disabled
            value={data.customerdetail.name}
          />
        </p>
      </div>
      <div class="inputwidth">
        <p>
          <input
            type="text"
            class="form-control form-control-sm"
            placeholder="phone-number"
            disabled
            value={data.customerdetail.phonenumber}
          />
        </p>
      </div>
      <div class="inputwidth">
        <p>
          <input
            type="text"
            class="form-control form-control-sm"
            placeholder="phone-number"
            disabled
            value={data.customerdetail.create_date}
          />
        </p>
      </div>
      <div class="inputwidth">
        <p>
          <select class="form-select form-select-sm" aria-label=".form-select-sm example" disabled>
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
            disabled
            value={data.customerdetail.address}
          />
        </p>
      </div>
      <div class="inputwidth">
        <p>
          <input
            type="text"
            class="form-control form-control-sm"
            placeholder="address-detail"
            disabled
            value={data.customerdetail.addressdetail}
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
            disabled
            value={data.customerdetail.body}
          />
        </p>
      </div>
    </form>
  </div>
</div>

<style>
  h1 {
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
  input:disabled,
  select:disabled,
  textarea:disabled {
    background-color: rgba(98, 105, 113, 0.8);
    color: white;
  }
</style>
