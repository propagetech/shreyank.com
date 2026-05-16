(function () {
  function init() {
    var bar = document.querySelector("[data-project-filters]");
    var list = document.querySelector("[data-project-list]");
    if (!bar || !list) {
      return;
    }

    var rows = list.querySelectorAll("[data-role]");
    var buttons = bar.querySelectorAll("[data-filter]");

    function applyFilter(value) {
      rows.forEach(function (row) {
        var roles = row.getAttribute("data-role") || "";
        var format = row.getAttribute("data-format") || "";
        var show =
          value === "all" ||
          roles.indexOf(value) !== -1 ||
          format === value;
        if (show) {
          row.removeAttribute("hidden");
        } else {
          row.setAttribute("hidden", "");
        }
      });

      var count = 0;
      rows.forEach(function (row) {
        if (!row.hasAttribute("hidden")) {
          count += 1;
        }
      });

      var live = document.getElementById("filter-status");
      if (live) {
        live.textContent =
          count + " project" + (count === 1 ? "" : "s") + " shown";
      }
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

    applyFilter("all");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
