(function () {
  var form = document.getElementById("contact-form");
  if (!form) {
    return;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = document.getElementById("name").value.trim();
    var email = document.getElementById("email").value.trim();
    var category = document.getElementById("category").value;
    var message = document.getElementById("message").value.trim();
    var subject = encodeURIComponent("Enquiry: " + category + " — " + name);
    var body = encodeURIComponent(
      "Name: " + name + "\nEmail: " + email + "\nType: " + category + "\n\n" + message
    );
    window.location.href =
      "mailto:shreyanknanjappa@gmail.com?subject=" + subject + "&body=" + body;
  });
})();
