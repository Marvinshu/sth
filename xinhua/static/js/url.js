// Generated by CoffeeScript 1.9.3
(function() {
  $('button[type="button"]').click(function() {
    var cata, data, source, title, url;
    cata = $('select[name="cata"]').val();
    source = $('select[name="source"]').val();
    url = $('input[name="url"]').val();
    title = $('input[name="title"]').val();
    data = {
      cata: cata,
      source: source,
      url: url,
      title: title
    };
    return $.only_ajax({
      url: "/j/url",
      data: data,
      success: function(r) {
        if (r.result) {
          $('select[name="cata"] option:first').attr('selected', true);
          $('select[name="source"] option:first').attr('selected', true);
          $('input[name="url"]').val('');
          $('input[name="title"]').val('');
          return $.tip("添加成功！<br>" + url);
        } else {
          return $.alert(r.msg);
        }
      }
    });
  });

}).call(this);