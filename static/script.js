$(document).ready(function () {
  $("#source, #target").change(function () {
    var sourceLang = $("#source").val();
    var targetLang = $("#target").val();

    if (sourceLang == targetLang) {
      alert("Please select different languages for source and target.");
      $(this).val("");
    }
  });
});
