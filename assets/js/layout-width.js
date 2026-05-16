(function () {
  "use strict";

  var KEY = "shreyank-layout-width";
  var DEFAULT = 68;
  var MIN = 48;
  var MAX = 88;

  var root = document.documentElement;
  var control = document.querySelector("[data-layout-width]");
  if (!control) {
    return;
  }

  var range = control.querySelector("[data-layout-width-range]");
  var reset = control.querySelector("[data-layout-width-reset]");
  if (!range) {
    return;
  }

  function clamp(value) {
    return Math.min(MAX, Math.max(MIN, value));
  }

  function apply(rem) {
    var width = clamp(rem);
    root.style.setProperty("--layout-max-width", width + "rem");
    range.value = String(width);
    range.setAttribute("aria-valuenow", String(width));
    range.setAttribute("aria-valuetext", width + " rem content width");
    try {
      localStorage.setItem(KEY, String(width));
    } catch (e) {
      /* storage unavailable */
    }
  }

  function readStored() {
    try {
      var stored = parseFloat(localStorage.getItem(KEY));
      if (!isNaN(stored)) {
        return clamp(stored);
      }
    } catch (e) {
      /* storage unavailable */
    }
    var css = getComputedStyle(root).getPropertyValue("--layout-max-width").trim();
    var parsed = parseFloat(css);
    if (!isNaN(parsed)) {
      return clamp(parsed);
    }
    return DEFAULT;
  }

  apply(readStored());
  control.removeAttribute("hidden");

  range.addEventListener("input", function () {
    apply(parseFloat(range.value, 10));
  });

  if (reset) {
    reset.addEventListener("click", function () {
      apply(DEFAULT);
    });
  }
})();
