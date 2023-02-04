<script>
  import { storeParams } from "./Store";
  let pathhash;
  window.onkeyup = (e) => {
    pathhash = window.location.hash;
    if (document.activeElement.tagName === "INPUT" || document.activeElement.tagName === "TEXTAREA") {
      switch (e.key) {
        case "Escape":
          $storeParams.keyword = "";
          document.getElementById(document.activeElement.id).blur();
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
        case "Escape":
          $storeParams.keyword = "";
          document.getElementById("search").blur();
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
          if (pathhash === "#/noticelist") {
            if ($storeParams.keyword.indexOf("important") < 0) $storeParams.keyword += "important ";
            break;
          }
          break;

        case "2":
          if (pathhash === "#/notice/create") {
            document.getElementById("pin").click();
            break;
          } else if (pathhash === "#/noticelist") {
            if ($storeParams.keyword.indexOf("pin") < 0) $storeParams.keyword += "pin ";
            break;
          }

          break;
        case "3":
          break;
        case "4":
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
