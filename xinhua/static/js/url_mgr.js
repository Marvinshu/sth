// Generated by CoffeeScript 1.9.3
(function() {
  $('.btn-del').click(function() {
    var self;
    self = $(this);
    return bootbox.confirm("确定删除？", function(result) {
      var id;
      if (result) {
        id = self.attr('data-id');
        return $.only_ajax({
          url: "/j/url/rm",
          data: {
            id: id
          },
          success: function(r) {
            return window.location.reload();
          }
        });
      }
    });
  });

}).call(this);
