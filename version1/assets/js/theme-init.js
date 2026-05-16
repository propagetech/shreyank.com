/* Prevent flash of wrong theme — load synchronously in <head> */
(function () {
  var STORAGE_KEY = "shreyank-theme";
  var stored = null;
  try {
    stored = localStorage.getItem(STORAGE_KEY);
  } catch (e) {
    stored = null;
  }
  if (stored === "light" || stored === "dark") {
    document.documentElement.setAttribute("data-theme", stored);
    return;
  }
  /* Default: dark cinematic look (original site) */
  document.documentElement.setAttribute("data-theme", "dark");
})();
