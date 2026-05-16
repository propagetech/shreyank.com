/* Lock dark theme — load synchronously in <head> */
(function () {
  document.documentElement.setAttribute("data-theme", "dark");
  try {
    localStorage.removeItem("shreyank-theme");
  } catch (e) {
    /* storage unavailable */
  }
})();
