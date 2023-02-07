<script>
  import axios from "axios";
  import { serverhost, popUp } from "../../Store";
  import Loading from "../Loading.svelte";
  import { onMount } from "svelte";
  import moment from "moment/min/moment-with-locales";
  import Paymentdb from "./Paymentdb.svelte";
  import Paymentpay from "./Paymentpay.svelte";

  onMount(() => ($popUp = !$popUp));

  export let params;
  let url = $serverhost + "/api/payment/list/detail/" + params.id;
  $: data = axios({ method: "get", url: url }).then((res) => res.data);
</script>

{#await data}
  <Loading />
{:then data}
  <div class="row">
    <div class="col"><Paymentdb {data} /></div>
    <div class="col"><Paymentpay {data} /></div>
  </div>
{/await}
