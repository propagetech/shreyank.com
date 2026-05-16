(function () {
  var FORMAT_FILTERS = ["feature", "documentary", "short", "series", "other"];
  var ROLE_SECTIONS = {
    recordist: ["recordist"],
    designer: ["designer"],
    dialogue: ["dialogue", "foley"],
    foley: ["foley"],
    "fx-editor": ["fx-editor"],
  };

  function init() {
    var bar = document.querySelector("[data-project-filters]");
    var list = document.querySelector("[data-project-list]");
    if (!bar || !list) {
      return;
    }

    var groups = list.querySelectorAll(".project-group");
    var items = list.querySelectorAll(".project-credit");
    var buttons = bar.querySelectorAll("[data-filter]");

    function applyFilter(value) {
      var isFormat = FORMAT_FILTERS.indexOf(value) !== -1;
      var roleSections = ROLE_SECTIONS[value];
      var count = 0;

      groups.forEach(function (group) {
        var sectionRole = group.getAttribute("data-role-section");
        var showSection =
          value === "all" ||
          isFormat ||
          (roleSections && roleSections.indexOf(sectionRole) !== -1);

        if (!showSection) {
          group.setAttribute("hidden", "");
          return;
        }

        group.removeAttribute("hidden");
        var visibleInGroup = 0;

        group.querySelectorAll(".project-credit").forEach(function (item) {
          var format = item.getAttribute("data-format") || "";
          var showItem = !isFormat || format === value;
          if (showItem) {
            item.removeAttribute("hidden");
            visibleInGroup += 1;
            count += 1;
          } else {
            item.setAttribute("hidden", "");
          }
        });

        if (visibleInGroup === 0) {
          group.setAttribute("hidden", "");
        }
      });

      var live = document.getElementById("filter-status");
      if (live) {
        live.textContent =
          count + " credit" + (count === 1 ? "" : "s") + " shown";
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
