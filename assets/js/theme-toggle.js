(function () {
  var STORAGE_KEY = "shreyank-theme";

  function getTheme() {
    return document.documentElement.getAttribute("data-theme") || "light";
  }

  function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (e) {
      /* storage unavailable */
    }
    updateToggleLabels(theme);
  }

  function updateToggleLabels(theme) {
    var buttons = document.querySelectorAll("[data-theme-toggle]");
    buttons.forEach(function (btn) {
      var next = theme === "light" ? "dark" : "light";
      btn.setAttribute(
        "aria-label",
        "Switch to " + next + " theme. Currently using " + theme + " theme."
      );
    });
  }

  function toggleTheme() {
    var current = getTheme();
    setTheme(current === "light" ? "dark" : "light");
  }

  function init() {
    updateToggleLabels(getTheme());
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.addEventListener("click", toggleTheme);
    });

    if (window.matchMedia) {
      window
        .matchMedia("(prefers-color-scheme: dark)")
        .addEventListener("change", function (e) {
          try {
            if (localStorage.getItem(STORAGE_KEY)) {
              return;
            }
          } catch (err) {
            return;
          }
          setTheme(e.matches ? "dark" : "light");
        });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
