<script>
  import { storeParams } from "./Store";

  let pathhash = window.location.hash;

  window.onkeyup = (e) => {
    if (document.activeElement.tagName === "INPUT" || document.activeElement.tagName === "TEXTAREA") {
      switch (e.key) {
        case "Escape":
          $storeParams.keyword = "";
          document.getElementById("search").blur();
          break;
      }
    } else {
      switch (e.key) {
        case "Enter":
          if (pathhash === "#/notice/create") {
            document.getElementById("summit").click();
          }

          document.getElementById("search").focus();

          break;
        case "h":
          document.getElementById("HOME").click();
          break;
        case "t":
          document.getElementById("TABLE").click();
          break;
        case "n":
          document.getElementById("NOTICE").click();
          break;
        case "p":
          document.getElementById("PAYMENT").click();
          break;
        case "d":
          document.getElementById("DB").click();
          break;
        case "s":
          document.getElementById("startdate").focus();
          break;
        case "e":
          document.getElementById("enddate").focus();
          break;
        case "c":
          document.getElementById("create").click();
          break;
        case "1":
          if (pathhash === "#/notice/create") {
            document.getElementById("important").click();

            break;
          }
          $storeParams.size = 10;
          break;
        case "2":
          if (pathhash === "#/notice/create") {
            document.getElementById("pin").click();
            break;
          }
          $storeParams.size = 20;

          break;
        case "3":
          $storeParams.size = 50;

          break;
        case "4":
          $storeParams.size = 100;

          break;
        case "ArrowLeft":
          document.getElementById("prev").click();
          break;
        case "ArrowRight":
          document.getElementById("next").click();
          break;
      }
    }
  };
</script>
