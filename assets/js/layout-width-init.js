/* Apply saved content width before first paint */
(function () {
  var KEY = "shreyank-layout-width";
  var DEFAULT = 68;
  var MIN = 48;
  var MAX = 88;
  var width = DEFAULT;

  try {
    var stored = parseFloat(localStorage.getItem(KEY));
    if (!isNaN(stored) && stored >= MIN && stored <= MAX) {
      width = stored;
    }
  } catch (e) {
    /* storage unavailable */
  }

  document.documentElement.style.setProperty("--layout-max-width", width + "rem");
})();
