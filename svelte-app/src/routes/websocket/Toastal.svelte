<script>
  import moment from "moment/min/moment-with-locales";
  moment.locale("ko");
  export let message;
  export let index;

  $: toast = JSON.parse(message);
  $: min = 0;
  $: sec = 0;
  setInterval(() => {
    sec += 1;
    if (sec % 60 === 0) {
      min += 1;
      sec = 0;
    }
  }, 1000);
</script>

<div id={"liveToast" + index} class="toast " role="alert" aria-live="assertive" aria-atomic="true">
  <div aria-label="Close" data-bs-dismiss="toast" type="button">
    <div class="toast-header">
      <strong class="me-auto">Notification</strong>
      <small>{min} 분 {min > 0 ? "" : sec + " 초"} 전에</small>

      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close" />
    </div>
    <div class="toast-header">
      <strong class="me-auto text-end">{toast.username}</strong>
      <small>From</small>
    </div>
    <div class="toast-body">{toast.message}</div>
    <div class=" toast-body text-end">
      <small>{"보낸 시간 : " + moment(toast.create_date).format("YYYY-MM-DD HH:mm:ss")}</small>
    </div>
  </div>
</div>

<style>
</style>
