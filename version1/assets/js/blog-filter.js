(function () {
  var bar = document.querySelector("[data-blog-filters]");
  var grid = document.querySelector("[data-blog-grid]");
  if (!bar || !grid) {
    return;
  }

  var cards = grid.querySelectorAll("[data-category]");
  var buttons = bar.querySelectorAll("[data-filter]");

  function applyFilter(value) {
    cards.forEach(function (card) {
      var cat = card.getAttribute("data-category") || "";
      var show = value === "all" || cat === value;
      card.toggleAttribute("hidden", !show);
    });
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var value = btn.getAttribute("data-filter");
      buttons.forEach(function (b) {
        b.setAttribute("aria-pressed", b === btn ? "true" : "false");
      });
      applyFilter(value);
    });
  });
})();
