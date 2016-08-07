// Generated by CoffeeScript 1.9.3
(function() {
  $('#btn-login').click(function() {
    var password, username;
    username = $("input[name='username']").val();
    password = $("input[name='password']").val();
    return $.only_ajax({
      url: "/j/login",
      data: {
        username: username,
        password: password
      },
      success: function(r) {
        if (r.login) {
          return window.location.href = '/';
        } else {
          return $.alert(r.msg);
        }
      }
    });
  });

}).call(this);