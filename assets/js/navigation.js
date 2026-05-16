(function () {
  function init() {
    var toggle = document.querySelector("[data-nav-toggle]");
    var nav = document.getElementById("site-nav");
    var header = document.querySelector(".site-header");
    if (!toggle || !nav) {
      return;
    }

    function scrollbarWidth() {
      return window.innerWidth - document.documentElement.clientWidth;
    }

    function setOpen(open) {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      document.body.classList.toggle("nav-open", open);
      if (open) {
        var gutter = scrollbarWidth();
        document.body.style.overflow = "hidden";
        if (gutter > 0) {
          document.body.style.paddingRight = gutter + "px";
          if (header) {
            header.style.paddingRight = gutter + "px";
          }
        }
      } else {
        document.body.style.overflow = "";
        document.body.style.paddingRight = "";
        if (header) {
          header.style.paddingRight = "";
        }
      }
    }

    toggle.addEventListener("click", function () {
      setOpen(!nav.classList.contains("is-open"));
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        if (window.matchMedia("(max-width: 63.99rem)").matches) {
          setOpen(false);
        }
      });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        setOpen(false);
        toggle.focus();
      }
    });

    window.addEventListener("resize", function () {
      if (window.matchMedia("(min-width: 64rem)").matches) {
        setOpen(false);
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
