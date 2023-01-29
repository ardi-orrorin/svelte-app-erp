<script>
  import { serverhost, popUp } from "../../Store";
  import { onMount } from "svelte";
  import axios from "axios";
  import moment from "moment/min/moment-with-locales";

  let data = [];

  onMount(async () => {
    $popUp = !$popUp;
    const url = serverhost + "/api/notice/list/detail/" + params.id;

    data = await axios({ method: "get", url: url }).then((res) => res.data);
  });

  export let params;

  const onClose = () => {
    window.close();
  };
</script>

<div class="m-2">
  <div class="">
    <h1 class="text-center mb-5">N O T I C E</h1>
  </div>
  <div class="mt-3 mb-3 text-end create-date">
    <p>{moment(data.create_date).format("YYYY-MM-DD HH:mm:ss")}</p>
  </div>
  <div class="w-100 mt-3 mb-3">
    {#if data.important}<span class="options">important</span>{/if}
    {#if data.pin}<span class="options">pin</span>{/if}
  </div>
  <div class="">
    <input class="w-100 create-date" value={data.title} disabled />
  </div>

  <div class=" mt-3 mb-3">
    <textarea class="w-100 create-date" value={data.body} rows="10" disabled />
  </div>

  <div class="text-center mt-5">
    <button on:click={() => onClose()}> Readed</button>
  </div>
</div>

<style>
  .options {
    border: 1px solid rgba(98, 105, 113, 1);

    border-radius: 5px;
    font-size: 13px;
    padding-top: 1%;
    padding-bottom: 1%;
    padding-left: 5%;
    padding-right: 5%;
    margin-right: 10px;
    margin-left: 0px;
  }
  .create-date {
    font-size: 14px;
  }
  input:disabled {
    color: black;
    background-color: white;
    border: 0px;
    border: 1px solid rgba(98, 105, 113, 0.5);
  }
  textarea:disabled {
    color: black;
    background-color: white;
    border: 0px;
    padding: 0.6em;
    border: 1px solid rgba(98, 105, 113, 0.5);
  }
  button {
    width: 200px;
    border: 1px solid rgba(98, 105, 113, 1);
    background-color: white;
    color: rgba(98, 105, 113, 1);
    border-radius: 5px;
  }
  button:hover {
    background-color: rgba(98, 105, 113, 1);
    color: white;
  }
</style>
